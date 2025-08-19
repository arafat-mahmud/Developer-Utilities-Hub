# 🚀 DevHub Quick Start Guide

Get up and running with DevHub CLI in minutes!

## ⚡ Installation (2 minutes)

### 🎯 **Fastest Installation**
```bash
# Install pipx (one-time setup)
python -m pip install --user pipx
python -m pipx ensurepath

# Install DevHub CLI
pipx install devhub-tools

# Verify it works
devhub --version
```

**Expected Output:**
```
DevHub CLI v1.0.0
The Swiss Army Knife for Developers
```

---

## 🧪 **Test Your Installation**

### 1. **Get Help**
```bash
devhub --help
```

### 2. **List Available Features**
```bash
devhub plugin list
```

### 3. **Test API Functionality**
```bash
devhub api test --url https://httpbin.org/get
```

You should see a beautiful formatted response showing JSON data, status codes, and timing information.

---

## � **Core Features & Examples**

### 🌐 **API Testing**

#### **Basic API Test**
```bash
# Test a simple GET request
devhub api test --url https://api.github.com/users/octocat
```

#### **POST Request with JSON Data**
```bash
devhub api test --url https://httpbin.org/post \
  --method POST \
  --json-data '{"name": "John", "age": 30}'
```

#### **Custom Headers**
```bash
devhub api test --url https://httpbin.org/headers \
  --headers "Authorization:Bearer your-token" \
  --headers "Content-Type:application/json"
```

#### **Check Response Headers**
```bash
devhub api headers https://github.com
```

#### **Benchmark API Performance**
```bash
devhub api benchmark --url https://httpbin.org/get --requests 50 --concurrency 5
```

### 🎨 **Code Formatting**

#### **Format Python Code**
```bash
# Create a sample Python file
echo 'def hello(name):print(f"Hello {name}!")' > test.py

# Format it
devhub format code test.py --lang python

# Check the result
cat test.py
```

#### **Format Multiple Files**
```bash
# Format all Python files in a directory
devhub format code ./src --lang python
```

#### **Check Without Modifying**
```bash
# Dry run - see what would be changed
devhub format code test.py --lang python --diff
devhub format check ./src --lang python
```

#### **Format JSON**
```bash
# Create messy JSON
echo '{"name":"John","age":30,"city":"NYC"}' > data.json

# Format it beautifully
devhub format code data.json --lang json

# Check result
cat data.json
```

#### **Format YAML**
```bash
# Format YAML files
devhub format code config.yml --lang yaml
```

---

## 🎯 **Real-World Workflows**

### 📝 **Daily Development Routine**

```bash
# 1. Format your code before committing
devhub format code ./src --lang python

# 2. Test your local API
devhub api test --url http://localhost:8000/api/health

# 3. Check external dependencies
devhub api test --url https://api.github.com/rate_limit
```

### 🔍 **API Development & Testing**

```bash
# Test API during development
devhub api test --url http://localhost:3000/api/users --method GET

# Test with authentication
devhub api test --url http://localhost:3000/api/users \
  --method POST \
  --headers "Authorization:Bearer $TOKEN" \
  --json-data '{"name": "New User", "email": "user@example.com"}'

# Benchmark your API
devhub api benchmark --url http://localhost:3000/api/health --requests 100
```

### 📊 **Code Quality Checks**

```bash
# Check if code needs formatting (CI/CD friendly)
devhub format check ./src --lang python

# Format specific file types
devhub format code ./src --lang python
devhub format code ./config --lang yaml
devhub format code ./data --lang json
```

---

## �️ **Command Reference**

### **Global Options**
```bash
--help, -h          # Show help
--version           # Show version
--verbose, -v       # Verbose output
--config FILE       # Use custom config file
```

### **API Commands**
```bash
# Test API endpoint
devhub api test --url URL [options]

# Options:
--method, -m        # HTTP method (GET, POST, PUT, DELETE, etc.)
--headers, -H       # Headers (can use multiple times)
--data, -d          # Raw request body
--json-data, -j     # JSON request body
--timeout, -t       # Request timeout (seconds)
--verbose, -v       # Show detailed information

# Check headers
devhub api headers URL

# Benchmark API
devhub api benchmark --url URL --requests N --concurrency C
```

### **Format Commands**
```bash
# Format code files
devhub format code FILES... --lang LANGUAGE [options]

# Check formatting
devhub format check PATH --lang LANGUAGE

# Options:
--lang, -l          # Language: python, javascript, typescript, json, yaml, go, rust
--check, -c         # Check only (don't modify files)
--diff, -d          # Show differences
--line-length       # Maximum line length (default: 88)
```

