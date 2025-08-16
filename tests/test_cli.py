"""Test the main CLI interface"""

from click.testing import CliRunner
from devhub.cli import cli


def test_cli_help(cli_runner):
    """Test that CLI help works"""
    result = cli_runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "DevHub" in result.output
    assert "Swiss Army Knife" in result.output


def test_cli_version(cli_runner):
    """Test version flag"""
    result = cli_runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "1.0.0" in result.output


def test_plugin_list(cli_runner):
    """Test plugin list command"""
    result = cli_runner.invoke(cli, ["plugin", "list"])
    assert result.exit_code == 0


def test_format_help(cli_runner):
    """Test format plugin help"""
    result = cli_runner.invoke(cli, ["format", "--help"])
    assert result.exit_code == 0
    assert "formatting" in result.output.lower()


def test_api_help(cli_runner):
    """Test API plugin help"""
    result = cli_runner.invoke(cli, ["api", "--help"])
    assert result.exit_code == 0
    assert "api" in result.output.lower()
