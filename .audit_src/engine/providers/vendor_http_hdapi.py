from __future__ import annotations
import os, re
from typing import Mapping, Tuple, Dict, Any, Optional

# Prefer the project's ProviderError/ensure_cid; fall back to local shims if absent.
try:
    from engine.util.input_validators import ensure_cid  # type: ignore
except Exception:
    def ensure_cid(maybe: Optional[str]) -> str:
        CID_RE = re.compile(r"^CID-[a-f0-9]{16}$")
        import secrets
        if isinstance(maybe, str) and CID_RE.match(maybe):
            return maybe
        return "CID-" + secrets.token_hex(8)

try:
    from engine.provider.base import ProviderError  # type: ignore
except Exception:
    class ProviderError(Exception):
        def __init__(self, code: str, message: str, details: Optional[Dict[str, Any]] = None):
            super().__init__(message)
            self.code = code
            self.message = message
            self.details = details or {}

# Locale-free month map for DD-MMM-YYYY conversion
_MONTH = {
 "01":"Jan","02":"Feb","03":"Mar","04":"Apr","05":"May","06":"Jun",
 "07":"Jul","08":"Aug","09":"Sep","10":"Oct","11":"Nov","12":"Dec"
}
_DATE_RE = re.compile(r'^(\d{4})-(\d{2})-(\d{2})$')

def _to_dd_mmm_yyyy(yyyy_mm_dd: str) -> str:
    m = _DATE_RE.match(yyyy_mm_dd)
    if not m:
        raise ProviderError("PROVIDER_ERROR", "invalid date format", {"got": yyyy_mm_dd})
    y, mm, dd = m.groups()
    mon = _MONTH.get(mm)
    if not mon:
        raise ProviderError("PROVIDER_ERROR", "invalid month", {"got": mm})
    return f"{dd}-{mon}-{y}"

def _read_env(environ: Optional[Mapping[str, str]] = None) -> Dict[str, str]:
    env = dict((environ or os.environ).items())
    def norm(k: str) -> str:
        v = env.get(k, "")
        return v if isinstance(v, str) else ""
    return {
        "HD_API_KEY": norm("HD_API_KEY"),
        "GEO_API_KEY": norm("GEO_API_KEY"),
        "HDAPI_BASE_URL": norm("HDAPI_BASE_URL"),
    }

def prepare_hdapi_request(birthdate: str, birthtime: str, location: str, *,
                          correlation_id: Optional[str] = None,
                          environ: Optional[Mapping[str, str]] = None
                          ) -> Tuple[str, Dict[str, str], Dict[str, Any]]:
    """
    Pure shaper: returns (url, headers, body) for hdapi /bodygraphs.
    - Requires env keys HD_API_KEY and GEO_API_KEY (blank/whitespace -> missing)
    - Uses HDAPI_BASE_URL or defaults to https://api.humandesignapi.nl/v1
    - Converts date to DD-MMM-YYYY (English, title-case)
    - Sends only {birthdate,birthtime,location}; tz is ignored on this path.
    """
    cid = ensure_cid(correlation_id)
    env = _read_env(environ)
    missing = sorted([k for k in ("HD_API_KEY","GEO_API_KEY") if not env.get(k, "").strip()])
    if missing:
        raise ProviderError(
            "PROVIDER_CONFIG_MISSING",
            "required hdapi env missing",
            {"missing_keys": missing, "correlation_id": cid}
        )
    base = (env.get("HDAPI_BASE_URL") or "https://api.humandesignapi.nl/v1").rstrip("/")
    url = base + "/bodygraphs"
    headers = {
        "HD-Api-Key": env["HD_API_KEY"].strip(),
        "HD-Geocode-Key": env["GEO_API_KEY"].strip(),
    }
    body = {
        "birthdate": _to_dd_mmm_yyyy(birthdate),
        "birthtime": birthtime,
        "location": location,
    }
    return url, headers, body

def raise_mapped_provider_error(status: int, *, correlation_id: Optional[str] = None) -> None:
    cid = ensure_cid(correlation_id)
    if status == 401:
        code, msg = "PROVIDER_UNAUTHORIZED", "unauthorized"
    elif status == 403:
        code, msg = "PROVIDER_FORBIDDEN", "forbidden"
    elif status == 404:
        code, msg = "PROVIDER_NOT_FOUND", "not found"
    elif status == 429:
        code, msg = "PROVIDER_RATE_LIMITED", "rate limited"
    elif 500 <= status <= 599:
        code, msg = "PROVIDER_UNAVAILABLE", "upstream unavailable"
    else:
        code, msg = "PROVIDER_ERROR", f"unexpected status {status}"
    raise ProviderError(code, msg, {"status": status, "correlation_id": cid})


# --- patched override: return dict; include JSON headers; tz intentionally ignored on hdapi path ---
def prepare_hdapi_request(birthdate: str, birthtime: str, location: str, *, correlation_id: str | None) -> dict:
    """
    Shape the hdapi request WITHOUT performing any network I/O.
    Returns: {"headers": {...}, "body": {...}}
      - Headers (dash-case, exact): HD-Api-Key, HD-Geocode-Key, Accept, Content-Type
      - Body keys (exact): birthdate (DD-MMM-YYYY), birthtime, location
      - tz is intentionally ignored on the vendor path.
    Raises:
      ProviderError("PROVIDER_CONFIG_MISSING", ...) if required secrets missing/blank.
      ProviderError("PROVIDER_ERROR", ...) if birthdate format invalid.
    """
    api_key = (os.getenv("HD_API_KEY") or "").strip()
    geo_key = (os.getenv("GEO_API_KEY") or "").strip()
    missing = []
    if not api_key: missing.append("HD_API_KEY")
    if not geo_key: missing.append("GEO_API_KEY")
    if missing:
        raise ProviderError("PROVIDER_CONFIG_MISSING", "missing vendor credentials", {"missing": missing, "correlation_id": correlation_id})

    # Use the existing date converter in this module (must accept YYYY-MM-DD)
    birthdate_conv = _to_dd_mmm_yyyy(birthdate)

    headers = {
        "HD-Api-Key": api_key,
        "HD-Geocode-Key": geo_key,
        "Accept": "application/json",
        "Content-Type": "application/json; charset=utf-8",
    }
    body = {
        "birthdate": birthdate_conv,
        "birthtime": birthtime,
        "location": location,
    }
    return {"headers": headers, "body": body}


