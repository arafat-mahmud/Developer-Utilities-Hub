"""
Code formatting plugin for DevHub

This plugin provides code formatting capabilities for multiple programming languages.
"""

import subprocess
import shutil
from pathlib import Path
from typing import Dict, Any, List, Optional

import click
from rich.console import Console
from rich.progress import track

from devhub.core.plugin_manager import Plugin
from devhub.utils.exceptions import FormatError

console = Console()


class FormatPlugin(Plugin):
    """Code formatting plugin"""

    name = "format"
    description = "Multi-language code formatter"
    version = "1.0.0"
    author = "DevHub Team"

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        super().__init__(config)
        self.supported_languages = {
            "python": self._format_python,
            "javascript": self._format_javascript,
            "typescript": self._format_typescript,
            "json": self._format_json,
            "yaml": self._format_yaml,
            "go": self._format_go,
            "rust": self._format_rust,
        }

    def is_available(self) -> bool:
        """Check if formatting tools are available"""
        required_tools = ["black", "isort"]  # Basic Python tools

        for tool in required_tools:
            if not shutil.which(tool):
                return False

        return True

    def register_commands(self, cli_group):
        """Register format commands"""

        @cli_group.group(name="format")
        def format_group():
            """🎨 Code formatting utilities"""
            pass

        @format_group.command(name="code")
        @click.argument("files", nargs=-1, type=click.Path(exists=True))
        @click.option(
            "--lang",
            "-l",
            type=click.Choice(list(self.supported_languages.keys())),
            help="Programming language to format",
        )
        @click.option(
            "--check", "-c", is_flag=True, help="Check if files would be reformatted"
        )
        @click.option("--diff", "-d", is_flag=True, help="Show diff of changes")
        @click.option("--line-length", type=int, default=88, help="Maximum line length")
        def format_code(files, lang, check, diff, line_length):
            """Format source code files"""

            if not files:
                console.print("[red]No files specified[/red]")
                return

            formatted_files = []
            errors = []

            for file_path in track(files, description="Formatting files..."):
                try:
                    result = self.format_file(
                        file_path,
                        language=lang,
                        check_only=check,
                        show_diff=diff,
                        line_length=line_length,
                    )

                    if result["changed"]:
                        formatted_files.append(file_path)

                except FormatError as e:
                    errors.append(str(e))

            # Show results
            if formatted_files:
                console.print(
                    f"[green]✓[/green] Formatted {len(formatted_files)} files"
                )
                for file_path in formatted_files:
                    console.print(f"  • {file_path}")

            if errors:
                console.print(f"[red]✗[/red] {len(errors)} errors occurred")
                for error in errors:
                    console.print(f"  • {error}")

        @format_group.command(name="check")
        @click.argument("path", type=click.Path(exists=True))
        @click.option(
            "--lang",
            "-l",
            type=click.Choice(list(self.supported_languages.keys())),
            help="Programming language to check",
        )
        def check_formatting(path, lang):
            """Check if code formatting is correct"""

            path = Path(path)
            files_to_check = []

            if path.is_file():
                files_to_check = [path]
            else:
                # Find files to check
                patterns = self._get_file_patterns(lang)
                for pattern in patterns:
                    files_to_check.extend(path.rglob(pattern))

            needs_formatting = []

            for file_path in track(files_to_check, description="Checking files..."):
                try:
                    result = self.format_file(file_path, check_only=True)
                    if result["changed"]:
                        needs_formatting.append(file_path)
                except FormatError:
                    pass  # Skip files with errors

            if needs_formatting:
                console.print(
                    f"[yellow]⚠[/yellow] {len(needs_formatting)} files need formatting:"
                )
                for file_path in needs_formatting:
                    console.print(f"  • {file_path}")
                raise click.ClickException("Code formatting check failed")
            else:
                console.print("[green]✓[/green] All files are properly formatted")

    def format_file(
        self,
        file_path: str,
        language: Optional[str] = None,
        check_only: bool = False,
        show_diff: bool = False,
        line_length: int = 88,
    ) -> Dict[str, Any]:
        """Format a single file"""

        file_path = Path(file_path)

        # Auto-detect language if not specified
        if not language:
            language = self._detect_language(file_path)

        if language not in self.supported_languages:
            raise FormatError(f"Unsupported language: {language}")

        # Get original content
        original_content = file_path.read_text()

        # Format content
        formatter = self.supported_languages[language]
        formatted_content = formatter(
            original_content, file_path, line_length=line_length
        )

        changed = original_content != formatted_content

        # Show diff if requested
        if show_diff and changed:
            self._show_diff(file_path, original_content, formatted_content)

        # Write formatted content if not check-only
        if not check_only and changed:
            file_path.write_text(formatted_content)

        return {
            "file": str(file_path),
            "language": language,
            "changed": changed,
            "original_lines": len(original_content.splitlines()),
            "formatted_lines": len(formatted_content.splitlines()),
        }

    def _detect_language(self, file_path: Path) -> str:
        """Auto-detect programming language from file extension"""

        extension_map = {
            ".py": "python",
            ".js": "javascript",
            ".ts": "typescript",
            ".json": "json",
            ".yml": "yaml",
            ".yaml": "yaml",
            ".go": "go",
            ".rs": "rust",
        }

        suffix = file_path.suffix.lower()
        return extension_map.get(suffix, "unknown")

    def _get_file_patterns(self, language: Optional[str]) -> List[str]:
        """Get file patterns for a language"""

        pattern_map = {
            "python": ["*.py"],
            "javascript": ["*.js"],
            "typescript": ["*.ts"],
            "json": ["*.json"],
            "yaml": ["*.yml", "*.yaml"],
            "go": ["*.go"],
            "rust": ["*.rs"],
        }

        if language:
            return pattern_map.get(language, ["*"])
        else:
            # Return all patterns
            patterns = []
            for lang_patterns in pattern_map.values():
                patterns.extend(lang_patterns)
            return patterns

    def _format_python(self, content: str, file_path: Path, **kwargs) -> str:
        """Format Python code using black and isort"""

        line_length = kwargs.get("line_length", 88)

        # Format with black
        try:
            result = subprocess.run(
                ["black", "--code", content, "--line-length", str(line_length)],
                capture_output=True,
                text=True,
                check=True,
            )
            content = result.stdout
        except subprocess.CalledProcessError as e:
            raise FormatError(f"Black formatting failed: {e.stderr}")

        # Sort imports with isort - write to temp file since isort doesn't support --code
        import tempfile

        try:
            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".py", delete=False
            ) as temp_file:
                temp_file.write(content)
                temp_file.flush()

                result = subprocess.run(
                    [
                        "isort",
                        temp_file.name,
                        "--line-length",
                        str(line_length),
                        "--stdout",
                    ],
                    capture_output=True,
                    text=True,
                    check=True,
                )
                content = result.stdout

        except subprocess.CalledProcessError as e:
            raise FormatError(f"isort failed: {e.stderr}")
        finally:
            # Clean up temp file
            import os

            try:
                os.unlink(temp_file.name)
            except:
                pass

        return content

    def _format_javascript(self, content: str, file_path: Path, **kwargs) -> str:
        """Format JavaScript code using prettier"""

        if not shutil.which("prettier"):
            raise FormatError(
                "Prettier not found. Install with: npm install -g prettier"
            )

        try:
            result = subprocess.run(
                ["prettier", "--stdin-filepath", str(file_path)],
                input=content,
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise FormatError(f"Prettier formatting failed: {e.stderr}")

    def _format_typescript(self, content: str, file_path: Path, **kwargs) -> str:
        """Format TypeScript code using prettier"""
        return self._format_javascript(content, file_path, **kwargs)

    def _format_json(self, content: str, file_path: Path, **kwargs) -> str:
        """Format JSON content"""
        import json

        try:
            data = json.loads(content)
            return json.dumps(data, indent=2, ensure_ascii=False) + "\n"
        except json.JSONDecodeError as e:
            raise FormatError(f"Invalid JSON: {e}")

    def _format_yaml(self, content: str, file_path: Path, **kwargs) -> str:
        """Format YAML content"""
        try:
            import yaml

            data = yaml.safe_load(content)
            return yaml.dump(data, default_flow_style=False, indent=2)
        except ImportError:
            raise FormatError("PyYAML not installed")
        except yaml.YAMLError as e:
            raise FormatError(f"Invalid YAML: {e}")

    def _format_go(self, content: str, file_path: Path, **kwargs) -> str:
        """Format Go code using gofmt"""

        if not shutil.which("gofmt"):
            raise FormatError("gofmt not found. Install Go tools")

        try:
            result = subprocess.run(
                ["gofmt"], input=content, capture_output=True, text=True, check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise FormatError(f"gofmt failed: {e.stderr}")

    def _format_rust(self, content: str, file_path: Path, **kwargs) -> str:
        """Format Rust code using rustfmt"""

        if not shutil.which("rustfmt"):
            raise FormatError(
                "rustfmt not found. Install with: rustup component add rustfmt"
            )

        try:
            result = subprocess.run(
                ["rustfmt", "--emit=stdout"],
                input=content,
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise FormatError(f"rustfmt failed: {e.stderr}")

    def _show_diff(self, file_path: Path, original: str, formatted: str):
        """Show diff between original and formatted content"""
        import difflib

        diff = difflib.unified_diff(
            original.splitlines(keepends=True),
            formatted.splitlines(keepends=True),
            fromfile=f"a/{file_path}",
            tofile=f"b/{file_path}",
        )

        console.print(f"\n[bold]Diff for {file_path}:[/bold]")
        for line in diff:
            if line.startswith("+"):
                console.print(line.rstrip(), style="green")
            elif line.startswith("-"):
                console.print(line.rstrip(), style="red")
            elif line.startswith("@"):
                console.print(line.rstrip(), style="cyan")
            else:
                console.print(line.rstrip())


def register_commands(cli_group):
    """Register format plugin commands"""
    plugin = FormatPlugin()
    plugin.register_commands(cli_group)
