# Creating Plugins

This guide walks you through creating your own DevHub plugins from scratch, including setup, development, testing, and distribution.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- DevHub installed in development mode
- Basic understanding of Click CLI framework

### Development Setup

```bash
# Clone DevHub for development
git clone https://github.com/username/devhub.git
cd devhub

# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install in development mode
pip install -e .
pip install -r requirements-dev.txt
```

## 🏗️ Plugin Structure

### Basic Plugin Template

```python
# src/devhub/plugins/myplugin/__init__.py
import click
from devhub.core.plugin_manager import Plugin
from devhub.utils.logger import get_logger

class MyPlugin(Plugin):
    """My custom DevHub plugin"""
    
    name = "myplugin"
    description = "A sample plugin for DevHub"
    version = "1.0.0"
    author = "Your Name <your.email@example.com>"
    
    def initialize(self):
        """Initialize plugin resources"""
        self.logger = get_logger(f"plugin.{self.name}")
        self.logger.info(f"Initializing {self.name} plugin")
        
        # Initialize any resources here
        self.config = self.get_config()
        
    def register_commands(self, cli_group):
        """Register CLI commands"""
        
        @cli_group.group(name=self.name)
        def myplugin():
            """My plugin commands"""
            pass
        
        @myplugin.command()
        @click.argument('input_text')
        @click.option('--uppercase', is_flag=True, help='Convert to uppercase')
        def process(input_text, uppercase):
            """Process input text"""
            if uppercase:
                result = input_text.upper()
            else:
                result = input_text.lower()
            
            click.echo(f"Processed: {result}")
        
        @myplugin.command()
        def status():
            """Show plugin status"""
            click.echo(f"Plugin {self.name} v{self.version} is running")
    
    def cleanup(self):
        """Cleanup resources"""
        self.logger.info(f"Cleaning up {self.name} plugin")
```

### Directory Structure

```
src/devhub/plugins/myplugin/
├── __init__.py          # Main plugin class
├── commands/            # Command implementations
│   ├── __init__.py
│   ├── process.py
│   └── status.py
├── utils/              # Plugin utilities
│   ├── __init__.py
│   └── helpers.py
├── config/             # Configuration schemas
│   ├── __init__.py
│   └── schema.py
└── tests/              # Plugin tests
    ├── __init__.py
    ├── test_commands.py
    └── test_utils.py
```

## 🎨 Advanced Plugin Features

### Configuration Management

```python
# config/schema.py
CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "enabled": {
            "type": "boolean",
            "default": True,
            "description": "Enable/disable plugin"
        },
        "timeout": {
            "type": "integer",
            "default": 30,
            "minimum": 1,
            "maximum": 300,
            "description": "Operation timeout in seconds"
        },
        "api": {
            "type": "object",
            "properties": {
                "base_url": {
                    "type": "string",
                    "default": "https://api.example.com"
                },
                "api_key": {
                    "type": "string",
                    "description": "API key for authentication"
                }
            }
        }
    }
}

# In your plugin class
class MyPlugin(Plugin):
    def get_config_schema(self):
        return CONFIG_SCHEMA
    
    def initialize(self):
        config = self.get_config()
        self.timeout = config.get('timeout', 30)
        self.api_base_url = config.get('api', {}).get('base_url')
```

### Command Organization

```python
# commands/process.py
import click
from pathlib import Path
from ..utils.helpers import process_file

@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
@click.option('--output-dir', type=click.Path(), help='Output directory')
@click.option('--format', type=click.Choice(['json', 'yaml', 'xml']), 
              default='json', help='Output format')
@click.option('--verbose', is_flag=True, help='Verbose output')
def process(files, output_dir, format, verbose):
    """Process multiple files"""
    output_path = Path(output_dir) if output_dir else Path.cwd()
    
    for file_path in files:
        if verbose:
            click.echo(f"Processing {file_path}...")
        
        try:
            result = process_file(file_path, format)
            output_file = output_path / f"{Path(file_path).stem}.{format}"
            output_file.write_text(result)
            
            if verbose:
                click.echo(f"✓ Saved to {output_file}")
                
        except Exception as e:
            click.echo(f"✗ Error processing {file_path}: {e}", err=True)

# Register in main plugin class
def register_commands(self, cli_group):
    from .commands.process import process
    
    @cli_group.group(name=self.name)
    def myplugin():
        """My plugin commands"""
        pass
    
    myplugin.add_command(process)
```

