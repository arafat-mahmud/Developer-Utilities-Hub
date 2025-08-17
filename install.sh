#!/bin/bash

# DevHub Installation Script
# This script helps users install DevHub locally

set -e

echo "🚀 DevHub Installation Script"
echo "============================="
echo ""

# Check if Python 3.8+ is available
echo "🐍 Checking Python version..."
python_cmd=""
for cmd in python3 python; do
    if command -v $cmd &> /dev/null; then
        version=$($cmd --version 2>&1 | grep -oE '[0-9]+\.[0-9]+' | head -1)
        major=$(echo $version | cut -d. -f1)
        minor=$(echo $version | cut -d. -f2)
        
        if [ "$major" -ge 3 ] && [ "$minor" -ge 8 ]; then
            python_cmd=$cmd
            echo "✅ Found $cmd version $version"
            break
        fi
    fi
done

if [ -z "$python_cmd" ]; then
    echo "❌ Error: Python 3.8 or higher is required"
    echo "Please install Python 3.8+ and try again"
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ] || [ ! -d "src/devhub" ]; then
    echo "❌ Error: Please run this script from the DevHub project root directory"
    echo "Expected files: pyproject.toml, src/devhub/"
    exit 1
fi

echo ""
echo "📁 Current directory: $(pwd)"
echo ""

# Check if virtual environment already exists
if [ -d "devhub-env" ]; then
    echo "📦 Virtual environment already exists"
    read -p "Do you want to recreate it? (y/N): " recreate
    if [[ $recreate =~ ^[Yy]$ ]]; then
        echo "🗑️ Removing existing virtual environment..."
        rm -rf devhub-env
    else
        echo "📦 Using existing virtual environment"
    fi
fi

# Create virtual environment
if [ ! -d "devhub-env" ]; then
    echo "🏗️ Creating virtual environment..."
    $python_cmd -m venv devhub-env
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source devhub-env/bin/activate

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip

# Install DevHub in development mode
echo "⚙️ Installing DevHub..."
pip install -e .

# Verify installation
echo ""
echo "🧪 Testing installation..."
if devhub --version > /dev/null 2>&1; then
    echo "✅ DevHub installed successfully!"
    echo ""
    echo "🎉 Installation Complete!"
    echo "===================="
    echo ""
    echo "To use DevHub:"
    echo "1. Activate the virtual environment:"
    echo "   source devhub-env/bin/activate"
    echo ""
    echo "2. Run DevHub commands:"
    echo "   devhub --help"
    echo "   devhub format --help"
    echo "   devhub api --help"
    echo ""
    echo "📖 For more information, see:"
    echo "   - README.md"
    echo "   - INSTALL.md"
    echo "   - docs/index.md"
    echo ""
    echo "🎯 Try this example:"
    echo "   devhub format --lang python --help"
    echo ""
else
    echo "❌ Installation failed. Please check the error messages above."
    exit 1
fi