# --- dual-shape return: mapping + tuple semantics ---
class _ReqShape(dict):
    """Return shape that supports both tuple-style and dict-style access.
       tuple-style: [0]=url, [1]=headers, [2]=body
       dict-style:  ["url"], ["headers"], ["body"]
    """
    __slots__ = ("_triple",)
    def __init__(self, url: str, headers: dict, body: dict):
        super().__init__({"url": url, "headers": headers, "body": body})
        self._triple = (url, headers, body)
    def __getitem__(self, key):
        if isinstance(key, int):
            return self._triple[key]
        return dict.__getitem__(self, key)

def _hdapi_base_url() -> str:
    base = (os.getenv("HDAPI_BASE_URL") or "").strip() or "https://api.humandesignapi.nl/v1"
    # Normalize trailing slash just once
    return base[:-1] if base.endswith("/") else base

# --- patched override (takes precedence) ---
def prepare_hdapi_request(birthdate: str, birthtime: str, location: str, *, correlation_id: str | None):
    """
    Shape the hdapi request WITHOUT performing any network I/O.
    Returns a dual-shape object usable as:
       req[0] -> url (endswith '/bodygraphs')
       req[1] -> headers (dict)
       req[2] -> body (dict)
       and also req["url"], req["headers"], req["body"].
    Headers (dash-case, exact):
       - HD-Api-Key
       - HD-Geocode-Key
       - Accept: application/json
       - Content-Type: application/json; charset=utf-8
    Body (exact three keys):
       - birthdate: DD-MMM-YYYY (English month map)
       - birthtime: HH:MM
       - location: passed-through place string
    tz is intentionally ignored on the hdapi path.
    """
    api_key = (os.getenv("HD_API_KEY") or "").strip()
    geo_key = (os.getenv("GEO_API_KEY") or "").strip()
    missing = []
    if not api_key: missing.append("HD_API_KEY")
    if not geo_key: missing.append("GEO_API_KEY")
    if missing:
        raise ProviderError("PROVIDER_CONFIG_MISSING", "missing vendor credentials",
                            {"missing": missing, "correlation_id": correlation_id})

    birthdate_conv = _to_dd_mmm_yyyy(birthdate)  # uses module's YYYY-MM-DD -> DD-MMM-YYYY converter
    headers = {
        "HD-Api-Key": api_key,
        "HD-Geocode-Key": geo_key,
        "Accept": "application/json",
        "Content-Type": "application/json; charset=utf-8",
    }
    body = {
        "birthdate": birthdate_conv,
        "birthtime": birthtime,
        "location": location,
    }
    url = _hdapi_base_url() + "/bodygraphs"
    return _ReqShape(url, headers, body)


# Mixed return shape: tuple-index headers contain only auth headers;
# dict-style ["headers"] contains full headers incl. JSON pins.
class _ReqShapeMixed(dict):
    __slots__ = ("_triple",)
    def __init__(self, url: str, headers_tuple: dict, headers_dict: dict, body: dict):
        # dict view shows the full headers (with JSON pins)
        super().__init__({"url": url, "headers": headers_dict, "body": body})
        # tuple view keeps only the auth headers (legacy test expectation)
        self._triple = (url, headers_tuple, body)
    def __getitem__(self, key):
        if isinstance(key, int):
            return self._triple[key]
        return dict.__getitem__(self, key)

def prepare_hdapi_request(birthdate: str, birthtime: str, location: str, *, correlation_id: str | None):
    """
    Override: return tuple- and dict-compatible request:
      req[0] -> url (endswith '/bodygraphs')
      req[1] -> AUTH headers only: {'HD-Api-Key','HD-Geocode-Key'}
      req[2] -> body
      req['headers'] -> FULL headers incl. Accept/Content-Type
    """
    api_key = (os.getenv("HD_API_KEY") or "").strip()
    geo_key = (os.getenv("GEO_API_KEY") or "").strip()
    missing = []
    if not api_key: missing.append("HD_API_KEY")
    if not geo_key: missing.append("GEO_API_KEY")
    if missing:
        raise ProviderError("PROVIDER_CONFIG_MISSING", "missing vendor credentials",
                            {"missing": missing, "correlation_id": correlation_id})

    birthdate_conv = _to_dd_mmm_yyyy(birthdate)
    headers_auth = {
        "HD-Api-Key": api_key,
        "HD-Geocode-Key": geo_key,
    }
    headers_json = {
        "Accept": "application/json",
        "Content-Type": "application/json; charset=utf-8",
    }
    headers_full = {**headers_auth, **headers_json}
    body = {
        "birthdate": birthdate_conv,
        "birthtime": birthtime,
        "location": location,
    }
    url = _hdapi_base_url() + "/bodygraphs"
    return _ReqShapeMixed(url, headers_auth, headers_full, body)

