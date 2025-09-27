from typing import Optional, Dict, Any
from engine.config.provider_types import Provider

class FixturesProvider(Provider):
    """
    Deterministic, in-repo fixtures-backed provider.
    For Step 1 it returns a simple, stable set; extended later if needed.
    """
    def get_chart(self, user_id: str, *, correlation_id: Optional[str] = None) -> Dict[str, Any]:
        # Keep tiny and predictable: fixed small gate set
        return {"gates": [1, 2, 3]}
