# Configuration Reference

Comprehensive reference for DevHub configuration options.

## Configuration File Formats

DevHub supports TOML (recommended), YAML, and JSON configuration formats:

```toml
# devhub.toml (recommended)
[global]
log_level = "INFO"
colored_output = true

[plugins]
enabled = ["format", "api", "security"]

[format]
line_length = 88
auto_detect = true
```

```yaml
# devhub.yaml
global:
  log_level: INFO
  colored_output: true

plugins:
  enabled:
    - format
    - api
    - security

format:
  line_length: 88
  auto_detect: true
```

## Global Configuration

### Core Settings

```toml
[global]
# Logging configuration
log_level = "INFO"              # DEBUG, INFO, WARNING, ERROR
log_file = "~/.devhub/logs/devhub.log"
colored_output = true           # Enable colored terminal output
progress_bars = true            # Show progress bars

# Performance settings
max_workers = 4                 # Maximum worker threads
timeout = 30                    # Default operation timeout
cache_enabled = true            # Enable result caching
cache_ttl = 3600               # Cache TTL in seconds
```

### Plugin Management

```toml
[plugins]
# Plugin enablement
enabled = ["format", "api", "security", "git"]
disabled = ["experimental"]

# Plugin settings
auto_update = false             # Auto-update plugins
update_check_interval = 86400   # Check for updates (seconds)
plugin_paths = [               # Additional plugin search paths
    "~/.devhub/plugins",
    "/opt/devhub/plugins"
]
```

## Plugin-Specific Configuration

### Format Plugin

```toml
[format]
# Global formatting options
enabled = true
line_length = 88
auto_detect = true              # Auto-detect file types
backup = false                  # Create backups before formatting
dry_run = false                # Default to dry-run mode
recursive = true               # Format directories recursively

# Language-specific settings
[format.python]
enabled = true
formatter = "black"             # black, autopep8, yapf
line_length = 88
target_version = ["py38", "py39", "py310"]
skip_string_normalization = false
skip_magic_trailing_comma = false

# isort configuration
isort_enabled = true
isort_profile = "black"
isort_line_length = 88
isort_multi_line_output = 3

# Additional formatter arguments
black_args = ["--fast"]
autopep8_args = ["--aggressive"]
yapf_args = ["--style=pep8"]

[format.javascript]
enabled = true
formatter = "prettier"
print_width = 80
tab_width = 2
use_tabs = false
semicolons = true
single_quote = false
trailing_comma = "es5"
bracket_spacing = true
arrow_parens = "always"

# ESLint integration
eslint_enabled = false
eslint_fix = false

[format.typescript]
enabled = true
# Inherits from javascript configuration
extends = "format.javascript"

[format.go]
enabled = true
formatter = "gofmt"
simplify = true
imports = true                  # Use goimports

[format.rust]
enabled = true
formatter = "rustfmt"
edition = "2021"
max_width = 100
hard_tabs = false
tab_spaces = 4

[format.json]
enabled = true
indent = 2
sort_keys = false
ensure_ascii = false

[format.yaml]
enabled = true
indent = 2
width = 80
default_flow_style = false
```

### API Plugin

```toml
[api]
enabled = true

# Request defaults
default_timeout = 30
max_retries = 3
retry_delay = 1                 # Seconds between retries
follow_redirects = true
verify_ssl = true
user_agent = "DevHub/1.0.0"

# Connection settings
connection_pool_size = 10
max_redirects = 30
keep_alive = true

# Default headers
[api.headers]
"User-Agent" = "DevHub API Client"
"Accept" = "application/json"
"Accept-Encoding" = "gzip, deflate"

# Authentication defaults
[api.auth]
type = "bearer"                 # bearer, basic, apikey, none
token = "${API_TOKEN}"          # Environment variable reference
username = ""
password = ""

# API key settings
api_key_header = "X-API-Key"
api_key_param = "api_key"

# Benchmarking defaults
[api.benchmark]
default_requests = 100
default_concurrency = 10
max_requests = 10000
max_concurrency = 100
warmup_requests = 10

# Output settings
[api.output]
format = "json"                 # json, yaml, table, raw
pretty_print = true
show_headers = true
show_timing = true
show_status = true
```

### Security Plugin

```toml
[security]
enabled = true

# Password generation
[security.password]
length = 16
include_uppercase = true
include_lowercase = true
include_numbers = true
include_symbols = true
exclude_similar = true          # Exclude 0, O, l, 1, etc.
exclude_ambiguous = true        # Exclude {, }, [, ], etc.
custom_symbols = "!@#$%^&*"
min_entropy = 60               # Minimum entropy bits

# Hash settings
[security.hash]
default_algorithm = "sha256"    # md5, sha1, sha256, sha512
salt_length = 32
iterations = 100000            # For PBKDF2

# Encryption settings
[security.encryption]
default_algorithm = "AES-256-GCM"
key_derivation = "PBKDF2"
iterations = 100000
salt_length = 32

# Security scanning
[security.scan]
enabled = true
check_secrets = true
check_permissions = true
exclude_patterns = [
    "*.pyc",
    "__pycache__",
    ".git",
    "node_modules"
]
```

