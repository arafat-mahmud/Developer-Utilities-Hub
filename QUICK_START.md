# 🚀 DevHub CLI - Working Setup Guide

This guide shows you how to get DevHub working on your system right now.

## ✅ Current Status

DevHub CLI is **fully functional** but requires local installation since it's not yet published to PyPI.

## 🏃‍♂️ Quick Setup (2 minutes)

### Option 1: Automatic Installation
```bash
# Clone and run the installer
git clone https://github.com/arafat-mahmud/Developer-Utilities-Hub.git
cd Developer-Utilities-Hub
./install.sh
```

### Option 2: Manual Installation
```bash
# Clone the repository
git clone https://github.com/arafat-mahmud/Developer-Utilities-Hub.git
cd Developer-Utilities-Hub

# Create virtual environment
python3 -m venv devhub-env
source devhub-env/bin/activate

# Install DevHub
pip install -e .

# Test it works
devhub --help
```

## 🎯 Using DevHub

Once installed, activate the virtual environment and use DevHub:

```bash
# Always activate first
cd Developer-Utilities-Hub
source devhub-env/bin/activate

# Now use DevHub commands
devhub --help
devhub format --help
devhub api --help
```

## ✨ Examples That Work Right Now

```bash
# Format Python code
devhub format code --lang python your_file.py

# Check formatting without changing files
devhub format code --lang python --check your_file.py

# Test APIs
devhub api test --url https://httpbin.org/get

# Get help for any command
devhub format code --help
devhub api test --help
```

## 🔧 Making It Global (Optional)

To use DevHub from anywhere without activating the environment:

### Option 1: Create an alias
Add to your `.zshrc` or `.bashrc`:
```bash
alias devhub='cd /Users/sanon/Developer-Utilities-Hub && source devhub-env/bin/activate && devhub'
```

### Option 2: Use the wrapper script
```bash
# From the DevHub directory
./devhub-wrapper.sh --help
./devhub-wrapper.sh format --help

# You can symlink this to your PATH
sudo ln -s $(pwd)/devhub-wrapper.sh /usr/local/bin/devhub-local
```

## 🚨 Troubleshooting

### "command not found: devhub"
**Solution**: Make sure you've activated the virtual environment:
```bash
cd Developer-Utilities-Hub
source devhub-env/bin/activate
devhub --help
```

### "externally-managed-environment"
**Solution**: This is expected! Use the virtual environment method above instead of system-wide pip install.

### Virtual environment issues
**Solution**: Recreate the environment:
```bash
rm -rf devhub-env
python3 -m venv devhub-env
source devhub-env/bin/activate
pip install -e .
```

## 📋 What Works Now

✅ **Code Formatting**: Python, JavaScript, TypeScript, JSON, YAML, Go, Rust  
✅ **API Testing**: HTTP requests with beautiful output  
✅ **Format Checking**: Verify code formatting without changes  
✅ **Plugin System**: Extensible architecture  
✅ **Rich Help**: Comprehensive help system  

## 🔜 What's Coming

🚧 **PyPI Package**: `pip install devhub-cli` (soon)  
🚧 **Homebrew**: `brew install devhub-cli`  
🚧 **Docker Image**: `docker run devhub/cli`  
🚧 **More Plugins**: Git tools, security utilities, data converters  

## 💡 For Other Programmers

If you're sharing DevHub with other developers, share this repository and tell them to:

1. **Clone the repo**: `git clone https://github.com/arafat-mahmud/Developer-Utilities-Hub.git`
2. **Run the installer**: `cd Developer-Utilities-Hub && ./install.sh`
3. **Use the tool**: `source devhub-env/bin/activate && devhub --help`

## 🎯 Pro Tips

1. **Keep the virtual environment activated** in your terminal session
2. **Use the wrapper script** for global access
3. **Add an alias** to your shell profile for convenience
4. **Check available commands** with `devhub --help`
5. **Use `--help` on any command** for detailed options

---

**Need help?** Create an issue on [GitHub](https://github.com/arafat-mahmud/Developer-Utilities-Hub/issues)
