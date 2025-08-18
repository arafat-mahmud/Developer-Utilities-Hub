# 📚 DevHub CLI - Complete Documentation

## 🚀 **DevHub - The Swiss Army Knife for Developers**

DevHub is a comprehensive CLI toolkit that combines multiple developer utilities into one powerful command-line interface. Built with Python, Rich formatting, and a plugin architecture for extensibility.

---

## 📦 **Installation**

### ✅ **Recommended Installation (pipx)**
```bash
# Install pipx (one-time setup)
brew install pipx

# Install DevHub CLI globally
pipx install devhub-tools

# Verify installation
devhub --version
```

### 🔄 **Alternative Installation Methods**
```bash
# Virtual Environment
python3 -m venv devhub-env
source devhub-env/bin/activate
pip install devhub-tools

# User Installation
pip3 install --user devhub-tools
```

---

## 🎯 **Main Commands Overview**

```bash
devhub --help              # Show main help
devhub --version           # Show version information
devhub -v, --verbose       # Enable verbose output
devhub --config PATH       # Use custom configuration file
```

### Available Commands:
- 🌐 **`api`** - API testing and utilities
- 🎨 **`format`** - Code formatting utilities  
- 🔌 **`plugin`** - Plugin management commands

---

## 🌐 **API Testing Module**

The API module provides comprehensive HTTP testing, benchmarking, and analysis tools.

### **Main Command:**
```bash
devhub api [SUBCOMMAND] [OPTIONS]
```

### **Available Subcommands:**

#### 🧪 **`api test` - HTTP API Testing**
Test any HTTP endpoint with detailed response analysis.

**Usage:**
```bash
devhub api test [OPTIONS]
```

**Options:**
- `-u, --url TEXT` - **[Required]** API endpoint URL
- `-m, --method TEXT` - HTTP method (GET, POST, PUT, DELETE, etc.)
- `-H, --headers TEXT` - Custom headers (format: key:value)
- `-d, --data TEXT` - Request body data
- `-j, --json-data TEXT` - JSON request body
- `-t, --timeout INTEGER` - Request timeout in seconds
- `-v, --verbose` - Verbose output
- `-h, --help` - Show help

**Examples:**
```bash
# Basic GET request
devhub api test --url https://httpbin.org/get

# POST request with JSON data
devhub api test --url https://httpbin.org/post --method POST --json-data '{"name": "test"}'

# Custom headers
devhub api test --url https://api.github.com/user --headers "Authorization: token YOUR_TOKEN"

# With timeout
devhub api test --url https://httpbin.org/delay/5 --timeout 10

# Test real APIs
devhub api test --url https://facebook.com
devhub api test --url https://api.github.com/users/octocat
```

**Output Features:**
- ✅ Beautiful response status display
- ✅ Response time measurement
- ✅ JSON formatting for API responses
- ✅ HTML/Text response handling
- ✅ Error handling and status codes

---

#### 📊 **`api headers` - HTTP Headers Analysis**
Analyze HTTP headers for any URL.

**Usage:**
```bash
devhub api headers [URL]
```

**Examples:**
```bash
# Check website headers
devhub api headers https://httpbin.org
devhub api headers https://github.com
devhub api headers https://google.com

# API endpoint headers
devhub api headers https://api.github.com
```

**Output Features:**
- ✅ Formatted header table display
- ✅ All response headers shown
- ✅ Security headers analysis
- ✅ Server information

---

#### ⚡ **`api benchmark` - Performance Benchmarking**
Performance test API endpoints with concurrent requests.

**Usage:**
```bash
devhub api benchmark [OPTIONS]
```

**Options:**
- `-u, --url TEXT` - **[Required]** API endpoint URL
- `-n, --requests INTEGER` - Number of requests to make
- `-c, --concurrency INTEGER` - Number of concurrent requests
- `-m, --method TEXT` - HTTP method to use
- `-h, --help` - Show help

**Examples:**
```bash
# Basic benchmark
devhub api benchmark --url https://httpbin.org/get --requests 10

# High concurrency test
devhub api benchmark --url https://httpbin.org/get --requests 50 --concurrency 10

# POST benchmark
devhub api benchmark --url https://httpbin.org/post --method POST --requests 20 --concurrency 5
```

