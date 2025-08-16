"""
API testing plugin for DevHub

This plugin provides HTTP API testing capabilities with beautiful output.
"""

import json
import time
from typing import Dict, Any, Optional
from urllib.parse import urlparse

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.json import JSON
from rich.progress import track

from devhub.core.plugin_manager import Plugin
from devhub.utils.exceptions import NetworkError

console = Console()


class APIPlugin(Plugin):
    """API testing and utilities plugin"""

    name = "api"
    description = "HTTP API testing tools"
    version = "1.0.0"
    author = "DevHub Team"

    def is_available(self) -> bool:
        """Check if required dependencies are available"""
        try:
            import requests
            import httpx

            return True
        except ImportError:
            return False

    def register_commands(self, cli_group):
        """Register API commands"""

        @cli_group.group(name="api")
        def api_group():
            """🌐 API testing and utilities"""
            pass

        @api_group.command(name="test")
        @click.option("--url", "-u", required=True, help="API endpoint URL")
        @click.option("--method", "-m", default="GET", help="HTTP method")
        @click.option("--headers", "-H", multiple=True, help="Headers (key:value)")
        @click.option("--data", "-d", help="Request body data")
        @click.option("--json-data", "-j", help="JSON request body")
        @click.option("--timeout", "-t", default=30, help="Request timeout in seconds")
        @click.option("--verbose", "-v", is_flag=True, help="Verbose output")
        def test_api(url, method, headers, data, json_data, timeout, verbose):
            """Test an HTTP API endpoint"""

            try:
                response = self.make_request(
                    url=url,
                    method=method,
                    headers=dict(h.split(":", 1) for h in headers),
                    data=data,
                    json_data=json_data,
                    timeout=timeout,
                )

                self._display_response(response, verbose)

            except NetworkError as e:
                console.print(f"[red]Error:[/red] {e}")
                raise click.Abort()

        @api_group.command(name="benchmark")
        @click.option("--url", "-u", required=True, help="API endpoint URL")
        @click.option("--requests", "-n", default=10, help="Number of requests")
        @click.option("--concurrency", "-c", default=1, help="Concurrent requests")
        @click.option("--method", "-m", default="GET", help="HTTP method")
        def benchmark_api(url, requests, concurrency, method):
            """Benchmark an API endpoint"""

            console.print(f"[blue]Benchmarking:[/blue] {url}")
            console.print(f"Requests: {requests}, Concurrency: {concurrency}")

            results = []
            start_time = time.time()

            for i in track(range(requests), description="Making requests..."):
                try:
                    request_start = time.time()
                    response = self.make_request(url, method)
                    request_time = time.time() - request_start

                    results.append(
                        {
                            "status_code": response["status_code"],
                            "response_time": request_time,
                            "success": response["status_code"] < 400,
                        }
                    )

                except Exception as e:
                    results.append(
                        {
                            "status_code": 0,
                            "response_time": 0,
                            "success": False,
                            "error": str(e),
                        }
                    )

            total_time = time.time() - start_time
            self._display_benchmark_results(results, total_time)

        @api_group.command(name="headers")
        @click.argument("url")
        def check_headers(url):
            """Check HTTP headers for a URL"""

            try:
                response = self.make_request(url, "HEAD")

                headers_table = Table(title=f"Headers for {url}")
                headers_table.add_column("Header", style="cyan")
                headers_table.add_column("Value", style="white")

                for key, value in response["headers"].items():
                    headers_table.add_row(key, value)

                console.print(headers_table)

            except NetworkError as e:
                console.print(f"[red]Error:[/red] {e}")

    def make_request(
        self,
        url: str,
        method: str = "GET",
        headers: Optional[Dict[str, str]] = None,
        data: Optional[str] = None,
        json_data: Optional[str] = None,
        timeout: int = 30,
    ) -> Dict[str, Any]:
        """Make an HTTP request"""

        try:
            import requests
        except ImportError:
            raise NetworkError("requests library not available")

        # Validate URL
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise NetworkError(f"Invalid URL: {url}")

        # Prepare request data
        request_headers = headers or {}
        request_data = None

        if json_data:
            try:
                request_data = json.loads(json_data)
                request_headers["Content-Type"] = "application/json"
            except json.JSONDecodeError as e:
                raise NetworkError(f"Invalid JSON data: {e}")
        elif data:
            request_data = data

        try:
            # Make request
            start_time = time.time()

            response = requests.request(
                method=method.upper(),
                url=url,
                headers=request_headers,
                json=request_data if json_data else None,
                data=request_data if data and not json_data else None,
                timeout=timeout,
            )

            response_time = time.time() - start_time

            # Parse response
            try:
                response_json = response.json()
            except json.JSONDecodeError:
                response_json = None

            return {
                "url": url,
                "method": method.upper(),
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "content": response.text,
                "json": response_json,
                "response_time": response_time,
                "request_headers": request_headers,
                "request_data": request_data,
            }

        except requests.exceptions.Timeout:
            raise NetworkError(f"Request timeout after {timeout} seconds")
        except requests.exceptions.ConnectionError:
            raise NetworkError(f"Connection error to {url}")
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Request failed: {e}")

    def _display_response(self, response: Dict[str, Any], verbose: bool = False):
        """Display API response with beautiful formatting"""

        # Status panel
        status_color = "green" if response["status_code"] < 400 else "red"
        status_panel = Panel(
            f"[{status_color}]{response['status_code']}[/{status_color}] "
            f"• {response['response_time']:.3f}s "
            f"• {response['method']} {response['url']}",
            title="Response Status",
            border_style=status_color,
        )
        console.print(status_panel)

        # Headers table (if verbose)
        if verbose and response["headers"]:
            headers_table = Table(title="Response Headers", show_header=True)
            headers_table.add_column("Header", style="cyan")
            headers_table.add_column("Value", style="white")

            for key, value in response["headers"].items():
                headers_table.add_row(key, value)

            console.print(headers_table)

        # Response body
        if response["json"]:
            console.print(
                Panel(
                    JSON.from_data(response["json"]),
                    title="Response Body (JSON)",
                    border_style="blue",
                )
            )
        elif response["content"]:
            # Truncate long responses
            content = response["content"]
            if len(content) > 1000 and not verbose:
                content = content[:1000] + "\n... (truncated, use -v for full output)"

            console.print(
                Panel(content, title="Response Body (Text)", border_style="blue")
            )

    def _display_benchmark_results(self, results: list, total_time: float):
        """Display benchmark results"""

        successful_requests = [r for r in results if r["success"]]
        failed_requests = [r for r in results if not r["success"]]

        # Summary table
        summary_table = Table(title="Benchmark Results")
        summary_table.add_column("Metric", style="cyan")
        summary_table.add_column("Value", style="white")

        summary_table.add_row("Total Requests", str(len(results)))
        summary_table.add_row(
            "Successful", f"[green]{len(successful_requests)}[/green]"
        )
        summary_table.add_row("Failed", f"[red]{len(failed_requests)}[/red]")
        summary_table.add_row("Total Time", f"{total_time:.3f}s")
        summary_table.add_row("Requests/sec", f"{len(results) / total_time:.2f}")

        if successful_requests:
            response_times = [r["response_time"] for r in successful_requests]
            avg_time = sum(response_times) / len(response_times)
            min_time = min(response_times)
            max_time = max(response_times)

            summary_table.add_row("Avg Response Time", f"{avg_time:.3f}s")
            summary_table.add_row("Min Response Time", f"{min_time:.3f}s")
            summary_table.add_row("Max Response Time", f"{max_time:.3f}s")

        console.print(summary_table)

        # Status code distribution
        if successful_requests:
            status_codes = {}
            for result in results:
                code = result["status_code"]
                status_codes[code] = status_codes.get(code, 0) + 1

            status_table = Table(title="Status Code Distribution")
            status_table.add_column("Status Code", style="cyan")
            status_table.add_column("Count", style="white")

            for code, count in sorted(status_codes.items()):
                color = "green" if code < 400 else "red"
                status_table.add_row(f"[{color}]{code}[/{color}]", str(count))

            console.print(status_table)


def register_commands(cli_group):
    """Register API plugin commands"""
    plugin = APIPlugin()
    plugin.register_commands(cli_group)
