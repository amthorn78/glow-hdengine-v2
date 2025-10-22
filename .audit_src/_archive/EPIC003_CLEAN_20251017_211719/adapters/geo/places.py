from __future__ import annotations
from adapters._net import require_network

def lookup_place(q: str):
    require_network('geo.places')
    raise NotImplementedError
