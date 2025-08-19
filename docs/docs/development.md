# Development Setup

Complete guide for setting up a DevHub development environment.

## Prerequisites

- **Python**: 3.8 or higher
- **Git**: Latest version
- **Code Editor**: VS Code recommended
- **Terminal**: Bash, Zsh, or PowerShell

## Quick Setup

```bash
# Clone repository
git clone https://github.com/username/devhub.git
cd devhub

# Run setup script
./setup-dev.sh  # Linux/macOS
# or
setup-dev.bat   # Windows
```

## Manual Setup

### 1. Clone and Navigate

```bash
git clone https://github.com/username/devhub.git
cd devhub
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv env

# Activate (Linux/macOS)
source env/bin/activate

# Activate (Windows)
env\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install DevHub in development mode
pip install -e .

# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

### 4. Verify Installation

```bash
# Check DevHub command
devhub --version

# Run tests
pytest

# Check formatting
black --check src/
```

## Development Dependencies

The development environment includes:

```txt
# requirements-dev.txt
pytest>=7.0.0
pytest-cov>=4.0.0
pytest-mock>=3.10.0
black>=23.0.0
isort>=5.12.0
flake8>=6.0.0
mypy>=1.0.0
bandit>=1.7.0
pre-commit>=3.0.0
mkdocs>=1.4.0
mkdocs-material>=9.0.0
```

## IDE Configuration

### VS Code Setup

Recommended extensions:

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.black-formatter",
    "ms-python.isort",
    "ms-python.flake8",
    "ms-python.mypy-type-checker",
    "charliermarsh.ruff",
    "redhat.vscode-yaml",
    "yzhang.markdown-all-in-one"
  ]
}
```

Settings (`.vscode/settings.json`):

```json
{
  "python.defaultInterpreterPath": "./env/bin/python",
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.mypyEnabled": true,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  }
}
```

### PyCharm Setup

1. Open project in PyCharm
2. Set interpreter to `./env/bin/python`
3. Configure code style to match Black
4. Enable type checking with MyPy
5. Set up run configurations for tests

## Project Structure

```
devhub/
├── src/devhub/                 # Source code
│   ├── __init__.py
│   ├── cli.py                  # Main CLI entry point
│   ├── core/                   # Core functionality
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── plugin_manager.py
│   │   └── events.py
│   ├── plugins/                # Built-in plugins
│   │   ├── __init__.py
│   │   ├── format/
│   │   ├── api/
│   │   └── security/
│   └── utils/                  # Utility modules
│       ├── __init__.py
│       ├── exceptions.py
│       ├── logger.py
│       └── cli.py
├── tests/                      # Test suite
│   ├── unit/                   # Unit tests
│   ├── integration/            # Integration tests
│   ├── fixtures/               # Test fixtures
│   └── conftest.py            # Pytest configuration
├── docs/                       # Documentation
│   ├── docs/
│   └── mkdocs.yml
├── scripts/                    # Development scripts
├── .github/                    # GitHub workflows
├── pyproject.toml             # Project configuration
├── requirements-dev.txt       # Development dependencies
└── README.md
```

## Development Workflow

### 1. Create Feature Branch

```bash
git checkout -b feature/my-new-feature
```

### 2. Make Changes

Edit code, following the established patterns and style guidelines.

### 3. Run Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_format.py

# Run with coverage
pytest --cov=devhub
```

### 4. Format and Lint

```bash
# Format code
black src/ tests/
isort src/ tests/

# Check linting
flake8 src/ tests/

# Type checking
mypy src/
```

### 5. Commit Changes

```bash
git add .
git commit -m "feat: add new feature"
```

### 6. Push and Create PR

```bash
git push origin feature/my-new-feature
# Create PR on GitHub
```

## Testing

### Running Tests

```bash
# All tests
pytest

# Specific test file
pytest tests/test_format.py

# Specific test method
pytest tests/test_format.py::TestFormatPlugin::test_python_formatting

# With coverage
pytest --cov=devhub --cov-report=html

# Parallel execution
pytest -n auto
```

### Test Categories

- **Unit tests**: Test individual functions/methods
- **Integration tests**: Test component interactions
- **End-to-end tests**: Test complete workflows
- **Performance tests**: Test performance characteristics

### Writing Tests

```python
# tests/test_my_feature.py
import pytest
from devhub.plugins.format import FormatPlugin

class TestFormatPlugin:
    def setup_method(self):
        self.plugin = FormatPlugin()
        self.plugin.initialize()
    
    def test_format_python(self):
        input_code = "def hello( ):\n  pass"
        result = self.plugin._format_python(input_code, Path("test.py"))
        assert "def hello():" in result
    
    def teardown_method(self):
        self.plugin.cleanup()
