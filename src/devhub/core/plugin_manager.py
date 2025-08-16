"""
Plugin management system for DevHub

This module handles plugin discovery, loading, and lifecycle management.
"""

import importlib
import inspect
from pathlib import Path
from typing import Dict, List, Any, Optional, Type
from abc import ABC, abstractmethod

from devhub.utils.exceptions import PluginError
from devhub.utils.logger import get_logger

logger = get_logger(__name__)


class Plugin(ABC):
    """Base class for all DevHub plugins"""

    name: str = ""
    description: str = ""
    version: str = "1.0.0"
    author: str = ""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.logger = get_logger(f"devhub.plugins.{self.name}")

    @abstractmethod
    def is_available(self) -> bool:
        """Check if plugin dependencies are available"""
        pass

    @abstractmethod
    def register_commands(self, cli_group):
        """Register plugin commands with the CLI"""
        pass

    def initialize(self):
        """Initialize plugin (called after loading)"""
        pass

    def cleanup(self):
        """Cleanup plugin resources"""
        pass

    def get_status(self) -> Dict[str, Any]:
        """Get plugin status information"""
        return {
            "name": self.name,
            "version": self.version,
            "available": self.is_available(),
            "loaded": True,
        }


class PluginManager:
    """Manages loading and lifecycle of plugins"""

    def __init__(self):
        self.plugins: Dict[str, Plugin] = {}
        self.loaded_plugins: List[str] = []
        self.failed_plugins: Dict[str, str] = {}

    def discover_plugins(self) -> List[str]:
        """Discover available plugins"""
        plugin_names = []
        plugins_dir = Path(__file__).parent.parent / "plugins"

        if not plugins_dir.exists():
            logger.warning(f"Plugins directory not found: {plugins_dir}")
            return plugin_names

        # Look for plugin directories
        for plugin_path in plugins_dir.iterdir():
            if plugin_path.is_dir() and not plugin_path.name.startswith("_"):
                # Check if it has an __init__.py file
                init_file = plugin_path / "__init__.py"
                if init_file.exists():
                    plugin_names.append(plugin_path.name)
                    logger.debug(f"Discovered plugin: {plugin_path.name}")

        return plugin_names

    def load_plugin(
        self, plugin_name: str, config: Optional[Dict[str, Any]] = None
    ) -> Plugin:
        """Load a single plugin"""
        try:
            # Import plugin module
            module_path = f"devhub.plugins.{plugin_name}"
            module = importlib.import_module(module_path)

            # Find plugin class (should inherit from Plugin)
            plugin_class = None
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, Plugin) and obj != Plugin:
                    plugin_class = obj
                    break

            if not plugin_class:
                raise PluginError(f"No plugin class found in {module_path}")

            # Create plugin instance
            plugin = plugin_class(config)

            # Check if plugin is available
            if not plugin.is_available():
                raise PluginError(f"Plugin dependencies not available")

            # Initialize plugin
            plugin.initialize()

            # Store plugin
            self.plugins[plugin_name] = plugin
            self.loaded_plugins.append(plugin_name)

            logger.info(f"Loaded plugin: {plugin_name}")
            return plugin

        except Exception as e:
            error_msg = f"Failed to load plugin {plugin_name}: {e}"
            self.failed_plugins[plugin_name] = str(e)
            logger.error(error_msg)
            raise PluginError(error_msg, plugin_name)

    def load_plugins(self, plugin_list: Optional[List[str]] = None):
        """Load multiple plugins"""
        if plugin_list is None:
            plugin_list = self.discover_plugins()

        for plugin_name in plugin_list:
            try:
                self.load_plugin(plugin_name)
            except PluginError:
                # Error already logged, continue with other plugins
                continue

    def unload_plugin(self, plugin_name: str):
        """Unload a plugin"""
        if plugin_name in self.plugins:
            try:
                self.plugins[plugin_name].cleanup()
                del self.plugins[plugin_name]
                self.loaded_plugins.remove(plugin_name)
                logger.info(f"Unloaded plugin: {plugin_name}")
            except Exception as e:
                logger.error(f"Error unloading plugin {plugin_name}: {e}")

    def unload_all_plugins(self):
        """Unload all loaded plugins"""
        for plugin_name in list(self.plugins.keys()):
            self.unload_plugin(plugin_name)

    def get_plugin(self, plugin_name: str) -> Optional[Plugin]:
        """Get a loaded plugin by name"""
        return self.plugins.get(plugin_name)

    def is_plugin_loaded(self, plugin_name: str) -> bool:
        """Check if a plugin is loaded"""
        return plugin_name in self.plugins

    def get_plugin_status(self) -> Dict[str, Any]:
        """Get status of all plugins"""
        return {
            "loaded": [plugin.get_status() for plugin in self.plugins.values()],
            "failed": self.failed_plugins,
            "discovered": self.discover_plugins(),
        }

    def register_all_commands(self, cli_group):
        """Register commands from all loaded plugins"""
        for plugin_name, plugin in self.plugins.items():
            try:
                plugin.register_commands(cli_group)
                logger.debug(f"Registered commands for plugin: {plugin_name}")
            except Exception as e:
                logger.error(
                    f"Failed to register commands for plugin {plugin_name}: {e}"
                )

    def reload_plugin(self, plugin_name: str, config: Optional[Dict[str, Any]] = None):
        """Reload a plugin (unload and load again)"""
        if self.is_plugin_loaded(plugin_name):
            self.unload_plugin(plugin_name)

        self.load_plugin(plugin_name, config)
