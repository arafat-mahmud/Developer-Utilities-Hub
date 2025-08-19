#!/bin/bash

# DevHub Deployment Setup Script
# This script helps configure the repository for automated deployments

set -e

echo "🚀 DevHub Deployment Setup"
echo "=========================="
echo

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    print_error "This script must be run from within a git repository."
    exit 1
fi

# Check if this is a GitHub repository
if ! git remote get-url origin | grep -q "github.com"; then
    print_warning "This doesn't appear to be a GitHub repository. Some features may not work."
fi

print_status "Checking repository setup..."

# Check if main branch exists
if git show-ref --verify --quiet refs/heads/main; then
    print_success "Main branch found"
else
    print_warning "Main branch not found. Documentation deployment is configured for 'main' branch."
fi

# Check if workflows directory exists
if [ -d ".github/workflows" ]; then
    print_success "GitHub workflows directory found"
    
    # List existing workflows
    print_status "Found workflows:"
    for workflow in .github/workflows/*.yml; do
        if [ -f "$workflow" ]; then
            echo "  - $(basename "$workflow")"
        fi
    done
else
    print_error "GitHub workflows directory not found. CI/CD will not work."
fi

# Check if documentation exists
if [ -d "docs" ] && [ -f "docs/mkdocs.yml" ]; then
    print_success "Documentation structure found"
    
    # Test documentation build
    print_status "Testing documentation build..."
    if command -v mkdocs >/dev/null 2>&1; then
        cd docs
        if mkdocs build --quiet; then
            print_success "Documentation builds successfully"
        else
            print_error "Documentation build failed"
        fi
        cd ..
    else
        print_warning "MkDocs not installed. Install with: pip install -e \".[docs]\""
    fi
else
    print_error "Documentation structure not found"
fi

# Check if Dockerfile exists
if [ -f "Dockerfile" ]; then
    print_success "Dockerfile found"
    
    # Test Docker build if Docker is available
    if command -v docker >/dev/null 2>&1; then
        print_status "Testing Docker build..."
        if docker build -t devhub-test . >/dev/null 2>&1; then
            print_success "Docker image builds successfully"
            docker rmi devhub-test >/dev/null 2>&1 || true
        else
            print_error "Docker build failed"
        fi
    else
        print_warning "Docker not installed. Docker builds will run in CI only."
    fi
else
    print_warning "Dockerfile not found"
fi

echo
print_status "Checking Python environment..."

# Check Python version
if command -v python >/dev/null 2>&1; then
    python_version=$(python --version 2>&1 | cut -d' ' -f2)
    print_success "Python $python_version found"
else
    print_error "Python not found"
fi

# Check if project is installable
if [ -f "pyproject.toml" ]; then
    print_success "pyproject.toml found"
    
    # Try to install in development mode
    print_status "Testing package installation..."
    if pip install -e . >/dev/null 2>&1; then
        print_success "Package installs successfully"
        
        # Test CLI if available
        if command -v devhub >/dev/null 2>&1; then
            print_success "DevHub CLI is available"
        else
            print_warning "DevHub CLI not found in PATH"
        fi
    else
        print_error "Package installation failed"
    fi
else
    print_error "pyproject.toml not found"
fi

echo
print_status "Repository secrets checklist:"
echo "  □ DOCKER_USERNAME (optional - for Docker Hub)"
echo "  □ DOCKER_PASSWORD (optional - for Docker Hub)" 
echo "  □ SLACK_WEBHOOK_URL (optional - for notifications)"
echo

print_status "GitHub repository settings checklist:"
echo "  □ GitHub Pages enabled (Settings > Pages)"
echo "  □ Actions permissions: Read and write (Settings > Actions > General)"
echo "  □ Allow Actions to create PRs (Settings > Actions > General)"
echo

print_status "Next steps:"
echo "1. Review DEPLOYMENT_SETUP.md for detailed setup instructions"
echo "2. Configure repository secrets in GitHub (if needed)"
echo "3. Enable GitHub Pages in repository settings"
echo "4. Push to main branch to trigger first deployment"
echo

repo_url=$(git remote get-url origin 2>/dev/null || echo "unknown")
if [[ "$repo_url" == *"github.com"* ]]; then
    # Extract owner and repo name
    repo_path=$(echo "$repo_url" | sed 's/.*github\.com[/:]\([^/]*\/[^/]*\)\.git.*/\1/' | sed 's/\.git$//')
    print_success "When deployed, documentation will be available at:"
    echo "  https://${repo_path%/*}.github.io/${repo_path#*/}/"
fi

echo
print_success "Setup check complete!"
