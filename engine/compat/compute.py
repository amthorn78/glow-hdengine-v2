from __future__ import annotations

# Public compat seam for Reader. Numeric-free, deterministic, AB↔BA identical.
# Inputs: two normalized private charts (dicts) from engine.charts.loader.load_chart(...)
# Output: minimal public shape (band + categories[id="harmony"]).

_BANDS = ("Cool", "Open", "Warm", "Glow")

def compat_public(a: dict, b: dict) -> dict:
    if not isinstance(a, dict) or not isinstance(b, dict):
        raise TypeError("compat_public expects two dicts")
    # Symmetric, order-independent choice (pinned for now)
    band = "Open"
    return {
        "band": band,
        "categories": [
            {"id": "harmony", "band": band},
        ],
    }
