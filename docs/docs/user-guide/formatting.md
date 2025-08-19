# Code Formatting

DevHub's formatting plugin provides powerful multi-language code formatting capabilities with a unified interface and beautiful output.

## 🎯 Overview

The format plugin supports:

- **Python**: Black, autopep8, yapf + isort
- **JavaScript/TypeScript**: Prettier + ESLint
- **Go**: gofmt + goimports
- **Rust**: rustfmt
- **JSON**: Built-in formatter
- **YAML**: Built-in formatter
- **CSS/SCSS**: Prettier
- **HTML**: Prettier
- **Markdown**: Prettier

## 🚀 Basic Usage

### Format Single Files

```bash
# Auto-detect file type and format
devhub format code main.py

# Specify language explicitly
devhub format code --lang python main.py

# Format multiple files
devhub format code src/main.py src/utils.py tests/test_main.py
```

### Format Directories

```bash
# Format entire directory
devhub format code src/

# Format with specific language
devhub format code --lang python src/

# Format multiple languages
devhub format code --lang python,javascript src/

# Recursive formatting
devhub format code --recursive project/
```

### Dry Run Mode

```bash
# Preview changes without applying
devhub format code --dry-run src/

# Check if files need formatting
devhub format code --check src/

# Exit with error if formatting needed (CI/CD)
devhub format code --check --fail-on-change src/
```

## 🐍 Python Formatting

### Black Integration

```bash
# Format with Black (default)
devhub format code --lang python src/

# Custom line length
devhub format code --lang python --line-length 100 src/

# Fast mode
devhub format code --lang python --fast src/

# Specific Python versions
devhub format code --lang python --target-version py38,py39 src/
```

### Configuration

```toml
[format.python]
enabled = true
formatter = "black"  # or "autopep8", "yapf"
line_length = 88
target_version = ["py38", "py39", "py310"]
skip_string_normalization = false
skip_magic_trailing_comma = false

# Import sorting with isort
isort_enabled = true
isort_profile = "black"
isort_line_length = 88
isort_multi_line_output = 3

# Additional Black arguments
black_args = ["--fast"]
```

### Examples

```bash
# Format Python files with custom settings
devhub format code \
  --lang python \
  --line-length 100 \
  --target-version py39 \
  src/

# Format with import sorting
devhub format code \
  --lang python \
  --isort \
  --isort-profile black \
  src/

# Check formatting for CI
devhub format code \
  --lang python \
  --check \
  --diff \
  src/
```

## 🌐 JavaScript/TypeScript Formatting

### Prettier Integration

```bash
# Format JavaScript/TypeScript
devhub format code --lang javascript src/
devhub format code --lang typescript src/

# Custom settings
devhub format code \
  --lang javascript \
  --print-width 120 \
  --tab-width 4 \
  --single-quote \
  src/
```

### Configuration

```toml
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

[format.typescript]
enabled = true
formatter = "prettier"
print_width = 80
tab_width = 2
# Inherits from javascript config
```

## 🔧 Go Formatting

```bash
# Format Go files
devhub format code --lang go src/

# With imports organization
devhub format code --lang go --imports src/

# Simplify code
devhub format code --lang go --simplify src/
```

### Configuration

```toml
[format.go]
enabled = true
formatter = "gofmt"
simplify = true
imports = true  # Use goimports
```

## 🦀 Rust Formatting

```bash
# Format Rust files
devhub format code --lang rust src/

# Custom edition
devhub format code --lang rust --edition 2021 src/

# Check formatting
devhub format code --lang rust --check src/
```

### Configuration

```toml
[format.rust]
enabled = true
formatter = "rustfmt"
edition = "2021"
max_width = 100
hard_tabs = false
tab_spaces = 4
```

## 📄 Data Format Formatting

### JSON

```bash
# Format JSON files
devhub format code --lang json data/

# Custom indentation
devhub format code --lang json --indent 4 config.json

# Sort keys
devhub format code --lang json --sort-keys data.json
```

### YAML

