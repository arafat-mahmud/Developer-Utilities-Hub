# 📋 DevHub CLI - Quick Reference Card

## 🚀 **Installation**
```bash
brew install pipx
pipx install devhub-tools
devhub --version
```

## 🎯 **Main Commands**
```bash
devhub --help              # Main help
devhub --version           # Version info
devhub -v [command]        # Verbose mode
```

## 🌐 **API Testing**

### **Test API Endpoint**
```bash
# Basic test
devhub api test --url https://httpbin.org/get

# POST with JSON
devhub api test --url https://httpbin.org/post --method POST --json-data '{"key":"value"}'

# Custom headers
devhub api test --url https://api.github.com/user --headers "Authorization: token TOKEN"

# With timeout
devhub api test --url https://slow-api.com --timeout 30
```

### **Check Headers**
```bash
devhub api headers https://httpbin.org
devhub api headers https://github.com
devhub api headers https://your-api.com
```

### **Benchmark Performance**
```bash
# Basic benchmark
devhub api benchmark --url https://httpbin.org/get --requests 10

# Load test
devhub api benchmark --url https://httpbin.org/get --requests 100 --concurrency 10

# POST benchmark
devhub api benchmark --url https://httpbin.org/post --method POST --requests 20
```

## 🎨 **Code Formatting**
```bash
devhub format check [PATH]        # Check formatting
devhub format code [PATH]         # Format code
devhub format --help              # See options
```

## 🔌 **Plugin Management**
```bash
devhub plugin list               # List plugins
devhub plugin --help             # Plugin help
```

## 🔧 **Common Options**
```bash
-u, --url TEXT          # API endpoint URL
-m, --method TEXT       # HTTP method (GET, POST, etc.)
-H, --headers TEXT      # Custom headers (key:value)
-d, --data TEXT         # Request body data
-j, --json-data TEXT    # JSON request body
-t, --timeout INTEGER   # Request timeout
-n, --requests INTEGER  # Number of requests
-c, --concurrency INT   # Concurrent requests
-v, --verbose           # Verbose output
-h, --help              # Show help
```

## 🎯 **Real-World Examples**

### **API Development**
```bash
# Test local development API
devhub api test --url http://localhost:3000/api/users

# Check API health
devhub api test --url http://localhost:8080/health

# Performance test
devhub api benchmark --url http://localhost:3000/api/data --requests 50
```

### **Third-Party APIs**
```bash
# GitHub API
devhub api test --url https://api.github.com/users/octocat

# Test with authentication
devhub api test --url https://api.service.com/data --headers "API-Key: your-key"

# JSONPlaceholder
devhub api test --url https://jsonplaceholder.typicode.com/posts/1
```

### **Performance Testing**
```bash
# Quick performance check
devhub api benchmark --url https://httpbin.org/get --requests 20

# Load testing
devhub api benchmark --url https://your-api.com --requests 1000 --concurrency 50

# Monitor response times
devhub api test --url https://your-service.com/health --verbose
```

## 📊 **Output Features**
- ✅ Beautiful colored output
- ✅ Response time measurement  
- ✅ Status code highlighting
- ✅ JSON formatting
- ✅ Progress bars for benchmarks
- ✅ Formatted tables for headers
- ✅ Error handling with context

## 🔍 **Troubleshooting**
```bash
# Installation issues
pipx ensurepath
source ~/.zshrc

# Force reinstall
pipx uninstall devhub-tools
pipx install devhub-tools --force

# Plugin dependency warnings are normal
# Core API functionality always works
```

## 🎨 **Aliases & Shortcuts**
```bash
dh --help                    # Short command alias
dh api test --url URL        # Use 'dh' instead of 'devhub'
```

## 📈 **Pro Tips**
- Use `--verbose` for debugging API issues
- Start benchmarks with small numbers (10-20 requests)
- Check headers first to understand API behavior
- Use timeouts for slow endpoints
- Test localhost during development

## 🔗 **Quick Links**
- **Install**: `pipx install devhub-tools`
- **Help**: `devhub --help`
- **Version**: `devhub --version`
- **Package**: https://pypi.org/project/devhub-tools/

---
**🚀 DevHub CLI - Your Swiss Army Knife for Development! 🛠️**
