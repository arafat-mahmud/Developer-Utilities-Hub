# Plugin Architecture

DevHub's plugin architecture provides a powerful and flexible way to extend functionality while maintaining clean separation of concerns.

## 🏗️ Architecture Overview

### Core Components

```
DevHub Core
├── Plugin Manager      # Discovers and loads plugins
├── Configuration       # Manages plugin settings
├── CLI Interface       # Handles command routing
└── Event System       # Inter-plugin communication
```

### Plugin Structure

```python
from devhub.core.plugin_manager import Plugin

class MyPlugin(Plugin):
    name = "myplugin"
    description = "My custom plugin"
    version = "1.0.0"
    author = "Your Name"
    
    def initialize(self):
        """Initialize plugin resources"""
        pass
    
    def register_commands(self, cli_group):
        """Register CLI commands"""
        pass
    
    def cleanup(self):
        """Cleanup resources on shutdown"""
        pass
```

## 🔌 Plugin Lifecycle

### 1. Discovery
DevHub automatically discovers plugins in:
- `devhub/plugins/` (built-in plugins)
- `~/.devhub/plugins/` (user plugins)
- Environment variable `DEVHUB_PLUGIN_PATH`

### 2. Loading
```python
# Plugin loading sequence
1. Import plugin module
2. Instantiate plugin class
3. Call initialize() method
4. Register CLI commands
5. Setup configuration
6. Add to active plugins
```

### 3. Execution
```python
# Command execution flow
1. CLI parser routes command to plugin
2. Plugin validates input
3. Plugin executes command logic
4. Plugin returns results
5. CLI formats and displays output
```

## 📦 Plugin Types

### Command Plugins
Add new CLI commands and subcommands:

```python
import click
from devhub.core.plugin_manager import Plugin

class FormatPlugin(Plugin):
    name = "format"
    
    def register_commands(self, cli_group):
        @cli_group.group()
        def format():
            """Code formatting commands"""
            pass
        
        @format.command()
        @click.argument('files', nargs=-1)
        @click.option('--lang', help='Language to format')
        def code(files, lang):
            """Format source code files"""
            # Implementation here
            pass
```

### Service Plugins
Provide background services or utilities:

```python
class MonitoringPlugin(Plugin):
    name = "monitoring"
    
    def initialize(self):
        self.metrics_collector = MetricsCollector()
        self.metrics_collector.start()
    
    def get_metrics(self):
        return self.metrics_collector.get_current_metrics()
```

### Filter Plugins
Process data between commands:

```python
class DataFilterPlugin(Plugin):
    name = "datafilter"
    
    def filter_json(self, data, query):
        # JSON filtering logic
        return filtered_data
    
    def transform_data(self, data, transformer):
        # Data transformation logic
        return transformed_data
```

## 🔧 Configuration Management

### Plugin Configuration Schema

```python
class MyPlugin(Plugin):
    name = "myplugin"
    
    def get_config_schema(self):
        return {
            "type": "object",
            "properties": {
                "enabled": {"type": "boolean", "default": True},
                "timeout": {"type": "integer", "default": 30},
                "options": {
                    "type": "object",
                    "properties": {
                        "verbose": {"type": "boolean", "default": False}
                    }
                }
            }
        }
    
    def initialize(self):
        config = self.get_config()
        self.timeout = config.get('timeout', 30)
        self.verbose = config.get('options', {}).get('verbose', False)
```

### Configuration Access

```python
# Reading configuration
config = self.get_config()
api_key = config.get('api_key')

# Writing configuration
self.set_config('last_update', datetime.now().isoformat())

# Global configuration access
from devhub.core.config import get_global_config
global_config = get_global_config()
```

## 🔗 Inter-Plugin Communication

### Event System

```python
# Publishing events
self.publish_event('data_processed', {
    'file_count': 5,
    'processing_time': 1.23
})

# Subscribing to events
def initialize(self):
    self.subscribe_event('data_processed', self.on_data_processed)

def on_data_processed(self, event_data):
    print(f"Processed {event_data['file_count']} files")
```

### Plugin Dependencies

```python
class AdvancedPlugin(Plugin):
    name = "advanced"
    dependencies = ["format", "api"]  # Required plugins
    
    def initialize(self):
        # Access other plugins
        format_plugin = self.get_plugin('format')
        api_plugin = self.get_plugin('api')
```

## 🧪 Testing Plugins

### Unit Testing

