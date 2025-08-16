# Contributing to DevHub

Thank you for your interest in contributing to DevHub! 🎉

This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- A virtual environment tool (venv, conda, etc.)

### Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/your-username/devhub.git
   cd devhub
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install development dependencies**
   ```bash
   pip install -e ".[dev]"
   ```

4. **Install pre-commit hooks**
   ```bash
   pre-commit install
   ```

5. **Run tests to verify setup**
   ```bash
   pytest
   ```

## 🔧 Development Workflow

### Making Changes

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write code following our style guidelines
   - Add tests for new functionality
   - Update documentation as needed

3. **Run tests and checks**
   ```bash
   # Run tests
   pytest
   
   # Check code formatting
   black --check src tests
   isort --check-only src tests
   
   # Run linting
   ruff check src tests
   
   # Type checking
   mypy src
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add new feature description"
   ```

### Commit Message Format

We use [Conventional Commits](https://www.conventionalcommits.org/) format:

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for formatting changes
- `refactor:` for code refactoring
- `test:` for adding/updating tests
- `chore:` for maintenance tasks

### Pull Request Process

1. **Push your branch**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request**
   - Use our PR template
   - Include a clear description of changes
   - Reference any related issues
   - Ensure CI checks pass

3. **Code Review**
   - Address reviewer feedback
   - Update your branch as needed
   - Maintain a clean commit history

## 🧩 Adding New Plugins

DevHub uses a plugin architecture. Here's how to add a new plugin:

### 1. Create Plugin Structure

```
src/devhub/plugins/myplugin/
├── __init__.py
├── plugin.py
└── tests/
    └── test_myplugin.py
```

### 2. Implement Plugin Class

```python
# src/devhub/plugins/myplugin/__init__.py
from devhub.core.plugin_manager import Plugin
import click

class MyPlugin(Plugin):
    name = "myplugin"
    description = "Description of my plugin"
    version = "1.0.0"
    
    def is_available(self) -> bool:
        # Check if dependencies are available
        return True
    
    def register_commands(self, cli_group):
        @cli_group.group(name="myplugin")
        def my_group():
            """My plugin commands"""
            pass
        
        @my_group.command()
        def my_command():
            """My command description"""
            click.echo("Hello from my plugin!")

def register_commands(cli_group):
    plugin = MyPlugin()
    plugin.register_commands(cli_group)
```

### 3. Add Tests

```python
# src/devhub/plugins/myplugin/tests/test_myplugin.py
import pytest
from click.testing import CliRunner
from devhub.cli import cli

def test_my_plugin_command():
    runner = CliRunner()
    result = runner.invoke(cli, ['myplugin', 'my-command'])
    assert result.exit_code == 0
    assert "Hello from my plugin!" in result.output
```

### 4. Update Plugin Registry

Add your plugin to the plugin discovery in `src/devhub/plugins/__init__.py`.

## 📋 Code Style Guidelines

### Python Code Style

- Use [Black](https://github.com/psf/black) for code formatting
- Use [isort](https://github.com/PyCQA/isort) for import sorting
- Use [Ruff](https://github.com/astral-sh/ruff) for linting
- Follow [PEP 8](https://pep8.org/) guidelines
- Use type hints where appropriate

### Documentation Style

- Use [Google style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- Keep line length under 88 characters
- Use Markdown for documentation files

### Example Code Style

```python
from typing import List, Optional
import click

def process_files(
    file_paths: List[str], 
    output_format: str = "json",
    verbose: bool = False
) -> Optional[dict]:
    """Process a list of files.
    
    Args:
        file_paths: List of file paths to process
        output_format: Output format (json, yaml, csv)
        verbose: Enable verbose output
        
    Returns:
        Processing results or None if no files
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If invalid output format
    """
    if not file_paths:
        return None
    
    results = {}
    for file_path in file_paths:
        # Process each file
        pass
    
    return results
```

## 🧪 Testing Guidelines

### Test Structure

- Put tests in `tests/` directory
- Mirror the source structure in tests
- Use descriptive test names
- Group related tests in classes

### Test Types

1. **Unit Tests** - Test individual functions/classes
2. **Integration Tests** - Test plugin interactions
3. **CLI Tests** - Test command-line interface
4. **Performance Tests** - Test performance requirements

### Writing Tests

```python
import pytest
from click.testing import CliRunner
from devhub.cli import cli

class TestFormatPlugin:
    
    def test_format_python_file(self, tmp_path):
        """Test Python file formatting"""
        # Create test file
        test_file = tmp_path / "test.py"
        test_file.write_text("def hello( ):\n    print('hello')")
        
        # Run format command
        runner = CliRunner()
        result = runner.invoke(cli, ['format', 'code', str(test_file)])
        
        # Assert results
        assert result.exit_code == 0
        assert "Formatted 1 files" in result.output
    
    @pytest.mark.slow
    def test_format_large_project(self):
        """Test formatting large codebase"""
        # Slow test implementation
        pass
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_plugins.py

# Run with coverage
pytest --cov=devhub

# Run only fast tests
pytest -m "not slow"

# Run in parallel
pytest -n auto
```

## 📚 Documentation

### Adding Documentation

1. **API Documentation** - Add docstrings to all public functions
2. **User Guides** - Add guides to `docs/` directory
3. **Plugin Documentation** - Document plugin usage and configuration
4. **Examples** - Add practical examples

### Building Documentation

```bash
# Install docs dependencies
pip install -e ".[docs]"

# Build documentation
cd docs
mkdocs serve

# View at http://localhost:8000
```

## 🔧 Development Tools

### Useful Commands

```bash
# Format code
black src tests
isort src tests

# Lint code
ruff check src tests

# Type checking
mypy src

# Security scan
bandit -r src

# Dependency check
safety check

# Build package
python -m build

# Install locally
pip install -e .
```

### IDE Setup

#### VS Code

Recommended extensions:
- Python
- Black Formatter
- isort
- Pylance
- GitLens

#### PyCharm

- Enable Black as external tool
- Configure isort as external tool
- Set up pytest as test runner

## 🐛 Reporting Issues

### Bug Reports

Include:
- DevHub version (`devhub --version`)
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages/logs

### Feature Requests

Include:
- Clear description of the feature
- Use case and motivation
- Proposed implementation (if any)
- Examples of similar features

## 📈 Performance Guidelines

### Performance Considerations

- Keep CLI startup time under 500ms
- Cache expensive operations
- Use lazy imports for heavy dependencies
- Provide progress indicators for long operations

### Benchmarking

```bash
# Time CLI startup
time devhub --help

# Profile with py-spy
py-spy record -o profile.svg -- devhub format large-file.py

# Memory profiling
memory_profiler devhub format large-project/
```

## 🔒 Security Guidelines

### Security Best Practices

- Validate all user inputs
- Use secure defaults
- Don't log sensitive information
- Use secure temporary files
- Validate file paths to prevent directory traversal

### Security Testing

```bash
# Security scan
bandit -r src

# Dependency vulnerability check
safety check

# License check
pip-licenses
```

## 📦 Release Process

### Version Bumping

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create git tag
4. Push to trigger release

### Release Checklist

- [ ] All tests pass
- [ ] Documentation updated
- [ ] Changelog updated
- [ ] Version bumped
- [ ] Security scan clean
- [ ] Performance regression check

## 🤝 Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## 💬 Getting Help

- 📖 [Documentation](https://devhub-cli.readthedocs.io/)
- 💬 [Discussions](https://github.com/username/devhub/discussions)
- 🐛 [Issues](https://github.com/username/devhub/issues)
- 🐦 [@devhub_cli](https://twitter.com/devhub_cli)

---

Thank you for contributing to DevHub! 🚀
