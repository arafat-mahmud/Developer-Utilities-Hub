# Plugin API Reference

Complete API reference for DevHub plugin development.

## Core Classes

### Plugin Base Class

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

### Configuration Management

```python
from devhub.core.config import ConfigManager

class ConfigManager:
    """Manages plugin and global configuration"""
    
    def get_config(self, plugin_name: str = None) -> Dict[str, Any]:
        """Get configuration for plugin or global config"""
        pass
    
    def set_config(self, key: str, value: Any, plugin_name: str = None) -> None:
        """Set configuration value"""
        pass
    
    def validate_config(self, config: Dict[str, Any], schema: Dict[str, Any]) -> bool:
        """Validate configuration against schema"""
        pass
```

### Event System

```python
from devhub.core.events import EventManager

class EventManager:
    """Manages inter-plugin communication via events"""
    
    def publish(self, event_name: str, data: Dict[str, Any]) -> None:
        """Publish an event"""
        pass
    
    def subscribe(self, event_name: str, callback: Callable) -> None:
        """Subscribe to an event"""
        pass
    
    def unsubscribe(self, event_name: str, callback: Callable) -> None:
        """Unsubscribe from an event"""
        pass
```

## Utility Functions

### Logging

```python
from devhub.utils.logger import get_logger

def get_logger(name: str) -> logging.Logger:
    """Get configured logger instance"""
    pass
```

### Exceptions

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
```

## Command Decorators

### Click Integration

```python
import click

# Common decorators for plugin commands
@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
@click.option('--output', type=click.Path(), help='Output file')
@click.option('--format', type=click.Choice(['json', 'yaml']), default='json')
@click.option('--verbose', is_flag=True, help='Verbose output')
def my_command(files, output, format, verbose):
    """Command implementation"""
    pass
```

For complete API documentation, see the [source code](https://github.com/username/devhub/tree/main/src/devhub/core).
