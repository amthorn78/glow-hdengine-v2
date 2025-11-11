"""Shared constants for narrative routing."""

BANDS = ("Cool", "Open", "Warm", "Glow")
PERSPECTIVES = ("shared", "a_to_b", "b_to_a")
MISSING_NARRATIVE_KEY = "missing_narrative_key"

# Lightweight heuristics to guard inclusive tone and jargon.
INCLUSIVE_BANNED_TOKENS = {
    "crazy",
    "insane",
    "stupid",
    "nuts",
    "lame",
    "normal",
    "abnormal",
}
JARGON_BANNED_TOKENS = {
    "synergy",
    "leverage",
    "bandwidth",
    "pipeline",
    "roadmap",
    "resource",
}
