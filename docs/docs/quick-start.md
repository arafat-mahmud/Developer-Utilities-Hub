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

# POST with JSON data
devhub api test --url https://httpbin.org/post \
  --method POST \
  --data '{"key": "value"}'

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