**Benchmark Metrics:**
- ✅ Total requests and success rate
- ✅ Failed requests count
- ✅ Total execution time
- ✅ Requests per second
- ✅ Average response time
- ✅ Min/Max response times
- ✅ Status code distribution
- ✅ Real-time progress bar

---

## 🎨 **Code Formatting Module**

Multi-language code formatting and style checking utilities.

### **Main Command:**
```bash
devhub format [SUBCOMMAND] [OPTIONS]
```

### **Available Subcommands:**

#### ✅ **`format check` - Code Style Checking**
Check if code formatting meets standards without modifying files.

```bash
devhub format check [OPTIONS]
```

**Features:**
- Check Python, JavaScript, TypeScript, Go, Rust files
- Non-destructive analysis
- Style compliance reporting

#### 🔧 **`format code` - Code Formatting**
Format source code files according to best practices.

```bash
devhub format code [OPTIONS]
```

**Supported Languages:**
- 🐍 **Python** - Black, autopep8, isort
- 🟨 **JavaScript/TypeScript** - Prettier
- 🦀 **Rust** - rustfmt
- 🐹 **Go** - gofmt
- 📄 **JSON** - Built-in formatter
- 📝 **YAML** - Built-in formatter

**Note:** *Some formatting features may require additional dependencies in global installation.*

---

## 🔌 **Plugin Management**

Manage and extend DevHub with plugins.

### **Main Command:**
```bash
devhub plugin [SUBCOMMAND] [OPTIONS]
```

### **Available Subcommands:**

#### 📋 **`plugin list` - List Available Plugins**
Display all available and loaded plugins.

```bash
devhub plugin list
```

**Plugin Architecture:**
- ✅ **API Plugin** - HTTP testing utilities (Always loaded)
- ⚠️ **Format Plugin** - Code formatting (May require dependencies)
- 🔮 **Future Plugins** - Git, Security, Data conversion, System monitoring

---

## 🎯 **Real-World Usage Examples**

### **API Development & Testing**
```bash
# Test your API during development
devhub api test --url http://localhost:3000/api/users

# Check if your API is returning correct headers
devhub api headers http://localhost:8080/health

# Benchmark your API performance
devhub api benchmark --url http://localhost:3000/api/data --requests 100 --concurrency 10

# Test production APIs
devhub api test --url https://jsonplaceholder.typicode.com/posts/1
```

### **Third-party API Integration**
```bash
# Test GitHub API
devhub api test --url https://api.github.com/users/octocat

# Check REST API endpoints
devhub api test --url https://httpbin.org/get
devhub api test --url https://httpbin.org/post --method POST --json-data '{"test": "data"}'

# Analyze response headers
devhub api headers https://api.stripe.com
```

### **Performance Testing**
```bash
# Quick performance check
devhub api benchmark --url https://httpbin.org/get --requests 20

# Load testing
devhub api benchmark --url https://your-api.com/endpoint --requests 1000 --concurrency 50

# Monitoring API response times
devhub api test --url https://your-service.com/health --verbose
```

### **Development Workflow**
```bash
# Daily development routine
devhub --version                          # Check DevHub version
devhub api test --url http://localhost:3000/api/status  # Test local API
devhub api headers http://localhost:3000  # Check local headers
devhub format check ./src                 # Check code formatting
```

---

## 🎨 **Output Features**

DevHub provides beautiful, informative output using Rich formatting:

### **Visual Elements:**
- 🎨 **Colored output** with syntax highlighting
- 📊 **Tables** for structured data (headers, benchmarks)
- 📈 **Progress bars** for long-running operations
- 🎯 **Status panels** with clear success/error indicators
- 📋 **Formatted JSON** with proper indentation
- ⚡ **Response time indicators**
- 🔢 **Status code highlighting**

### **Information Display:**
- ✅ **Request/Response details**
- ✅ **Performance metrics**
- ✅ **Error messages with context**
- ✅ **Help documentation**
- ✅ **Version and system information**

---

## 🔧 **Configuration & Customization**

### **Configuration File**
```bash
# Use custom config
devhub --config /path/to/config.yaml

# Default config locations:
# ~/.devhub/config.yaml
# ./devhub.yaml
```

### **Verbose Mode**
```bash
# Enable detailed output for any command
devhub -v api test --url https://httpbin.org/get
devhub --verbose api benchmark --url https://httpbin.org/get --requests 10
```

