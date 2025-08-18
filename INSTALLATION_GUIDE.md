# 🚀 DevHub CLI - Installation Guide

## ✅ **WORKING SOLUTION** - How to Install DevHub CLI

Your DevHub CLI is published on PyPI and ready to use! Here's the **correct installation method**:

### 🎯 **Recommended Installation (pipx)**

```bash
# Install pipx (if not already installed)
brew install pipx

# Install DevHub CLI globally
pipx install devhub-tools

# Test installation
devhub --version
```

### 📋 **Alternative Installation Methods**

**Method 1: Virtual Environment (for development)**
```bash
# Create virtual environment
python3 -m venv devhub-env
source devhub-env/bin/activate

# Install DevHub
pip install devhub-tools

# Test
devhub --version
```

**Method 2: User Installation**
```bash
# Install for current user only
pip3 install --user devhub-tools

# Test
devhub --version
```

**Method 3: Force System Installation (NOT recommended)**
```bash
# Only if you understand the risks
pip3 install --break-system-packages devhub-tools
```

### ❌ **What DOESN'T Work (and why)**

**❌ `pip install devhub-tools`**
- Error: `zsh: command not found: pip`
- Reason: Modern systems use `pip3` or pipx

**❌ `pip3 install devhub-tools`**  
- Error: `externally-managed-environment`
- Reason: macOS protects system Python

**❌ `npm install -g @devhub/cli`**
- Error: `404 Not Found`
- Reason: DevHub is a Python package, not Node.js

**❌ `brew install devhub-cli`**
- Error: `No available formula`
- Reason: Not published to Homebrew (only PyPI)

**❌ `npx devhub-cli`**
- Error: `No versions available`  
- Reason: Wrong package name and platform

### ✅ **Correct Package Information**

- **Package Name**: `devhub-tools` (NOT `devhub-cli`)
- **Platform**: PyPI (Python Package Index)
- **Installation Tool**: `pipx` (recommended) or `pip3`
- **Commands Available**: `devhub` and `dh`

### 🧪 **Verify Installation**

After installation, test with:

```bash
# Check version
devhub --version

# See all commands
devhub --help

# Test API functionality
devhub api test --url https://httpbin.org/get

# Test with short command
dh --help
```

### 🎯 **Quick Start Examples**

```bash
# API Testing
devhub api test --url https://api.github.com/users/octocat
devhub api headers https://example.com

# Get help for any command
devhub api --help
devhub format --help
```

### 🔧 **Troubleshooting**

**If you get "command not found: devhub":**
1. Make sure pipx is in your PATH: `pipx ensurepath`
2. Restart your terminal
3. Try: `~/.local/bin/devhub --version`

**If you get plugin errors:**
- These are normal for some features in global installation
- Core functionality (API testing) works perfectly

**If you want to uninstall:**
```bash
pipx uninstall devhub-tools
```

### 📊 **Installation Summary**

| Method | Command | Use Case |
|--------|---------|----------|
| **pipx** (Recommended) | `pipx install devhub-tools` | Global CLI tool |
| Virtual Environment | `pip install devhub-tools` | Development |
| User Install | `pip3 install --user devhub-tools` | User-specific |

### 🎉 **Success!**

Once installed, you have access to a powerful developer toolkit with:
- ✅ API testing and benchmarking
- ✅ HTTP header analysis  
- ✅ Code formatting utilities
- ✅ Beautiful CLI interface
- ✅ Plugin system for extensibility

**Your DevHub CLI is now ready to use! 🚀**
