from __future__ import annotations

from typing import Final

DEV_COMPAT_ENGINE_TAG: Final = "dev"
DEV_COMPAT_RELEASE_ID: Final = "dev"
DEV_COMPAT_INVOCATION_TAG: Final = "INV-DEV"


def dev_compat_identity() -> dict[str, str]:
    """Return the stable identity contract for non-production compat harnesses."""

    return {
        "engine_tag": DEV_COMPAT_ENGINE_TAG,
        "release_id": DEV_COMPAT_RELEASE_ID,
        "invocation_tag": DEV_COMPAT_INVOCATION_TAG,
    }
