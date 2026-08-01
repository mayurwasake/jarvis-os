"""
JARVIS OS Plugin Manager

Responsible for managing plugins throughout the operating system.

Responsibilities
----------------
- Register plugins
- Unregister plugins
- Retrieve plugins
- List available plugins
- Future:
    - Auto-discovery
    - Plugin loading from folder
    - Plugin lifecycle
"""

from __future__ import annotations

from typing import Any

from app.logging_system import logger


class PluginManager:
    """
    Central Plugin Manager.
    """

    def __init__(self) -> None:

        self._plugins: dict[str, Any] = {}

        logger.info("Plugin Manager initialized.")

    # -------------------------------------------------------
    # Register
    # -------------------------------------------------------

    def register(self, name: str, plugin: Any) -> None:
        """
        Register a plugin.
        """

        if name in self._plugins:
            raise ValueError(
                f"Plugin '{name}' is already registered."
            )

        self._plugins[name] = plugin

        logger.info(f"Plugin '{name}' registered.")

    # -------------------------------------------------------
    # Get
    # -------------------------------------------------------

    def get(self, name: str) -> Any:
        """
        Return a plugin.
        """

        if name not in self._plugins:
            raise KeyError(
                f"Plugin '{name}' is not registered."
            )

        return self._plugins[name]

    # -------------------------------------------------------
    # Remove
    # -------------------------------------------------------

    def unregister(self, name: str) -> None:
        """
        Remove a plugin.
        """

        if name not in self._plugins:
            raise KeyError(
                f"Plugin '{name}' is not registered."
            )

        del self._plugins[name]

        logger.info(f"Plugin '{name}' removed.")

    # -------------------------------------------------------
    # Exists
    # -------------------------------------------------------

    def exists(self, name: str) -> bool:
        """
        Check if plugin exists.
        """

        return name in self._plugins

    # -------------------------------------------------------
    # List
    # -------------------------------------------------------

    def list_plugins(self) -> list[str]:
        """
        Return all plugin names.
        """

        return sorted(self._plugins.keys())

    # -------------------------------------------------------
    # Count
    # -------------------------------------------------------

    def count(self) -> int:
        """
        Return number of plugins.
        """

        return len(self._plugins)

    # -------------------------------------------------------
    # Clear
    # -------------------------------------------------------

    def clear(self) -> None:
        """
        Remove all plugins.
        """

        self._plugins.clear()

        logger.info("All plugins removed.")

    # -------------------------------------------------------
    # Dunder Methods
    # -------------------------------------------------------

    def __contains__(self, name: str) -> bool:
        return name in self._plugins

    def __len__(self) -> int:
        return len(self._plugins)

    def __repr__(self) -> str:
        return (
            f"PluginManager("
            f"plugins={list(self._plugins.keys())})"
        )