### Utility Functions

```python
# utils/helpers.py
import json
import yaml
from pathlib import Path
from typing import Any, Dict
from devhub.utils.exceptions import PluginError

def read_data_file(file_path: str) -> Dict[str, Any]:
    """Read data from JSON or YAML file"""
    path = Path(file_path)
    
    try:
        content = path.read_text()
        
        if path.suffix.lower() in ['.json']:
            return json.loads(content)
        elif path.suffix.lower() in ['.yaml', '.yml']:
            return yaml.safe_load(content)
        else:
            raise PluginError(f"Unsupported file format: {path.suffix}")
            
    except Exception as e:
        raise PluginError(f"Failed to read {file_path}: {e}")

def write_data_file(data: Dict[str, Any], file_path: str, format: str) -> None:
    """Write data to file in specified format"""
    path = Path(file_path)
    
    try:
        if format == 'json':
            content = json.dumps(data, indent=2, ensure_ascii=False)
        elif format == 'yaml':
            content = yaml.dump(data, default_flow_style=False, indent=2)
        else:
            raise PluginError(f"Unsupported format: {format}")
        
        path.write_text(content)
        
    except Exception as e:
        raise PluginError(f"Failed to write {file_path}: {e}")

def validate_input(data: Dict[str, Any], schema: Dict[str, Any]) -> bool:
    """Validate input data against schema"""
    # Implement validation logic
    return True
```

## 🧪 Testing Your Plugin

### Unit Tests

```python
# tests/test_commands.py
import unittest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from devhub.plugins.myplugin.commands.process import process

class TestProcessCommand(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
    
    def test_process_single_file(self):
        """Test processing a single file"""
        with self.runner.isolated_filesystem():
            # Create test file
            with open('test.txt', 'w') as f:
                f.write('hello world')
            
            # Run command
            result = self.runner.invoke(process, ['test.txt', '--uppercase'])
            
            # Assertions
            self.assertEqual(result.exit_code, 0)
            self.assertIn('HELLO WORLD', result.output)
    
    def test_process_invalid_file(self):
        """Test error handling for invalid file"""
        result = self.runner.invoke(process, ['nonexistent.txt'])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn('Error', result.output)

# tests/test_utils.py
import unittest
import tempfile
from pathlib import Path
from devhub.plugins.myplugin.utils.helpers import read_data_file, write_data_file

class TestUtilityFunctions(unittest.TestCase):
    def test_read_json_file(self):
        """Test reading JSON files"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump({'key': 'value'}, f)
            f.flush()
            
            data = read_data_file(f.name)
            self.assertEqual(data['key'], 'value')
            
            Path(f.name).unlink()  # Cleanup
    
    def test_write_yaml_file(self):
        """Test writing YAML files"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            test_data = {'name': 'test', 'values': [1, 2, 3]}
            write_data_file(test_data, f.name, 'yaml')
            
            # Verify file was written correctly
            content = Path(f.name).read_text()
            self.assertIn('name: test', content)
            
            Path(f.name).unlink()  # Cleanup
```

### Integration Tests

```python
# tests/test_integration.py
import unittest
from click.testing import CliRunner
from devhub.cli import cli
from devhub.core.plugin_manager import PluginManager

class TestPluginIntegration(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.plugin_manager = PluginManager()
    
    def test_plugin_loaded(self):
        """Test that plugin is properly loaded"""
        plugins = self.plugin_manager.get_loaded_plugins()
        plugin_names = [p.name for p in plugins]
        self.assertIn('myplugin', plugin_names)
    
    def test_cli_integration(self):
        """Test CLI integration"""
        result = self.runner.invoke(cli, ['myplugin', 'status'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Plugin myplugin', result.output)
    
    def test_config_integration(self):
        """Test configuration integration"""
        result = self.runner.invoke(cli, ['config', 'get', 'myplugin.timeout'])
        self.assertEqual(result.exit_code, 0)
```

