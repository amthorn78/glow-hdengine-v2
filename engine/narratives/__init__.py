"""Narrative pack loader, router, and composer for Aux narratives."""

from .state import get_pack
from .router import route_keys
from .composer import compose_text
from .preview import AuxPublicEmission, emit_public_aux
from .constants import MISSING_NARRATIVE_KEY

__all__ = [
    "get_pack",
    "route_keys",
    "compose_text",
    "AuxPublicEmission",
    "emit_public_aux",
    "MISSING_NARRATIVE_KEY",
]
