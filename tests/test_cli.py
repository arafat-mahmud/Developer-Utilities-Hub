"""Test the main CLI interface"""

import pytest
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


def test_verbose_flag(cli_runner):
    """Test verbose flag"""
    result = cli_runner.invoke(cli, ["--verbose", "--help"])
    assert result.exit_code == 0


def test_config_option(cli_runner):
    """Test config option"""
    result = cli_runner.invoke(cli, ["--config", "/nonexistent/config.yaml", "--help"])
    assert result.exit_code == 0


def test_api_test_help(cli_runner):
    """Test API test command help"""
    result = cli_runner.invoke(cli, ["api", "test", "--help"])
    assert result.exit_code == 0
    assert "url" in result.output.lower()


def test_api_headers_help(cli_runner):
    """Test API headers command help"""
    result = cli_runner.invoke(cli, ["api", "headers", "--help"])
    assert result.exit_code == 0


def test_api_benchmark_help(cli_runner):
    """Test API benchmark command help"""
    result = cli_runner.invoke(cli, ["api", "benchmark", "--help"])
    assert result.exit_code == 0
    assert "requests" in result.output.lower()


def test_format_check_help(cli_runner):
    """Test format check command help"""
    result = cli_runner.invoke(cli, ["format", "check", "--help"])
    assert result.exit_code == 0


def test_format_code_help(cli_runner):
    """Test format code command help"""
    result = cli_runner.invoke(cli, ["format", "code", "--help"])
    assert result.exit_code == 0


def test_invalid_command(cli_runner):
    """Test invalid command"""
    result = cli_runner.invoke(cli, ["invalid-command"])
    assert result.exit_code != 0


def test_empty_args(cli_runner):
    """Test CLI with no arguments"""
    result = cli_runner.invoke(cli, [])
    assert result.exit_code == 0  # Should show help