### **Plugin Commands**
```bash
# List available plugins
devhub plugin list

# Get plugin information
devhub plugin info PLUGIN_NAME
```

---

## 🎨 **Output Examples**

### **API Test Output**
When you run `devhub api test --url https://api.github.com/users/octocat`, you'll see:

```
┌─ Response Status ──────────────────────────────────────┐
│ 200 • 0.234s • GET https://api.github.com/users/octocat │
└────────────────────────────────────────────────────────┘

┌─ Response Body (JSON) ─────────────────────────────────┐
│ {                                                      │
│   "login": "octocat",                                  │
│   "id": 1,                                             │
│   "name": "The Octocat",                               │
│   "public_repos": 8                                    │
│   ...                                                  │
│ }                                                      │
└────────────────────────────────────────────────────────┘
```

### **Benchmark Output**
```
┌─ Benchmark Results ────────────────────────────────────┐
│ Total Requests    │ 50                                 │
│ Successful        │ 50                                 │
│ Failed            │ 0                                  │
│ Total Time        │ 2.345s                             │
│ Requests/sec      │ 21.32                              │
│ Avg Response Time │ 0.047s                             │
│ Min Response Time │ 0.023s                             │
│ Max Response Time │ 0.089s                             │
└────────────────────────────────────────────────────────┘
```

---

## ⚙️ **Configuration**

### **Create Config File (Optional)**
```bash
mkdir -p ~/.config/devhub
cat > ~/.config/devhub/config.yml << EOF
# DevHub Configuration
verbose: false

# Format settings
format:
  line_length: 88
  check_only: false

# API settings  
api:
  timeout: 30
  verbose: false
EOF
```

### **Use Custom Config**
```bash
devhub --config ./my-config.yml api test --url https://example.com
```

---

## 🚨 **Troubleshooting**

### **Command Not Found**
```bash
# If devhub command is not found
which devhub
echo $PATH

# Fix: Add pipx bin to PATH
pipx ensurepath
source ~/.bashrc  # or ~/.zshrc
```

### **Permission Issues**
```bash
# Use pipx instead of pip
pipx install devhub-tools

# Or install for user only
pip install --user devhub-tools
```

### **Python Version Issues**
```bash
# Check Python version (requires 3.8+)
python --version
python3 --version

# Install newer Python if needed
```

---

## 🎯 **Next Steps**

### **Explore More Features**
```bash
# See all available commands
devhub --help

# Get detailed help for each feature
devhub api --help
devhub format --help
```

### **Integration Examples**

#### **Pre-commit Hook**
```bash
# .git/hooks/pre-commit
#!/bin/bash
devhub format check ./src --lang python
if [ $? -ne 0 ]; then
    echo "Code formatting check failed. Run: devhub format code ./src --lang python"
    exit 1
fi
```

#### **CI/CD Pipeline**
```yaml
# .github/workflows/ci.yml
- name: Check code formatting
  run: devhub format check ./src --lang python

- name: Test API endpoints
  run: devhub api test --url ${{ env.API_URL }}/health
```

#### **Development Script**
```bash
#!/bin/bash
# dev-workflow.sh

echo "🎨 Formatting code..."
devhub format code ./src --lang python

echo "🧪 Testing API..."
devhub api test --url http://localhost:8000/health

echo "✅ Ready for commit!"
```

---

## �️ **Uninstalling DevHub**

If you need to remove DevHub:

### **pipx (Recommended)**
```bash
pipx uninstall devhub-tools
```

### **pip**
```bash
pip uninstall devhub-tools
# or
pip uninstall --user devhub-tools
```

### **Virtual Environment**
```bash
# Simply remove the environment directory
rm -rf devhub-env
```

### **Clean Up (Optional)**
```bash
# Remove configuration
rm -rf ~/.config/devhub

# Remove shell completion (if added)
# Edit your shell config file and remove devhub completion lines
```

---

## �📚 **Learn More**

- 📖 **[Full Documentation](README.md)** - Complete feature guide
- 🔧 **[Installation Guide](INSTALLATION_GUIDE.md)** - Detailed installation options
- 🤝 **[Contributing](CONTRIBUTING.md)** - How to contribute
- 🐛 **[Issues](https://github.com/arafat-mahmud/Developer-Utilities-Hub/issues)** - Report bugs or request features

---

## 🎉 **You're Ready!**

Congratulations! You now know how to:
- ✅ Install and configure DevHub CLI
- ✅ Test APIs with beautiful output
- ✅ Format code across multiple languages
- ✅ Use DevHub in your daily workflow
- ✅ Integrate DevHub into CI/CD pipelines

**Happy coding with DevHub! 🚀**
