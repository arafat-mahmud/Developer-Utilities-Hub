# Installation Guide

DevHub can be installed through multiple methods depending on your preference and use case.

## 📦 PyPI Installation (Recommended)

The easiest way to install DevHub is through PyPI:

```bash
# Install DevHub
pip install devhub-cli

# Verify installation
devhub --version
```

### Requirements

- Python 3.8 or higher
- pip package manager

## 🐳 Docker Installation

For containerized environments or to avoid dependency conflicts:

```bash
# Pull the official image
docker pull devhub/cli

# Run DevHub in a container
docker run --rm -v $(pwd):/workspace devhub/cli --help

# Format code using Docker
docker run --rm -v $(pwd):/workspace devhub/cli format code --lang python
```

## 🛠️ Development Installation

For contributing to DevHub or using the latest features:

```bash
# Clone the repository
git clone https://github.com/username/devhub.git
cd devhub

# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install in development mode
pip install -e .

# Install development dependencies
pip install -r requirements-dev.txt
```

## 🔧 System-specific Installation

### macOS (Homebrew)

```bash
# Coming soon
brew install devhub-cli
```

### Ubuntu/Debian

```bash
# Using pipx (recommended)
sudo apt install pipx
pipx install devhub-cli

# Or using pip
pip install --user devhub-cli
```

### Windows

```bash
# Using pip
pip install devhub-cli

# Or using pipx
pip install pipx
pipx install devhub-cli
```

## ✅ Verify Installation

After installation, verify that DevHub is working correctly:

```bash
# Check version
devhub --version

# List available plugins
devhub --help

# Test code formatting
echo "print('hello')" | devhub format code --lang python
```

## 🔄 Updating DevHub

To update to the latest version:

```bash
# PyPI
pip install --upgrade devhub-cli

# Docker
docker pull devhub/cli:latest

# Development
git pull origin main
pip install -e .
```

## 🗑️ Uninstallation

To remove DevHub:

```bash
# PyPI installation
pip uninstall devhub-cli

# Docker
docker rmi devhub/cli

# Development installation
pip uninstall devhub-cli
rm -rf devhub/  # Remove cloned repository
```

## 🚨 Troubleshooting

### Common Issues

**Command not found after installation**
```bash
# Check if pip bin directory is in PATH
pip show devhub-cli

# On macOS/Linux, add to ~/.bashrc or ~/.zshrc:
export PATH="$HOME/.local/bin:$PATH"
```

**Permission denied on Linux/macOS**
```bash
# Use --user flag
pip install --user devhub-cli

# Or use pipx
pipx install devhub-cli
```

**Docker permission issues**
```bash
# Add user to docker group (Linux)
sudo usermod -aG docker $USER
# Then logout and login again
```

For more help, visit our [GitHub Issues](https://github.com/username/devhub/issues) or [Discussions](https://github.com/username/devhub/discussions).
