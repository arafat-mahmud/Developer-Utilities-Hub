# Plugin Examples

Real-world examples and templates for common plugin patterns.

## 🔧 Simple Command Plugin

### Hello World Plugin

```python
import click
from devhub.core.plugin_manager import Plugin

class HelloPlugin(Plugin):
    name = "hello"
    description = "Simple greeting plugin"
    version = "1.0.0"
    
    def register_commands(self, cli_group):
        @cli_group.command()
        @click.option('--name', default='World', help='Name to greet')
        @click.option('--times', default=1, help='Number of times to greet')
        def hello(name, times):
            """Say hello to someone"""
            for i in range(times):
                click.echo(f"Hello, {name}!")
```

### Usage
```bash
devhub hello --name Alice --times 3
```

## 📊 Data Processing Plugin

### CSV Processor Plugin

```python
import csv
import json
import click
from pathlib import Path
from devhub.core.plugin_manager import Plugin
from devhub.utils.exceptions import PluginError

class CSVProcessorPlugin(Plugin):
    name = "csvproc"
    description = "CSV data processing plugin"
    version = "1.0.0"
    
    def register_commands(self, cli_group):
        @cli_group.group()
        def csv():
            """CSV processing commands"""
            pass
        
        @csv.command()
        @click.argument('input_file', type=click.Path(exists=True))
        @click.option('--output', type=click.Path(), help='Output JSON file')
        @click.option('--delimiter', default=',', help='CSV delimiter')
        def to_json(input_file, output, delimiter):
            """Convert CSV to JSON"""
            try:
                data = []
                with open(input_file, 'r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=delimiter)
                    for row in reader:
                        data.append(dict(row))
                
                json_data = json.dumps(data, indent=2)
                
                if output:
                    Path(output).write_text(json_data)
                    click.echo(f"✓ Converted to {output}")
                else:
                    click.echo(json_data)
                    
            except Exception as e:
                raise PluginError(f"Conversion failed: {e}")
        
        @csv.command()
        @click.argument('input_file', type=click.Path(exists=True))
        @click.option('--column', required=True, help='Column to analyze')
        def stats(input_file, column):
            """Calculate statistics for a column"""
            try:
                values = []
                with open(input_file, 'r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if column in row:
                            try:
                                values.append(float(row[column]))
                            except ValueError:
                                pass  # Skip non-numeric values
                
                if values:
                    stats = {
                        'count': len(values),
                        'sum': sum(values),
                        'mean': sum(values) / len(values),
                        'min': min(values),
                        'max': max(values)
                    }
                    
                    for key, value in stats.items():
                        click.echo(f"{key}: {value}")
                else:
                    click.echo(f"No numeric values found in column '{column}'")
                    
            except Exception as e:
                raise PluginError(f"Statistics calculation failed: {e}")
```

## 🌐 HTTP Client Plugin

### API Client Plugin

```python
import json
import requests
import click
from devhub.core.plugin_manager import Plugin
from devhub.utils.exceptions import NetworkError

class APIClientPlugin(Plugin):
    name = "apiclient"
    description = "HTTP API client plugin"
    version = "1.0.0"
    
    def get_config_schema(self):
        return {
            "type": "object",
            "properties": {
                "default_timeout": {"type": "integer", "default": 30},
                "default_headers": {
                    "type": "object",
                    "default": {"User-Agent": "DevHub API Client"}
                }
            }
        }
    
    def register_commands(self, cli_group):
        @cli_group.group()
        def api():
            """API client commands"""
            pass
        
        @api.command()
        @click.argument('url')
        @click.option('--method', default='GET', type=click.Choice(['GET', 'POST', 'PUT', 'DELETE']))
        @click.option('--data', help='JSON data for request body')
        @click.option('--header', multiple=True, help='HTTP headers (key:value)')
        @click.option('--timeout', type=int, help='Request timeout')
        def request(url, method, data, header, timeout):
            """Make HTTP request"""
            config = self.get_config()
            
            # Prepare headers
            headers = config.get('default_headers', {}).copy()
            for h in header:
                if ':' in h:
                    key, value = h.split(':', 1)
                    headers[key.strip()] = value.strip()
            
            # Prepare request
            kwargs = {
                'url': url,
                'method': method,
                'headers': headers,
                'timeout': timeout or config.get('default_timeout', 30)
            }
            
            if data:
                try:
                    kwargs['json'] = json.loads(data)
                    headers['Content-Type'] = 'application/json'
                except json.JSONDecodeError:
                    kwargs['data'] = data
            
            try:
                response = requests.request(**kwargs)
                
                # Display response
                click.echo(f"Status: {response.status_code}")
                click.echo(f"Headers: {dict(response.headers)}")
                
                try:
                    json_response = response.json()
                    click.echo(f"Body: {json.dumps(json_response, indent=2)}")
                except json.JSONDecodeError:
                    click.echo(f"Body: {response.text}")
                    
            except requests.exceptions.RequestException as e:
                raise NetworkError(f"Request failed: {e}")
```

