# DevHub Manual Publishing Guide

This guide explains how to publish DevHub to PyPI using the GitHub Actions workflow.

## Automatic Publishing on Release

The DevHub package is automatically published to PyPI when a new GitHub Release is created. This is the recommended method for publishing new versions.

1. Update the version in `pyproject.toml`
2. Create a new GitHub Release with a tag that matches the version (e.g., `v0.1.0`)
3. Add release notes describing the changes
4. Publish the release
5. The CI/CD pipeline will automatically build and publish the package to PyPI

## Manual Publishing via Workflow Dispatch

In some cases, you may need to manually trigger the publishing process. DevHub supports this through the GitHub Actions workflow dispatch feature.

### Steps to Publish Manually

1. Go to the GitHub repository Actions tab
2. Select the "CI/CD Pipeline" workflow
3. Click the "Run workflow" dropdown button
4. Choose the branch you want to run from (typically `main`)
5. Set "Publish to PyPI?" to `true`
6. Click "Run workflow"

![Manual publishing screenshot](docs/docs/assets/images/manual-publishing.png)

### Important Notes

- The version in `pyproject.toml` must be unique and not already published on PyPI
- Manual publishing requires appropriate permissions on the GitHub repository
- The workflow will skip publishing if the version already exists on PyPI

## Troubleshooting

If you encounter issues with the publishing process:

1. Check that the version in `pyproject.toml` is unique
2. Verify you have the required permissions on GitHub
3. Check the workflow run logs for detailed error messages
4. Ensure the package builds successfully locally with `python -m build`
5. Verify the package can be installed from the local wheel with `pip install dist/*.whl`

## PyPI Project Information

- Project name: `devhub-cli`
- PyPI URL: https://pypi.org/project/devhub-cli/
- Package requires Python 3.8+

## Security Considerations

- Never share PyPI API tokens or credentials
- Always use GitHub's trusted publishing for PyPI (configured in the workflow)
- Review the package contents before publishing: `python -m twine check dist/*`
