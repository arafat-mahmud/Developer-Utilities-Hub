# Quick Start Guide

Get up and running with DevHub in minutes! This guide covers the essential commands and workflows you'll use daily.

## 🚀 First Steps

After [installation](installation.md), verify DevHub is working:

```bash
# Check version and available commands
devhub --version
devhub --help
```

## 🎨 Code Formatting

DevHub supports multiple programming languages with automatic detection:

```bash
# Format a single file
devhub format code src/main.py

# Format an entire directory
devhub format code --lang python src/

# Format multiple languages at once
devhub format code --lang python,javascript src/

# Check what would be formatted (dry run)
devhub format code --dry-run src/
```

### Supported Languages

- **Python**: Uses Black + isort
- **JavaScript/TypeScript**: Uses Prettier
- **Go**: Uses gofmt
- **Rust**: Uses rustfmt
- **JSON/YAML**: Built-in formatters

## 🌐 API Testing

Test and benchmark APIs with beautiful output:

```bash
# Simple GET request
devhub api test --url https://api.github.com/users/octocat

# Quick Start Guide

Get up and running with DevHub in minutes! This guide covers the essential commands and workflows you'll use daily.

## 🚀 First Steps

After [installation](installation.md), verify DevHub is working:

```bash
# Check version and available commands
devhub --version
devhub --help

# List available plugins
devhub plugin list
```

## 🎨 Code Formatting

DevHub supports multiple programming languages with intelligent formatting:

```bash
# Format a single Python file
devhub format code main.py --lang python

# Format all Python files in a directory
devhub format code ./src --lang python

# Check what would be formatted (dry run)
devhub format code main.py --lang python --diff

# Check if files need formatting (CI/CD friendly)
devhub format check ./src --lang python

# Format with custom line length
devhub format code main.py --lang python --line-length 100
```

### Supported Languages

- **Python**: Uses Black + isort for PEP 8 compliance
- **JavaScript/TypeScript**: Uses Prettier for consistent style
- **Go**: Uses gofmt for Go standard formatting
- **Rust**: Uses rustfmt for Rust style guide
- **JSON**: Built-in formatter with proper indentation
- **YAML**: PyYAML formatter for clean YAML files

### Format Examples

```bash
# Create and format a messy Python file
echo 'def hello(name):print(f"Hello {name}!")' > test.py
devhub format code test.py --lang python
cat test.py  # See the beautifully formatted result

# Format JSON data
echo '{"name":"John","age":30}' > data.json
devhub format code data.json --lang json
cat data.json  # Pretty printed JSON

# Format YAML configuration
devhub format code config.yml --lang yaml
```

## 🌐 API Testing

Test and benchmark APIs with beautiful, informative output:

```bash
# Simple GET request
devhub api test --url https://api.github.com/users/octocat

# POST with JSON data
devhub api test --url https://httpbin.org/post \
  --method POST \
  --json-data '{"name": "John", "age": 30}'

# Add custom headers (multiple headers supported)
devhub api test --url https://httpbin.org/headers \
  --headers "Authorization:Bearer token123" \
  --headers "Content-Type:application/json"

# Send form data
devhub api test --url https://httpbin.org/post \
  --method POST \
  --data "name=John&age=30"

# Check response headers only
devhub api headers https://github.com

# Benchmark an endpoint
devhub api benchmark --url https://httpbin.org/get \
  --requests 50 \
  --concurrency 5

# Test with timeout and verbose output
devhub api test --url https://slow-api.com/endpoint \
  --timeout 60 \
  --verbose
```

### API Testing Features

- **Beautiful Response Formatting**: JSON syntax highlighting and structured output
- **Performance Metrics**: Response times, status codes, and benchmarking
- **Header Inspection**: Detailed request and response header analysis
- **Error Handling**: Clear error messages and debugging information
- **Timeout Control**: Configurable request timeouts
- **Concurrent Testing**: Load testing with concurrent requests

## 🔧 Plugin Management

Manage DevHub's modular plugin system:

```bash
# List all available plugins
devhub plugin list

# Get detailed information about a plugin
devhub plugin info format
devhub plugin info api
```

Current available plugins:
- **format**: Multi-language code formatting
- **api**: HTTP API testing and benchmarking

## ⚙️ Configuration

Configure DevHub for your preferences:

```bash
# Use verbose output globally
devhub --verbose api test --url https://httpbin.org/get

# Use custom configuration file
devhub --config ./my-config.yml format code main.py

