import os, re, glob
from adapter.logging_filter import log_startup_line

class EnvGuardError(Exception):
    """Pre-serve env/override violation with typed code."""
    def __init__(self, code: str, message: str | None = None):
        self.code = code
        self.details = None
        super().__init__(message or code)

_PAT = re.compile(r'(?i)(?:^|_)(OVERRIDE|OVERRIDES|TOGGLES)(?:$)')

def _is_prod() -> bool:
    env = os.getenv("ENGINE_ENV") or os.getenv("APP_ENV") or "dev"
    return env.lower() == "prod"

def _has_env_override() -> bool:
    for k in os.environ.keys():
        if _PAT.search(k) or k.startswith("ENGINE_TOGGLES_"):
            return True
    return False

def _has_file_override() -> bool:
    return bool(glob.glob("config/overrides/*.json"))

def validate_or_fail(app) -> None:
    hit = _has_env_override() or _has_file_override()
    if _is_prod() and hit:
        log_startup_line(app, status=0)  # keys-only startup line; then fail
        raise EnvGuardError("CANON_TOGGLES_OVERRIDE_IN_PROD", "prod overrides detected")
    # non-prod: warn handled elsewhere; do not raise
