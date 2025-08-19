# API Reference

Complete API reference for DevHub's Python API and plugin development.

## Core API

### Plugin Base Class

The foundation for all DevHub plugins.

```python
from devhub.core.plugin_manager import Plugin

class Plugin:
    """Base class for all DevHub plugins"""
    
    # Plugin metadata
    name: str = ""
    description: str = ""
    version: str = "1.0.0"
    author: str = ""
    dependencies: List[str] = []
    
    def initialize(self) -> None:
        """Initialize plugin resources"""
        pass
    
    def register_commands(self, cli_group) -> None:
        """Register CLI commands with the main CLI group"""
        pass
    
    def cleanup(self) -> None:
        """Cleanup resources on plugin shutdown"""
        pass
    
    def get_config(self) -> Dict[str, Any]:
        """Get plugin configuration"""
        pass
    
    def set_config(self, key: str, value: Any) -> None:
        """Set plugin configuration value"""
        pass
    
    def get_config_schema(self) -> Dict[str, Any]:
        """Return JSON schema for plugin configuration"""
        pass
```

### Configuration Manager

Manages plugin and global configuration.

```python
from devhub.core.config import ConfigManager

class ConfigManager:
    """Manages plugin and global configuration"""
    
    def get_config(self, plugin_name: str = None) -> Dict[str, Any]:
        """Get configuration for plugin or global config
        
        Args:
            plugin_name: Name of plugin to get config for, or None for global
            
        Returns:
            Configuration dictionary
        """
        pass
    
    def set_config(self, key: str, value: Any, plugin_name: str = None) -> None:
        """Set configuration value
        
        Args:
            key: Configuration key
            value: Configuration value
            plugin_name: Plugin name, or None for global config
        """
        pass
    
    def validate_config(self, config: Dict[str, Any], schema: Dict[str, Any]) -> bool:
        """Validate configuration against schema
        
        Args:
            config: Configuration to validate
            schema: JSON schema for validation
            
        Returns:
            True if valid, raises ValidationError if invalid
        """
        pass
```

### Event System

Manages inter-plugin communication via events.

```python
from devhub.core.events import EventManager

class EventManager:
    """Manages inter-plugin communication via events"""
    
    def publish(self, event_name: str, data: Dict[str, Any]) -> None:
        """Publish an event
        
        Args:
            event_name: Name of the event
            data: Event data payload
        """
        pass
    
    def subscribe(self, event_name: str, callback: Callable) -> None:
        """Subscribe to an event
        
        Args:
            event_name: Name of the event to subscribe to
            callback: Function to call when event is published
        """
        pass
    
    def unsubscribe(self, event_name: str, callback: Callable) -> None:
        """Unsubscribe from an event
        
        Args:
            event_name: Name of the event
            callback: Function to unsubscribe
        """
        pass
```

## Plugin APIs

### Format Plugin

The format plugin provides code formatting capabilities.

```python
from devhub.plugins.format import FormatPlugin

class FormatPlugin(Plugin):
    """Code formatting plugin"""
    
    name = "format"
    description = "Multi-language code formatter"
    
    def _format_python(self, content: str, file_path: Path, **kwargs) -> str:
        """Format Python code using Black
        
        Args:
            content: Python code to format
            file_path: Path to the file being formatted
            **kwargs: Additional formatting options
            
        Returns:
            Formatted Python code
        """
        pass
    
    def _format_javascript(self, content: str, file_path: Path, **kwargs) -> str:
        """Format JavaScript code using Prettier
        
        Args:
            content: JavaScript code to format
            file_path: Path to the file being formatted
            **kwargs: Additional formatting options
            
        Returns:
            Formatted JavaScript code
        """
        pass
```

### API Plugin

The API plugin provides HTTP client capabilities.

```python
from devhub.plugins.api import APIPlugin

class APIPlugin(Plugin):
    """HTTP API testing plugin"""
    
    name = "api"
    description = "HTTP API testing and benchmarking"
    
    def make_request(self, url: str, method: str = "GET", **kwargs) -> Dict[str, Any]:
        """Make HTTP request
        
        Args:
            url: URL to request
            method: HTTP method
            **kwargs: Additional request options
            
        Returns:
            Response data
        """
        pass
    
    def benchmark_endpoint(self, url: str, requests: int = 100, **kwargs) -> Dict[str, Any]:
        """Benchmark API endpoint
        
        Args:
            url: URL to benchmark
            requests: Number of requests to make
            **kwargs: Additional benchmark options
            
        Returns:
            Benchmark results
        """
        pass
```

## Utility Classes

### Logger

Provides logging functionality for plugins.

