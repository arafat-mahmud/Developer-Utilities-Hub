# PyPI Publishing Guide

This guide explains how to publish the DevHub CLI package to PyPI using the GitHub Actions automated workflow.

## 📋 Prerequisites

Before publishing to PyPI, ensure:

1. Your code is ready for release
2. All tests pass
3. Documentation is up-to-date
4. Version number is incremented in `pyproject.toml`

## 🚀 Publishing Options

There are two ways to publish to PyPI:

### Option 1: Publish with GitHub Release (Recommended)

1. **Create a GitHub Release**:
   - Go to GitHub > Releases > "Draft a new release"
   - Choose a tag (e.g., `v1.0.0`) that matches your version in `pyproject.toml`
   - Write release notes
   - Click "Publish release"

2. **Automatic Publishing**:
   - The CI/CD workflow will automatically build and publish the package to PyPI
   - Check the Actions tab to monitor progress

### Option 2: Manual Publish

1. **Trigger the Workflow**:
   - Go to Actions tab in GitHub
   - Select "Publish to PyPI" workflow
   - Click "Run workflow"
   - Select branch (usually `main`)
   - Click "Run workflow"

2. **Monitor Progress**:
   - Check the Actions tab to monitor publishing progress

## 🔒 PyPI Configuration (For Repository Administrators)

The package uses OpenID Connect (OIDC) for secure PyPI authentication. If you're setting up a new repository:

1. **Configure PyPI Trusted Publisher**:
   - Go to PyPI > Account settings > Add trusted publisher
   - Owner: `arafat-mahmud`
   - Repository name: `Developer-Utilities-Hub`
   - Workflow name: `publish.yml`
   - Environment (optional): `release`

2. **GitHub Workflow Environment**:
   - In GitHub > Repository > Settings > Environments > "release"
   - Configure environment protection rules if needed

## 📦 Verifying Publication

After publishing:

1. **Check PyPI**:
   - Visit https://pypi.org/project/devhub-cli/
   - Verify the new version is available

2. **Test Installation**:
   ```bash
   pip install devhub-cli==X.Y.Z  # Replace X.Y.Z with your version
   ```

3. **Verify Functionality**:
   ```bash
   devhub --version
   ```

## 📝 Version Management

Always update the version in `pyproject.toml` before publishing:

```toml
[project]
name = "devhub-cli"
version = "X.Y.Z"  # Increment this
```

Follow [Semantic Versioning](https://semver.org/):
- MAJOR version for incompatible API changes
- MINOR version for added functionality (backwards-compatible)
- PATCH version for bug fixes (backwards-compatible)

## 🔍 Troubleshooting

If publishing fails:

1. **Version Already Exists**:
   - If the version already exists on PyPI, increment the version in `pyproject.toml`

2. **Authentication Issues**:
   - Check that the trusted publisher configuration is correct on PyPI
   - Verify GitHub workflow has proper permissions

3. **Build Problems**:
   - Check the build logs in GitHub Actions for specific errors

## 📈 After Publishing

1. **Update Changelog**
2. **Create a new development version** (e.g., bump `1.0.0` to `1.0.1-dev`)
3. **Announce the release** to relevant channels
