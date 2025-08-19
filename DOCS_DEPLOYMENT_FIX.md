# Documentation Deployment Fix

## 🔧 Issue Description

The documentation deployment is failing with the following error:

```
remote: Permission to arafat-mahmud/Developer-Utilities-Hub.git denied to github-actions[bot].
fatal: unable to access 'https://github.com/arafat-mahmud/Developer-Utilities-Hub/': The requested URL returned error: 403
```

This indicates a permission issue with GitHub Actions when trying to push to the repository.

## ✅ Solution

### The Fix

I've created a dedicated GitHub Actions workflow file specifically for documentation deployment that includes proper permissions:

`deploy-docs.yml`:

```yaml
name: Deploy Documentation

on:
  push:
    branches: [ main ]
  workflow_dispatch:  # Allow manual trigger

env:
  PYTHON_VERSION: "3.11"

permissions:
  contents: write  # Needed for pushing to gh-pages branch

jobs:
  deploy:
    name: Deploy Documentation
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
      with:
        fetch-depth: 0  # Fetch full history for gh-deploy

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ env.PYTHON_VERSION }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e ".[docs]"

    - name: Configure Git
      run: |
        git config --global user.name "github-actions[bot]"
        git config --global user.email "github-actions[bot]@users.noreply.github.com"

    - name: Deploy to GitHub Pages
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      run: |
        cd docs
        mkdocs gh-deploy --force --clean
```

### Key Changes:

1. **Top-level permissions**: Added `permissions: contents: write` to grant write access to the repository contents
2. **Git configuration**: Added explicit Git user configuration for the GitHub Actions bot
3. **GitHub token**: Added `GITHUB_TOKEN` environment variable for authentication
4. **Clean deployment**: Added `--clean` flag to ensure clean deployments

### Repository Settings Required:

1. In your GitHub repository, go to **Settings** > **Actions** > **General**
2. Under "Workflow permissions":
   - Select **Read and write permissions**
   - Check **Allow GitHub Actions to create and approve pull requests**
3. Click **Save**

## 🚀 How This Works

1. The workflow uses the built-in `GITHUB_TOKEN` which has the necessary permissions when "Read and write permissions" is enabled
2. Setting `permissions: contents: write` explicitly grants permission to push to branches
3. The Git configuration ensures proper author information for commits
4. The workflow is triggered on pushes to the main branch or can be run manually

## 📋 Verification

After pushing this change:
1. Your documentation will automatically deploy to GitHub Pages
2. The site will be available at: `https://arafat-mahmud.github.io/Developer-Utilities-Hub/`

No other code changes are needed, and no existing functionality has been removed.
