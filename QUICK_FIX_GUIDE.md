# 🔧 DevHub CLI - Quick Fix Guide

## ❌ **Common Installation Errors & Solutions**

### Error 1: `zsh: command not found: pip`
**Solution**: Use `pip3` instead of `pip`
```bash
pip3 install devhub-tools  # But this leads to Error 2...
```

### Error 2: `externally-managed-environment`
**Root Cause**: Modern macOS protects system Python

**✅ SOLUTION**: Use `pipx` (recommended)
```bash
brew install pipx
pipx install devhub-tools
devhub --version
```

### Error 3: `npm install -g @devhub/cli` → `404 Not Found`
**Root Cause**: DevHub is a **Python** package, not Node.js

**✅ SOLUTION**: Use PyPI, not npm
```bash
pipx install devhub-tools  # Correct package name
```

### Error 4: `brew install devhub-cli` → `No available formula`
**Root Cause**: DevHub is published on **PyPI**, not Homebrew

**✅ SOLUTION**: Use pipx to install from PyPI
```bash
pipx install devhub-tools
```

### Error 5: `npx devhub-cli` → `No versions available`  
**Root Cause**: Wrong package name and platform

**✅ SOLUTION**: Use correct package name
```bash
pipx install devhub-tools
devhub --help  # Use 'devhub' command
```

## ✅ **The ONE Command That Works**

```bash
# Install pipx (one-time setup)
brew install pipx

# Install DevHub CLI
pipx install devhub-tools

# Test it works
devhub --version
devhub api test --url https://httpbin.org/get
```

## 🎯 **Key Points to Remember**

1. **Package Name**: `devhub-tools` (NOT `devhub-cli`)
2. **Platform**: PyPI (Python), NOT npm or Homebrew  
3. **Installation Tool**: `pipx` (recommended for CLI tools)
4. **Command**: `devhub` (after installation)

## 🚀 **Quick Test**

After installation, verify everything works:

```bash
devhub --version     # Shows version info
devhub --help        # Shows all commands  
devhub api --help    # Shows API testing options
dh --help           # Short command alias
```

**That's it! Your DevHub CLI is now ready to use! 🎉**
