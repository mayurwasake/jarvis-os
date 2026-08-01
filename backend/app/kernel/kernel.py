"""
JARVIS OS Kernel

The Kernel is the heart of the operating system.

Responsibilities
----------------
- Boot the system
- Shutdown the system
- Manage core services
- Maintain system state

The Kernel DOES NOT:
- Talk to LLMs
- Read files
- Execute tools
- Perform business logic
"""

from __future__ import annotations

from enum import Enum

from app.events import EventBus
from app.logging_system import logger
from app.registry import ServiceRegistry


class KernelState(str, Enum):
    """
    Possible states of the Kernel.
    """

    CREATED = "CREATED"
    BOOTING = "BOOTING"
    RUNNING = "RUNNING"
    STOPPED = "STOPPED"


class Kernel:
    """
    Central Kernel of JARVIS OS.
    """

    def __init__(self) -> None:

        logger.info("Creating Kernel...")

        self.state = KernelState.CREATED

        self.registry = ServiceRegistry()

        self.event_bus = EventBus()

        logger.info("Kernel created successfully.")

    # --------------------------------------------------
    # Boot
    # --------------------------------------------------

    def boot(self) -> None:

        logger.info("Boot sequence started.")

        self.state = KernelState.BOOTING

        # Register Core Services

        self.registry.register("event_bus", self.event_bus)

        self.registry.register("registry", self.registry)

        self.state = KernelState.RUNNING

        logger.info("Kernel boot completed.")

    # --------------------------------------------------
    # Shutdown
    # --------------------------------------------------

    def shutdown(self) -> None:

        logger.info("Shutdown sequence started.")

        self.state = KernelState.STOPPED

        self.registry.clear()

        self.event_bus.clear()

        logger.info("Kernel shutdown complete.")

    # --------------------------------------------------
    # Status
    # --------------------------------------------------

    def is_running(self) -> bool:

        return self.state == KernelState.RUNNING

    # --------------------------------------------------
    # Info
    # --------------------------------------------------

    def status(self) -> dict:

        return {
            "state": self.state.value,
            "registered_services": self.registry.count(),
            "event_bus_ready": True,
        }

    def __repr__(self) -> str:

        return (
            f"Kernel(state={self.state}, "
            f"services={self.registry.count()})"
        )