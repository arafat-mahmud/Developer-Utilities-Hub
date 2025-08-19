# DevHub Manual Publishing Guide

This guide explains how to publish DevHub to PyPI using the dedicated GitHub Actions workflow.

## Initial Setup

Before you can publish to PyPI, ensure the following prerequisites are met:

1. **PyPI Project**: Create a project on PyPI with the name `devhub-cli`
2. **Trusted Publishing**: Configure trusted publishing on PyPI for your GitHub repository
   - Go to your PyPI project settings
   - Add a new "Publishing API token" with GitHub Actions as the publisher
   - Configure the token for your GitHub repository

## Automatic Publishing on Release

The DevHub package is automatically published to PyPI when a new GitHub Release is created. This is the recommended method for publishing new versions.

1. Update the version in `pyproject.toml`
2. Create a new GitHub Release with a tag that matches the version (e.g., `v0.1.0`)
3. Add release notes describing the changes
4. Publish the release
5. The publishing workflow will automatically build and publish the package to PyPI

## Manual Publishing via Dedicated Workflow

DevHub now has a dedicated workflow for publishing to PyPI, making it more reliable and independent of other CI processes.

### Steps to Publish Manually

1. Go to the GitHub repository Actions tab
2. Select the "**Publish to PyPI**" workflow (not the CI/CD Pipeline)
3. Click the "Run workflow" dropdown button
4. Choose the branch you want to run from (typically `main`)
5. Select a version bump type (patch, minor, major, or none)
6. Click "Run workflow"

![Manual publishing screenshot](docs/docs/assets/images/manual-publishing.png)

### Version Bumping

The publishing workflow includes automatic version bumping:

- **patch**: Increments the patch version (1.0.0 → 1.0.1)
- **minor**: Increments the minor version (1.0.0 → 1.1.0)
- **major**: Increments the major version (1.0.0 → 2.0.0)
- **none**: Uses the current version without bumping

![Manual publishing screenshot](docs/docs/assets/images/manual-publishing.png)

### Important Notes

- When using version bumping, the workflow will commit the version change and push it to the repository
- The workflow will skip publishing if the version already exists on PyPI
- The dedicated workflow runs independently from the main CI/CD pipeline

## Troubleshooting

If you encounter issues with the publishing process:

1. Check that the version in `pyproject.toml` is unique and not already published on PyPI
2. Verify you have the required permissions on GitHub
3. Check the workflow run logs for detailed error messages
4. Ensure the package builds successfully locally with `python -m build`
5. Verify the package can be installed from the local wheel with `pip install dist/*.whl`

### Common Issues and Solutions

#### Publishing Workflow Not Running

If the publishing workflow doesn't start:

1. Verify you have selected the correct workflow ("Publish to PyPI" not "CI/CD Pipeline")
2. Make sure your GitHub account has permissions to trigger workflows
3. Check if the repository has any workflow restrictions in place

#### Version Already Exists Error

If you get an error about the version already existing on PyPI:

1. Check the current version on PyPI: https://pypi.org/project/devhub-tools/
2. Update the version in `pyproject.toml` and `src/devhub/__init__.py` to a new version
3. Commit and push the version changes
4. Try the publishing workflow again

**Note**: The workflow uses `skip-existing: true` so it will silently skip publishing if the version already exists.

#### Version Bumping Failing

If automatic version bumping fails:

1. Ensure the repository has a proper `.bumpversion.cfg` file
2. Check that your GitHub token has `contents: write` permission
3. Try using the "none" option and manually update the version first

#### PyPI Authentication Errors

If you encounter authentication errors with PyPI:

1. Ensure your GitHub repository has the correct PyPI trusted publishing configuration
2. Verify that your PyPI project is correctly set up for trusted publishing
3. Check that the GitHub Action has the required permissions (`id-token: write`)

## PyPI Project Information

- Project name: `devhub-cli`
- PyPI URL: https://pypi.org/project/devhub-cli/
- Package requires Python 3.8+

## Security Considerations

- Never share PyPI API tokens or credentials
- Always use GitHub's trusted publishing for PyPI (configured in the workflow)
- Review the package contents before publishing: `python -m twine check dist/*`
