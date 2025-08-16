"""
DevHub Plugins

This module contains all available plugins for DevHub.
"""

from typing import Any
import click

from devhub.utils.logger import get_logger

logger = get_logger(__name__)


def register_plugins(cli_group: click.Group):
    """Register all available plugins with the CLI"""

    # Import and register each plugin
    plugins_to_register = ["format", "api"]  # Only load existing plugins

    for plugin_name in plugins_to_register:
        try:
            # Dynamic import of plugin module
            module = __import__(f"devhub.plugins.{plugin_name}", fromlist=[plugin_name])

            # Register plugin commands if available
            if hasattr(module, "register_commands"):
                module.register_commands(cli_group)
                logger.debug(f"Registered plugin: {plugin_name}")

        except ImportError as e:
            logger.warning(f"Could not import plugin {plugin_name}: {e}")
        except Exception as e:
            logger.error(f"Error registering plugin {plugin_name}: {e}")


__all__ = ["register_plugins"]
