# Deployment Setup Guide

This guide explains how to set up the required credentials and configurations for the DevHub project's CI/CD pipeline.

## 🚀 GitHub Actions Deployment

### Required Secrets

The project's CI/CD pipeline requires the following GitHub repository secrets to be configured:

#### 📚 Documentation Deployment
Documentation is automatically deployed to GitHub Pages using the dedicated workflow in `.github/workflows/docs.yml`.

**No additional secrets required** - GitHub Pages deployment uses built-in GitHub tokens with proper permissions.

#### 🐳 Docker Hub Deployment (Optional)
If you want to push Docker images to Docker Hub, set up these secrets:

1. Go to your GitHub repository settings
2. Navigate to **Secrets and variables** > **Actions**
3. Add the following repository secrets:

| Secret Name | Description | Example |
|-------------|-------------|---------|
| `DOCKER_USERNAME` | Your Docker Hub username | `yourusername` |
| `DOCKER_PASSWORD` | Your Docker Hub access token | `dckr_pat_...` |

**Note**: If these secrets are not configured, the Docker build will still run but won't push images to Docker Hub.

#### 📢 Slack Notifications (Optional)
For build status notifications via Slack:

| Secret Name | Description |
|-------------|-------------|
| `SLACK_WEBHOOK_URL` | Slack webhook URL for notifications |

### GitHub Pages Setup

1. **Enable GitHub Pages**:
   - Go to repository **Settings** > **Pages**
   - Source: **Deploy from a branch**
   - Branch: **gh-pages** (will be created automatically)
   - Folder: **/ (root)**

2. **Set Repository Permissions**:
   - Go to **Settings** > **Actions** > **General**
   - Under "Workflow permissions", select **Read and write permissions**
   - Check **Allow GitHub Actions to create and approve pull requests**

## 🔧 Local Development Setup

### Documentation Development
```bash
# Install documentation dependencies
pip install -e ".[docs]"

# Serve documentation locally
cd docs
mkdocs serve

# Build documentation
mkdocs build --strict
```

### Docker Development
```bash
# Build Docker image locally
docker build -t devhub/cli:local .

# Test Docker image
docker run --rm devhub/cli:local --version
```

## 🎯 Deployment Workflows

### Automatic Deployments

| Trigger | Workflow | Description |
|---------|----------|-------------|
| Push to `main` | `docs.yml` | Deploys documentation to GitHub Pages |
| Push to any branch | `ci.yml` | Runs tests, builds packages, creates Docker images |
| Release published | `ci.yml` | Publishes to PyPI (when release workflow is triggered) |

### Manual Deployments

You can manually trigger the documentation deployment:

1. Go to **Actions** tab in GitHub
2. Select **Deploy Documentation** workflow
3. Click **Run workflow**
4. Select branch and click **Run workflow**

## 📋 Verification Checklist

After setting up the deployment:

### ✅ Documentation
- [ ] GitHub Pages is enabled in repository settings
- [ ] Documentation workflow runs successfully
- [ ] Site is accessible at `https://arafat-mahmud.github.io/Developer-Utilities-Hub/`

### ✅ Docker (if configured)
- [ ] Docker Hub credentials are set in repository secrets
- [ ] Docker build workflow completes successfully
- [ ] Images are pushed to Docker Hub (if credentials provided)

### ✅ CI/CD Pipeline
- [ ] All tests pass on multiple Python versions
- [ ] Code quality checks (linting, formatting) pass
- [ ] Security scans complete without critical issues
- [ ] Package builds successfully

## 🔧 Troubleshooting

### Documentation Deployment Issues

**Problem**: `Permission denied` when pushing to gh-pages
**Solution**: Ensure workflow permissions are set to "Read and write permissions" in repository settings.

**Problem**: `mkdocs build` fails with missing files
**Solution**: Verify all documentation files exist in the `docs/docs/` directory.

### Docker Build Issues

**Problem**: Docker login fails
**Solution**: Verify `DOCKER_USERNAME` and `DOCKER_PASSWORD` secrets are correctly set.

**Problem**: Docker image build fails
**Solution**: Check the Dockerfile and ensure all dependencies are properly specified.

### General CI Issues

**Problem**: Tests fail on specific Python versions
**Solution**: Check compatibility matrix and update code for cross-version compatibility.

**Problem**: Import errors during testing
**Solution**: Ensure all test dependencies are listed in `pyproject.toml` under `[project.optional-dependencies.test]`.

## 📞 Support

If you encounter issues with the deployment setup:

1. Check the **Actions** tab for detailed error logs
2. Review this setup guide for missing configurations
3. Open an issue in the repository with details about the error

## 🔒 Security Notes

- Never commit secrets or credentials to the repository
- Use GitHub's encrypted secrets for sensitive information
- Regularly rotate Docker Hub access tokens
- Review and audit workflow permissions periodically

---

This setup ensures reliable, automated deployments while maintaining security best practices.
