"""Test configuration and fixtures for DevHub tests"""

import pytest
import tempfile
from pathlib import Path
from click.testing import CliRunner

from devhub.cli import cli
from devhub.core.config import Config


@pytest.fixture
def cli_runner():
    """Provide a Click CLI runner for testing"""
    # Register plugins for testing
    from devhub.plugins import register_plugins

    register_plugins(cli)

    return CliRunner()


@pytest.fixture
def temp_dir():
    """Provide a temporary directory for tests"""
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield Path(tmp_dir)


@pytest.fixture
def sample_python_file(temp_dir):
    """Create a sample Python file for testing"""
    file_path = temp_dir / "sample.py"
    file_path.write_text(
        """
def hello( name ):
    print(f'Hello {name}!')

if __name__ == '__main__':
    hello('World')
"""
    )
    return file_path


@pytest.fixture
def sample_json_file(temp_dir):
    """Create a sample JSON file for testing"""
    file_path = temp_dir / "sample.json"
    file_path.write_text('{"name": "test", "value": 123}')
    return file_path


@pytest.fixture
def config():
    """Provide a test configuration"""
    return Config()


@pytest.fixture
def mock_api_response():
    """Mock API response for testing"""
    return {
        "status_code": 200,
        "headers": {"content-type": "application/json"},
        "json": {"message": "success"},
        "content": '{"message": "success"}',
        "response_time": 0.123,
    }
