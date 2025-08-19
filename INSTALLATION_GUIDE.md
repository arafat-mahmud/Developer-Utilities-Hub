# � DevHub Installation Guide

Complete step-by-step installation guide for DevHub CLI on all platforms.

## 🎯 Quick Installation (Recommended)

### ✅ **Method 1: pipx (Best for CLI tools)**

```bash
# Install pipx if not already installed
python -m pip install --user pipx
python -m pipx ensurepath

# Install DevHub CLI
pipx install devhub-tools

# Verify installation
devhub --version
```

**Why pipx?**
- ✅ Installs CLI tools in isolated environments
- ✅ Makes them globally available
- ✅ Prevents dependency conflicts
- ✅ Easy to uninstall: `pipx uninstall devhub-tools`

---

## 🔧 Platform-Specific Installation

### 🍎 **macOS**

#### Option 1: pipx (Recommended)
```bash
# Install Python if not available
brew install python

# Install pipx
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Restart terminal and install DevHub
pipx install devhub-tools
```

#### Option 2: Homebrew (Coming Soon)
```bash
# Future release
brew install devhub-cli
```

#### Option 3: pip
```bash
pip3 install devhub-tools
```

### 🐧 **Linux (Ubuntu/Debian)**

#### Option 1: pipx (Recommended)
```bash
# Install Python and pip
sudo apt update
sudo apt install python3 python3-pip

# Install pipx
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Restart terminal and install DevHub
pipx install devhub-tools
```

#### Option 2: System pip
```bash
# Install DevHub
pip3 install --user devhub-tools

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$HOME/.local/bin:$PATH"
```

### 🐧 **Linux (CentOS/RHEL/Fedora)**

#### Fedora
```bash
# Install Python and pip
sudo dnf install python3 python3-pip

# Install pipx
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Install DevHub
pipx install devhub-tools
```

#### CentOS/RHEL 8+
```bash
# Install Python and pip
sudo dnf install python3 python3-pip

# Install pipx
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Install DevHub
pipx install devhub-tools
```

### 🪟 **Windows**

#### Option 1: pipx (Recommended)
```powershell
# Install Python from Microsoft Store or python.org

# Install pipx
python -m pip install --user pipx
python -m pipx ensurepath

# Restart terminal and install DevHub
pipx install devhub-tools
```

#### Option 2: pip
```powershell
# Install DevHub
pip install devhub-tools
```

#### Option 3: Windows Package Manager (Coming Soon)
```powershell
# Future release
winget install devhub-cli
```

---

## 🐳 **Docker Installation**

### Quick Run
```bash
# Run DevHub with Docker (no installation required)
docker run --rm -v $(pwd):/workspace ghcr.io/arafat-mahmud/devhub:latest --help

# Format code in current directory
docker run --rm -v $(pwd):/workspace ghcr.io/arafat-mahmud/devhub:latest format code --lang python
```

### Docker Alias (Recommended)
```bash
# Add to ~/.bashrc or ~/.zshrc
alias devhub='docker run --rm -v $(pwd):/workspace ghcr.io/arafat-mahmud/devhub:latest'

# Now use devhub normally
devhub --help
devhub api test --url https://httpbin.org/get
```

---

## 🛠️ **Development Installation**

### From Source
```bash
# Clone repository
git clone https://github.com/arafat-mahmud/Developer-Utilities-Hub.git
cd Developer-Utilities-Hub

# Create virtual environment
python -m venv env

# Activate virtual environment
source env/bin/activate  # On macOS/Linux
# env\Scripts\activate   # On Windows

# Install in development mode
pip install -e .

# Or with development dependencies
pip install -e ".[dev]"

# Verify installation
devhub --version
```

### Development Dependencies
```bash
# Install all development tools
pip install -e ".[dev,docs,test]"

# Run tests
pytest

# Run linting
ruff check .

# Format code
black .

# Type checking
mypy .
```

---

## ✅ **Verify Installation**

### Basic Verification
```bash
# Check version
devhub --version

# Get help
devhub --help

# List available plugins
devhub plugin list
```

### Test Core Features
```bash
# Test API functionality
devhub api test --url https://httpbin.org/get

# Test formatting (requires code files)
echo 'print("hello world")' > test.py
devhub format code test.py --lang python
rm test.py
```

### Expected Output
```
$ devhub --version
DevHub CLI v1.0.0
The Swiss Army Knife for Developers

$ devhub --help
🚀 DevHub - The Swiss Army Knife for Developers
...
```

---

## 🔧 **Post-Installation Setup**

### Shell Completion (Optional)
```bash
# For bash
devhub --install-completion bash

# For zsh
devhub --install-completion zsh

# For fish
devhub --install-completion fish
```

