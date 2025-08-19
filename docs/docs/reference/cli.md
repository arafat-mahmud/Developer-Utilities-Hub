# CLI Reference

Complete command-line interface reference for DevHub.

## Global Options

```bash
devhub [GLOBAL_OPTIONS] COMMAND [COMMAND_OPTIONS] [ARGS]
```

### Global Options

| Option | Description |
|--------|-------------|
| `--version` | Show DevHub version |
| `--help` | Show help message |
| `--config PATH` | Use custom configuration file |
| `--verbose, -v` | Enable verbose output |
| `--quiet, -q` | Suppress output |
| `--debug` | Enable debug mode |
| `--no-color` | Disable colored output |

## Core Commands

### Configuration Management

```bash
# Configuration commands
devhub config init                    # Initialize configuration
devhub config show                    # Show current configuration
devhub config get KEY                 # Get configuration value
devhub config set KEY VALUE           # Set configuration value
devhub config unset KEY               # Remove configuration value
devhub config reset                   # Reset to defaults
devhub config validate                # Validate configuration
```

### Plugin Management

```bash
# Plugin commands
devhub plugin list                    # List available plugins
devhub plugin info PLUGIN             # Show plugin information
devhub plugin enable PLUGIN           # Enable plugin
devhub plugin disable PLUGIN          # Disable plugin
devhub plugin update [PLUGIN]         # Update plugins
```

## Format Plugin

```bash
# Code formatting
devhub format code [OPTIONS] [FILES...]

Options:
  --lang TEXT              Language to format (python, javascript, etc.)
  --line-length INTEGER    Maximum line length
  --dry-run               Show changes without applying
  --check                 Check if formatting needed
  --diff                  Show differences
  --backup                Create backup before formatting
  --recursive             Format directories recursively
```

## API Plugin

```bash
# HTTP API testing
devhub api test [OPTIONS]

Options:
  --url TEXT              URL to test
  --method TEXT           HTTP method (GET, POST, PUT, DELETE)
  --data TEXT             Request body data
  --header TEXT           HTTP headers (can be used multiple times)
  --auth TEXT             Authentication type (bearer, basic, apikey)
  --token TEXT            Authentication token
  --timeout INTEGER       Request timeout in seconds
  --format TEXT           Response format (json, raw)
```

```bash
# API benchmarking
devhub api benchmark [OPTIONS]

Options:
  --url TEXT              URL to benchmark
  --requests INTEGER      Number of requests
  --concurrency INTEGER   Concurrent requests
  --duration TEXT         Test duration (e.g., 30s, 5m)
  --output PATH          Save results to file
```

## Security Plugin

```bash
# Password generation
devhub security password [OPTIONS]

Options:
  --length INTEGER        Password length (default: 16)
  --count INTEGER         Number of passwords (default: 1)
  --no-symbols           Exclude symbols
  --no-numbers           Exclude numbers
  --no-uppercase         Exclude uppercase letters
  --no-lowercase         Exclude lowercase letters
```

```bash
# Hash generation
devhub security hash [OPTIONS] TEXT

Options:
  --algorithm TEXT        Hash algorithm (md5, sha1, sha256, sha512)
  --file PATH            Hash file contents instead of text
```

## Git Plugin

```bash
# Branch management
devhub git clean-branches [OPTIONS]

Options:
  --merged               Only clean merged branches
  --dry-run              Preview without deleting
  --preserve TEXT        Branches to preserve (comma-separated)
  --force                Force deletion without confirmation
```

```bash
# Repository analysis
devhub git stats [OPTIONS]

Options:
  --since TEXT           Analyze commits since date
  --author TEXT          Filter by author
  --format TEXT          Output format (table, json, csv)
```

## Data Plugin

```bash
# Data conversion
devhub data convert FORMAT1 FORMAT2 [OPTIONS] INPUT

Options:
  --output PATH          Output file path
  --indent INTEGER       Indentation for formatted output
  --delimiter TEXT       Delimiter for CSV files
  --encoding TEXT        File encoding (default: utf-8)
```

## System Plugin

```bash
# System monitoring
devhub system monitor [OPTIONS]

Options:
  --interval INTEGER     Monitoring interval in seconds
  --duration INTEGER     Monitoring duration in seconds
  --output PATH          Save metrics to file
  --format TEXT          Output format (table, json, csv)
```

```bash
# Process management
devhub system processes [OPTIONS]

Options:
  --sort TEXT            Sort by (cpu, memory, name, pid)
  --filter TEXT          Filter by process name
  --top INTEGER          Show top N processes
```

## Exit Codes

| Code | Description |
|------|-------------|
| 0 | Success |
| 1 | General error |
| 2 | Configuration error |
| 3 | Plugin error |
| 4 | Network error |
| 5 | Format error |
| 126 | Permission denied |
| 127 | Command not found |

## Environment Variables

| Variable | Description |
|----------|-------------|
| `DEVHUB_CONFIG_PATH` | Path to configuration file |
| `DEVHUB_PLUGIN_PATH` | Additional plugin search paths |
| `DEVHUB_LOG_LEVEL` | Logging level (DEBUG, INFO, WARNING, ERROR) |
| `DEVHUB_NO_COLOR` | Disable colored output |
| `DEVHUB_API_TOKEN` | Default API token |

## Configuration File Locations

DevHub searches for configuration files in this order:

1. Command-line `--config` option
2. `DEVHUB_CONFIG_PATH` environment variable
3. Current directory: `.devhub.toml`, `devhub.toml`, etc.
4. Parent directories (walking up the tree)
5. Home directory: `~/.devhub/config.toml`
6. System directory: `/etc/devhub/config.toml`

## Shell Completion

Enable shell completion for better CLI experience:

```bash
# Bash
eval "$(_DEVHUB_COMPLETE=bash_source devhub)" >> ~/.bashrc

# Zsh
eval "$(_DEVHUB_COMPLETE=zsh_source devhub)" >> ~/.zshrc

# Fish
_DEVHUB_COMPLETE=fish_source devhub > ~/.config/fish/completions/devhub.fish
```

## Examples

### Common Workflows

```bash
# Format Python code and check for issues
devhub format code --lang python --check src/

# Test API with authentication
devhub api test --url https://api.github.com/user \
  --auth bearer --token "$GITHUB_TOKEN"

# Generate secure password and copy to clipboard
devhub security password --length 20 | pbcopy

# Clean up old Git branches
devhub git clean-branches --merged --preserve main,develop

# Convert JSON to CSV
devhub data convert json csv data.json --output data.csv

# Monitor system for 5 minutes
devhub system monitor --duration 300 --interval 10
```

### Advanced Usage

```bash
# Chain commands with pipes
devhub api test --url https://api.github.com/users/octocat | \
  jq '.public_repos' | \
  devhub data convert json csv --output repos.csv

# Batch process files
find . -name "*.py" | xargs devhub format code --lang python

# Configuration management
devhub config set format.python.line_length 100
devhub config set api.default_timeout 60
devhub config validate
```

For more examples, see the [User Guide](../user-guide/formatting.md).
