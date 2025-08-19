# Contributing to DevHub

We welcome contributions from the community! This guide will help you get started with contributing to DevHub.

## 🤝 Ways to Contribute

- **Bug Reports**: Help us identify and fix issues
- **Feature Requests**: Suggest new functionality
- **Code Contributions**: Submit pull requests
- **Documentation**: Improve docs and examples
- **Testing**: Help expand test coverage
- **Community**: Help others in discussions

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- GitHub account

### Development Setup

1. **Fork the repository**
   ```bash
   # Fork on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/devhub.git
   cd devhub
   ```

2. **Set up development environment**
   ```bash
   # Create virtual environment
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   
   # Install development dependencies
   pip install -e .
   pip install -r requirements-dev.txt
   ```

3. **Set up pre-commit hooks**
   ```bash
   pre-commit install
   ```

4. **Run tests to verify setup**
   ```bash
   pytest
   ```

## 🔄 Development Workflow

### 1. Create a Branch

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Or bug fix branch
git checkout -b fix/issue-number-description
```

### 2. Make Changes

- Write clear, well-documented code
- Follow the existing code style
- Add tests for new functionality
- Update documentation as needed

### 3. Test Your Changes

```bash
# Run tests
pytest

# Run linting
flake8 src/
black --check src/
isort --check-only src/

# Run type checking
mypy src/

# Run security checks
bandit -r src/
```

### 4. Commit Changes

```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "feat: add new formatting option for Python files

- Add support for custom line length configuration
- Update documentation with new option
- Add tests for line length validation"
```

### 5. Push and Create Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name

# Create pull request on GitHub
```

## 📝 Code Style

### Python Code Style

We use the following tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **Flake8**: Linting
- **MyPy**: Type checking

Configuration is in `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py38', 'py39', 'py310', 'py311']

[tool.isort]
profile = "black"
line_length = 88

[tool.mypy]
python_version = "3.8"
strict = true
```

### Commit Messages

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding/updating tests
- `chore`: Maintenance tasks

Examples:
```
feat(format): add support for custom Python formatters

fix(api): handle timeout errors gracefully

docs: update installation guide for Windows users

test: add integration tests for Git plugin
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_format.py

# Run with coverage
pytest --cov=devhub --cov-report=html

# Run only unit tests
pytest tests/unit/

# Run only integration tests
pytest tests/integration/
```

### Writing Tests

#### Unit Tests

```python
import unittest
from devhub.plugins.format import FormatPlugin

class TestFormatPlugin(unittest.TestCase):
    def setUp(self):
        self.plugin = FormatPlugin()
        self.plugin.initialize()
    
    def test_format_python_code(self):
        """Test Python code formatting"""
        input_code = "def hello( name ):\n    print(f'Hello {name}!')"
        expected = "def hello(name):\n    print(f'Hello {name}!')\n"
        
        result = self.plugin._format_python(input_code, Path("test.py"))
        self.assertEqual(result, expected)
    
    def tearDown(self):
        self.plugin.cleanup()
```

#### Integration Tests

```python
from click.testing import CliRunner
from devhub.cli import cli

def test_format_command_integration():
    """Test format command end-to-end"""
    runner = CliRunner()
    
    with runner.isolated_filesystem():
        # Create test file
        with open('test.py', 'w') as f:
            f.write('def hello( name ):\n    print(f"Hello {name}!")')
        
        # Run format command
        result = runner.invoke(cli, ['format', 'code', 'test.py'])
        
        # Check result
        assert result.exit_code == 0
        
        # Check file was formatted
        with open('test.py', 'r') as f:
            content = f.read()
            assert 'def hello(name):' in content
```

### Test Coverage

We aim for 90%+ test coverage. Check coverage with:

```bash
pytest --cov=devhub --cov-report=html
open htmlcov/index.html  # View coverage report
```

## 📚 Documentation

### Writing Documentation

- Use clear, concise language
- Include code examples
- Add screenshots for UI features
- Follow the existing documentation structure

### Documentation Structure

