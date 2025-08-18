# DevHub - The Swiss Army Knife for Developers

Welcome to DevHub, a comprehensive command-line interface (CLI) tool that combines multiple developer utilities into one powerful, extensible platform.

## 🚀 What is DevHub?

DevHub is designed to be the ultimate developer toolkit, offering:

- **Multi-language code formatting** for Python, JavaScript, TypeScript, Go, Rust, JSON, and YAML
- **API testing and benchmarking** with beautiful output
- **Git workflow automation** for branch management and commit analysis  
- **Security utilities** for password generation and encryption
- **Data format conversion** between JSON, CSV, YAML, and XML
- **System monitoring** for performance and process management
- **Extensible plugin architecture** for custom tools

## ⚡ Quick Start

```bash
# Install DevHub
pip install devhub-cli

# Format your code
devhub format code --lang python ./src

# Test an API
devhub api test --url https://api.github.com/users/octocat

# Generate a secure password
devhub gen password --length 20

# Clean up Git branches  
devhub git clean-branches --merged
```

## 🎯 Key Features

### 🎨 Beautiful CLI Experience
- Rich, colorful output with progress indicators
- Intuitive command structure
- Comprehensive help system
- Tab completion support

### 🧩 Plugin Architecture
- Modular design for easy extensibility
- Plugin-specific configuration
- Hot-reloading during development
- Community plugin ecosystem

### ⚙️ Powerful Configuration
- Multiple configuration formats (TOML, YAML, JSON)
- Environment variable support
- Per-project configuration
- Sensible defaults

### 🐳 Multiple Installation Options
- PyPI package: `pip install devhub-cli`
- Docker image: `docker pull devhub/cli`
- From source: Easy development setup

## 📖 Documentation

- [Installation Guide](installation.md) - Get DevHub up and running
- [Quick Start](quick-start.md) - Essential commands and workflows
- [User Guide](user-guide/formatting.md) - Detailed feature documentation
- [Plugin Development](plugins/architecture.md) - Create your own plugins
- [Contributing](contributing.md) - Join our community

## 🤝 Community

- **GitHub**: [github.com/username/devhub](https://github.com/username/devhub)
- **Twitter**: [@devhub_cli](https://twitter.com/devhub_cli)
- **Discord**: [Join our server](https://discord.gg/devhub)
- **Discussions**: [GitHub Discussions](https://github.com/username/devhub/discussions)

## 📄 License

DevHub is open source software licensed under the [MIT License](https://github.com/username/devhub/blob/main/LICENSE).
