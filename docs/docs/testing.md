# Testing

Comprehensive testing guide for DevHub development and contribution.

## Testing Philosophy

DevHub follows a comprehensive testing strategy:

- **Unit Tests**: Test individual functions and methods
- **Integration Tests**: Test component interactions
- **End-to-End Tests**: Test complete user workflows
- **Performance Tests**: Ensure acceptable performance
- **Security Tests**: Validate security measures

## Test Structure

```
tests/
├── unit/                       # Unit tests
│   ├── test_config.py
│   ├── test_plugin_manager.py
│   └── plugins/
│       ├── test_format.py
│       ├── test_api.py
│       └── test_security.py
├── integration/                # Integration tests
│   ├── test_cli_integration.py
│   ├── test_plugin_loading.py
│   └── test_config_integration.py
├── e2e/                       # End-to-end tests
│   ├── test_workflows.py
│   └── test_real_world_usage.py
├── performance/               # Performance tests
│   ├── test_startup_time.py
│   └── test_memory_usage.py
├── security/                  # Security tests
│   ├── test_input_validation.py
│   └── test_secret_handling.py
├── fixtures/                  # Test data and fixtures
│   ├── config/
│   ├── sample_files/
│   └── mock_data/
└── conftest.py               # Pytest configuration
```

## Running Tests

### Basic Test Execution

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_format.py

# Run specific test method
pytest tests/unit/test_format.py::TestFormatPlugin::test_python_formatting

# Run tests matching pattern
pytest -k "test_format"

# Run tests with verbose output
pytest -v

# Run tests and stop on first failure
pytest -x
```

### Test Categories

```bash
# Unit tests only
pytest tests/unit/

# Integration tests only
pytest tests/integration/

# End-to-end tests only
pytest tests/e2e/

# Fast tests (skip slow tests)
pytest -m "not slow"

# All tests including slow ones
pytest -m ""
```

### Parallel Execution

```bash
# Install pytest-xdist
pip install pytest-xdist

# Run tests in parallel
pytest -n auto

# Run with specific number of workers
pytest -n 4
```

## Test Coverage

### Measuring Coverage

```bash
# Run tests with coverage
pytest --cov=devhub

# Generate HTML coverage report
pytest --cov=devhub --cov-report=html

# Open coverage report
open htmlcov/index.html

