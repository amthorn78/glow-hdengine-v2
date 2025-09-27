import re

# Canonical pattern: "INV-" + 16 lowercase hex (v4.1 edits)
_INV_RE = re.compile(r"^INV-[a-f0-9]{16}$")

def is_valid_invocation_tag(tag: str) -> bool:
    """Return True iff tag matches ^INV-[a-f0-9]{16}$ exactly."""
    if not isinstance(tag, str):
        return False
    return bool(_INV_RE.fullmatch(tag))

def validate_invocation_tag(tag: str) -> str:
    """Return tag if valid; else raise ValueError (code: INVOCATION_TAG_INVALID)."""
    if is_valid_invocation_tag(tag):
        return tag
    raise ValueError("INVOCATION_TAG_INVALID")