```

## Code Quality

### Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.3.0
    hooks:
      - id: mypy
```

### Quality Checks

```bash
# All quality checks
make check

# Individual checks
make format      # Black formatting
make lint        # Flake8 linting
make typecheck   # MyPy type checking
make security    # Bandit security check
```

## Documentation Development

### Building Docs

```bash
# Install docs dependencies
pip install -r docs/requirements.txt

# Serve locally
cd docs
mkdocs serve

# Build static site
mkdocs build
```

### Writing Documentation

- Use Markdown format
- Include code examples
- Add screenshots for UI features
- Follow existing style and structure

## Debugging

### Using Debugger

```python
# Add breakpoint in code
import pdb; pdb.set_trace()

# Or use rich debugger
from rich.console import Console
console = Console()
console.print_exception()
```

### VS Code Debugging

Create `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug DevHub",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/src/devhub/cli.py",
      "args": ["format", "code", "--help"],
      "console": "integratedTerminal",
      "cwd": "${workspaceFolder}"
    }
  ]
}
```

### Logging

```python
from devhub.utils.logger import get_logger

logger = get_logger(__name__)
logger.debug("Debug information")
logger.info("General information")
logger.warning("Warning message")
logger.error("Error occurred")
```

## Performance Profiling

### CPU Profiling

```bash
# Profile with cProfile
python -m cProfile -o profile.stats -m devhub format code src/

# Analyze results
python -c "import pstats; p = pstats.Stats('profile.stats'); p.sort_stats('cumulative').print_stats(20)"
```

### Memory Profiling

```bash
# Install memory profiler
pip install memory-profiler

# Profile memory usage
python -m memory_profiler devhub/cli.py
```

## Environment Variables

Development-specific environment variables:

```bash
# Development mode
export DEVHUB_DEV=1

# Debug logging
export DEVHUB_LOG_LEVEL=DEBUG

# Custom plugin path
export DEVHUB_PLUGIN_PATH=/path/to/dev/plugins

# Test configuration
export DEVHUB_CONFIG_PATH=tests/fixtures/config.toml
```

## Common Issues

### Import Errors

```bash
# Ensure DevHub is installed in development mode
pip install -e .

# Check Python path
python -c "import sys; print(sys.path)"
```

### Test Failures

```bash
# Clear pytest cache
pytest --cache-clear

# Run specific failing test
pytest -xvs tests/test_format.py::test_python_formatting
```

### Permission Issues

```bash
# Fix file permissions
chmod +x scripts/setup-dev.sh

# Install in user space
pip install --user -e .
```

## Makefile Commands

```makefile
# Makefile
.PHONY: install test format lint typecheck clean docs

install:
	pip install -e .
	pip install -r requirements-dev.txt

test:
	pytest

format:
	black src/ tests/
	isort src/ tests/

lint:
	flake8 src/ tests/

typecheck:
	mypy src/

clean:
	find . -type d -name __pycache__ -delete
	find . -name "*.pyc" -delete
	rm -rf .pytest_cache/
	rm -rf htmlcov/

docs:
	cd docs && mkdocs serve
```

## Docker Development

### Development Container

```dockerfile
# Dockerfile.dev
FROM python:3.11-slim

WORKDIR /app
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

COPY . .
RUN pip install -e .

CMD ["bash"]
```

```bash
# Build and run
docker build -f Dockerfile.dev -t devhub-dev .
docker run -it -v $(pwd):/app devhub-dev
```

## Release Preparation

### Version Bump

```bash
# Update version in src/devhub/__init__.py
__version__ = "1.2.0"

# Update CHANGELOG.md
# Create release branch
git checkout -b release/1.2.0
```

### Release Checklist

- [ ] Update version number
- [ ] Update changelog
- [ ] Run all tests
- [ ] Update documentation
- [ ] Create release PR
- [ ] Tag release after merge

## Getting Help

### Resources

- **Documentation**: [DevHub Docs](https://devhub-cli.readthedocs.io/)
- **Examples**: [GitHub Examples](https://github.com/username/devhub-examples)
- **Discussions**: [GitHub Discussions](https://github.com/username/devhub/discussions)
- **Discord**: [DevHub Community](https://discord.gg/devhub)

### Troubleshooting

1. Check the troubleshooting guide
2. Search existing issues
3. Ask in GitHub Discussions
4. Join Discord for real-time help

Happy coding! 🚀