```python
import unittest
from devhub.core.plugin_manager import PluginManager
from my_plugin import MyPlugin

class TestMyPlugin(unittest.TestCase):
    def setUp(self):
        self.plugin_manager = PluginManager()
        self.plugin = MyPlugin()
        self.plugin.initialize()
    
    def test_plugin_functionality(self):
        result = self.plugin.process_data("test input")
        self.assertEqual(result, "expected output")
    
    def tearDown(self):
        self.plugin.cleanup()
```

### Integration Testing

```python
from click.testing import CliRunner
from devhub.cli import cli

def test_plugin_cli_integration():
    runner = CliRunner()
    result = runner.invoke(cli, ['myplugin', 'command', '--option', 'value'])
    assert result.exit_code == 0
    assert 'expected output' in result.output
```

## 📚 Best Practices

### Error Handling

```python
from devhub.utils.exceptions import PluginError

class MyPlugin(Plugin):
    def process_file(self, file_path):
        try:
            # File processing logic
            return result
        except FileNotFoundError:
            raise PluginError(f"File not found: {file_path}")
        except Exception as e:
            raise PluginError(f"Processing failed: {e}") from e
```

### Logging

```python
from devhub.utils.logger import get_logger

class MyPlugin(Plugin):
    def initialize(self):
        self.logger = get_logger(f"plugin.{self.name}")
    
    def process_data(self, data):
        self.logger.info(f"Processing {len(data)} items")
        # Processing logic
        self.logger.debug("Processing completed successfully")
```

### Performance

```python
import time
from functools import wraps

def performance_monitor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time
        print(f"{func.__name__} took {duration:.2f} seconds")
        return result
    return wrapper

class MyPlugin(Plugin):
    @performance_monitor
    def expensive_operation(self, data):
        # Time-consuming operation
        pass
```

## 🔒 Security Considerations

### Input Validation

```python
import click
from marshmallow import Schema, fields, ValidationError

class InputSchema(Schema):
    file_path = fields.Str(required=True)
    format = fields.Str(validate=lambda x: x in ['json', 'yaml', 'xml'])

class MyPlugin(Plugin):
    def process_file(self, **kwargs):
        try:
            schema = InputSchema()
            validated_data = schema.load(kwargs)
        except ValidationError as e:
            raise PluginError(f"Invalid input: {e.messages}")
        
        # Process validated data
```

### Safe File Operations

```python
import os
from pathlib import Path

class MyPlugin(Plugin):
    def safe_file_operation(self, file_path):
        # Validate file path
        path = Path(file_path).resolve()
        
        # Check if path is within allowed directories
        allowed_dirs = [Path.cwd(), Path.home() / 'projects']
        if not any(path.is_relative_to(allowed_dir) for allowed_dir in allowed_dirs):
            raise PluginError("Access to this path is not allowed")
        
        # Safe file operations
        if path.exists() and path.is_file():
            # Process file
            pass
```

## 📖 Plugin Examples

### Simple Hello World Plugin

```python
import click
from devhub.core.plugin_manager import Plugin

class HelloPlugin(Plugin):
    name = "hello"
    description = "Hello world plugin"
    version = "1.0.0"
    
    def register_commands(self, cli_group):
        @cli_group.command()
        @click.option('--name', default='World', help='Name to greet')
        def hello(name):
            """Say hello to someone"""
            click.echo(f"Hello, {name}!")
```

### File Processing Plugin

```python
import click
from pathlib import Path
from devhub.core.plugin_manager import Plugin
from devhub.utils.exceptions import PluginError

class FileProcessorPlugin(Plugin):
    name = "fileprocessor"
    description = "Process files with various operations"
    version = "1.0.0"
    
    def register_commands(self, cli_group):
        @cli_group.group()
        def process():
            """File processing commands"""
            pass
        
        @process.command()
        @click.argument('input_file', type=click.Path(exists=True))
        @click.option('--output', type=click.Path(), help='Output file')
        @click.option('--operation', type=click.Choice(['uppercase', 'lowercase']))
        def text(input_file, output, operation):
            """Process text files"""
            try:
                content = Path(input_file).read_text()
                
                if operation == 'uppercase':
                    processed = content.upper()
                elif operation == 'lowercase':
                    processed = content.lower()
                else:
                    processed = content
                
                if output:
                    Path(output).write_text(processed)
                    click.echo(f"Processed file saved to {output}")
                else:
                    click.echo(processed)
                    
            except Exception as e:
                raise PluginError(f"Failed to process file: {e}")
```

For more plugin examples and templates, visit: [DevHub Plugin Examples](https://github.com/username/devhub-examples/tree/main/plugins)