## 🔐 Password Generator Plugin

### Security Plugin

```python
import secrets
import string
import click
from devhub.core.plugin_manager import Plugin

class SecurityPlugin(Plugin):
    name = "security"
    description = "Security utilities plugin"
    version = "1.0.0"
    
    def register_commands(self, cli_group):
        @cli_group.group()
        def security():
            """Security utilities"""
            pass
        
        @security.command()
        @click.option('--length', default=16, help='Password length')
        @click.option('--no-symbols', is_flag=True, help='Exclude symbols')
        @click.option('--no-numbers', is_flag=True, help='Exclude numbers')
        @click.option('--count', default=1, help='Number of passwords')
        def password(length, no_symbols, no_numbers, count):
            """Generate secure passwords"""
            chars = string.ascii_letters
            
            if not no_numbers:
                chars += string.digits
            
            if not no_symbols:
                chars += "!@#$%^&*"
            
            for _ in range(count):
                password = ''.join(secrets.choice(chars) for _ in range(length))
                click.echo(password)
        
        @security.command()
        @click.argument('text')
        @click.option('--algorithm', default='sha256', 
                     type=click.Choice(['md5', 'sha1', 'sha256', 'sha512']))
        def hash(text, algorithm):
            """Generate hash of text"""
            import hashlib
            
            hash_func = getattr(hashlib, algorithm)
            hash_value = hash_func(text.encode()).hexdigest()
            click.echo(f"{algorithm.upper()}: {hash_value}")
```

## 📁 File Management Plugin

### File Utilities Plugin

```python
import os
import shutil
import click
from pathlib import Path
from devhub.core.plugin_manager import Plugin
from devhub.utils.exceptions import PluginError

class FileUtilsPlugin(Plugin):
    name = "fileutils"
    description = "File management utilities"
    version = "1.0.0"
    
    def register_commands(self, cli_group):
        @cli_group.group()
        def files():
            """File management commands"""
            pass
        
        @files.command()
        @click.argument('directory', type=click.Path(exists=True))
        @click.option('--extension', help='Filter by file extension')
        @click.option('--size', help='Filter by size (e.g., +1M, -100K)')
        @click.option('--recursive', is_flag=True, help='Search recursively')
        def find(directory, extension, size, recursive):
            """Find files matching criteria"""
            path = Path(directory)
            pattern = "**/*" if recursive else "*"
            
            for file_path in path.glob(pattern):
                if file_path.is_file():
                    # Extension filter
                    if extension and not file_path.suffix.lower().endswith(extension.lower()):
                        continue
                    
                    # Size filter (simplified)
                    if size:
                        file_size = file_path.stat().st_size
                        # Add size filtering logic here
                    
                    click.echo(str(file_path))
        
        @files.command()
        @click.argument('source', type=click.Path(exists=True))
        @click.argument('destination', type=click.Path())
        @click.option('--backup', is_flag=True, help='Create backup')
        def copy(source, destination, backup):
            """Copy files or directories"""
            src_path = Path(source)
            dst_path = Path(destination)
            
            try:
                if backup and dst_path.exists():
                    backup_path = dst_path.with_suffix(dst_path.suffix + '.backup')
                    shutil.move(str(dst_path), str(backup_path))
                    click.echo(f"✓ Backup created: {backup_path}")
                
                if src_path.is_file():
                    shutil.copy2(src_path, dst_path)
                else:
                    shutil.copytree(src_path, dst_path)
                
                click.echo(f"✓ Copied {source} to {destination}")
                
            except Exception as e:
                raise PluginError(f"Copy failed: {e}")
        
        @files.command()
        @click.argument('directory', type=click.Path(exists=True))
        def size(directory):
            """Calculate directory size"""
            total_size = 0
            file_count = 0
            
            for dirpath, dirnames, filenames in os.walk(directory):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    try:
                        total_size += os.path.getsize(filepath)
                        file_count += 1
                    except OSError:
                        pass
            
            # Format size
            for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                if total_size < 1024.0:
                    break
                total_size /= 1024.0
            
            click.echo(f"Directory: {directory}")
            click.echo(f"Files: {file_count}")
            click.echo(f"Total size: {total_size:.1f} {unit}")
```

