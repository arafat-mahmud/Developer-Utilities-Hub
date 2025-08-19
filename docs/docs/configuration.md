# Configuration

DevHub provides extensive configuration options to customize its behavior for your specific needs. Configuration can be set globally, per-project, or via environment variables.

## 📁 Configuration Files

DevHub supports multiple configuration file formats:

### TOML (Recommended)
```toml
# devhub.toml or .devhub.toml
[format]
line_length = 88
auto_detect = true

[format.python]
enabled = true
black_args = ["--fast"]

[api]
default_timeout = 30
follow_redirects = true

[security]
password_length = 16
include_symbols = true
```

### YAML
```yaml
# devhub.yaml or .devhub.yaml
format:
  line_length: 88
  auto_detect: true
  python:
    enabled: true
    black_args: ["--fast"]

api:
  default_timeout: 30
  follow_redirects: true

security:
  password_length: 16
  include_symbols: true
```

### JSON
```json
{
  "format": {
    "line_length": 88,
    "auto_detect": true,
    "python": {
      "enabled": true,
      "black_args": ["--fast"]
    }
  },
  "api": {
    "default_timeout": 30,
    "follow_redirects": true
  }
}
```

## 🔍 Configuration Discovery

DevHub searches for configuration files in this order:

1. Command-line arguments (`--config path/to/config`)
2. Environment variable (`DEVHUB_CONFIG_PATH`)
3. Current directory (`.devhub.toml`, `devhub.toml`, etc.)
4. Parent directories (walking up the tree)
5. Home directory (`~/.devhub/config.toml`)
6. System directory (`/etc/devhub/config.toml`)

## ⚙️ Configuration Sections

### Format Plugin

```toml
[format]
# Global formatting options
enabled = true
auto_detect = true  # Auto-detect file types
line_length = 88
dry_run = false
backup = true

[format.python]
enabled = true
formatter = "black"  # or "autopep8", "yapf"
line_length = 88
target_version = ["py38", "py39", "py310"]
skip_string_normalization = false
black_args = []
isort_enabled = true
isort_profile = "black"

[format.javascript]
enabled = true
formatter = "prettier"
print_width = 80
tab_width = 2
use_tabs = false
semicolons = true
single_quote = false
trailing_comma = "es5"

[format.typescript]
enabled = true
formatter = "prettier"
print_width = 80
tab_width = 2

[format.go]
enabled = true
formatter = "gofmt"
simplify = true

[format.rust]
enabled = true
formatter = "rustfmt"
edition = "2021"

[format.json]
enabled = true
indent = 2
sort_keys = false

[format.yaml]
enabled = true
indent = 2
width = 80
```

### API Plugin

```toml
[api]
enabled = true
default_timeout = 30
max_retries = 3
follow_redirects = true
verify_ssl = true
user_agent = "DevHub/1.0.0"

[api.headers]
# Default headers for all requests
"User-Agent" = "DevHub API Client"
"Accept" = "application/json"

[api.auth]
# Default authentication (can be overridden)
type = "bearer"  # or "basic", "api_key"
token = "${API_TOKEN}"  # Environment variable

[api.benchmark]
default_requests = 100
default_concurrency = 10
max_requests = 1000
max_concurrency = 50
```

### Security Plugin

```toml
[security]
enabled = true

[security.password]
length = 16
include_uppercase = true
include_lowercase = true
include_numbers = true
include_symbols = true
exclude_similar = true  # Exclude 0, O, l, 1, etc.
custom_symbols = "!@#$%^&*"

[security.hash]
default_algorithm = "sha256"
salt_length = 32

[security.encryption]
default_algorithm = "AES-256-GCM"
key_derivation = "PBKDF2"
iterations = 100000
```

### Git Plugin

```toml
[git]
enabled = true

[git.clean]
preserve_branches = ["main", "master", "develop", "staging"]
confirm_before_delete = true
remote_tracking = true

[git.commit]
conventional_commits = true
auto_sign = false
gpg_key_id = ""

[git.hooks]
pre_commit_format = true
pre_push_test = false
```

### Data Plugin

```toml
[data]
enabled = true

[data.csv]
delimiter = ","
quote_char = '"'
encoding = "utf-8"
skip_blank_lines = true

[data.json]
indent = 2
sort_keys = false
ensure_ascii = false

[data.yaml]
default_flow_style = false
indent = 2
width = 80
```

