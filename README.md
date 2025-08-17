# 🚀 DevHub - Developer Utilities Hub

<div align="center">

![DevHub Logo](https://via.placeholder.com/300x100/1e1e2e/cdd6f4?text=DevHub%20CLI)

**The Swiss Army Knife for Developers**  
*One CLI tool to rule them all*

[![PyPI version](https://badge.fury.io/py/devhub-cli.svg)](https://badge.fury.io/py/devhub-cli)
[![Downloads](https://pepy.tech/badge/devhub-cli)](https://pepy.tech/project/devhub-cli)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

[🎬 Demo](#demo) • [📦 Installation](#installation) • [🔧 Features](#features) • [🤝 Contributing](#contributing)

</div>

## 🎯 What is DevHub?

DevHub is a powerful, extensible CLI tool that combines the most useful developer utilities into one unified interface. Stop juggling multiple tools - DevHub has everything you need for your daily development workflow.

## 🎬 Why DevHub CLI?

- ✅ **Free tier**: 60 requests/min and 1,000 requests/day with personal account
- ⚡ **Powerful DevHub Pro**: Access to advanced features and higher limits
- 🔧 **Built-in tools**: Code formatting, API testing, file operations, shell commands, web fetching
- 🧩 **Extensible**: Plugin architecture for custom integrations
- 💻 **Terminal-first**: Designed for developers who live in the command line
- 🔒 **Open source**: Apache 2.0 licensed

## 📦 Installation

DevHub CLI is an open-source developer agent that brings the power of multiple development tools directly into your terminal. It provides lightweight access to essential developer utilities, giving you the most direct path from your prompt to productivity.

## 🎬 Demo

![DevHub in Action](docs/demo.gif)

```bash
# Format your code across multiple languages
devhub format --lang python --path ./src

# Clean up Git branches and commits
devhub git clean-branches --merged

# Test APIs with beautiful output
devhub api test --url https://api.github.com/users/octocat --method GET

# Generate secure passwords
devhub gen password --length 16 --symbols

# Convert data formats instantly
devhub convert json2csv data.json --output data.csv

# Monitor system performance
devhub monitor system --interval 5
```

## 📦 Installation

### 🔥 Quick Install
```bash
pip install devhub-cli
```

### 🚀 Alternative Installation Methods

#### Install globally with npm (Node.js)
```bash
npm install -g @devhub/cli
```

#### Install globally with Homebrew (macOS/Linux)
```bash
brew install devhub-cli
```

#### Run instantly with npx
```bash
# Using npx (no installation required)
npx devhub-cli --help
```

### 🛠️ From Source (Development)
```bash
# Clone the repository
git clone https://github.com/arafat-mahmud/Developer-Utilities-Hub.git
cd Developer-Utilities-Hub

# Create and activate virtual environment
python3 -m venv devhub-env
source devhub-env/bin/activate  # On macOS/Linux
# or
devhub-env\Scripts\activate     # On Windows

# Install in development mode
pip install -e .

# Verify installation
devhub --help
```

### 🐳 Docker
```bash
# Run with Docker
docker run --rm -v $(pwd):/workspace devhub/cli format --lang python
```

### 📋 System Requirements

- **Python**: 3.8 or higher
- **Operating System**: macOS, Linux, Windows
- **Node.js**: 20 or higher (for npm installation)
- **Memory**: 512MB RAM minimum
- **Storage**: 100MB available space

## 🔧 Features

### 🎨 Code Management
- **Multi-language Formatter** - Format Python, JavaScript, Go, Rust, and more
- **Linting & Quality Checks** - Integrated with popular linters
- **Dependency Analysis** - Analyze and update project dependencies

### 📊 Git Utilities
- **Smart Branch Cleanup** - Remove merged/stale branches
- **Commit Analysis** - Analyze commit patterns and statistics
- **Release Management** - Automated changelog generation

### 🌐 API & Network Tools
- **API Testing** - Beautiful HTTP client with response formatting
- **Network Diagnostics** - Ping, traceroute, port scanning
- **SSL Certificate Checker** - Validate and monitor certificates

### 🔐 Security & Crypto
- **Password Generator** - Secure password generation with custom rules
- **Hash Calculator** - MD5, SHA256, bcrypt and more
- **Encryption Tools** - File encryption/decryption utilities

### 📈 Data Processing
- **Format Converters** - JSON ↔ CSV ↔ YAML ↔ XML
- **Data Validation** - JSON Schema, CSV validation
- **Text Processing** - Regex testing, text transformations

### 🖥️ System Monitoring
- **Performance Monitor** - CPU, Memory, Disk usage
- **Process Management** - Kill processes, monitor resources
- **System Information** - Hardware specs, OS details

## 🚀 Quick Start

```bash
# Install DevHub
pip install devhub-cli

# Get help
devhub --help

# Format a Python file
devhub format code --lang python main.py

# Test an API endpoint
devhub api test --url https://httpbin.org/get

# Generate a secure password
devhub gen password --length 20

# Check available plugins
devhub plugin list
```

## 🎯 Getting Started

### Basic Usage

**Start in current directory**
```bash
devhub
```

**Include multiple directories**
```bash
devhub --include-directories ./lib,./docs
```

**Use specific model**
```bash
devhub -m gemini-2.5-flash
```

**Non-interactive mode for scripts**
```bash
devhub -p "Explain the architecture of this codebase"
```

### Quick Examples

**Start a new project**
```bash
cd new-project/
devhub
> Write me a Discord bot that answers questions using a FAQ.md file I will provide
```

**Analyze existing code**
```bash
#### Analyze existing code
```bash
git clone https://github.com/google-gemini/gemini-cli
cd gemini-cli
devhub
> Give me a summary of all of the changes that went in yesterday
```

## 📖 Documentation

| Command Category | Documentation |
|-----------------|---------------|
| 📝 **Formatting** | [Format Guide](docs/formatting.md) |
| 🔀 **Git Tools** | [Git Guide](docs/git.md) |
| 🌐 **API Testing** | [API Guide](docs/api.md) |
| 🔐 **Security** | [Security Guide](docs/security.md) |
| 📊 **Data Tools** | [Data Guide](docs/data.md) |
| 🖥️ **System** | [System Guide](docs/system.md) |

## 🏗️ Architecture

DevHub follows a modular plugin architecture:

```
devhub/
├── core/           # Core CLI framework
├── plugins/        # Feature modules
│   ├── format/     # Code formatting
│   ├── git/        # Git utilities
│   ├── api/        # API tools
│   ├── security/   # Security tools
│   ├── data/       # Data processing
│   └── system/     # System monitoring
├── utils/          # Shared utilities
└── tests/          # Test suite
```

## 🤝 Contributing

We love contributions! DevHub is designed to be easily extensible.

### 🔧 Adding a New Plugin

1. Create a new plugin directory: `devhub/plugins/myplugin/`
2. Implement the plugin interface
3. Add tests and documentation
4. Submit a PR!

See our [Contributing Guide](CONTRIBUTING.md) for detailed instructions.

### 🐛 Found a Bug?

Please open an issue with:
- DevHub version (`devhub --version`)
- Operating system
- Steps to reproduce

## 📊 Plugin Ecosystem

| Plugin | Description | Status |
|--------|-------------|--------|
| 🎨 **formatter** | Multi-language code formatting | ✅ Stable |
| 🔀 **git** | Git workflow automation | ✅ Stable |
| 🌐 **api** | HTTP API testing tools | ✅ Stable |
| 🔐 **security** | Security and crypto utilities | ✅ Stable |
| 📊 **data** | Data format conversion | ✅ Stable |
| 🖥️ **system** | System monitoring | ✅ Stable |
| 🐳 **docker** | Docker management | 🚧 Coming Soon |
| ☁️ **cloud** | Cloud provider tools | 🚧 Coming Soon |
| 📱 **mobile** | Mobile dev utilities | 💡 Planned |

## 🎯 Roadmap

- [x] Core CLI framework
- [x] Plugin system architecture
- [x] Basic formatting tools
- [x] Git utilities
- [x] API testing
- [x] Security tools
- [ ] Web dashboard interface
- [ ] VS Code extension
- [ ] GitHub Actions integration
- [ ] Cloud deployment tools
- [ ] AI-powered code suggestions

## 🏆 Why DevHub?

### ⚡ **Performance First**
- Written in Python with C extensions for speed
- Minimal startup time
- Efficient memory usage

### 🧩 **Extensible**
- Plugin architecture
- Custom command creation
- Third-party integrations

### 🎯 **Developer Experience**
- Intuitive command structure
- Rich help system
- Beautiful output formatting

### 🔒 **Secure**
- No data collection
- Local-first approach
- Security-focused utilities


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Click](https://click.palletsprojects.com/) for CLI framework
- Inspired by the amazing developer community
- Thanks to all our [contributors](https://github.com/username/devhub/graphs/contributors)

## 📞 Support

- 📖 [Documentation](https://devhub-cli.readthedocs.io/)
- 💬 [Discussions](https://github.com/username/devhub/discussions)
- 🐛 [Issues](https://github.com/username/devhub/issues)
- 🐦 [@devhub_cli](https://twitter.com/devhub_cli)

---

<div align="center">

**Made with ❤️ by developers, for developers**

[⭐ Star us on GitHub](https://github.com/username/devhub) • [🐦 Follow on Twitter](https://twitter.com/devhub_cli) • [📖 Read the Docs](https://devhub-cli.readthedocs.io/)

</div>