# Generate XML coverage report (for CI)
pytest --cov=devhub --cov-report=xml
```

### Coverage Configuration

```ini
# .coveragerc
[run]
source = src/devhub
omit = 
    */tests/*
    */test_*
    setup.py
    venv/*
    env/*

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    if self.debug:
    if settings.DEBUG
    raise AssertionError
    raise NotImplementedError
    if 0:
    if __name__ == .__main__.:

[html]
directory = htmlcov
```

### Coverage Goals

- **Overall**: 90%+ coverage
- **Core modules**: 95%+ coverage
- **New features**: 100% coverage
- **Bug fixes**: Must add tests

## Writing Tests

### Unit Test Example

```python
# tests/unit/test_format.py
import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
import tempfile

from devhub.plugins.format import FormatPlugin
from devhub.utils.exceptions import FormatError

class TestFormatPlugin(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.plugin = FormatPlugin()
        self.plugin.initialize()
        
        # Create temporary directory for test files
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = Path(self.temp_dir) / "test.py"
    
    def tearDown(self):
        """Clean up after tests"""
        self.plugin.cleanup()
        # Clean up temporary files
        import shutil
        shutil.rmtree(self.temp_dir)
    
    def test_format_python_code(self):
        """Test Python code formatting"""
        # Input code with formatting issues
        input_code = """
def hello( name ):
    print( f"Hello {name}!" )
"""
        
        # Expected formatted output
        expected = '''def hello(name):
    print(f"Hello {name}!")
'''
        
        # Test formatting
        result = self.plugin._format_python(input_code, self.test_file)
        self.assertEqual(result.strip(), expected.strip())
    
    def test_format_python_syntax_error(self):
        """Test handling of syntax errors"""
        invalid_code = "def hello(\n    print('incomplete"
        
        with self.assertRaises(FormatError):
            self.plugin._format_python(invalid_code, self.test_file)
    
    @patch('devhub.plugins.format.subprocess.run')
    def test_format_with_external_tool(self, mock_run):
        """Test formatting with external tool"""
        # Mock successful subprocess call
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout="formatted code",
            stderr=""
        )
        
        result = self.plugin._run_external_formatter("test.py", "black")
        
        # Verify subprocess was called correctly
        mock_run.assert_called_once()
        self.assertEqual(result, "formatted code")
    
    def test_config_integration(self):
        """Test configuration integration"""
        # Set custom configuration
        config = {
            "line_length": 100,
            "skip_string_normalization": True
        }
        self.plugin.update_config(config)
        
        # Verify configuration is applied
        self.assertEqual(self.plugin.line_length, 100)
        self.assertTrue(self.plugin.skip_string_normalization)
```

### Integration Test Example

```python
# tests/integration/test_cli_integration.py
import pytest
from click.testing import CliRunner
from pathlib import Path
import tempfile
import os

from devhub.cli import cli

class TestCLIIntegration:
    def setup_method(self):
        """Set up test environment"""
        self.runner = CliRunner()
        self.temp_dir = tempfile.mkdtemp()
        
    def teardown_method(self):
        """Clean up test environment"""
        import shutil
        shutil.rmtree(self.temp_dir)
    
    def test_format_command_integration(self):
        """Test format command end-to-end"""
        # Create test file
        test_file = Path(self.temp_dir) / "test.py"
        test_file.write_text("def hello( name ):\n    print(f'Hello {name}!')")
        
        # Run format command
        result = self.runner.invoke(cli, [
            'format', 'code', str(test_file), '--lang', 'python'
        ])
        
        # Check command succeeded
        assert result.exit_code == 0
        
        # Check file was formatted
        formatted_content = test_file.read_text()
        assert "def hello(name):" in formatted_content
    
    def test_config_command_integration(self):
        """Test configuration commands"""
        with self.runner.isolated_filesystem():
            # Initialize configuration
            result = self.runner.invoke(cli, ['config', 'init'])
            assert result.exit_code == 0
            
            # Set configuration value
            result = self.runner.invoke(cli, [
                'config', 'set', 'format.line_length', '100'
            ])
            assert result.exit_code == 0
            
            # Get configuration value
            result = self.runner.invoke(cli, [
                'config', 'get', 'format.line_length'
            ])
            assert result.exit_code == 0
            assert '100' in result.output
    
    def test_plugin_loading_integration(self):
        """Test plugin loading and command registration"""
        # List available plugins
        result = self.runner.invoke(cli, ['plugin', 'list'])
        assert result.exit_code == 0
        assert 'format' in result.output
        
        # Get plugin info
        result = self.runner.invoke(cli, ['plugin', 'info', 'format'])
        assert result.exit_code == 0
        assert 'Code formatting plugin' in result.output
```

### End-to-End Test Example

```python
# tests/e2e/test_workflows.py
import pytest
from click.testing import CliRunner
from pathlib import Path
import tempfile
import json

from devhub.cli import cli

class TestRealWorldWorkflows:
    def setup_method(self):
        self.runner = CliRunner()
        self.project_dir = tempfile.mkdtemp()
        
    def teardown_method(self):
        import shutil
        shutil.rmtree(self.project_dir)
    
    def test_python_project_workflow(self):
        """Test complete Python project formatting workflow"""
        project_path = Path(self.project_dir)
        
        # Create Python project structure
        src_dir = project_path / "src"
        src_dir.mkdir()
        
        # Create Python files with formatting issues
        (src_dir / "main.py").write_text("""
import os,sys
def main( ):
    print( "Hello World!" )
if __name__=="__main__":
    main()
""")
        
        (src_dir / "utils.py").write_text("""
def helper( x,y ):
    return x+y
class MyClass:
    def __init__( self,value ):
        self.value=value
""")
        
        # Create DevHub configuration
        config = {
            "format": {
                "line_length": 88,
                "python": {
                    "enabled": True,
                    "isort_enabled": True
                }
            }
        }
        (project_path / ".devhub.toml").write_text(
            f"[format]\nline_length = 88\n[format.python]\nenabled = true"
        )
        
        # Run formatting on entire project
        result = self.runner.invoke(cli, [
            'format', 'code', 
            '--lang', 'python',
            '--recursive',
            str(src_dir)
        ], cwd=str(project_path))
        
        # Check command succeeded
        assert result.exit_code == 0
        
        # Verify files were formatted
        main_content = (src_dir / "main.py").read_text()
        assert "import os" in main_content
        assert "import sys" in main_content
        assert "def main():" in main_content
        assert 'if __name__ == "__main__":' in main_content
        
        utils_content = (src_dir / "utils.py").read_text()
        assert "def helper(x, y):" in utils_content
        assert "def __init__(self, value):" in utils_content
    
    def test_api_testing_workflow(self):
        """Test API testing workflow"""
        # Test API endpoint
        result = self.runner.invoke(cli, [
            'api', 'test',
            '--url', 'https://httpbin.org/json',
            '--format', 'json'
        ])
        
        # Check command succeeded
        assert result.exit_code == 0
        assert 'slideshow' in result.output  # httpbin.org/json content
        
        # Test with custom headers
        result = self.runner.invoke(cli, [
            'api', 'test',
            '--url', 'https://httpbin.org/headers',
            '--header', 'Custom-Header: test-value',
            '--format', 'json'
        ])
        
        assert result.exit_code == 0
        assert 'Custom-Header' in result.output
```

### Performance Test Example

```python
# tests/performance/test_startup_time.py
import time
import subprocess
import pytest

class TestPerformance:
    def test_startup_time(self):
        """Test DevHub startup time"""
        start_time = time.time()
        
        result = subprocess.run([
            'devhub', '--version'
        ], capture_output=True, text=True)
        
        end_time = time.time()
        startup_time = end_time - start_time
        
        # DevHub should start in less than 2 seconds
        assert startup_time < 2.0
        assert result.returncode == 0
    
    @pytest.mark.slow
    def test_large_file_formatting(self):
        """Test formatting performance on large files"""
        # Create large Python file
        large_code = "def function_{}():\n    pass\n\n" * 1000
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(large_code)
            f.flush()
            
            start_time = time.time()
            
            result = subprocess.run([
                'devhub', 'format', 'code', f.name
            ], capture_output=True)
            
            end_time = time.time()
            format_time = end_time - start_time
            
            # Should format large file in reasonable time
            assert format_time < 10.0
            assert result.returncode == 0
            
            os.unlink(f.name)
```

## Test Fixtures and Utilities

### Fixtures

```python
# tests/conftest.py
import pytest
import tempfile
from pathlib import Path
from devhub.core.plugin_manager import PluginManager
from devhub.core.config import ConfigManager

@pytest.fixture
def temp_dir():
    """Provide temporary directory for tests"""
    temp_path = tempfile.mkdtemp()
    yield Path(temp_path)
    # Cleanup
    import shutil
    shutil.rmtree(temp_path)

@pytest.fixture
def sample_python_file(temp_dir):
    """Provide sample Python file for testing"""
    file_path = temp_dir / "sample.py"
    file_path.write_text("""
def hello( name ):
    print( f"Hello {name}!" )
""")
    return file_path

@pytest.fixture
def plugin_manager():
    """Provide configured plugin manager"""
    manager = PluginManager()
    manager.initialize()
    yield manager
    manager.cleanup()

@pytest.fixture
def mock_config():
    """Provide mock configuration"""
    return {
        "format": {
            "line_length": 88,
            "python": {
                "enabled": True,
                "formatter": "black"
            }
        },
        "api": {
            "default_timeout": 30
        }
    }
```

### Test Utilities

```python
# tests/utils.py
import json
import yaml
from pathlib import Path

def create_test_file(path: Path, content: str, file_type: str = "txt"):
    """Create test file with specified content"""
    if file_type == "json":
        path.write_text(json.dumps(json.loads(content), indent=2))
    elif file_type == "yaml":
        path.write_text(yaml.dump(yaml.safe_load(content)))
    else:
        path.write_text(content)
    return path

def assert_file_formatted(file_path: Path, expected_patterns: list):
    """Assert that file contains expected formatting patterns"""
    content = file_path.read_text()
    for pattern in expected_patterns:
        assert pattern in content, f"Pattern '{pattern}' not found in {file_path}"

def run_cli_command(command_args: list, cwd: Path = None):
    """Run CLI command and return result"""
    from click.testing import CliRunner
    from devhub.cli import cli
    
    runner = CliRunner()
    return runner.invoke(cli, command_args, cwd=str(cwd) if cwd else None)
```

## Mocking and Stubbing

### Mocking External Dependencies

```python
import unittest.mock as mock
from devhub.plugins.api import APIPlugin

class TestAPIPlugin:
    @mock.patch('requests.get')
    def test_api_request(self, mock_get):
        """Test API request with mocked response"""
        # Setup mock response
        mock_response = mock.MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": "success"}
        mock_get.return_value = mock_response
        
        # Test API call
        plugin = APIPlugin()
        result = plugin.make_request("https://api.example.com/test")
        
        # Verify mock was called correctly
        mock_get.assert_called_once_with("https://api.example.com/test")
        assert result["result"] == "success"
    
    @mock.patch('subprocess.run')
    def test_external_tool_execution(self, mock_run):
        """Test external tool execution"""
        mock_run.return_value = mock.MagicMock(
            returncode=0,
            stdout="tool output",
            stderr=""
        )
        
        from devhub.plugins.format import FormatPlugin
        plugin = FormatPlugin()
        result = plugin._run_external_tool(["black", "file.py"])
        
        assert result == "tool output"
        mock_run.assert_called_once()
```

## Test Configuration

### Pytest Configuration

```ini
# pytest.ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    --strict-markers
    --disable-warnings
    --tb=short
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    integration: marks tests as integration tests
    e2e: marks tests as end-to-end tests
    unit: marks tests as unit tests
```

### Test Environment Variables

```bash
# Set test environment
export DEVHUB_ENV=test
export DEVHUB_LOG_LEVEL=DEBUG
export DEVHUB_CONFIG_PATH=tests/fixtures/test_config.toml
```

## Continuous Integration

### GitHub Actions Test Workflow

```yaml
# .github/workflows/test.yml
name: Test Suite

on: [push, pull_request]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: [3.8, 3.9, '3.10', 3.11]
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e .
        pip install -r requirements-dev.txt
    
    - name: Run tests
      run: |
        pytest --cov=devhub --cov-report=xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
```

## Test Data Management

### Test Fixtures

```
tests/fixtures/
├── config/
│   ├── minimal.toml
│   ├── complete.toml
│   └── invalid.toml
├── sample_files/
│   ├── python/
│   │   ├── well_formatted.py
│   │   ├── needs_formatting.py
│   │   └── syntax_error.py
│   ├── javascript/
│   └── json/
└── expected_outputs/
    ├── python/
    └── javascript/
```

### Loading Test Data

```python
def load_test_fixture(filename: str) -> str:
    """Load test fixture file"""
    fixtures_dir = Path(__file__).parent / "fixtures"
    return (fixtures_dir / filename).read_text()

def get_sample_files(language: str) -> list:
    """Get list of sample files for language"""
    samples_dir = Path(__file__).parent / "fixtures" / "sample_files" / language
    return list(samples_dir.glob("*.py" if language == "python" else "*"))
```

## Test Automation

### Test Scripts

```bash
#!/bin/bash
# scripts/run-tests.sh

set -e

echo "Running DevHub test suite..."

# Unit tests
echo "Running unit tests..."
pytest tests/unit/ -v

# Integration tests
echo "Running integration tests..."
pytest tests/integration/ -v

# Performance tests (if not CI)
if [ "$CI" != "true" ]; then
    echo "Running performance tests..."
    pytest tests/performance/ -v -m "not slow"
fi

# Coverage report
echo "Generating coverage report..."
pytest --cov=devhub --cov-report=html tests/

echo "Tests completed successfully!"
```

### Pre-commit Testing

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: tests
        name: Run tests
        entry: pytest tests/unit/ tests/integration/
        language: system
        pass_filenames: false
        always_run: true
```

## Debugging Tests

### Debug Configuration

```python
# Add to conftest.py for debugging
import logging

def pytest_configure(config):
    """Configure pytest for debugging"""
    if config.getoption("--pdb"):
        # Enable detailed logging when debugging
        logging.basicConfig(level=logging.DEBUG)
```

### VS Code Test Debugging

```json
{
  "name": "Debug Tests",
  "type": "python",
  "request": "launch",
  "module": "pytest",
  "args": [
    "tests/unit/test_format.py::TestFormatPlugin::test_python_formatting",
    "-v",
    "-s"
  ],
  "console": "integratedTerminal",
  "cwd": "${workspaceFolder}"
}
```

This comprehensive testing guide ensures DevHub maintains high quality and reliability across all components and use cases.