```bash
# Format YAML files
devhub format code --lang yaml config/

# Custom settings
devhub format code \
  --lang yaml \
  --indent 4 \
  --width 120 \
  config.yaml
```

### Configuration

```toml
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

## 🎨 Advanced Features

### Language Detection

DevHub automatically detects file types:

```bash
# Auto-detection based on file extension
devhub format code src/main.py        # Detected as Python
devhub format code src/app.js         # Detected as JavaScript
devhub format code config.json        # Detected as JSON

# Override detection
devhub format code --lang python script  # No extension
```

### Batch Operations

```bash
# Format multiple file types
devhub format code \
  --lang python,javascript,json \
  --recursive \
  project/

# Format specific patterns
devhub format code --pattern "*.py,*.js" src/

# Exclude patterns
devhub format code --exclude "*.min.js,*test*" src/
```

### Backup and Safety

```bash
# Create backups before formatting
devhub format code --backup src/

# Custom backup directory
devhub format code --backup-dir .backups src/

# Restore from backup
devhub format restore --backup-id 20231201_143052
```

### Integration with Git

```bash
# Format only changed files
devhub format code --git-diff HEAD~1

# Format staged files
devhub format code --git-staged

# Format files in current branch
devhub format code --git-branch feature/new-feature
```

## 📊 Output and Reporting

### Progress and Statistics

```bash
# Show progress bar
devhub format code --progress src/

# Detailed statistics
devhub format code --stats src/

# JSON output for parsing
devhub format code --output json src/
```

### Diff Output

```bash
# Show differences
devhub format code --diff src/

# Colored diff
devhub format code --diff --color src/

# Save diff to file
devhub format code --diff --output-file changes.diff src/
```

## 🔧 Configuration Examples

### Project-specific Configuration

```toml
# .devhub.toml in project root
[format]
line_length = 120
auto_detect = true
backup = false

[format.python]
enabled = true
formatter = "black"
line_length = 120
target_version = ["py39"]
isort_enabled = true
isort_profile = "black"

[format.javascript]
enabled = true
print_width = 120
single_quote = true
trailing_comma = "all"
```

### Team Configuration

```toml
# Shared team configuration
[format]
line_length = 88
auto_detect = true
backup = true

[format.python]
enabled = true
formatter = "black"
isort_enabled = true
isort_profile = "black"

# Enforce consistent settings
[format.javascript]
enabled = true
formatter = "prettier"
print_width = 80
tab_width = 2
single_quote = false
```

## 🚀 CI/CD Integration

### GitHub Actions

```yaml
name: Code Format Check
on: [push, pull_request]

jobs:
  format:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    - name: Install DevHub
      run: pip install devhub-cli
    - name: Check formatting
      run: devhub format code --check --fail-on-change src/
```

### Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: devhub-format
        name: DevHub Format
        entry: devhub format code
        language: system
        types: [python, javascript, typescript]
```

### Make/npm Scripts

```makefile
# Makefile
format:
	devhub format code src/

format-check:
	devhub format code --check src/

format-diff:
	devhub format code --diff src/
```

```json
{
  "scripts": {
    "format": "devhub format code src/",
    "format:check": "devhub format code --check src/",
    "format:diff": "devhub format code --diff src/"
  }
}
```

## 🚨 Troubleshooting

### Common Issues

**Formatter not found**
```bash
# Install required formatter
pip install black isort  # For Python
npm install -g prettier  # For JavaScript

# Check installed formatters
devhub format check-deps
```

**Permission errors**
```bash
# Check file permissions
ls -la src/main.py

# Fix permissions
chmod 644 src/main.py
```

**Configuration conflicts**
```bash
# Validate configuration
devhub config validate

# Check formatter-specific configs
devhub format config-check --lang python
```

### Performance Tips

- Use `--fast` mode for Python formatting in development
- Format incrementally with `--git-diff` in large projects
- Use `--parallel` for faster directory formatting
- Exclude large files with `--exclude` patterns

## 📚 Examples Repository

For more examples and configuration templates, visit:
[DevHub Examples](https://github.com/username/devhub-examples/tree/main/formatting)