### System Plugin

```toml
[system]
enabled = true

[system.monitor]
default_interval = 5
default_duration = 60
include_processes = true
include_network = true
include_disk = true

[system.process]
sort_by = "cpu"  # or "memory", "name", "pid"
show_threads = false
filter_system = false
```

## 🌍 Environment Variables

All configuration options can be set via environment variables using the pattern `DEVHUB_<SECTION>_<KEY>`:

```bash
# Format configuration
export DEVHUB_FORMAT_LINE_LENGTH=100
export DEVHUB_FORMAT_PYTHON_ENABLED=true

# API configuration
export DEVHUB_API_DEFAULT_TIMEOUT=60
export DEVHUB_API_AUTH_TOKEN="your-token-here"

# Security configuration
export DEVHUB_SECURITY_PASSWORD_LENGTH=20

# Plugin enablement
export DEVHUB_PLUGINS_ENABLED="format,api,security"
```

## 🔧 CLI Configuration

Use the built-in configuration commands:

```bash
# Initialize configuration with defaults
devhub config init

# Show current configuration
devhub config show

# Get specific values
devhub config get format.line_length
devhub config get api.default_timeout

# Set configuration values
devhub config set format.line_length 100
devhub config set api.default_timeout 60

# Unset configuration values
devhub config unset format.python.black_args

# Reset to defaults
devhub config reset

# Validate configuration
devhub config validate

# Export configuration
devhub config export --format yaml > devhub.yaml
```

## 🎯 Project-specific Configuration

Create project-specific configurations:

```bash
# Initialize project config
cd my-project
devhub config init --local

# This creates .devhub.toml in the current directory
```

Example project configuration:
```toml
# .devhub.toml (project root)
[format]
line_length = 120  # Wider for this project

[format.python]
target_version = ["py39"]  # Specific Python version

[api]
base_url = "http://localhost:3000"  # Local development server

[plugins]
enabled = ["format", "api"]  # Only enable needed plugins
```

## 📋 Configuration Templates

DevHub provides configuration templates for common use cases:

```bash
# Python project template
devhub config template python

# Web development template
devhub config template web

# Enterprise template
devhub config template enterprise

# Minimal template
devhub config template minimal
```

## 🔒 Secure Configuration

For sensitive data like API tokens:

```toml
[api.auth]
# Use environment variables
token = "${API_TOKEN}"

# Or use external key management
token_file = "/path/to/token/file"

# Or use system keyring
token_keyring = "devhub/api_token"
```

## 🧪 Configuration Profiles

Switch between different configuration profiles:

```bash
# Create profiles
devhub config profile create development
devhub config profile create production

# Switch profiles
devhub config profile use development

# List profiles
devhub config profile list

# Current profile
devhub config profile current
```

## ✅ Configuration Validation

DevHub validates configuration on startup:

```bash
# Manually validate configuration
devhub config validate

# Check for deprecated options
devhub config check-deprecated

# Migration from old versions
devhub config migrate
```

## 🚨 Troubleshooting

### Common Issues

**Configuration not found**
```bash
# Check discovery path
devhub config where

# Debug configuration loading
devhub --debug config show
```

**Invalid configuration**
```bash
# Validate syntax
devhub config validate

# Check specific section
devhub config validate format
```

**Environment variables not working**
```bash
# List all DevHub environment variables
env | grep DEVHUB

# Test variable expansion
devhub config get api.auth.token --expand
```

## 📚 Examples

### Complete Configuration Example

```toml
# Complete devhub.toml example
[global]
log_level = "INFO"
colored_output = true
progress_bars = true

[plugins]
enabled = ["format", "api", "security", "git"]
auto_update = false

[format]
line_length = 88
auto_detect = true
backup = true

[format.python]
enabled = true
formatter = "black"
line_length = 88
isort_enabled = true

[api]
default_timeout = 30
follow_redirects = true
verify_ssl = true

[security]
password_length = 16
include_symbols = true

[git]
preserve_branches = ["main", "develop"]
conventional_commits = true
```

For more configuration examples, see our [Examples Repository](https://github.com/username/devhub-examples).
