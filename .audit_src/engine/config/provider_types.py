from typing import Protocol, Optional, Dict, Any

class Provider(Protocol):
    def get_chart(self, user_id: str, *, correlation_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Contract:
          - Return a dict like {"gates": [int, ...]} deterministically.
          - MUST NOT perform network in tests; no import-time I/O.
          - May raise typed provider errors (e.g., refusal in SAFE_MODE).
        """
        ...
