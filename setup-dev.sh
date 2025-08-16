#!/bin/bash

# DevHub Development Setup Script
# This script sets up the development environment for DevHub

set -e

echo "🚀 Setting up DevHub development environment..."

# Check Python version
python_version=$(python3 --version 2>&1 | cut -d' ' -f2 | cut -d'.' -f1,2)
min_version="3.8"

if [ "$(printf '%s\n' "$min_version" "$python_version" | sort -V | head -n1)" != "$min_version" ]; then
    echo "❌ Python 3.8+ is required, but found $python_version"
    exit 1
fi

echo "✅ Python $python_version detected"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install development dependencies
echo "📚 Installing dependencies..."
pip install -e ".[dev]"

# Install pre-commit hooks
echo "🪝 Setting up pre-commit hooks..."
pre-commit install

# Install additional formatting tools
echo "🎨 Installing formatting tools..."
pip install black isort ruff mypy

# Install system tools (if available)
echo "🛠️ Checking for external tools..."

# Check for Node.js and prettier
if command -v npm &> /dev/null; then
    echo "✅ Node.js found, installing prettier..."
    npm install -g prettier
else
    echo "⚠️ Node.js not found - JavaScript/TypeScript formatting will be limited"
fi

# Check for Go
if command -v go &> /dev/null; then
    echo "✅ Go found - gofmt available"
else
    echo "⚠️ Go not found - Go formatting will be limited"
fi

# Check for Rust
if command -v rustc &> /dev/null; then
    echo "✅ Rust found - rustfmt available"
else
    echo "⚠️ Rust not found - Rust formatting will be limited"
fi

# Run initial tests
echo "🧪 Running initial tests..."
pytest tests/ -v || echo "⚠️ Some tests failed - this is expected in initial setup"

# Create initial config directory
echo "📁 Creating config directory..."
mkdir -p ~/.config/devhub

echo ""
echo "🎉 DevHub development environment setup complete!"
echo ""
echo "To get started:"
echo "  1. Activate the virtual environment: source venv/bin/activate"
echo "  2. Test the installation: python -m devhub --help"
echo "  3. Run tests: pytest"
echo "  4. Check code quality: pre-commit run --all-files"
echo ""
echo "Happy coding! 🚀"
