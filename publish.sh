#!/bin/bash

# DevHub PyPI Publishing Script
# This script publishes DevHub to PyPI so users can install with: pip install devhub-cli

set -e

echo "🚀 DevHub PyPI Publishing Script"
echo "==============================="
echo ""
echo "This will publish DevHub to PyPI so users can install with:"
echo "pip install devhub-cli"
echo ""

# Check if we're in a virtual environment
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "❌ Error: Please activate the virtual environment first:"
    echo "cd Developer-Utilities-Hub"
    echo "source devhub-env/bin/activate"
    echo "Then run: ./publish.sh"
    exit 1
fi

# Check if build tools are installed
echo "📦 Installing/upgrading build tools..."
pip install --upgrade build twine setuptools wheel

echo ""
echo "🧹 Cleaning previous builds..."
rm -rf dist/ build/ src/*.egg-info/

echo ""
echo "🏗️ Building the package..."
python -m build

echo ""
echo "📦 Built packages:"
ls -la dist/

echo ""
echo "🧪 Testing the built package locally..."
# Test if the wheel can be installed
pip install dist/devhub_cli-*.whl --force-reinstall --quiet

# Test if CLI works
echo "✅ Testing CLI functionality..."
if devhub --version > /dev/null 2>&1; then
    echo "✅ Package test successful!"
else
    echo "❌ Package test failed!"
    exit 1
fi

echo ""
echo "🎯 Ready to publish to PyPI!"
echo ""
echo "📋 You need:"
echo "1. PyPI account: https://pypi.org/account/register/"
echo "2. API token: https://pypi.org/manage/account/token/"
echo ""

read -p "Do you have a PyPI account and API token? (y/N): " ready
if [[ ! $ready =~ ^[Yy]$ ]]; then
    echo ""
    echo "📝 Please complete these steps first:"
    echo "1. Create PyPI account: https://pypi.org/account/register/"
    echo "2. Verify your email"
    echo "3. Generate API token: https://pypi.org/manage/account/token/"
    echo "4. Run this script again"
    exit 0
fi

echo ""
echo "🚀 Publishing to PyPI..."
echo "When prompted, use:"
echo "Username: __token__"
echo "Password: your-api-token"
echo ""

# Upload to PyPI
python -m twine upload dist/*

echo ""
echo "🎉 SUCCESS! DevHub has been published to PyPI!"
echo ""
echo "✅ Users can now install DevHub globally with:"
echo "pip install devhub-cli"
echo ""
echo "🧪 Test the published package:"
echo "pip install devhub-cli --upgrade"
echo "devhub --help"
echo ""
echo "📖 Update your README.md to include the PyPI installation method!"
echo ""
