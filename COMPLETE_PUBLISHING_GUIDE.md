# 🚀 Complete PyPI Publishing Guide for DevHub CLI

## 📋 Step-by-Step Publishing Process

Follow these exact steps to publish DevHub to PyPI so users can install it with `pip install devhub-cli`:

### Step 1: Create PyPI Account

1. **Go to PyPI**: https://pypi.org/account/register/
2. **Fill out the form**:
   - Username: (choose a unique username)
   - Email: your email address
   - Password: create a strong password
3. **Verify your email** (check your inbox)

### Step 2: Generate API Token

1. **Login to PyPI**: https://pypi.org/account/login/
2. **Go to Account Settings**: https://pypi.org/manage/account/
3. **Click "API tokens"** in the left sidebar
4. **Click "Add API token"**
5. **Fill out**:
   - Token name: `DevHub CLI Publishing`
   - Scope: `Entire account (all projects)`
6. **Click "Add token"**
7. **Copy the token** (starts with `pypi-`) - save it securely!

### Step 3: Prepare Local Environment

```bash
# Navigate to project directory
cd /Users/sanon/Developer-Utilities-Hub

# Activate virtual environment
source devhub-env/bin/activate

# Verify DevHub works
devhub --version
```

### Step 4: Run the Publishing Script

```bash
# Make sure script is executable
chmod +x publish.sh

# Run the publishing script
./publish.sh
```

**The script will**:
- ✅ Install/upgrade build tools
- ✅ Clean previous builds
- ✅ Build the package
- ✅ Test the package locally
- ✅ Upload to PyPI

### Step 5: When Prompted for Credentials

```
Username: __token__
Password: pypi-AgEIcHlwaS5vcmcC... (your full API token)
```

### Step 6: Verify Publication

After successful upload, check:
- **PyPI page**: https://pypi.org/project/devhub-cli/
- **Test installation**: `pip install devhub-cli`

## 🎯 Complete Terminal Commands

Here's the complete sequence of commands:

```bash
# Step 1: Navigate to project
cd /Users/sanon/Developer-Utilities-Hub

# Step 2: Activate environment
source devhub-env/bin/activate

# Step 3: Run publishing script
./publish.sh

# Step 4: Test published package (in a new terminal)
pip install devhub-cli
devhub --help
devhub --version
```

## 📝 Manual Publishing (Alternative)

If you prefer manual control:

```bash
# 1. Install build tools
pip install --upgrade build twine

# 2. Clean previous builds
rm -rf dist/ build/ src/*.egg-info/

# 3. Build package
python -m build

# 4. Upload to PyPI
python -m twine upload dist/*
```

## 🧪 Testing Before Production

To test on TestPyPI first:

```bash
# Upload to TestPyPI
python -m twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ devhub-cli
```

## ✅ Success Indicators

After publishing, you should see:

1. **Upload success message**:
   ```
   Uploading distributions to https://upload.pypi.org/legacy/
   Uploading devhub_cli-1.0.0-py3-none-any.whl
   100%|████████████| 23.0k/23.0k [00:01<00:00, 12.8kB/s]
   Uploading devhub_cli-1.0.0.tar.gz
   100%|████████████| 25.4k/25.4k [00:01<00:00, 13.2kB/s]
   ```

2. **Package appears on PyPI**: https://pypi.org/project/devhub-cli/

3. **Global installation works**:
   ```bash
   pip install devhub-cli
   devhub --help
   ```

## 🚨 Troubleshooting

### Error: "Package already exists"
- Change version number in `pyproject.toml`
- Rebuild and upload again

### Error: "Invalid credentials"
- Check API token is correct
- Use `__token__` as username, not your PyPI username

### Error: "Package name taken"
- Choose a different name in `pyproject.toml`
- Suggestions: `devhub-tools`, `developer-hub-cli`, `dev-utilities-hub`

## 🎉 After Successful Publishing

1. **Update README.md** with PyPI installation
2. **Create GitHub release** with version tag
3. **Test installation** from different machines
4. **Share with the community**!

## 📋 Commands Summary

```bash
# Complete publishing workflow
cd /Users/sanon/Developer-Utilities-Hub
source devhub-env/bin/activate
./publish.sh

# Test published package
pip install devhub-cli
devhub --version
devhub --help
```

**That's it! Your CLI will be globally available via `pip install devhub-cli`! 🚀**
