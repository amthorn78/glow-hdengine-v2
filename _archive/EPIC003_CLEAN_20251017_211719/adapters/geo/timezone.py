from __future__ import annotations
from adapters._net import require_network

def timezone_for(lat: str, lng: str, birth_utc_ts: int):
    require_network('geo.timezone')
    raise NotImplementedError
