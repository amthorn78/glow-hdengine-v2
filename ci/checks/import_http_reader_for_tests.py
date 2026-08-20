"""Canonical test-only import seam for ``adapter.http_reader``.

Dynamic Reader import tests use this helper so CI ownership is explicit and
machine-checkable without attempting to interpret arbitrary Python programs.
"""
from __future__ import annotations

import importlib
import sys
from types import ModuleType


def import_http_reader_for_test() -> ModuleType:
    """Import a fresh Reader module for one isolated behavioral assertion."""
    importlib.invalidate_caches()
    sys.modules.pop("adapter.http_reader", None)
    sys.modules.pop("adapter", None)
    return importlib.import_module("adapter.http_reader")
