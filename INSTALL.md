# 📦 DevHub Installation Guide

DevHub is currently in development and not yet published to PyPI. This guide will help you install and run DevHub locally.

## 🚨 Current Status

**Note**: DevHub is not yet available on PyPI. The package `devhub-cli` mentioned in the README is not published yet. Please use the local installation method below.

## 🛠️ Local Installation (Recommended)

### Prerequisites
- Python 3.8 or higher
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/arafat-mahmud/Developer-Utilities-Hub.git
cd Developer-Utilities-Hub
```

### Step 2: Set Up Virtual Environment
```bash
# Create virtual environment
python3 -m venv devhub-env

# Activate virtual environment
source devhub-env/bin/activate  # On macOS/Linux
# or
devhub-env\Scripts\activate     # On Windows
```

### Step 3: Install DevHub in Development Mode
```bash
# Install the package in editable mode
pip install -e .

# Or run the setup script
./setup-dev.sh
```

### Step 4: Verify Installation
```bash
devhub --help
```

You should see the DevHub CLI help message.

## 🚀 Quick Start

Once installed, you can use DevHub commands:

```bash
# Format Python code
devhub format --lang python your_file.py

# Test APIs
devhub api test --url https://httpbin.org/get

# Get help for any command
devhub format --help
devhub api --help
```

## 🔧 Alternative Installation Methods

### Method 1: Direct Python Execution
If you prefer not to install the package, you can run it directly:

```bash
cd Developer-Utilities-Hub
python -m src.devhub.cli --help
```

### Method 2: Add to PATH
Add the DevHub script to your PATH:

```bash
# Add to your shell profile (.bashrc, .zshrc, etc.)
export PATH="$PATH:/path/to/Developer-Utilities-Hub/devhub-env/bin"
```

## 🐳 Docker Installation (Coming Soon)

```bash
# Pull the Docker image (when available)
docker pull devhub/cli

# Run DevHub in Docker
docker run --rm -v $(pwd):/workspace devhub/cli format --lang python
```

## 🍺 Homebrew Installation (Planned)

```bash
# Install via Homebrew (when available)
brew install devhub-cli
```

## 📦 PyPI Installation (Future)

```bash
# Install from PyPI (when published)
pip install devhub-cli
```

## 🔧 Development Setup

For contributors and developers:

```bash
# Clone and setup
git clone https://github.com/arafat-mahmud/Developer-Utilities-Hub.git
cd Developer-Utilities-Hub

# Run development setup
./setup-dev.sh

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=devhub
```

## 🚨 Troubleshooting

### "externally-managed-environment" Error
If you see this error when trying to install with `pip3 install devhub-cli`:

```
error: externally-managed-environment
```

This is because:
1. The package isn't published to PyPI yet
2. Your system Python is protected from direct package installation

**Solution**: Use the local installation method above with a virtual environment.

### "command not found: devhub" Error
This happens when:
1. DevHub isn't installed
2. Virtual environment isn't activated
3. PATH doesn't include the DevHub binary

**Solution**:
```bash
# Make sure you're in the project directory
cd Developer-Utilities-Hub

# Activate virtual environment
source devhub-env/bin/activate

# Verify installation
which devhub
devhub --help
```

### Virtual Environment Issues
If you have issues with the virtual environment:

```bash
# Remove existing environment
rm -rf devhub-env

# Create new environment
python3 -m venv devhub-env
source devhub-env/bin/activate

# Reinstall
pip install -e .
```

## 🆘 Getting Help

If you encounter issues:

1. **Check our [Issues](https://github.com/arafat-mahmud/Developer-Utilities-Hub/issues)**
2. **Read the [Contributing Guide](CONTRIBUTING.md)**
3. **Join our [Discussions](https://github.com/arafat-mahmud/Developer-Utilities-Hub/discussions)**
4. **Contact us**: hello@devhub.dev

## 📋 System Requirements

- **Python**: 3.8 or higher
- **Operating System**: macOS, Linux, Windows
- **Memory**: 512MB RAM minimum
- **Storage**: 100MB available space

## 🔄 Updating DevHub

To update your local installation:

```bash
cd Developer-Utilities-Hub
git pull origin main
source devhub-env/bin/activate
pip install -e .
```

## 🎯 Next Steps

After installation:

1. **Read the [User Guide](docs/index.md)**
2. **Try the examples**: `devhub --help`
3. **Explore plugins**: `devhub plugin list`
4. **Configure DevHub**: `devhub --config`

---

**Note**: This is a development project. The installation process will be simplified once we publish to PyPI and package managers.
