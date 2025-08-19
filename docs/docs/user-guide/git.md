# Git Tools

DevHub's Git plugin provides powerful automation for common Git workflows, branch management, and repository analysis.

## 🎯 Overview

The Git plugin offers:
- **Branch management** and cleanup
- **Commit analysis** and statistics  
- **Workflow automation**
- **Repository health checks**
- **Conventional commits** support
- **Git hooks** integration

## 🌿 Branch Management

### Branch Cleanup
```bash
# Clean up merged branches
devhub git clean-branches --merged

# Preview without deletion
devhub git clean-branches --merged --dry-run

# Preserve specific branches
devhub git clean-branches --merged --preserve main,develop,staging
```

### Branch Analysis
```bash
# List all branches with info
devhub git branches --info

# Find stale branches
devhub git branches --stale --days 30

# Branch comparison
devhub git compare-branches feature/new main
```

## 📊 Commit Analysis

### Repository Statistics
```bash
# Overall repository stats
devhub git stats

# Commit analysis for time period
devhub git analyze --since "1 month ago"

# Author contributions
devhub git contributors --since "2023-01-01"
```

### Commit Quality
```bash
# Check conventional commits
devhub git check-commits --conventional

# Analyze commit messages
devhub git message-analysis --branch main

# Find commits without issue references
devhub git orphan-commits
```

For detailed examples and configuration, see the [Git Tools Documentation](https://github.com/username/devhub-examples/tree/main/git).
