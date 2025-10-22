"""
Import-time I/O guard for engine.compat.type_strategy_v0

We monkeypatch file I/O and socket creation to raise during import/reload.
The module must import successfully and leave its internal caches as None.
"""

import importlib
import builtins
import pathlib
import socket


def test_import_no_io() -> None:
    import engine.compat.type_strategy_v0 as ts

    # Save originals
    orig_open = builtins.open
    orig_path_open = pathlib.Path.open
    orig_socket = socket.socket

    try:
        # Raise on any file open during import
        def _boom_file(*args, **kwargs):
            raise RuntimeError("I/O not allowed during import")

        # Raise on any socket creation during import
        def _boom_sock(*args, **kwargs):
            raise RuntimeError("net I/O not allowed during import")

        builtins.open = _boom_file        # type: ignore[assignment]
        pathlib.Path.open = _boom_file    # type: ignore[assignment]
        socket.socket = _boom_sock        # type: ignore[assignment]

        # Reload with guards active
        ts = importlib.reload(ts)
    finally:
        # Restore originals
        builtins.open = orig_open         # type: ignore[assignment]
        pathlib.Path.open = orig_path_open  # type: ignore[assignment]
        socket.socket = orig_socket       # type: ignore[assignment]

    # Caches must still be None (no pinned data read on import)
    assert getattr(ts, "_band_rules") is None
    assert getattr(ts, "_band_order") is None
    assert getattr(ts, "_type_strategy_map") is None
