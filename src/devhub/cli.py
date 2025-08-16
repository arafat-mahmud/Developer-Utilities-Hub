"""
Core CLI module for DevHub

This module provides the main CLI interface using Click and Rich
for beautiful command-line interactions.
"""

import sys
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

from devhub import __version__, __description__
from devhub.core.config import Config
from devhub.core.plugin_manager import PluginManager
from devhub.utils.exceptions import DevHubError
from devhub.utils.logger import setup_logger

console = Console()
logger = setup_logger(__name__)


class DevHubCLI:
    """Main CLI class for DevHub"""

    def __init__(self):
        self.config = Config()
        self.plugin_manager = PluginManager()
        self._setup_plugins()

    def _setup_plugins(self):
        """Initialize and load all plugins"""
        try:
            self.plugin_manager.load_plugins()
            logger.debug(f"Loaded {len(self.plugin_manager.plugins)} plugins")
        except Exception as e:
            logger.error(f"Failed to load plugins: {e}")


@click.group(
    name="devhub",
    context_settings={
        "help_option_names": ["-h", "--help"],
        "max_content_width": 120,
    },
    invoke_without_command=True,
)
@click.option(
    "--version",
    is_flag=True,
    help="Show version information",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Enable verbose output",
)
@click.option(
    "--config",
    type=click.Path(exists=True),
    help="Path to configuration file",
)
@click.pass_context
def cli(ctx: click.Context, version: bool, verbose: bool, config: Optional[str]):
    """🚀 DevHub - The Swiss Army Knife for Developers

    A comprehensive CLI toolkit that combines multiple developer utilities
    into one powerful command-line interface.

    Examples:
        devhub format --lang python main.py
        devhub git clean-branches --merged
        devhub api test --url https://httpbin.org/get
        devhub gen password --length 16
    """

    # Initialize CLI instance
    if ctx.obj is None:
        ctx.obj = DevHubCLI()

    # Handle version flag
    if version:
        show_version()
        return

    # Configure logging
    if verbose:
        setup_logger(__name__, level="DEBUG")
        ctx.obj.config.verbose = True

    # Load custom config if provided
    if config:
        ctx.obj.config.load_from_file(config)

    # Show help if no command provided
    if ctx.invoked_subcommand is None:
        show_welcome()
        click.echo(ctx.get_help())


def show_version():
    """Display version information with beautiful formatting"""

    version_table = Table(show_header=False, box=None, padding=(0, 2))
    version_table.add_row("Version:", f"[bold cyan]{__version__}[/bold cyan]")
    version_table.add_row("Description:", __description__)
    version_table.add_row("Python:", f"{sys.version.split()[0]}")
    version_table.add_row("Platform:", f"{sys.platform}")

    panel = Panel(
        version_table,
        title="[bold blue]🚀 DevHub[/bold blue]",
        border_style="blue",
        padding=(1, 2),
    )

    console.print(panel)


def show_welcome():
    """Display welcome message"""

    welcome_text = Text()
    welcome_text.append("🚀 ", style="bold blue")
    welcome_text.append("Welcome to DevHub", style="bold")
    welcome_text.append(" - The Swiss Army Knife for Developers\n", style="dim")

    console.print(
        Panel(
            welcome_text,
            border_style="blue",
            padding=(0, 2),
        )
    )


def show_plugin_list():
    """Display available plugins"""

    from devhub.core.plugin_manager import PluginManager

    pm = PluginManager()
    pm.load_plugins()

    if not pm.plugins:
        console.print("[yellow]No plugins available[/yellow]")
        return

    plugins_table = Table(
        title="Available Plugins", show_header=True, header_style="bold blue"
    )
    plugins_table.add_column("Plugin", style="cyan", no_wrap=True)
    plugins_table.add_column("Description", style="white")
    plugins_table.add_column("Status", justify="center")

    for plugin_name, plugin in pm.plugins.items():
        status = "[green]✓[/green]" if plugin.is_available() else "[red]✗[/red]"
        plugins_table.add_row(plugin_name, plugin.description, status)

    console.print(plugins_table)


@cli.group(name="plugin")
def plugin_group():
    """Plugin management commands"""
    pass


@plugin_group.command(name="list")
def list_plugins():
    """List all available plugins"""
    show_plugin_list()


def main():
    """Main entry point for the CLI"""
    try:
        # Import and register all plugin commands
        from devhub.plugins import register_plugins

        register_plugins(cli)

        # Run the CLI
        cli()

    except DevHubError as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        console.print("\n[yellow]Operation cancelled by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        logger.exception("Unexpected error occurred")
        console.print(f"[red]Unexpected error:[/red] {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
