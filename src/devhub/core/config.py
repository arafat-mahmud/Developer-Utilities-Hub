"""
Configuration management for DevHub

This module handles all configuration-related functionality including
loading from files, environment variables, and providing defaults.
"""

import os
import json
import toml
import yaml
from pathlib import Path
from typing import Dict, Any, Optional, Union
from dataclasses import dataclass, field

from devhub.utils.exceptions import ConfigError


@dataclass
class Config:
    """DevHub configuration management"""

    # Core settings
    verbose: bool = False
    debug: bool = False
    config_file: Optional[str] = None

    # Plugin settings
    plugins_enabled: Dict[str, bool] = field(default_factory=dict)
    plugin_config: Dict[str, Dict[str, Any]] = field(default_factory=dict)

    # Output settings
    output_format: str = "auto"  # auto, json, yaml, table
    color: bool = True
    pager: bool = True

    # API settings
    api_timeout: int = 30
    api_retries: int = 3

    # Security settings
    password_length: int = 16
    password_symbols: bool = True

    # Git settings
    git_auto_push: bool = False
    git_default_branch: str = "main"

    # Format settings
    format_line_length: int = 88
    format_style: str = "black"

    def __post_init__(self):
        """Initialize configuration after creation"""
        self._load_defaults()
        self._load_from_env()

    def _load_defaults(self):
        """Load default plugin configurations"""
        self.plugins_enabled = {
            "format": True,
            "git": True,
            "api": True,
            "security": True,
            "data": True,
            "system": True,
        }

    def _load_from_env(self):
        """Load configuration from environment variables"""
        if os.getenv("DEVHUB_VERBOSE"):
            self.verbose = os.getenv("DEVHUB_VERBOSE").lower() in ("1", "true", "yes")

        if os.getenv("DEVHUB_DEBUG"):
            self.debug = os.getenv("DEVHUB_DEBUG").lower() in ("1", "true", "yes")

        if os.getenv("DEVHUB_NO_COLOR"):
            self.color = False

        if os.getenv("DEVHUB_API_TIMEOUT"):
            try:
                self.api_timeout = int(os.getenv("DEVHUB_API_TIMEOUT"))
            except ValueError:
                pass

    def load_from_file(self, config_path: Union[str, Path]):
        """Load configuration from file

        Args:
            config_path: Path to configuration file (JSON, YAML, or TOML)

        Raises:
            ConfigError: If file cannot be loaded or parsed
        """
        config_path = Path(config_path)

        if not config_path.exists():
            raise ConfigError(f"Configuration file not found: {config_path}")

        try:
            content = config_path.read_text()

            # Determine file format and parse
            if config_path.suffix.lower() == ".json":
                data = json.loads(content)
            elif config_path.suffix.lower() in (".yml", ".yaml"):
                data = yaml.safe_load(content)
            elif config_path.suffix.lower() == ".toml":
                data = toml.loads(content)
            else:
                # Try to auto-detect
                try:
                    data = json.loads(content)
                except json.JSONDecodeError:
                    try:
                        data = yaml.safe_load(content)
                    except yaml.YAMLError:
                        data = toml.loads(content)

            self._update_from_dict(data)
            self.config_file = str(config_path)

        except Exception as e:
            raise ConfigError(f"Failed to load configuration from {config_path}: {e}")

    def _update_from_dict(self, data: Dict[str, Any]):
        """Update configuration from dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
            elif key == "plugins":
                if isinstance(value, dict):
                    for plugin_name, plugin_config in value.items():
                        if isinstance(plugin_config, bool):
                            self.plugins_enabled[plugin_name] = plugin_config
                        elif isinstance(plugin_config, dict):
                            self.plugin_config[plugin_name] = plugin_config
                            if "enabled" in plugin_config:
                                self.plugins_enabled[plugin_name] = plugin_config[
                                    "enabled"
                                ]

    def save_to_file(self, config_path: Union[str, Path], format: str = "toml"):
        """Save current configuration to file

        Args:
            config_path: Path where to save configuration
            format: File format (json, yaml, toml)
        """
        config_path = Path(config_path)

        # Create config directory if it doesn't exist
        config_path.parent.mkdir(parents=True, exist_ok=True)

        data = self.to_dict()

        try:
            if format == "json":
                content = json.dumps(data, indent=2)
            elif format == "yaml":
                content = yaml.dump(data, default_flow_style=False)
            elif format == "toml":
                content = toml.dumps(data)
            else:
                raise ConfigError(f"Unsupported format: {format}")

            config_path.write_text(content)

        except Exception as e:
            raise ConfigError(f"Failed to save configuration to {config_path}: {e}")

    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary"""
        return {
            "verbose": self.verbose,
            "debug": self.debug,
            "output_format": self.output_format,
            "color": self.color,
            "pager": self.pager,
            "api_timeout": self.api_timeout,
            "api_retries": self.api_retries,
            "password_length": self.password_length,
            "password_symbols": self.password_symbols,
            "git_auto_push": self.git_auto_push,
            "git_default_branch": self.git_default_branch,
            "format_line_length": self.format_line_length,
            "format_style": self.format_style,
            "plugins": {
                **self.plugins_enabled,
                **self.plugin_config,
            },
        }

    def is_plugin_enabled(self, plugin_name: str) -> bool:
        """Check if a plugin is enabled"""
        return self.plugins_enabled.get(plugin_name, True)

    def get_plugin_config(self, plugin_name: str) -> Dict[str, Any]:
        """Get configuration for a specific plugin"""
        return self.plugin_config.get(plugin_name, {})

    def set_plugin_config(self, plugin_name: str, config: Dict[str, Any]):
        """Set configuration for a specific plugin"""
        self.plugin_config[plugin_name] = config

    @classmethod
    def get_default_config_path(cls) -> Path:
        """Get the default configuration file path"""
        config_home = Path.home() / ".config" / "devhub"
        return config_home / "config.toml"

    @classmethod
    def load_default(cls) -> "Config":
        """Load configuration from default location"""
        config = cls()
        default_path = cls.get_default_config_path()

        if default_path.exists():
            config.load_from_file(default_path)

        return config
