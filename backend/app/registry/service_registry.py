"""
JARVIS OS Service Registry

The Service Registry is responsible for registering and
providing access to shared services throughout the operating system.

Examples of services:
- Logger
- Event Bus
- Kernel
- Memory
- Planner
- Database
- Plugin Manager
"""

from __future__ import annotations

from typing import Any

from app.logging_system import logger


class ServiceRegistry:
    """
    Central registry for all shared services.
    """

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}

        logger.info("Service Registry initialized.")

    # ---------------------------------------------------------
    # Register
    # ---------------------------------------------------------

    def register(self, name: str, service: Any) -> None:
        """
        Register a service.

        Raises
        ------
        ValueError
            If the service is already registered.
        """

        if name in self._services:
            raise ValueError(f"Service '{name}' is already registered.")

        self._services[name] = service

        logger.info(f"Registered service '{name}'.")

    # ---------------------------------------------------------
    # Get
    # ---------------------------------------------------------

    def get(self, name: str) -> Any:
        """
        Retrieve a registered service.

        Raises
        ------
        KeyError
            If the service does not exist.
        """

        if name not in self._services:
            raise KeyError(f"Service '{name}' is not registered.")

        return self._services[name]

    # ---------------------------------------------------------
    # Remove
    # ---------------------------------------------------------

    def unregister(self, name: str) -> None:
        """
        Remove a registered service.
        """

        if name not in self._services:
            raise KeyError(f"Service '{name}' is not registered.")

        del self._services[name]

        logger.info(f"Unregistered service '{name}'.")

    # ---------------------------------------------------------
    # Utility Methods
    # ---------------------------------------------------------

    def exists(self, name: str) -> bool:
        """
        Check whether a service exists.
        """

        return name in self._services

    def list_services(self) -> list[str]:
        """
        Return all registered service names.
        """

        return sorted(self._services.keys())

    def clear(self) -> None:
        """
        Remove all registered services.
        """

        self._services.clear()

        logger.info("Service Registry cleared.")

    def count(self) -> int:
        """
        Return the number of registered services.
        """

        return len(self._services)

    def __contains__(self, name: str) -> bool:
        return name in self._services

    def __len__(self) -> int:
        return len(self._services)

    def __repr__(self) -> str:
        return f"ServiceRegistry(services={list(self._services.keys())})"