from __future__ import annotations
from typing import Any, Dict
from adapters._net import require_network

def fetch_chart_raw(payload: Dict[str, Any]) -> Dict[str, Any]:
    require_network('hdapi')
    raise NotImplementedError
