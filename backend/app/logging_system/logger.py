"""
JARVIS OS Logging System

This module provides a centralized logger for the entire
operating system.

Every module in JARVIS OS should import this logger instead
of creating its own.
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from app.config import settings

# ------------------------------------------------------------------
# Log Directory
# ------------------------------------------------------------------

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "jarvis.log"


# ------------------------------------------------------------------
# Custom Formatter
# ------------------------------------------------------------------

class JarvisFormatter(logging.Formatter):
    """
    Custom log formatter.
    """

    FORMAT = (
        "%(asctime)s | "
        "%(levelname)-8s | "
        "%(name)s | "
        "%(message)s"
    )

    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self) -> None:
        super().__init__(
            fmt=self.FORMAT,
            datefmt=self.DATE_FORMAT,
        )


# ------------------------------------------------------------------
# Logger Factory
# ------------------------------------------------------------------

def create_logger() -> logging.Logger:
    """
    Creates and configures the global JARVIS logger.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """

    logger = logging.getLogger("JARVIS")

    if logger.handlers:
        return logger

    logger.setLevel(settings.log_level)

    formatter = JarvisFormatter()

    # ---------------- Console ----------------

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # ---------------- File ----------------

    file_handler = RotatingFileHandler(
        filename=LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


# ------------------------------------------------------------------
# Singleton Logger
# ------------------------------------------------------------------

logger = create_logger()