# Create a configuration file
mkdir -p ~/.config/devhub
cat > ~/.config/devhub/config.yml << EOF
verbose: false
format:
  line_length: 88
  check_only: false
api:
  timeout: 30
  verbose: false
EOF
```

## 📋 Common Workflows

### Daily Development Workflow

```bash
# 1. Format your code before committing
devhub format code ./src --lang python

# 2. Test your local API endpoints
devhub api test --url http://localhost:8000/api/health

# 3. Check external API dependencies
devhub api test --url https://api.github.com/rate_limit

# 4. Verify code formatting in CI/CD
devhub format check ./src --lang python
```

### API Development & Testing

```bash
# Test API during development
devhub api test --url http://localhost:3000/api/users --method GET

# Test authentication
devhub api test --url http://localhost:3000/api/users \
  --method POST \
  --headers "Authorization:Bearer $API_TOKEN" \
  --json-data '{"name": "New User", "email": "user@example.com"}'

# Load test your API
devhub api benchmark --url http://localhost:3000/api/health \
  --requests 100 \
  --concurrency 10

# Check API response headers
devhub api headers https://api.your-service.com/v1/status
```

### Code Quality Assurance

```bash
# Pre-commit formatting check
devhub format check ./src --lang python
if [ $? -ne 0 ]; then
    echo "❌ Code formatting issues found"
    echo "🔧 Run: devhub format code ./src --lang python"
    exit 1
fi

# Format multiple language types
devhub format code ./src --lang python
devhub format code ./config --lang yaml  
devhub format code ./data --lang json
devhub format code ./frontend --lang javascript
```

### CI/CD Integration

```bash
# GitHub Actions example
- name: Check code formatting
  run: devhub format check ./src --lang python

- name: Test API endpoints
  run: devhub api test --url ${{ secrets.STAGING_API_URL }}/health

# Pre-commit hook example
#!/bin/bash
devhub format check ./src --lang python
if [ $? -ne 0 ]; then
    echo "Code formatting check failed"
    echo "Run: devhub format code ./src --lang python"
    exit 1
fi
```

## 💡 Tips and Tricks

### Performance Tips

- Use `--diff` to preview formatting changes before applying
- Use `--check` for CI/CD to verify formatting without modifying files
- Format specific file types with `--lang` to avoid unnecessary processing
- Use `--verbose` for debugging API issues

### Command Shortcuts

```bash
# Most commands support short aliases
devhub -h          # --help
devhub -v          # --verbose
devhub format -l   # --lang
devhub api -m      # --method
devhub api -u      # --url
```

### Integration Examples

**VS Code Settings:**
```json
{
  "python.formatting.provider": "none",
  "python.formatting.blackPath": "devhub format code --lang python"
}
```

**Makefile Integration:**
```makefile
format:
	devhub format code ./src --lang python

format-check:
	devhub format check ./src --lang python

test-api:
	devhub api test --url http://localhost:8000/health
```

**Package.json Scripts:**
```json
{
  "scripts": {
    "format": "devhub format code ./src --lang javascript",
    "format:check": "devhub format check ./src --lang javascript",
    "test:api": "devhub api test --url http://localhost:3000/health"
  }
}
```

## 🚨 Troubleshooting

### Common Issues

**Command not found:**
```bash
# Check if devhub is in PATH
which devhub
echo $PATH

# If using pipx
pipx ensurepath
source ~/.bashrc  # or ~/.zshrc
```

**Formatting tool not found:**
```bash
# Install required formatters
pip install black isort          # Python
npm install -g prettier          # JavaScript/TypeScript
# Install Go from https://golang.org
# Install Rust from https://rustup.rs
```

**API connection issues:**
```bash
# Use verbose mode for debugging
devhub api test --url https://example.com --verbose

# Test with longer timeout
devhub api test --url https://slow-api.com --timeout 60
```

**Uninstalling DevHub:**
```bash
# pipx uninstall (recommended)
pipx uninstall devhub-tools

# pip uninstall
pip uninstall devhub-tools

# Clean up configuration (optional)
rm -rf ~/.config/devhub
```

## 🆘 Getting Help

```bash
# Get help for any command
devhub --help
devhub format --help
devhub api --help
devhub format code --help
devhub api test --help

