# GitHub Pages Setup Guide

## 🔧 Quick Setup Steps

To enable GitHub Pages for your documentation:

1. **Go to Repository Settings**:
   - Navigate to `Settings` tab in your repository

2. **Configure Pages**:
   - In the left sidebar, click on `Pages`
   - Under "Source", select `Deploy from a branch`
   - For "Branch", select `gh-pages` and folder `/ (root)`
   - Click `Save`

3. **Wait for Deployment**:
   - GitHub will begin building and deploying your site
   - This typically takes 1-2 minutes

4. **Access Your Documentation**:
   - Once deployed, your site will be available at:
   - `https://arafat-mahmud.github.io/Developer-Utilities-Hub/`

## 🚀 Understanding the Deployment Process

The documentation deployment uses two complementary workflows:

### 1. `docs.yml` - Build and Verify
- Builds the documentation
- Verifies that it compiles correctly
- Saves the output as an artifact
- **Does not require GitHub Pages setup**

### 2. `deploy-docs.yml` - Deployment
- Uses the git-based approach with `mkdocs gh-deploy`
- Creates/updates the `gh-pages` branch with the documentation
- Works regardless of GitHub Pages configuration status
- Requires `contents: write` permission

## 🔍 Troubleshooting

### The documentation build succeeds but the site isn't accessible:
- Verify GitHub Pages is enabled in repository settings
- Check if the `gh-pages` branch exists
- Ensure the source is set to `gh-pages` branch
- Check for any errors in the Actions tab

### Permission errors:
- Verify workflow permissions are set to "Read and write permissions"
- Repository Settings → Actions → General → Workflow permissions

### Custom domain:
- If you want to use a custom domain, add it in the Pages settings
- Create a CNAME file in the `docs/docs` directory with your domain

## 📋 GitHub Actions Permissions

The workflows need specific permissions:

1. **docs.yml**:
   - `contents: read` - To read repository content
   - No additional permissions needed

2. **deploy-docs.yml**:
   - `contents: write` - To push to gh-pages branch
   - Uses built-in GITHUB_TOKEN

## 📖 Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [MkDocs Documentation](https://www.mkdocs.org/user-guide/deploying-your-docs/)
- [Troubleshooting GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/troubleshooting-404-errors-for-github-pages-sites)

## 🔄 Updating the Documentation

After setting up GitHub Pages, future updates will happen automatically:
- Push changes to the `main` branch
- The deployment workflows will run
- Your documentation site will update
