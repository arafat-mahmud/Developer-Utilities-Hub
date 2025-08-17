# 🚀 How to Publish DevHub to PyPI

## 📋 Prerequisites

1. **Create PyPI Accounts**:
   - [PyPI Account](https://pypi.org/account/register/) (Production)
   - [TestPyPI Account](https://test.pypi.org/account/register/) (Testing)

2. **Get API Tokens**:
   - Go to Account Settings → API Tokens
   - Create tokens with "Entire account" scope
   - Save them securely (you'll need them for publishing)

## 🚀 Quick Publishing (Using Our Script)

```bash
# 1. Activate virtual environment
cd Developer-Utilities-Hub
source devhub-env/bin/activate

# 2. Run the publishing script
./publish.sh
```

The script will:
- ✅ Build the package
- ✅ Test the installation
- ✅ Give you options to publish to TestPyPI or PyPI

## 📝 Manual Publishing Steps

### Step 1: Build the Package
```bash
# Clean previous builds
rm -rf dist/ build/ src/*.egg-info/

# Build the package
python -m build
```

### Step 2: Test on TestPyPI (Recommended)
```bash
# Upload to TestPyPI
python -m twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ devhub-cli
```

### Step 3: Publish to PyPI
```bash
# Upload to PyPI (production)
python -m twine upload dist/*
```

## ✅ After Publishing

Users can now install DevHub with:
```bash
pip install devhub-cli
```

## 📋 Update Documentation

After successful publishing, update these files:

### 1. README.md
```markdown
## 📦 Installation

### 🔥 Quick Install
```bash
pip install devhub-cli
```

### 🛠️ From Source
```bash
git clone https://github.com/arafat-mahmud/Developer-Utilities-Hub.git
cd Developer-Utilities-Hub
pip install -e .
```
```

### 2. Update Badges
Replace the development badges with PyPI badges:
```markdown
[![PyPI version](https://badge.fury.io/py/devhub-cli.svg)](https://badge.fury.io/py/devhub-cli)
[![Downloads](https://pepy.tech/badge/devhub-cli)](https://pepy.tech/project/devhub-cli)
```

## 🔄 For Future Updates

1. **Update version** in `pyproject.toml`
2. **Update CHANGELOG.md**
3. **Build and publish**:
   ```bash
   python -m build
   twine upload dist/*
   ```

## 🚨 Troubleshooting

### Package Name Already Exists
If `devhub-cli` is taken, try:
- `devhub-tools`
- `developer-hub-cli`
- `dev-utilities-hub`

### Authentication Issues
- Use API tokens instead of passwords
- Make sure tokens have correct permissions
- Check token expiration dates

### Build Errors
- Make sure all dependencies are listed in `pyproject.toml`
- Check Python version compatibility
- Verify entry points are configured correctly

## 📊 Checking Your Package

After publishing, verify at:
- **PyPI**: https://pypi.org/project/devhub-cli/
- **TestPyPI**: https://test.pypi.org/project/devhub-cli/

## 🎯 Success Indicators

✅ Package builds without errors  
✅ Can install from TestPyPI  
✅ CLI commands work after installation  
✅ Package appears on PyPI  
✅ Users can `pip install devhub-cli`  

---

**Ready to publish?** Run `./publish.sh` to get started!
