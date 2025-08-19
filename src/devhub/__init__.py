"""
DevHub - Developer Utilities Hub

A comprehensive CLI toolkit for developers that combines multiple
useful utilities into one powerful command-line interface.

Author: DevHub Team
License: MIT
Version: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "DevHub Team"
__email__ = "hello@devhub.dev"
__license__ = "MIT"
__description__ = "The Swiss Army Knife for Developers"

# Core imports for easy access
from devhub.core.config import Config
from devhub.core.plugin_manager import PluginManager

__all__ = [
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "__description__",
    "Config",
    "PluginManager",
]
