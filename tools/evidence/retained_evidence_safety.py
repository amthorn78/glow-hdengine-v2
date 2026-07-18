"""Shared retained-evidence text safety checks for HDE-EPIC038."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Iterator

SAFE_ENV_REFERENCE = re.compile(r"\$(?:[A-Za-z_][A-Za-z0-9_]*|\{[A-Za-z_][A-Za-z0-9_]*\})\Z")
RAW_PAYLOAD_MARKERS = frozenset({
    "raw_vendor_payload",
    "raw_vendor_envelope",
    "raw_request_body",
    "raw_response_body",
})
_ERROR_ORDER = (
    "NON_UTF8_RETAINED_TEXT",
    "FORBIDDEN_SERVICE_URI",
    "UNREDACTED_BEARER_VALUE",
    "UNREDACTED_VENDOR_HEADER_VALUE",
    "UNREDACTED_CREDENTIAL_VALUE",
    "UNREDACTED_BIRTH_INPUT_VALUE",
    "UNSAFE_RAW_PAYLOAD_MARKER_VALUE",
)
_RETAINED_VALUE = r'(?:"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|presence\((?:"[^"]*"|\'[^\']*\')\)|\$\{[^}\r\n]*\}|\$[A-Za-z_][A-Za-z0-9_]*|[^\s,"\'}\]]+)'
_CREDENTIAL_ASSIGNMENT = re.compile(rf"(?i)(?P<key_quote>[\"']?)\b(?:DATABASE_URL|DB_BRIDGE_URL|HD_API_KEY|GEO_API_KEY|HD_API_BASE_URL|HDAPI_BASE_URL)\b(?P=key_quote)\s*[:=]\s*(?P<value>{_RETAINED_VALUE})")
_BEARER = re.compile(rf"(?i)\bBearer\s+(?P<value>{_RETAINED_VALUE})")
_VENDOR_HEADER = re.compile(rf"(?i)(?P<key_quote>[\"']?)\bHD-(?:Geocode|Api)-Key\b(?P=key_quote)\s*[:=]\s*(?P<value>{_RETAINED_VALUE})")
_BIRTH_ASSIGNMENT = re.compile(rf"(?i)(?P<key_quote>[\"']?)\b(?:birth[-_]?date|date[-_]?of[-_]?birth|dob|birth[-_]?time|time[-_]?of[-_]?birth|birth[-_]?place|place[-_]?of[-_]?birth|birth[-_]?location|location)\b(?P=key_quote)\s*[:=]\s*(?P<value>{_RETAINED_VALUE})")
_BIRTH_OPTION = re.compile(rf"(?i)--(?:birth[-_]?date|date[-_]?of[-_]?birth|dob|birth[-_]?time|time[-_]?of[-_]?birth|birth[-_]?place|place[-_]?of[-_]?birth|birth[-_]?location|location)(?:=|\s+)(?P<value>{_RETAINED_VALUE})")
_FORBIDDEN_URI = re.compile(r"(?i)\b(?:postgres(?:ql)?|railway)://")
_RAW_MARKER = re.compile(r"(?i)(?<![A-Za-z0-9_])(?P<key>raw_vendor_payload|raw_vendor_envelope|raw_request_body|raw_response_body)(?![A-Za-z0-9_])\s*[:=]|(?P<q>[\"'])(?P<qkey>raw_vendor_payload|raw_vendor_envelope|raw_request_body|raw_response_body)(?P=q)\s*[:=]")

def _normalized_value(raw: str) -> str:
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"\"", "'"}:
        return value[1:-1]
    return value

def _value_is_safe(raw: str, allowed: set[str], *, allow_presence: bool = False) -> bool:
    value = _normalized_value(raw)
    return value.lower() in allowed or SAFE_ENV_REFERENCE.fullmatch(value) is not None or (allow_presence and re.fullmatch(r"presence\((['\"])(?:DATABASE_URL|DB_BRIDGE_URL|HD_API_KEY|GEO_API_KEY|HD_API_BASE_URL|HDAPI_BASE_URL)\1\)", value, flags=re.I) is not None)

def _birth_value_is_safe(raw: str) -> bool:
    v = _normalized_value(raw); l = v.lower()
    return l in {"<redacted>", "redacted", "set:redacted", "unset", "none", "null", "false", "not-recorded", "not_recorded", "***"} or SAFE_ENV_REFERENCE.fullmatch(v) is not None or re.fullmatch(r"<approved-synthetic-(?:birthdate|birthtime|location)>", l) is not None

def _iter_raw_marker_assignments(text: str) -> Iterator[tuple[str, str]]:
    for line in text.splitlines():
        m = _RAW_MARKER.search(line)
        if m:
            yield ((m.group('key') or m.group('qkey')).lower(), line[m.end():].strip())

def _raw_marker_value_is_safe(value: str) -> bool:
    
    rhs = value.strip()
    rhs = re.sub(r"\s*(?:[,}\]]).*$", "", rhs).strip()
    return re.fullmatch(r"(?i)(?:false|null|\"(?:none|redacted)\")", rhs) is not None

def validate_retained_text_safety(path: Path, payload: bytes) -> tuple[str, ...]:
    errors: set[str] = set()
    try:
        text = payload.decode('utf-8', 'strict')
    except UnicodeDecodeError:
        return ("NON_UTF8_RETAINED_TEXT",)
    if _FORBIDDEN_URI.search(text): errors.add("FORBIDDEN_SERVICE_URI")
    for m in _BEARER.finditer(text):
        if not _value_is_safe(m.group('value'), {"<redacted>", "redacted"}): errors.add("UNREDACTED_BEARER_VALUE")
    for m in _VENDOR_HEADER.finditer(text):
        if not _value_is_safe(m.group('value'), {"<redacted>", "redacted", "set:redacted", "set", "unset", "***"}): errors.add("UNREDACTED_VENDOR_HEADER_VALUE")
    for m in _CREDENTIAL_ASSIGNMENT.finditer(text):
        if not _value_is_safe(m.group('value'), {"redacted", "<redacted>", "set:redacted", "set", "unset"}, allow_presence=True): errors.add("UNREDACTED_CREDENTIAL_VALUE")
    for pat in (_BIRTH_ASSIGNMENT, _BIRTH_OPTION):
        for m in pat.finditer(text):
            if not _birth_value_is_safe(m.group('value')): errors.add("UNREDACTED_BIRTH_INPUT_VALUE")
    for _, value in _iter_raw_marker_assignments(text):
        if not _raw_marker_value_is_safe(value): errors.add("UNSAFE_RAW_PAYLOAD_MARKER_VALUE")
    return tuple(sorted(errors))
