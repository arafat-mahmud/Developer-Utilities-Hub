"""
Custom exceptions for DevHub

This module defines all custom exceptions used throughout the DevHub application.
"""


class DevHubError(Exception):
    """Base exception for all DevHub errors"""

    def __init__(self, message: str, code: int = 1):
        super().__init__(message)
        self.message = message
        self.code = code


class ConfigError(DevHubError):
    """Raised when there are configuration-related errors"""

    def __init__(self, message: str):
        super().__init__(f"Configuration error: {message}", code=2)


class PluginError(DevHubError):
    """Raised when there are plugin-related errors"""

    def __init__(self, message: str, plugin_name: str = None):
        if plugin_name:
            message = f"Plugin '{plugin_name}': {message}"
        super().__init__(f"Plugin error: {message}", code=3)


class CommandError(DevHubError):
    """Raised when a command execution fails"""

    def __init__(self, message: str, command: str = None):
        if command:
            message = f"Command '{command}': {message}"
        super().__init__(f"Command error: {message}", code=4)


class ValidationError(DevHubError):
    """Raised when input validation fails"""

    def __init__(self, message: str, field: str = None):
        if field:
            message = f"Field '{field}': {message}"
        super().__init__(f"Validation error: {message}", code=5)


class NetworkError(DevHubError):
    """Raised when network operations fail"""

    def __init__(self, message: str, url: str = None):
        if url:
            message = f"URL '{url}': {message}"
        super().__init__(f"Network error: {message}", code=6)


class FileSystemError(DevHubError):
    """Raised when file system operations fail"""

    def __init__(self, message: str, path: str = None):
        if path:
            message = f"Path '{path}': {message}"
        super().__init__(f"File system error: {message}", code=7)


class SecurityError(DevHubError):
    """Raised when security-related operations fail"""

    def __init__(self, message: str):
        super().__init__(f"Security error: {message}", code=8)


class FormatError(DevHubError):
    """Raised when formatting operations fail"""

    def __init__(self, message: str, formatter: str = None):
        if formatter:
            message = f"Formatter '{formatter}': {message}"
        super().__init__(f"Format error: {message}", code=9)


class GitError(DevHubError):
    """Raised when Git operations fail"""

    def __init__(self, message: str, repository: str = None):
        if repository:
            message = f"Repository '{repository}': {message}"
        super().__init__(f"Git error: {message}", code=10)