```
docs/
├── docs/
│   ├── index.md                    # Home page
│   ├── installation.md             # Installation guide
│   ├── quick-start.md              # Quick start guide
│   ├── user-guide/                 # User documentation
│   ├── plugins/                    # Plugin development
│   ├── reference/                  # API reference
│   └── contributing.md             # This file
├── mkdocs.yml                      # MkDocs configuration
└── requirements.txt                # Documentation dependencies
```

### Building Documentation

```bash
# Install documentation dependencies
pip install -r docs/requirements.txt

# Serve documentation locally
cd docs
mkdocs serve

# Build documentation
mkdocs build
```

## 🔍 Code Review Process

### Pull Request Guidelines

1. **Clear description**: Explain what your PR does and why
2. **Link issues**: Reference related issues with "Fixes #123"
3. **Screenshots**: Include screenshots for UI changes
4. **Tests**: Ensure all tests pass
5. **Documentation**: Update docs for new features

### Review Criteria

- Code quality and style
- Test coverage
- Documentation completeness
- Performance impact
- Backward compatibility
- Security implications

### Review Process

1. Automated checks must pass
2. At least one maintainer approval required
3. Address review feedback
4. Squash commits if requested
5. Merge after approval

## 🚨 Reporting Issues

### Bug Reports

Use the bug report template and include:

- DevHub version
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages/logs

### Feature Requests

Use the feature request template and include:

- Problem description
- Proposed solution
- Alternative solutions considered
- Implementation ideas

### Security Issues

For security vulnerabilities, email security@devhub.dev instead of creating a public issue.

## 🏷️ Release Process

### Versioning

We follow [Semantic Versioning](https://semver.org/):

- `MAJOR.MINOR.PATCH`
- Major: Breaking changes
- Minor: New features (backward compatible)
- Patch: Bug fixes (backward compatible)

### Release Checklist

1. Update version in `src/devhub/__init__.py`
2. Update `CHANGELOG.md`
3. Create release PR
4. Tag release after merge
5. GitHub Actions handles PyPI deployment

## 🎯 Areas for Contribution

### High Priority

- **Plugin development**: New plugins for popular tools
- **Performance optimization**: Improve startup time and memory usage
- **Documentation**: More examples and tutorials
- **Testing**: Increase test coverage

### Plugin Ideas

- Docker management
- Database utilities
- Cloud provider tools
- CI/CD integrations
- Code analysis tools

### Documentation Needs

- Video tutorials
- Plugin development guide
- Migration guides
- Best practices

## 💬 Community

### Communication Channels

- **GitHub Discussions**: General questions and ideas
- **Discord**: Real-time chat
- **Issues**: Bug reports and feature requests
- **Email**: security@devhub.dev for security issues

### Code of Conduct

We follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/). Please read it before participating.

### Recognition

Contributors are recognized in:

- `CONTRIBUTORS.md` file
- Release notes
- Documentation credits
- Annual contributor highlights

## 🛠️ Maintainer Guidelines

### For Core Maintainers

#### Review Process

1. Check automated tests pass
2. Review code quality and style
3. Verify documentation updates
4. Test locally if needed
5. Provide constructive feedback
6. Approve when ready

#### Release Management

1. Review changelog
2. Test release candidate
3. Update version numbers
4. Create and push tags
5. Monitor deployment
6. Communicate release

#### Community Management

1. Respond to issues promptly
2. Welcome new contributors
3. Guide community discussions
4. Maintain project roadmap

## 📋 Checklist for Contributors

Before submitting a PR, ensure:

- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] New features have tests
- [ ] Documentation is updated
- [ ] Commit messages follow convention
- [ ] PR description is clear
- [ ] Related issues are linked

## 🎉 Getting Help

If you need help contributing:

1. Check existing documentation
2. Search GitHub issues
3. Ask in GitHub Discussions
4. Join our Discord server
5. Attend community meetings

## 📞 Contact

- **General questions**: GitHub Discussions
- **Bug reports**: GitHub Issues
- **Security issues**: security@devhub.dev
- **Discord**: [DevHub Community](https://discord.gg/devhub)

Thank you for contributing to DevHub! 🚀
