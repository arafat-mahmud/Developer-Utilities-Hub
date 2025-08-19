#!/bin/bash

# DevHub CLI Release Script
# This script helps prepare and publish a new release of DevHub CLI

set -e

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
    print_error "This script must be run from within the git repository."
    exit 1
fi

# Read current version from pyproject.toml
if [ ! -f "pyproject.toml" ]; then
    print_error "pyproject.toml not found. Are you in the project root directory?"
    exit 1
fi

CURRENT_VERSION=$(python -c "import tomli; print(tomli.load(open('pyproject.toml', 'rb'))['project']['version'])" 2>/dev/null || python -c "import toml; print(toml.load('pyproject.toml')['project']['version'])")

if [ -z "$CURRENT_VERSION" ]; then
    print_error "Failed to read version from pyproject.toml"
    exit 1
fi

print_status "Current version: $CURRENT_VERSION"

# Ask for release type
echo
echo "Release type:"
echo "1) Patch (bug fixes)"
echo "2) Minor (new features, backwards compatible)"
echo "3) Major (breaking changes)"
echo "4) Custom version"
echo
read -p "Select release type [1-4]: " RELEASE_TYPE

case $RELEASE_TYPE in
    1)
        # Patch version
        IFS='.' read -r MAJOR MINOR PATCH <<< "$CURRENT_VERSION"
        NEW_VERSION="${MAJOR}.${MINOR}.$((PATCH + 1))"
        ;;
    2)
        # Minor version
        IFS='.' read -r MAJOR MINOR PATCH <<< "$CURRENT_VERSION"
        NEW_VERSION="${MAJOR}.$((MINOR + 1)).0"
        ;;
    3)
        # Major version
        IFS='.' read -r MAJOR MINOR PATCH <<< "$CURRENT_VERSION"
        NEW_VERSION="$((MAJOR + 1)).0.0"
        ;;
    4)
        # Custom version
        read -p "Enter custom version: " NEW_VERSION
        ;;
    *)
        print_error "Invalid selection"
        exit 1
        ;;
esac

print_status "Preparing release $NEW_VERSION"

# Update version in pyproject.toml
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS version of sed requires an empty extension argument
    sed -i '' "s/version = \"$CURRENT_VERSION\"/version = \"$NEW_VERSION\"/" pyproject.toml
else
    # Linux version
    sed -i "s/version = \"$CURRENT_VERSION\"/version = \"$NEW_VERSION\"/" pyproject.toml
fi

# Update changelog if it exists
if [ -f "CHANGELOG.md" ]; then
    print_status "Updating CHANGELOG.md"
    DATE=$(date +"%Y-%m-%d")
    
    # Create a temporary file with the new changelog entry
    cat > /tmp/changelog_entry.tmp << EOL
## $NEW_VERSION - $DATE

### Added
- 

### Changed
- 

### Fixed
- 

EOL

    # Insert the new entry after the first occurrence of "# Changelog"
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS version
        sed -i '' -e "/# Changelog/{n;r /tmp/changelog_entry.tmp" -e "}" CHANGELOG.md
    else
        # Linux version
        sed -i -e "/# Changelog/{n;r /tmp/changelog_entry.tmp" -e "}" CHANGELOG.md
    fi

    print_warning "Please edit CHANGELOG.md to add release notes"
fi

# Create a git commit with the version changes
git add pyproject.toml
if [ -f "CHANGELOG.md" ]; then
    git add CHANGELOG.md
fi

git commit -m "chore: Bump version to $NEW_VERSION"

# Create a git tag for the release
print_status "Creating git tag v$NEW_VERSION"
git tag -a "v$NEW_VERSION" -m "Release $NEW_VERSION"

print_success "Version updated to $NEW_VERSION"
print_success "Tag created: v$NEW_VERSION"

echo
echo "Next steps:"
echo "1. Review the changes"
echo "2. Run: git push origin main"
echo "3. Run: git push --tags"
echo "4. Create a GitHub Release at: https://github.com/arafat-mahmud/Developer-Utilities-Hub/releases/new?tag=v$NEW_VERSION"
echo
print_status "The GitHub Actions workflow will automatically publish to PyPI when the release is created"
