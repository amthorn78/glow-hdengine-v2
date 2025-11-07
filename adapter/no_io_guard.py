"""Request-scoped guard that records outbound network attempts."""
from __future__ import annotations

import functools
import socket
from typing import Callable, List, Tuple


PatchSpec = Tuple[object, str, Callable[..., object]]


class NoIoGuard:
    """Context manager that counts socket/DNS attempts within the process."""

    def __init__(self) -> None:
        self.attempts = 0
        self._patches: List[PatchSpec] = []

    def __enter__(self) -> "NoIoGuard":
        self._patch(socket.socket, "connect")
        self._patch(socket.socket, "connect_ex")
        self._patch(socket, "getaddrinfo")
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        for target, attr, original in reversed(self._patches):
            setattr(target, attr, original)
        self._patches.clear()
        return False

    def _patch(self, target: object, attribute: str) -> None:
        try:
            original = getattr(target, attribute)
        except AttributeError:  # pragma: no cover - guard for exotic runtimes
            return
        if not callable(original):  # pragma: no cover - safety net
            return

        @functools.wraps(original)
        def wrapper(*args, **kwargs):
            self.attempts += 1
            return original(*args, **kwargs)

        setattr(target, attribute, wrapper)  # type: ignore[attr-defined]
        self._patches.append((target, attribute, original))


__all__ = ["NoIoGuard"]
