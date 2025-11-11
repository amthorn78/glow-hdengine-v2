"""Narrative pack loader, router, and composer for Aux narratives."""

from .state import get_pack
from .router import route_keys
from .composer import compose_text
from .constants import MISSING_NARRATIVE_KEY

__all__ = [
    "get_pack",
    "route_keys",
    "compose_text",
    "MISSING_NARRATIVE_KEY",
]
