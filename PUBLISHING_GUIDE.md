# Publishing DevHub to PyPI

This guide will help you publish DevHub to PyPI so users can install it with `pip install devhub-cli`.

## 📋 Prerequisites

1. **PyPI Account**: Create accounts on both:
   - [PyPI](https://pypi.org/account/register/) (Production)
   - [TestPyPI](https://test.pypi.org/account/register/) (Testing)

2. **API Tokens**: Generate API tokens for both accounts:
   - Go to Account Settings → API Tokens
   - Create tokens with "Entire account" scope
   - Save them securely

## 🛠️ Step 1: Prepare the Package

### Update pyproject.toml
Make sure your `pyproject.toml` has the correct package name:

```toml
[project]
name = "devhub-cli"  # This is what users will install
version = "1.0.0"    # Update version for each release
```

### Check Package Structure
```bash
src/
└── devhub/
    ├── __init__.py
    ├── cli.py
    ├── core/
    ├── plugins/
    └── utils/
```

### Install Build Tools
```bash
pip install build twine
```

## 🚀 Step 2: Build the Package

```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info/

# Build the package
python -m build

# This creates:
# dist/devhub_cli-1.0.0-py3-none-any.whl
# dist/devhub_cli-1.0.0.tar.gz
```

## 🧪 Step 3: Test on TestPyPI

```bash
# Upload to TestPyPI first
python -m twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ devhub-cli
```

## 📦 Step 4: Publish to PyPI

```bash
# Upload to PyPI
python -m twine upload dist/*

# Users can now install with:
pip install devhub-cli
```

## 🔐 Step 5: Secure Publishing with GitHub Actions

Create `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    - name: Build package
      run: python -m build
    - name: Publish to PyPI
      uses: pypa/gh-action-pypi-publish@release/v1
      with:
        password: ${{ secrets.PYPI_API_TOKEN }}
```

## 🏷️ Step 6: Version Management

For future updates:

```bash
# 1. Update version in pyproject.toml
# 2. Create a git tag
git tag v1.0.1
git push origin v1.0.1

# 3. Create GitHub release (triggers auto-publish)
```

## ✅ Verification

After publishing, users can:

```bash
pip install devhub-cli
devhub --help
devhub format --help
```

## 🔄 Updating the Package

For each new version:

1. Update `version` in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Build and upload: `python -m build && twine upload dist/*`

## 🚨 Troubleshooting

### Name Already Taken
If `devhub-cli` is taken, try:
- `devhub-tools`
- `developer-hub`
- `dev-utilities-hub`

### Permission Errors
- Make sure you're logged in: `twine upload --username __token__ --password YOUR_TOKEN`
- Use API tokens instead of passwords

### Dependencies Issues
- Test in a clean virtual environment
- Make sure all dependencies are in `pyproject.toml`

## 📋 Checklist Before Publishing

- [ ] Package name is unique on PyPI
- [ ] Version number is updated
- [ ] All dependencies are listed
- [ ] Entry points are configured correctly
- [ ] README.md is included
- [ ] LICENSE file exists
- [ ] Tests pass
- [ ] Package builds successfully
- [ ] Tested on TestPyPI

Once published, update your README.md to show the PyPI installation method!