```python
from devhub.utils.logger import get_logger

def get_logger(name: str) -> logging.Logger:
    """Get configured logger instance
    
    Args:
        name: Logger name (usually plugin name)
        
    Returns:
        Configured logger instance
    """
    pass

# Usage in plugins
class MyPlugin(Plugin):
    def initialize(self):
        self.logger = get_logger(f"plugin.{self.name}")
        self.logger.info("Plugin initialized")
```

### Exceptions

Custom exception classes for DevHub.

```python
from devhub.utils.exceptions import (
    PluginError,
    ConfigError,
    NetworkError,
    FormatError
)

class PluginError(Exception):
    """Base exception for plugin errors"""
    pass

class ConfigError(PluginError):
    """Configuration related errors"""
    pass

class NetworkError(PluginError):
    """Network operation errors"""
    pass

class FormatError(PluginError):
    """Data formatting errors"""
    pass

# Usage
def risky_operation():
    try:
        # Some operation
        pass
    except Exception as e:
        raise PluginError(f"Operation failed: {e}") from e
```

## CLI Integration

### Command Decorators

Common Click decorators for plugin commands:

```python
import click
from devhub.utils.cli import (
    common_options,
    output_option,
    verbose_option,
    config_option
)

@click.command()
@common_options
@output_option
@verbose_option
def my_command(output, verbose, **kwargs):
    """My command with common options"""
    pass
```

### Progress Reporting

```python
from rich.progress import track
from devhub.utils.progress import create_progress

# Simple progress with track
for item in track(items, description="Processing..."):
    process_item(item)

# Advanced progress reporting
with create_progress() as progress:
    task = progress.add_task("Processing files", total=len(files))
    for file in files:
        process_file(file)
        progress.advance(task)
```

## Configuration Schema

### Plugin Configuration Schema

```python
from devhub.core.config import validate_config

# Define configuration schema
schema = {
    "type": "object",
    "properties": {
        "enabled": {"type": "boolean", "default": True},
        "timeout": {"type": "integer", "minimum": 1, "maximum": 300}
    },
    "required": ["enabled"]
}

# Validate configuration
config = {"enabled": True, "timeout": 30}
is_valid = validate_config(config, schema)
```

## Event System

### Publishing Events

```python
from devhub.core.events import get_event_manager

event_manager = get_event_manager()

# Publish event
event_manager.publish("file_processed", {
    "file_path": "/path/to/file.py",
    "processing_time": 1.23,
    "lines_formatted": 150
})
```

### Subscribing to Events

```python
def on_file_processed(event_data):
    print(f"File processed: {event_data['file_path']}")

# Subscribe to event
event_manager.subscribe("file_processed", on_file_processed)

# Unsubscribe
event_manager.unsubscribe("file_processed", on_file_processed)
```

## Error Handling

### Custom Exceptions

```python
from devhub.utils.exceptions import (
    PluginError,
    ConfigError,
    NetworkError,
    FormatError
)

class MyPluginError(PluginError):
    """Custom plugin exception"""
    pass

# Usage
def risky_operation():
    try:
        # Some operation
        pass
    except Exception as e:
        raise MyPluginError(f"Operation failed: {e}") from e
```

## Testing Utilities

### Plugin Testing

```python
import unittest
from devhub.testing import PluginTestCase
from my_plugin import MyPlugin

class TestMyPlugin(PluginTestCase):
    plugin_class = MyPlugin
    
    def test_plugin_functionality(self):
        result = self.plugin.process_data("test input")
        self.assertEqual(result, "expected output")
    
    def test_configuration(self):
        config = {"timeout": 60}
        self.plugin.update_config(config)
        self.assertEqual(self.plugin.timeout, 60)
```

### CLI Testing

```python
from click.testing import CliRunner
from devhub.cli import cli

def test_cli_command():
    runner = CliRunner()
    result = runner.invoke(cli, ['plugin', 'command', '--option', 'value'])
    assert result.exit_code == 0
    assert 'expected output' in result.output
```

## Performance Monitoring

### Timing Decorators

```python
from devhub.utils.performance import timing, memory_usage

class MyPlugin(Plugin):
    @timing
    def slow_operation(self, data):
        # Time-consuming operation
        return processed_data
    
    @memory_usage
    def memory_intensive_operation(self, large_data):
        # Memory-intensive operation
        return result
```

### Profiling

```python
from devhub.utils.profiling import profile

@profile
def complex_function():
    # Complex operation to profile
    pass
```

## Caching

### Result Caching

```python
from devhub.utils.cache import cached

class MyPlugin(Plugin):
    @cached(ttl=300)  # Cache for 5 minutes
    def expensive_api_call(self, endpoint):
        # Expensive operation
        return api_response
```

## Async Support

### Async Plugin Operations

