"""
JARVIS OS Event Bus

The Event Bus is the communication backbone of the operating system.

Instead of modules talking directly to one another,
they communicate by publishing and subscribing to events.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Callable

from app.logging_system import logger

EventHandler = Callable[[Any], None]


class EventBus:
    """
    Central Event Bus.

    Example
    -------
    >>> bus = EventBus()

    >>> def greet(name):
    ...     print(f"Hello {name}")

    >>> bus.subscribe("user_login", greet)
    >>> bus.publish("user_login", "Mayur")
    Hello Mayur
    """

    def __init__(self) -> None:
        self._subscribers: dict[str, list[EventHandler]] = defaultdict(list)

        logger.info("Event Bus initialized.")

    # ----------------------------------------------------
    # Subscribe
    # ----------------------------------------------------

    def subscribe(self, event_name: str, handler: EventHandler) -> None:
        """
        Subscribe a handler to an event.
        """

        if handler not in self._subscribers[event_name]:
            self._subscribers[event_name].append(handler)

            logger.debug(
                f"Subscribed '{handler.__name__}' "
                f"to event '{event_name}'."
            )

    # ----------------------------------------------------
    # Unsubscribe
    # ----------------------------------------------------

    def unsubscribe(self, event_name: str, handler: EventHandler) -> None:
        """
        Remove a handler from an event.
        """

        if handler in self._subscribers[event_name]:

            self._subscribers[event_name].remove(handler)

            logger.debug(
                f"Unsubscribed '{handler.__name__}' "
                f"from event '{event_name}'."
            )

    # ----------------------------------------------------
    # Publish
    # ----------------------------------------------------

    def publish(
        self,
        event_name: str,
        data: Any = None,
    ) -> None:
        """
        Publish an event.

        Every subscriber receives the same data.
        """

        logger.info(f"Publishing event '{event_name}'")

        handlers = self._subscribers.get(event_name, [])

        for handler in handlers:
            handler(data)

    # ----------------------------------------------------
    # Utility
    # ----------------------------------------------------

    def has_subscribers(self, event_name: str) -> bool:
        """
        Returns True if the event has subscribers.
        """

        return len(self._subscribers[event_name]) > 0

    def clear(self) -> None:
        """
        Remove all subscribers.
        """

        self._subscribers.clear()

        logger.info("Event Bus cleared.")