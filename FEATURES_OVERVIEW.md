# 🚀 DevHub CLI - Complete Features Overview

**The Swiss Army Knife for Developers** - A comprehensive overview of all DevHub features with examples and benefits.

---

## 📋 **Table of Contents**

1. [🎨 Code Formatting & Quality](#-code-formatting--quality)
2. [🌐 API Testing & HTTP Tools](#-api-testing--http-tools)
3. [🔧 Plugin System](#-plugin-system)
4. [⚙️ Configuration Management](#-configuration-management)
5. [🛠️ Command-Line Interface](#-command-line-interface)
6. [📊 Benefits & Use Cases](#-benefits--use-cases)
7. [🚀 Installation & Setup](#-installation--setup)

---

## 🎨 **Code Formatting & Quality**

### **Multi-Language Code Formatter**

Format and beautify code across multiple programming languages with industry-standard tools.

#### **Supported Languages**

| Language | Tool Used | Features |
|----------|-----------|----------|
| 🐍 **Python** | Black + isort | PEP 8 compliance, import sorting |
| 🟨 **JavaScript** | Prettier | Consistent style, semicolons, quotes |
| 🔷 **TypeScript** | Prettier | Type-safe formatting |
| 🦀 **Rust** | rustfmt | Official Rust style guide |
| 🐹 **Go** | gofmt | Go standard formatting |
| 📋 **JSON** | Built-in | Pretty printing, validation |
| 📄 **YAML** | PyYAML | Clean structure, proper indentation |

#### **Commands & Examples**

```bash
# Format a single file
devhub format code main.py --lang python

# Format entire directory
devhub format code ./src --lang python

# Check formatting without changes (CI/CD friendly)
devhub format check ./src --lang python

# Show diff of changes
devhub format code main.py --lang python --diff

# Custom line length
devhub format code main.py --lang python --line-length 100
```

#### **Real-World Examples**

**Before Formatting (Python):**
```python
def hello(name):print(f"Hello {name}!");import os,sys
```

**After Formatting:**
```python
import os
import sys


def hello(name):
    print(f"Hello {name}!")
```

**Before Formatting (JSON):**
```json
{"name":"John","age":30,"city":"New York","hobbies":["reading","coding"]}
```

**After Formatting:**
```json
{
  "name": "John",
  "age": 30,
  "city": "New York",
  "hobbies": [
    "reading",
    "coding"
  ]
}
```

#### **Benefits**

- ✅ **Consistent Code Style** - Enforce team standards across projects
- ✅ **Time Saving** - Automated formatting eliminates manual work
- ✅ **CI/CD Integration** - Check formatting in automated pipelines
- ✅ **Multiple Languages** - One tool for all your formatting needs
- ✅ **Industry Standards** - Uses proven, popular formatting tools
- ✅ **Pre-commit Hooks** - Integrate into Git workflow

#### **Use Cases**

1. **Team Development** - Ensure consistent code style across team members
2. **CI/CD Pipelines** - Automated code quality checks
3. **Legacy Code Cleanup** - Clean up and standardize old codebases
4. **Open Source Projects** - Maintain professional code standards
5. **Code Reviews** - Reduce style-related review comments

---

## 🌐 **API Testing & HTTP Tools**

### **Comprehensive HTTP Client with Beautiful Output**

Test, debug, and benchmark HTTP APIs with rich terminal output and detailed metrics.

#### **Core Features**

- 🎯 **HTTP Methods** - GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS
- 📊 **Performance Metrics** - Response times, status codes, headers analysis
- 🎨 **Beautiful Output** - JSON syntax highlighting, structured tables
- 🔍 **Header Inspection** - Detailed request/response header analysis
- ⚡ **Benchmarking** - Load testing with concurrent requests
- 🔒 **Authentication** - Support for various auth methods
- ⏱️ **Timeout Control** - Configurable request timeouts
- 📈 **Progress Tracking** - Real-time progress for benchmarks

#### **Commands & Examples**

**Basic API Testing:**
```bash
# Simple GET request
devhub api test --url https://api.github.com/users/octocat

# POST with JSON data
devhub api test --url https://httpbin.org/post \
  --method POST \
  --json-data '{"name": "John", "age": 30}'

# Custom headers
devhub api test --url https://httpbin.org/headers \
  --headers "Authorization:Bearer token123" \
  --headers "Content-Type:application/json"

# Form data submission
devhub api test --url https://httpbin.org/post \
  --method POST \
  --data "name=John&email=john@example.com"
```

**Advanced Features:**
```bash
# Check response headers only
devhub api headers https://github.com

# Benchmark API performance
devhub api benchmark --url https://httpbin.org/get \
  --requests 100 \
  --concurrency 10

# Test with custom timeout
devhub api test --url https://slow-api.com/endpoint \
  --timeout 60 \
  --verbose
```

#### **Output Examples**

**API Test Response:**
```
┌─ Response Status ──────────────────────────────────────┐
│ 200 • 0.234s • GET https://api.github.com/users/octocat │
└────────────────────────────────────────────────────────┘

┌─ Response Body (JSON) ─────────────────────────────────┐
│ {                                                      │
│   "login": "octocat",                                  │
│   "id": 1,                                             │
│   "name": "The Octocat",                               │
│   "company": "@github",                                │
│   "public_repos": 8,                                   │
│   "followers": 9458                                    │
│ }                                                      │
└────────────────────────────────────────────────────────┘
```

**Benchmark Results:**
```
┌─ Benchmark Results ────────────────────────────────────┐
│ Metric            │ Value                              │
├───────────────────┼────────────────────────────────────┤
│ Total Requests    │ 100                                │
│ Successful        │ 98                                 │
│ Failed            │ 2                                  │
│ Total Time        │ 4.567s                             │
│ Requests/sec      │ 21.89                              │
│ Avg Response Time │ 0.234s                             │
│ Min Response Time │ 0.123s                             │
│ Max Response Time │ 1.456s                             │
└─────────────────────────────────────────────────────────┘

┌─ Status Code Distribution ─────────────────────────────┐
│ Status Code │ Count                                    │
├─────────────┼──────────────────────────────────────────┤
│ 200         │ 98                                       │
│ 500         │ 2                                        │
└─────────────────────────────────────────────────────────┘
```

#### **Benefits**

- ✅ **Beautiful Output** - Rich terminal formatting with colors and tables
- ✅ **Performance Insights** - Detailed timing and benchmark data
- ✅ **Debugging Support** - Verbose mode for troubleshooting
- ✅ **Load Testing** - Built-in benchmarking capabilities
- ✅ **Development Workflow** - Perfect for API development and testing
- ✅ **CI/CD Integration** - Automated API health checks
- ✅ **Documentation** - Great for API documentation examples

#### **Use Cases**

1. **API Development** - Test endpoints during development
2. **Integration Testing** - Verify API integrations work correctly
3. **Performance Monitoring** - Regular performance checks
4. **Documentation** - Generate API usage examples
5. **Debugging** - Troubleshoot API issues with detailed output
6. **Load Testing** - Simple load testing for APIs
7. **CI/CD Health Checks** - Automated endpoint verification

---

## 🔧 **Plugin System**

### **Modular, Extensible Architecture**

DevHub is built on a flexible plugin system that allows for easy extension and customization.

#### **Current Plugins**

| Plugin | Status | Description |
|--------|---------|-------------|
| 🎨 **format** | ✅ Active | Multi-language code formatting |
| 🌐 **api** | ✅ Active | HTTP API testing and benchmarking |
| 🔀 **git** | 🚧 Planned | Git workflow automation |
| 🔐 **security** | 🚧 Planned | Security tools and password generation |
| 📊 **data** | 🚧 Planned | Data format conversion |
| 🖥️ **system** | 🚧 Planned | System monitoring and diagnostics |

#### **Plugin Management**

```bash
# List all available plugins
devhub plugin list

# Get detailed plugin information
devhub plugin info format
devhub plugin info api

# Check plugin availability
devhub plugin list  # Shows status indicators
```

#### **Plugin Architecture Benefits**

- ✅ **Modular Design** - Only load features you need
- ✅ **Easy Extension** - Add new functionality without core changes
- ✅ **Community Contributions** - Third-party plugin support
- ✅ **Lightweight** - Minimal overhead for unused features
- ✅ **Isolation** - Plugin errors don't affect core functionality

---

## ⚙️ **Configuration Management**

### **Flexible Configuration System**

Customize DevHub behavior with configuration files and command-line options.

#### **Configuration Options**

```bash
# Global command options
devhub --verbose api test --url https://example.com
devhub --config ./custom-config.yml format code main.py

# Create configuration file
mkdir -p ~/.config/devhub
cat > ~/.config/devhub/config.yml << EOF
# DevHub Configuration
verbose: false

# Format plugin settings
format:
  line_length: 88
  check_only: false

# API plugin settings
api:
  timeout: 30
  verbose: false
EOF
```

#### **Configuration Hierarchy**

1. **Command-line arguments** (highest priority)
2. **Custom config file** (`--config path`)
3. **User config file** (`~/.config/devhub/config.yml`)
4. **Default settings** (lowest priority)

#### **Benefits**

- ✅ **Personalization** - Customize behavior to your preferences
- ✅ **Team Standards** - Share configuration across team members
- ✅ **Environment-Specific** - Different configs for different environments
- ✅ **Override Flexibility** - Command-line options override config files

---

## 🛠️ **Command-Line Interface**

### **Rich, User-Friendly CLI Experience**

DevHub provides an intuitive command-line interface with comprehensive help and beautiful output.

#### **CLI Features**

- 🎨 **Rich Output** - Colors, tables, progress bars, and panels
- 📖 **Comprehensive Help** - Detailed help for every command
- ⚡ **Fast Performance** - Quick startup and execution times
- 🔍 **Error Handling** - Clear error messages and debugging info
- 🎯 **Tab Completion** - Shell completion support
- 📊 **Progress Tracking** - Visual progress for long operations

#### **Global Commands**

```bash
# Get help and version info
devhub --help
devhub --version

# Enable verbose output
devhub --verbose <command>

# Use custom configuration
devhub --config ./config.yml <command>

# Plugin management
devhub plugin list
devhub plugin info <plugin-name>
```

#### **Help System Examples**

```bash
# Global help
devhub --help

# Plugin-specific help
devhub format --help
devhub api --help

# Command-specific help
devhub format code --help
devhub api test --help
devhub api benchmark --help
```

#### **Benefits**

- ✅ **Intuitive Design** - Easy to learn and use
- ✅ **Rich Feedback** - Beautiful, informative output
- ✅ **Self-Documenting** - Comprehensive built-in help
- ✅ **Error-Friendly** - Clear error messages and suggestions
- ✅ **Performance** - Fast execution and minimal overhead

---

## 📊 **Benefits & Use Cases**

### **Why Choose DevHub CLI?**

#### **Developer Benefits**

1. **🎯 All-in-One Solution**
   - Replace multiple tools with one unified CLI
   - Consistent interface across different functionalities
   - Reduced context switching and tool learning

2. **⚡ Productivity Boost**
   - Automated code formatting saves time
   - Quick API testing without external tools
   - Rich output makes debugging faster

3. **🤝 Team Collaboration**
   - Consistent code formatting across team
   - Shared configuration files
   - Standardized development workflows

4. **🔧 Development Workflow Integration**
   - Git pre-commit hooks
   - CI/CD pipeline integration
   - IDE and editor integration

5. **📈 Quality Improvement**
   - Automated code quality checks
   - Performance monitoring
   - Consistent standards enforcement

#### **Enterprise Benefits**

1. **🏢 Standardization**
   - Organization-wide code standards
   - Consistent tooling across teams
   - Reduced onboarding time for new developers

2. **💰 Cost Efficiency**
   - Open source with no licensing costs
   - Reduced tool sprawl and maintenance
   - Faster development cycles

3. **🔒 Security & Privacy**
   - Local-first approach (no data sent to external services)
   - Open source transparency
   - Self-hosted deployment options

4. **📊 Scalability**
   - Plugin architecture for custom extensions
   - Configuration management for large teams
   - CI/CD integration for automated workflows

### **Real-World Use Cases**

#### **Daily Development**
```bash
# Morning workflow
devhub format code ./src --lang python        # Format overnight changes
devhub api test --url http://localhost:8000/health  # Check local dev server
```

#### **Pre-Commit Workflow**
```bash
# Git pre-commit hook
#!/bin/bash
devhub format check ./src --lang python
if [ $? -ne 0 ]; then
    echo "❌ Code formatting issues found"
    echo "🔧 Run: devhub format code ./src --lang python"
    exit 1
fi
```

#### **CI/CD Pipeline**
```yaml
# GitHub Actions
- name: Check code formatting
  run: devhub format check ./src --lang python

- name: Test API endpoints  
  run: devhub api test --url ${{ env.STAGING_API_URL }}/health
```

#### **API Development**
```bash
# Test API during development
devhub api test --url http://localhost:3000/api/users \
  --method POST \
  --headers "Authorization:Bearer $TOKEN" \
  --json-data '{"name": "Test User"}'

# Benchmark performance
devhub api benchmark --url http://localhost:3000/api/search \
  --requests 100 --concurrency 5
```

#### **Code Review Process**
```bash
# Before code review
devhub format code ./feature-branch --lang python
devhub api test --url $STAGING_URL/new-endpoint
```

---

## 🚀 **Installation & Setup**

### **Quick Installation Guide**

#### **Recommended: pipx Installation**
```bash
# Install pipx (one-time setup)
python -m pip install --user pipx
python -m pipx ensurepath

# Install DevHub CLI
pipx install devhub-tools

# Verify installation
devhub --version
```

#### **Alternative Installation Methods**

**Virtual Environment:**
```bash
python -m venv devhub-env
source devhub-env/bin/activate  # On macOS/Linux
pip install devhub-tools
```

**User Installation:**
```bash
pip install --user devhub-tools
```

**Development Installation:**
```bash
git clone https://github.com/arafat-mahmud/Developer-Utilities-Hub.git
cd Developer-Utilities-Hub
python -m venv env
source env/bin/activate
pip install -e .
```

#### **Verification & Testing**
```bash
# Basic verification
devhub --version
devhub --help
devhub plugin list

# Test core features
devhub api test --url https://httpbin.org/get
echo 'def hello():print("world")' > test.py
devhub format code test.py --lang python
```

#### **Post-Installation Setup**
```bash
# Optional: Create configuration
mkdir -p ~/.config/devhub
cat > ~/.config/devhub/config.yml << EOF
verbose: false
format:
  line_length: 88
api:
  timeout: 30
EOF

# Optional: Shell completion
devhub --install-completion bash  # or zsh, fish
```

### **Uninstalling DevHub**

If you need to remove DevHub from your system:

#### **pipx Uninstall (Recommended)**
```bash
# Uninstall DevHub
pipx uninstall devhub-tools

# Verify removal
devhub --version  # Should show "command not found"
```

#### **pip Uninstall**
```bash
# Standard uninstall
pip uninstall devhub-tools

# User installation uninstall
pip uninstall --user devhub-tools
```

#### **Development Installation Cleanup**
```bash
# Navigate to project directory and uninstall
cd Developer-Utilities-Hub
pip uninstall devhub-tools

# Remove the entire project
cd ..
rm -rf Developer-Utilities-Hub
```

#### **Complete Cleanup (Optional)**
```bash
# Remove configuration files
rm -rf ~/.config/devhub

# Remove shell completion
# Edit your shell config file (~/.bashrc, ~/.zshrc, etc.)
# and remove any devhub completion lines

# Remove any custom aliases
# Edit your shell config and remove devhub aliases
```

#### **Docker Cleanup**
```bash
# Remove Docker image
docker rmi ghcr.io/arafat-mahmud/devhub:latest

# Remove Docker alias (if created)
# Edit ~/.bashrc or ~/.zshrc and remove the devhub alias
```

---

## 🎯 **Summary**

DevHub CLI is a comprehensive developer toolkit that combines multiple essential development utilities into one powerful, extensible command-line interface. With its focus on code formatting, API testing, and beautiful output, DevHub streamlines daily development workflows while maintaining the flexibility to grow with your needs through its plugin architecture.

### **Key Strengths**
- 🎨 **Multi-language code formatting** with industry-standard tools
- 🌐 **Comprehensive API testing** with beautiful, informative output
- 🧩 **Extensible plugin architecture** for future growth
- ⚡ **Performance-focused** with fast startup and execution
- 🔒 **Privacy-first** local processing approach
- 🤝 **Team-friendly** with configuration sharing and CI/CD integration

### **Perfect For**
- Individual developers seeking to streamline their toolkit
- Development teams wanting consistent standards and workflows
- Organizations looking for unified, cost-effective developer tools
- DevOps engineers integrating quality checks into CI/CD pipelines
- Open source projects maintaining professional code standards

**Ready to get started?** Install DevHub CLI today and experience the difference of having all your essential developer tools in one beautiful, powerful interface.

```bash
pipx install devhub-tools
devhub --help
```

**Happy coding with DevHub! 🚀**