```python
import asyncio
from devhub.core.plugin_manager import AsyncPlugin

class MyAsyncPlugin(AsyncPlugin):
    async def async_operation(self, data):
        """Async operation"""
        result = await self.fetch_data(data)
        return result
    
    async def fetch_data(self, url):
        """Fetch data asynchronously"""
        # Implementation
        pass
```

## Security Utilities

### Input Validation

```python
from devhub.utils.security import sanitize_path, validate_url

def safe_file_operation(file_path):
    # Sanitize file path
    safe_path = sanitize_path(file_path)
    
    # Validate URL
    if not validate_url(url):
        raise ValueError("Invalid URL")
```

### Secret Management

```python
from devhub.utils.secrets import get_secret, set_secret

# Store secret securely
set_secret("api_key", "secret-value")

# Retrieve secret
api_key = get_secret("api_key")
```

## Data Processing

### Data Transformation

```python
from devhub.utils.data import transform_json, validate_schema

# Transform JSON data
transformed = transform_json(data, {
    "name": "$.user.full_name",
    "email": "$.user.email",
    "posts": "$.posts[*].title"
})

# Validate against schema
is_valid = validate_schema(data, schema)
```

## File Operations

### Safe File Handling

```python
from devhub.utils.files import safe_read, safe_write, atomic_write

# Safe file operations
content = safe_read("/path/to/file.txt")
safe_write("/path/to/output.txt", content)

# Atomic write (prevents corruption)
with atomic_write("/path/to/important.txt") as f:
    f.write(content)
```

## Network Utilities

### HTTP Client

```python
from devhub.utils.http import HTTPClient

client = HTTPClient(
    timeout=30,
    retries=3,
    headers={"User-Agent": "DevHub"}
)

# Make request
response = client.get("https://api.example.com/data")
json_data = response.json()
```

## Logging

### Structured Logging

```python
from devhub.utils.logger import get_logger

logger = get_logger("my_plugin")

# Structured logging
logger.info("Processing file", extra={
    "file_path": "/path/to/file.py",
    "file_size": 1024,
    "processing_time": 1.23
})
```

## Example: Complete Plugin Implementation

```python
import click
import asyncio
from pathlib import Path
from typing import List, Dict, Any
from devhub.core.plugin_manager import Plugin
from devhub.utils.logger import get_logger
from devhub.utils.exceptions import PluginError
from devhub.utils.cache import cached

class ExamplePlugin(Plugin):
    """Example plugin demonstrating API usage"""
    
    name = "example"
    description = "Example plugin for API demonstration"
    version = "1.0.0"
    author = "DevHub Team"
    
    def get_config_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "enabled": {"type": "boolean", "default": True},
                "timeout": {"type": "integer", "default": 30},
                "cache_ttl": {"type": "integer", "default": 300}
            }
        }
    
    def initialize(self):
        self.logger = get_logger(f"plugin.{self.name}")
        config = self.get_config()
        self.timeout = config.get('timeout', 30)
        self.cache_ttl = config.get('cache_ttl', 300)
        
        # Subscribe to events
        self.subscribe_event('file_processed', self.on_file_processed)
    
    def register_commands(self, cli_group):
        @cli_group.group(name=self.name)
        def example():
            """Example plugin commands"""
            pass
        
        @example.command()
        @click.argument('files', nargs=-1, type=click.Path(exists=True))
        @click.option('--output', type=click.Path(), help='Output file')
        def process(files, output):
            """Process files"""
            try:
                results = self.process_files(files)
                
                if output:
                    Path(output).write_text(str(results))
                else:
                    click.echo(results)
                    
            except Exception as e:
                raise PluginError(f"Processing failed: {e}")
    
    @cached(ttl=300)
    def process_files(self, files: List[str]) -> Dict[str, Any]:
        """Process multiple files with caching"""
        results = {}
        
        for file_path in files:
            self.logger.info(f"Processing {file_path}")
            result = self.process_single_file(file_path)
            results[file_path] = result
            
            # Publish event
            self.publish_event('file_processed', {
                'file_path': file_path,
                'result': result
            })
        
        return results
    
    def process_single_file(self, file_path: str) -> Dict[str, Any]:
        """Process a single file"""
        path = Path(file_path)
        return {
            'size': path.stat().st_size,
            'lines': len(path.read_text().splitlines()),
            'extension': path.suffix
        }
    
    def on_file_processed(self, event_data: Dict[str, Any]):
        """Handle file processed event"""
        self.logger.debug(f"File processed: {event_data['file_path']}")
    
    def cleanup(self):
        """Cleanup resources"""
        self.unsubscribe_event('file_processed', self.on_file_processed)
        self.logger.info("Plugin cleanup completed")
```

For the complete API documentation, see the [source code](https://github.com/username/devhub/tree/main/src/devhub) and [API examples](https://github.com/username/devhub-examples/tree/main/api).
