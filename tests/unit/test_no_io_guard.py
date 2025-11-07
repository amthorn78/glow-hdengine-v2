from __future__ import annotations

import socket

from adapter.no_io_guard import NoIoGuard


def test_no_io_guard_counts_attempts():
    guard = NoIoGuard()
    with guard:
        try:
            socket.getaddrinfo("localhost", 80)
        except socket.gaierror:
            pass
    assert guard.attempts >= 1
