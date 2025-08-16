"""
Logging utilities for DevHub

This module provides consistent logging setup across the application.
"""

import logging
import sys
from pathlib import Path
from typing import Optional, Union

from rich.logging import RichHandler
from rich.console import Console


def setup_logger(
    name: str,
    level: Union[str, int] = "INFO",
    log_file: Optional[Union[str, Path]] = None,
    console_output: bool = True,
    rich_tracebacks: bool = True,
) -> logging.Logger:
    """
    Set up a logger with Rich formatting

    Args:
        name: Logger name
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional path to log file
        console_output: Whether to output to console
        rich_tracebacks: Whether to use rich tracebacks

    Returns:
        Configured logger instance
    """

    # Convert string level to int if needed
    if isinstance(level, str):
        level = getattr(logging, level.upper())

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Clear any existing handlers
    logger.handlers.clear()

    # Create console handler with Rich formatting
    if console_output:
        console = Console(stderr=True)
        rich_handler = RichHandler(
            console=console,
            show_time=True,
            show_level=True,
            show_path=False,
            rich_tracebacks=rich_tracebacks,
            tracebacks_suppress=[
                "click",
                "rich",
                "urllib3",
                "requests",
            ],
        )
        rich_handler.setLevel(level)

        # Format for rich handler
        rich_format = "%(message)s"
        rich_handler.setFormatter(logging.Formatter(rich_format))

        logger.addHandler(rich_handler)

    # Create file handler if log file is specified
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)

        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(level)

        # Format for file handler (more detailed)
        file_format = (
            "%(asctime)s - %(name)s - %(levelname)s - "
            "%(filename)s:%(lineno)d - %(message)s"
        )
        file_handler.setFormatter(logging.Formatter(file_format))

        logger.addHandler(file_handler)

    # Prevent propagation to root logger
    logger.propagate = False

    return logger


def get_logger(name: str) -> logging.Logger:
    """
    Get an existing logger or create a new one with default settings

    Args:
        name: Logger name

    Returns:
        Logger instance
    """
    logger = logging.getLogger(name)

    # If logger has no handlers, set it up with defaults
    if not logger.handlers:
        return setup_logger(name)

    return logger


def set_global_log_level(level: Union[str, int]):
    """
    Set log level for all DevHub loggers

    Args:
        level: Logging level to set
    """
    if isinstance(level, str):
        level = getattr(logging, level.upper())

    # Set level for all existing DevHub loggers
    for logger_name in logging.root.manager.loggerDict:
        if logger_name.startswith("devhub"):
            logger = logging.getLogger(logger_name)
            logger.setLevel(level)

            # Update handler levels too
            for handler in logger.handlers:
                handler.setLevel(level)


def configure_debug_logging():
    """Configure logging for debug mode"""
    import os

    # Create debug log file in temp directory
    debug_log = Path.home() / ".cache" / "devhub" / "debug.log"

    # Set up root DevHub logger for debug
    setup_logger(
        "devhub",
        level="DEBUG",
        log_file=debug_log,
        console_output=True,
        rich_tracebacks=True,
    )

    # Also log to stderr for immediate visibility
    debug_handler = logging.StreamHandler(sys.stderr)
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(logging.Formatter("DEBUG: %(name)s - %(message)s"))

    # Add debug handler to all DevHub loggers
    for logger_name in logging.root.manager.loggerDict:
        if logger_name.startswith("devhub"):
            logger = logging.getLogger(logger_name)
            logger.addHandler(debug_handler)


def silence_noisy_loggers():
    """Silence overly verbose third-party loggers"""
    noisy_loggers = [
        "urllib3.connectionpool",
        "requests.packages.urllib3.connectionpool",
        "git.cmd",
        "asyncio",
    ]

    for logger_name in noisy_loggers:
        logging.getLogger(logger_name).setLevel(logging.WARNING)