---

## 🚀 **Advanced Usage**

### **Chaining Commands**
```bash
# Test multiple endpoints
devhub api test --url https://httpbin.org/get && \
devhub api test --url https://httpbin.org/post --method POST

# Performance testing workflow
devhub api headers https://your-api.com && \
devhub api benchmark --url https://your-api.com/endpoint --requests 50
```

### **Integration with Other Tools**
```bash
# Use with curl
curl -s https://httpbin.org/get | jq . && devhub api test --url https://httpbin.org/get

# Combine with shell scripts
#!/bin/bash
echo "Testing API endpoints..."
devhub api test --url https://api.github.com/users/octocat
devhub api headers https://api.github.com
```

---

## 🔍 **Troubleshooting**

### **Common Issues:**

#### **"Plugin dependencies not available" Error**
This is normal for global installations. Core functionality (API testing) works perfectly.

**Solutions:**
- Use virtual environment for full formatting features
- Install additional dependencies if needed
- Core API features work regardless of this warning

#### **Installation Issues**
```bash
# If pipx not found
brew install pipx

# If DevHub not found after installation
pipx ensurepath
source ~/.zshrc  # or ~/.bashrc

# If permission issues
pipx uninstall devhub-tools
pipx install devhub-tools --force
```

#### **Network Issues**
```bash
# Test with timeout
devhub api test --url https://slow-endpoint.com --timeout 30

# Check if URL is accessible
devhub api headers https://your-url.com
```

---

## 📊 **Command Reference Quick Guide**

### **Global Options:**
```bash
--version      # Show version information
-v, --verbose  # Enable verbose output  
--config PATH  # Path to configuration file
-h, --help     # Show help message
```

### **API Commands:**
```bash
devhub api test -u URL [-m METHOD] [-H HEADERS] [-d DATA] [-j JSON] [-t TIMEOUT] [-v]
devhub api headers URL
devhub api benchmark -u URL [-n REQUESTS] [-c CONCURRENCY] [-m METHOD]
```

### **Format Commands:**
```bash
devhub format check [PATH]
devhub format code [PATH] [--lang LANGUAGE]
```

### **Plugin Commands:**
```bash
devhub plugin list
```

---

## 🎯 **Tips & Best Practices**

### **Performance Testing:**
- Start with small request numbers (10-20) to test
- Increase concurrency gradually
- Monitor your system resources during large tests
- Use appropriate timeouts for slow endpoints

### **API Development:**
- Test localhost endpoints during development
- Use verbose mode for debugging
- Check headers for security and caching information
- Benchmark critical endpoints regularly

### **Integration:**
- Add DevHub commands to your CI/CD pipeline
- Create shell aliases for frequently used commands
- Use configuration files for team standardization

---

## 🔮 **Future Features (Roadmap)**

### **Coming Soon:**
- 🔐 **Security Plugin** - Password generation, hashing, encryption
- 🐙 **Git Plugin** - Branch management, commit analysis
- 📊 **Data Plugin** - JSON/CSV/YAML conversion
- 🖥️ **System Plugin** - Performance monitoring
- 🐳 **Docker Plugin** - Container management
- ☁️ **Cloud Plugin** - AWS/GCP/Azure utilities

### **Advanced Features:**
- 📈 **Reporting** - Generate performance reports
- 🔄 **Automation** - Scheduled API monitoring
- 🎯 **Templates** - Pre-configured test scenarios
- 🔌 **Custom Plugins** - User-defined extensions

---

## 📞 **Support & Resources**

### **Getting Help:**
```bash
devhub --help           # Main help
devhub api --help       # API module help  
devhub api test --help  # Specific command help
```

### **Community:**
- 📧 **Issues**: GitHub Issues
- 💬 **Discussions**: GitHub Discussions  
- 🐦 **Updates**: Follow development updates
- 📚 **Documentation**: This comprehensive guide

### **Quick Reference:**
- **Package**: `devhub-tools` on PyPI
- **Commands**: `devhub` or `dh` (short alias)
- **Installation**: `pipx install devhub-tools`
- **Version**: 1.0.0

---

**🎉 DevHub CLI - Making developers more productive, one command at a time! 🚀**