# Get plugin information
devhub plugin list
devhub plugin info format
```

### Community Support

- 📖 [Full Documentation](https://github.com/arafat-mahmud/Developer-Utilities-Hub/blob/main/README.md)
- 💬 [GitHub Discussions](https://github.com/arafat-mahmud/Developer-Utilities-Hub/discussions)
- 🐛 [GitHub Issues](https://github.com/arafat-mahmud/Developer-Utilities-Hub/issues)
- 🔧 [Installation Guide](installation.md)

## 🚀 Next Steps

- Explore advanced formatting options in the [User Guide](user-guide/formatting.md)
- Learn about API testing features in the [API Guide](user-guide/api.md)
- Check out [Plugin Development](plugins/creating.md) to extend DevHub
- See [Configuration Guide](configuration.md) for customization options

Happy coding with DevHub! 🎉

# Add custom headers
devhub api test --url https://api.example.com \
  --header "Authorization: Bearer token123" \
  --header "Content-Type: application/json"

# Benchmark an endpoint
devhub api benchmark --url https://api.github.com \
  --requests 100 \
  --concurrency 10
```

## 🔐 Security Tools

Generate secure passwords and hashes:

```bash
# Generate a strong password
devhub gen password --length 20 --symbols

# Generate multiple passwords
devhub gen password --count 5

# Hash a string
devhub security hash --text "hello world" --algorithm sha256

# Generate API keys
devhub gen apikey --length 32
```

## 🔄 Git Workflow

Automate common Git operations:

```bash
# Clean up merged branches
devhub git clean-branches --merged

# Analyze commit history
devhub git analyze --since "1 month ago"

# Generate commit message
devhub git suggest-commit

# Check repository health
devhub git health-check
```

## 📊 Data Conversion

Convert between data formats easily:

```bash
# JSON to CSV
devhub convert json2csv data.json --output data.csv

# CSV to JSON
devhub convert csv2json data.csv --output data.json

# YAML to JSON
devhub convert yaml2json config.yaml

# Pretty print JSON
devhub convert json data.json --pretty
```

## 🖥️ System Monitoring

Monitor system resources and processes:

```bash
# Quick system overview
devhub monitor system

# Continuous monitoring
devhub monitor system --interval 5 --duration 60

# Monitor specific processes
devhub monitor process --name python

# Check disk usage
devhub monitor disk --path /home/user
```

## ⚙️ Configuration

Configure DevHub for your preferences:

```bash
# Initialize configuration
devhub config init

# View current configuration
devhub config show

# Set configuration values
devhub config set format.python.line_length 88
devhub config set api.default_timeout 30

# Reset to defaults
devhub config reset
```

## 🔧 Plugin Management

Manage DevHub plugins:

```bash
# List available plugins
devhub plugin list

# Enable/disable plugins
devhub plugin enable format
devhub plugin disable git

# Plugin information
devhub plugin info format

# Update plugins
devhub plugin update
```

## 📋 Common Workflows

### Daily Development Workflow

```bash
# Format code before committing
devhub format code src/

# Test APIs during development
devhub api test --url http://localhost:3000/api/health

# Generate secure tokens
devhub gen password --length 16

# Clean up Git branches weekly
devhub git clean-branches --merged
```

### CI/CD Integration

```bash
# In your CI pipeline
devhub format code --check src/  # Fail if not formatted
devhub api test --url $STAGING_URL  # Test staging
devhub security scan src/  # Security check
```

### Data Processing

```bash
# Convert and process data files
devhub convert csv2json raw_data.csv | \
  jq '.[] | select(.status == "active")' | \
  devhub convert json2csv --output filtered.csv
```

## 💡 Tips and Tricks

### Performance

- Use `--dry-run` to preview changes before applying
- Format specific file types: `devhub format code --lang python`
- Use `--quiet` flag for CI/CD scripts

### Shortcuts

- Most commands have short aliases: `devhub fmt` = `devhub format`
- Use shell completion: `devhub completion bash >> ~/.bashrc`
- Set environment variables: `export DEVHUB_CONFIG_PATH=~/.devhub`

### Integration

- **VS Code**: Install the DevHub extension
- **Git hooks**: Add to pre-commit hooks
- **Make/npm scripts**: Add common commands to build scripts

## 🆘 Getting Help

- Use `--help` on any command: `devhub format --help`
- Check the [User Guide](user-guide/formatting.md) for detailed documentation
- Visit [GitHub Discussions](https://github.com/username/devhub/discussions) for community support
- Report issues on [GitHub Issues](https://github.com/username/devhub/issues)

## 🚀 Next Steps

- Explore the [User Guide](user-guide/formatting.md) for detailed feature documentation
- Learn about [Plugin Development](plugins/architecture.md) to extend DevHub
- Join our [Community](https://discord.gg/devhub) to stay updated

Happy coding with DevHub! 🎉