### Running Tests

```bash
# Run plugin tests
python -m pytest src/devhub/plugins/myplugin/tests/ -v

# Run with coverage
python -m pytest src/devhub/plugins/myplugin/tests/ --cov=devhub.plugins.myplugin

# Run integration tests
python -m pytest tests/integration/ -k myplugin
```

## 📦 Plugin Distribution

### Package Setup

```python
# setup.py for standalone plugin
from setuptools import setup, find_packages

setup(
    name="devhub-plugin-myplugin",
    version="1.0.0",
    description="My custom DevHub plugin",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "devhub-cli>=1.0.0",
        "click>=8.0.0",
        "pyyaml>=6.0",
    ],
    entry_points={
        "devhub.plugins": [
            "myplugin = myplugin:MyPlugin"
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
```

### Documentation

Create comprehensive documentation for your plugin:

```markdown
# MyPlugin Documentation

## Installation

```bash
pip install devhub-plugin-myplugin
```

## Usage

```bash
# Basic usage
devhub myplugin process "hello world" --uppercase

# Advanced usage
devhub myplugin process file1.txt file2.txt --output-dir ./processed/
```

## Configuration

```toml
[myplugin]
timeout = 60
api.base_url = "https://api.example.com"
api.api_key = "your-api-key"
```

## Examples

...
```

### Publishing

```bash
# Build package
python setup.py sdist bdist_wheel

# Test installation
pip install dist/devhub-plugin-myplugin-1.0.0.tar.gz

# Upload to PyPI
twine upload dist/*
```

## 🚀 Plugin Development Tips

### Performance Optimization

```python
import functools
import time
from typing import Any, Callable

def cache_result(ttl_seconds: int = 300):
    """Cache function results with TTL"""
    def decorator(func: Callable) -> Callable:
        cache = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(sorted(kwargs.items()))
            current_time = time.time()
            
            if key in cache:
                result, timestamp = cache[key]
                if current_time - timestamp < ttl_seconds:
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (result, current_time)
            return result
        
        return wrapper
    return decorator

class MyPlugin(Plugin):
    @cache_result(ttl_seconds=60)
    def expensive_api_call(self, endpoint: str) -> Any:
        # Expensive operation
        return api_response
```

### Error Handling

```python
from devhub.utils.exceptions import PluginError
import logging

class MyPlugin(Plugin):
    def safe_operation(self, risky_input: str) -> str:
        try:
            # Validate input
            if not risky_input.strip():
                raise ValueError("Input cannot be empty")
            
            # Perform operation
            result = self.process_input(risky_input)
            
            # Validate output
            if not result:
                raise RuntimeError("Processing failed to produce output")
            
            return result
            
        except ValueError as e:
            self.logger.warning(f"Invalid input: {e}")
            raise PluginError(f"Invalid input: {e}")
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
            raise PluginError(f"Operation failed: {e}") from e
```

### Async Operations

```python
import asyncio
import aiohttp
from typing import List

class MyPlugin(Plugin):
    async def fetch_multiple_urls(self, urls: List[str]) -> List[dict]:
        """Fetch multiple URLs concurrently"""
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_url(session, url) for url in urls]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Handle results and exceptions
            successful_results = []
            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    self.logger.error(f"Failed to fetch {urls[i]}: {result}")
                else:
                    successful_results.append(result)
            
            return successful_results
    
    async def fetch_url(self, session: aiohttp.ClientSession, url: str) -> dict:
        """Fetch single URL"""
        async with session.get(url) as response:
            return await response.json()
```

## 📚 Additional Resources

- [DevHub Plugin API Reference](../reference/api.md)
- [Plugin Examples Repository](https://github.com/username/devhub-examples/tree/main/plugins)
- [DevHub Development Guide](../development.md)
- [Community Plugins](https://github.com/username/devhub-plugins)

For questions and support, visit our [Discord Community](https://discord.gg/devhub) or [GitHub Discussions](https://github.com/username/devhub/discussions).
