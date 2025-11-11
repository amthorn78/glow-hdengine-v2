"""Singleton access to the loaded narrative pack."""

from __future__ import annotations

from threading import Lock
from typing import Optional

from .loader import NarrativePack, load_pack


_PACK: Optional[NarrativePack] = None
_LOCK = Lock()


def get_pack() -> NarrativePack:
    """Return the loaded narrative pack, loading it on first use."""

    global _PACK
    if _PACK is None:
        with _LOCK:
            if _PACK is None:
                _PACK = load_pack()
    return _PACK