### Configuration File (Optional)
```bash
# Create config directory
mkdir -p ~/.config/devhub

# Create basic config
cat > ~/.config/devhub/config.yml << EOF
# DevHub Configuration
verbose: false
format:
  line_length: 88
  check_only: false
api:
  timeout: 30
  verbose: false
EOF
```

---

## � **Troubleshooting**

### Common Issues

#### 1. **Command not found: devhub**

**Solution for pipx:**
```bash
# Ensure pipx is in PATH
python -m pipx ensurepath

# Restart terminal
# Or manually add to PATH
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**Solution for pip:**
```bash
# Check if ~/.local/bin is in PATH
echo $PATH

# Add to PATH if missing
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

#### 2. **Permission denied**

**Linux/macOS:**
```bash
# Use --user flag with pip
pip install --user devhub-tools

# Or use pipx (recommended)
pipx install devhub-tools
```

**Windows:**
```powershell
# Run PowerShell as Administrator, or use --user flag
pip install --user devhub-tools
```

#### 3. **Python version issues**

```bash
# Check Python version
python --version
python3 --version

# DevHub requires Python 3.8+
# Install newer Python if needed
```

#### 4. **Module not found errors**

```bash
# Reinstall with all dependencies
pip uninstall devhub-tools
pip install devhub-tools

# Or try with specific Python version
python3.9 -m pip install devhub-tools
```

#### 5. **Docker permission denied**

```bash
# Add user to docker group (Linux)
sudo usermod -aG docker $USER
newgrp docker

# Or use sudo
sudo docker run --rm ghcr.io/arafat-mahmud/devhub:latest --help
```

### Getting Help

If you're still having issues:

1. 📖 Check our [documentation](docs/)
2. 🔍 Search [existing issues](https://github.com/arafat-mahmud/Developer-Utilities-Hub/issues)
3. 💬 Ask in [discussions](https://github.com/arafat-mahmud/Developer-Utilities-Hub/discussions)
4. 🐛 Report a [new issue](https://github.com/arafat-mahmud/Developer-Utilities-Hub/issues/new)

---

## 🔄 **Updating DevHub**

### pipx
```bash
# Update to latest version
pipx upgrade devhub-tools

# Or reinstall
pipx uninstall devhub-tools
pipx install devhub-tools
```

### pip
```bash
# Update to latest version
pip install --upgrade devhub-tools
```

### Docker
```bash
# Pull latest image
docker pull ghcr.io/arafat-mahmud/devhub:latest
```

---

## 🗑️ **Uninstalling DevHub**

Complete guide to removing DevHub from your system.

### **pipx Uninstall (Recommended)**
```bash
# Uninstall DevHub
pipx uninstall devhub-tools

# Verify removal
devhub --version  # Should show "command not found"

# List remaining pipx packages
pipx list
```

### **pip Uninstall**

#### **Global pip installation:**
```bash
# Uninstall DevHub
pip uninstall devhub-tools

# Verify removal
pip list | grep devhub  # Should show no results
```

#### **User pip installation:**
```bash
# Uninstall user installation
pip uninstall --user devhub-tools

# Check user packages
pip list --user | grep devhub  # Should show no results
```

### **Virtual Environment Uninstall**
```bash
# Method 1: Deactivate and remove environment
deactivate  # If currently activated
rm -rf devhub-env

# Method 2: Uninstall from within environment
source devhub-env/bin/activate  # Activate first
pip uninstall devhub-tools
deactivate
rm -rf devhub-env  # Optional: remove entire environment
```

### **Development Installation Uninstall**
```bash
# Navigate to the project directory
cd Developer-Utilities-Hub

# Uninstall the package
pip uninstall devhub-tools

# Deactivate virtual environment (if using one)
deactivate

# Remove the project directory (optional)
cd ..
rm -rf Developer-Utilities-Hub
```

### **Docker Cleanup**
```bash
# Remove DevHub Docker image
docker rmi ghcr.io/arafat-mahmud/devhub:latest

# Remove all DevHub-related images (if multiple versions)
docker images | grep devhub | awk '{print $3}' | xargs docker rmi

# Remove any containers that used DevHub image
docker ps -a | grep devhub | awk '{print $1}' | xargs docker rm
```

### **Complete System Cleanup**

#### **Remove Configuration Files**
```bash
# Remove user configuration directory
rm -rf ~/.config/devhub

# Remove any project-specific config files you created
rm -f .devhub-config.yml
rm -f devhub.yml
```

#### **Remove Shell Completion**
```bash
# For bash
# Edit ~/.bashrc and remove any lines containing 'devhub'
sed -i '/devhub/d' ~/.bashrc

# For zsh  
# Edit ~/.zshrc and remove any lines containing 'devhub'
sed -i '/devhub/d' ~/.zshrc

# For fish
# Remove completion file if it exists
rm -f ~/.config/fish/completions/devhub.fish
```

#### **Remove Custom Aliases**
```bash
# Check for devhub aliases in shell config
grep -n "alias.*devhub" ~/.bashrc ~/.zshrc ~/.profile 2>/dev/null

# Remove manually or use sed
sed -i '/alias.*devhub/d' ~/.bashrc
sed -i '/alias.*devhub/d' ~/.zshrc
```

#### **Clean Up Environment Variables**
```bash
# Check for DevHub environment variables
env | grep -i devhub

# Remove from shell config files
sed -i '/DEVHUB/d' ~/.bashrc
sed -i '/DEVHUB/d' ~/.zshrc
sed -i '/DEVHUB/d' ~/.profile
```

### **Verification Steps**

After uninstalling, verify complete removal:

```bash
# 1. Check command availability
devhub --version
# Expected: "zsh: command not found: devhub" or "bash: devhub: command not found"

# 2. Check Python packages
pip list | grep devhub
pip list --user | grep devhub
# Expected: No output

# 3. Check pipx packages
pipx list | grep devhub
# Expected: No output

# 4. Check configuration files
ls -la ~/.config/ | grep devhub
# Expected: No output

# 5. Check for remaining files
find / -name "*devhub*" 2>/dev/null | grep -v /proc | head -10
# Expected: Minimal or no results (exclude system/proc files)
```

### **Troubleshooting Uninstall Issues**

#### **"Package not found" Error**
```bash
# If pip says package not found, check installation method
pip list | grep devhub
pipx list | grep devhub

# Try both methods
pip uninstall devhub-tools
pipx uninstall devhub-tools
```

#### **Permission Issues**
```bash
# If permission denied on macOS/Linux
sudo pip uninstall devhub-tools

# Better approach: Check installation location
pip show devhub-tools
# Then use appropriate uninstall method
```

#### **Command Still Available After Uninstall**
```bash
# Check if it's cached or aliased
which devhub
type devhub

# Clear shell hash table
hash -r

# Source your shell config again
source ~/.bashrc  # or ~/.zshrc

# Check if it's an alias
alias | grep devhub
```

#### **Configuration Files Won't Delete**
```bash
# Check file permissions
ls -la ~/.config/devhub/

# Force remove if needed
sudo rm -rf ~/.config/devhub

# Check for hidden files
ls -la ~/.*devhub* 2>/dev/null
```

### **Reinstallation After Uninstall**

If you want to reinstall DevHub after uninstalling:

```bash
# Wait a moment after uninstall, then
pipx install devhub-tools

# Or if there were issues, force reinstall
pipx install --force devhub-tools

# Verify fresh installation
devhub --version
devhub --help
```

---

## 📋 **System Requirements**

## �️ **Uninstalling DevHub**

### pipx
```bash
pipx uninstall devhub-tools
```

### pip
```bash
pip uninstall devhub-tools
```

### Docker
```bash
# Remove image
docker rmi ghcr.io/arafat-mahmud/devhub:latest
```

### Clean up config (optional)
```bash
# Remove config directory
rm -rf ~/.config/devhub

# Remove shell completion
# (varies by shell, check your shell's completion directory)
```

---

## �📋 **System Requirements**

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| **Python** | 3.8+ | 3.10+ |
| **OS** | macOS 10.14+, Ubuntu 18.04+, Windows 10+ | Latest versions |
| **Memory** | 512MB RAM | 1GB+ RAM |
| **Storage** | 100MB available space | 500MB+ available |
| **Network** | Optional (for API features) | Required for updates |

### Optional Dependencies

For enhanced functionality, install these tools:

```bash
# Code formatting
pip install black isort autopep8

# For JavaScript/TypeScript formatting
npm install -g prettier

# For Go formatting
# Install Go from https://golang.org/

# For Rust formatting
# Install Rust from https://rustup.rs/
# rustup component add rustfmt
```

---

## 🎯 **Quick Start After Installation**

```bash
# 1. Verify installation
devhub --version

# 2. Get help
devhub --help

# 3. Try your first command
devhub api test --url https://httpbin.org/get

# 4. Explore available features
devhub plugin list
devhub format --help
devhub api --help

# 5. Read the documentation
# Visit: https://github.com/arafat-mahmud/Developer-Utilities-Hub
```

---

**🎉 Congratulations! You're ready to use DevHub CLI!**

For more information, check out our [Quick Start Guide](docs/quick-start.md) and [User Documentation](docs/).