### Git Plugin

```toml
[git]
enabled = true

# Branch management
[git.clean]
preserve_branches = ["main", "master", "develop", "staging", "production"]
confirm_before_delete = true
remote_tracking = true
force_delete = false

# Commit settings
[git.commit]
conventional_commits = true
auto_sign = false
gpg_key_id = ""
template_file = ""

# Analysis settings
[git.analysis]
default_since = "30 days ago"
include_merges = false
author_aliases = {}             # Map of author email aliases

# Hook settings
[git.hooks]
pre_commit_format = true
pre_commit_lint = false
pre_push_test = false
commit_msg_validate = true
```

### Data Plugin

```toml
[data]
enabled = true

# CSV settings
[data.csv]
delimiter = ","
quote_char = '"'
escape_char = "\\"
encoding = "utf-8"
skip_blank_lines = true
header = true

# JSON settings
[data.json]
indent = 2
sort_keys = false
ensure_ascii = false
separators = [",", ":"]

# YAML settings
[data.yaml]
default_flow_style = false
indent = 2
width = 80
allow_unicode = true

# XML settings
[data.xml]
encoding = "utf-8"
pretty_print = true
declaration = true
```

### System Plugin

```toml
[system]
enabled = true

# Monitoring settings
[system.monitor]
default_interval = 5            # Seconds
default_duration = 60          # Seconds
include_processes = true
include_network = true
include_disk = true
include_memory = true
include_cpu = true

# Process settings
[system.process]
sort_by = "cpu"                # cpu, memory, name, pid
show_threads = false
filter_system = false
update_interval = 1

# Alert settings
[system.alerts]
enabled = false
cpu_threshold = 80             # Percentage
memory_threshold = 90          # Percentage
disk_threshold = 95            # Percentage
webhook_url = ""
email_notifications = false
```

## Environment-Specific Configuration

### Development Environment

```toml
# .devhub.toml (project root)
[global]
log_level = "DEBUG"
colored_output = true

[format]
backup = true                  # Create backups in development
dry_run = false

[api]
base_url = "http://localhost:3000"
verify_ssl = false            # For self-signed certificates

[git]
conventional_commits = true
pre_commit_format = true
```

### Production Environment

```toml
# Production configuration
[global]
log_level = "WARNING"
log_file = "/var/log/devhub/devhub.log"

[format]
backup = false                # No backups in production
check_only = true            # Only check, don't modify

[api]
verify_ssl = true
timeout = 10                 # Shorter timeout
max_retries = 1

[security]
password.length = 32         # Longer passwords
encryption.iterations = 200000
```

## Configuration Inheritance

Configuration is merged in this order (later values override earlier ones):

1. Default values
2. System configuration (`/etc/devhub/config.toml`)
3. User configuration (`~/.devhub/config.toml`)
4. Project configuration (`.devhub.toml` in project root)
5. Environment variables (`DEVHUB_*`)
6. Command-line arguments

## Environment Variable Mapping

All configuration options can be set via environment variables:

```bash
# Global settings
export DEVHUB_GLOBAL_LOG_LEVEL=DEBUG
export DEVHUB_GLOBAL_COLORED_OUTPUT=true

# Plugin settings
export DEVHUB_FORMAT_LINE_LENGTH=100
export DEVHUB_API_DEFAULT_TIMEOUT=60
export DEVHUB_SECURITY_PASSWORD_LENGTH=20

# Nested settings (use double underscore)
export DEVHUB_FORMAT_PYTHON__FORMATTER=black
export DEVHUB_API_AUTH__TOKEN=your-token-here
```

## Configuration Validation

DevHub validates configuration using JSON Schema:

```bash
# Validate current configuration
devhub config validate

# Validate specific file
devhub config validate --file custom-config.toml

# Show validation schema
devhub config schema
```

## Configuration Examples

### Minimal Configuration

```toml
# Minimal .devhub.toml
[plugins]
enabled = ["format"]

[format]
line_length = 88
```

### Complete Configuration

See [examples/complete-config.toml](https://github.com/username/devhub-examples/blob/main/config/complete-config.toml) for a comprehensive configuration example.

## Migration

### From v1.x to v2.x

```bash
# Migrate old configuration
devhub config migrate --from-version 1.x

# Check for deprecated options
devhub config check-deprecated
```

For more configuration examples, visit: [DevHub Configuration Examples](https://github.com/username/devhub-examples/tree/main/config)
