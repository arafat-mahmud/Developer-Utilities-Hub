#!/bin/bash

# DevHub PyPI Publishing Script
# Use this script to publish DevHub to PyPI

set -e

echo "🚀 DevHub PyPI Publishing Script"
echo "==============================="
echo ""

# Check if we're in a virtual environment
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "❌ Error: Please activate the virtual environment first:"
    echo "source devhub-env/bin/activate"
    exit 1
fi

# Check if build tools are installed
if ! command -v twine &> /dev/null; then
    echo "📦 Installing build tools..."
    pip install build twine
fi

echo "🧹 Cleaning previous builds..."
rm -rf dist/ build/ src/*.egg-info/

echo "🏗️ Building the package..."
python -m build

echo ""
echo "📦 Built packages:"
ls -la dist/

echo ""
echo "🧪 Testing the built package..."
# Test if the wheel can be installed
pip install dist/devhub_cli-*.whl --force-reinstall

echo "✅ Package test successful!"
echo ""

echo "📋 Publishing Options:"
echo "1. Test on TestPyPI (recommended first)"
echo "2. Publish to PyPI (production)"
echo "3. Exit"
echo ""

read -p "Choose an option (1-3): " choice

case $choice in
    1)
        echo ""
        echo "🧪 Publishing to TestPyPI..."
        echo "You'll need your TestPyPI API token"
        echo "Get it from: https://test.pypi.org/manage/account/token/"
        echo ""
        python -m twine upload --repository testpypi dist/*
        echo ""
        echo "✅ Published to TestPyPI!"
        echo ""
        echo "🔍 Test installation:"
        echo "pip install --index-url https://test.pypi.org/simple/ devhub-cli"
        ;;
    2)
        echo ""
        echo "🚀 Publishing to PyPI..."
        echo "⚠️  WARNING: This will publish to the real PyPI!"
        echo "You'll need your PyPI API token"
        echo "Get it from: https://pypi.org/manage/account/token/"
        echo ""
        read -p "Are you sure you want to publish to PyPI? (y/N): " confirm
        if [[ $confirm =~ ^[Yy]$ ]]; then
            python -m twine upload dist/*
            echo ""
            echo "🎉 Published to PyPI!"
            echo ""
            echo "✅ Users can now install with:"
            echo "pip install devhub-cli"
        else
            echo "❌ Publishing cancelled"
        fi
        ;;
    3)
        echo "👋 Exiting..."
        exit 0
        ;;
    *)
        echo "❌ Invalid option"
        exit 1
        ;;
esac

echo ""
echo "📝 Next Steps:"
echo "1. Update README.md with PyPI installation instructions"
echo "2. Create a GitHub release"
echo "3. Update version number for next release"
echo ""
