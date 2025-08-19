# DevHub Manual Publishing Guide

This guide explains how to publish DevHub to PyPI using the GitHub Actions workflow.

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

The publishing job will run independently from other jobs, building and publishing the package directly without waiting for tests to complete. This is useful for quick publishing after you've already verified everything works.

![Manual publishing screenshot](docs/docs/assets/images/manual-publishing.png)

### Important Notes

- The version in `pyproject.toml` must be unique and not already published on PyPI
- Manual publishing requires appropriate permissions on the GitHub repository
- The workflow will skip publishing if the version already exists on PyPI

## Troubleshooting

If you encounter issues with the publishing process:

1. Check that the version in `pyproject.toml` is unique and not already published on PyPI
2. Verify you have the required permissions on GitHub
3. Check the workflow run logs for detailed error messages
4. Ensure the package builds successfully locally with `python -m build`
5. Verify the package can be installed from the local wheel with `pip install dist/*.whl`

### Common Issues and Solutions

#### Publishing Job Being Skipped

If the publishing job is being skipped when you trigger the workflow manually:

1. Make sure you set the "Publish to PyPI?" option to `true` when running the workflow
2. Check the workflow run logs for the debug information in the publish job
3. Verify that you're using the latest workflow file version
4. Remember that the manual publish job now runs independently of other jobs

#### PyPI Authentication Errors

If you encounter authentication errors with PyPI:

1. Ensure your GitHub repository has the correct PyPI publishing configuration
2. Verify that trusted publishing is configured correctly in your PyPI account
3. Check that the GitHub Action has the required permissions (`id-token: write`)

## PyPI Project Information

- Project name: `devhub-cli`
- PyPI URL: https://pypi.org/project/devhub-cli/
- Package requires Python 3.8+

## Security Considerations

- Never share PyPI API tokens or credentials
- Always use GitHub's trusted publishing for PyPI (configured in the workflow)
- Review the package contents before publishing: `python -m twine check dist/*`