## 🔧 Configuration Example

### Plugin with Complex Configuration

```python
import click
from devhub.core.plugin_manager import Plugin

class ConfigurablePlugin(Plugin):
    name = "configurable"
    description = "Plugin with complex configuration"
    version = "1.0.0"
    
    def get_config_schema(self):
        return {
            "type": "object",
            "properties": {
                "enabled": {"type": "boolean", "default": True},
                "processing": {
                    "type": "object",
                    "properties": {
                        "timeout": {"type": "integer", "default": 30},
                        "batch_size": {"type": "integer", "default": 100},
                        "parallel": {"type": "boolean", "default": False}
                    }
                },
                "output": {
                    "type": "object",
                    "properties": {
                        "format": {
                            "type": "string",
                            "enum": ["json", "yaml", "csv"],
                            "default": "json"
                        },
                        "compression": {"type": "boolean", "default": False}
                    }
                },
                "notifications": {
                    "type": "object",
                    "properties": {
                        "enabled": {"type": "boolean", "default": False},
                        "webhook_url": {"type": "string"},
                        "email": {"type": "string"}
                    }
                }
            }
        }
    
    def initialize(self):
        config = self.get_config()
        
        # Processing settings
        processing = config.get('processing', {})
        self.timeout = processing.get('timeout', 30)
        self.batch_size = processing.get('batch_size', 100)
        self.parallel = processing.get('parallel', False)
        
        # Output settings
        output = config.get('output', {})
        self.output_format = output.get('format', 'json')
        self.compression = output.get('compression', False)
        
        # Notification settings
        notifications = config.get('notifications', {})
        self.notifications_enabled = notifications.get('enabled', False)
        self.webhook_url = notifications.get('webhook_url')
        
    def register_commands(self, cli_group):
        @cli_group.command()
        @click.argument('input_files', nargs=-1)
        def process(input_files):
            """Process files with configured settings"""
            click.echo(f"Processing {len(input_files)} files...")
            click.echo(f"Timeout: {self.timeout}s")
            click.echo(f"Batch size: {self.batch_size}")
            click.echo(f"Output format: {self.output_format}")
            
            # Processing logic here
```

## 📋 Testing Examples

### Plugin Test Suite

```python
# tests/test_plugin.py
import unittest
import tempfile
from pathlib import Path
from click.testing import CliRunner
from my_plugin import MyPlugin

class TestMyPlugin(unittest.TestCase):
    def setUp(self):
        self.plugin = MyPlugin()
        self.plugin.initialize()
        self.runner = CliRunner()
    
    def test_command_execution(self):
        """Test basic command execution"""
        result = self.runner.invoke(self.plugin.my_command, ['--option', 'value'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('expected output', result.output)
    
    def test_file_processing(self):
        """Test file processing functionality"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write('test content')
            f.flush()
            
            result = self.plugin.process_file(f.name)
            self.assertIsNotNone(result)
            
            Path(f.name).unlink()  # Cleanup
    
    def test_error_handling(self):
        """Test error handling"""
        with self.assertRaises(PluginError):
            self.plugin.invalid_operation()
    
    def tearDown(self):
        self.plugin.cleanup()
```

For more examples and templates, visit our [Examples Repository](https://github.com/username/devhub-examples/tree/main/plugins).
