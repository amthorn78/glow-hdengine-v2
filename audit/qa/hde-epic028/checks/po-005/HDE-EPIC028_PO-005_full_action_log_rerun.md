# HDE-EPIC028 PO-005 Full Action Log (Rerun)

## Manifest Header
- HDE-EPIC: HDE-EPIC028 / Conjunction Pass 4
- Step: PO-005 - Governed Reader proof-surface designation
- Approved QA Plan File: r9 Live QA Plan HDE-EPIC028.md
- Approval Doc File: none
- Previous Step Report File: report - po-004 QA HDE-EPIC028.md
- PF-Canon consulted: PF10 (current) + PF05 + PF02
- Generated at (UTC): 2026-04-02T22:11:01Z

## Outcome
- Final status: PASS
- Fail status: (empty)
- Decision lane: PF10 addendum 2.14 first-priority interpretation
- Scope discipline: no new route, no new flag, no new proof-surface carrier

## Rails and Repo State
- SAFE_MODE=1
- ALLOW_NETWORK=0
- APP_ENV=dev
- LC_ALL=C
- LANG=C
- TZ=UTC
- git HEAD: e5703d58447f38394f25cbcd113eebf6883366b5
- git status (po-005 scope):
```text
 M audit/qa/hde-epic028/checks/po-005/blocked_note.txt
 M audit/qa/hde-epic028/checks/po-005/catalog_snapshot.txt
 M audit/qa/hde-epic028/checks/po-005/http_reader_snapshot.txt
 M audit/qa/hde-epic028/checks/po-005/primary.log
```

## Executed Actions (Rerun)
1. Enabled strict shell rails and exported deterministic environment variables.
2. Verified D0 and required loci exist at approved paths.
3. Captured catalog snapshot from docs/ENDPOINTS_CATALOG.json (first 40 lines).
4. Captured ownership snapshot from adapter/http_reader.py (first 180 lines).
5. Wrote blocked_note.txt as preserved drift note per approved evidence family.
6. Evaluated lookup lane and wrote primary.log using PASS block.

## Commands Used
```bash
set -euo pipefail
export LC_ALL=C
export LANG=C
export TZ=UTC
export SAFE_MODE=1
export ALLOW_NETWORK=0
export APP_ENV=dev
mkdir -p audit/qa/hde-epic028/checks/po-005
test -f audit/qa/hde-epic028/checks/d0/primary.log
test -f audit/qa/hde-epic028/qa_step_logs_manifest.json
test -f docs/ENDPOINTS_CATALOG.json
test -f adapter/http_reader.py
python -c "from pathlib import Path; src=Path('docs/ENDPOINTS_CATALOG.json').read_text(encoding='utf-8').splitlines(); Path('audit/qa/hde-epic028/checks/po-005/catalog_snapshot.txt').write_text('\n'.join(src[:40])+'\n', encoding='utf-8')"
python -c "from pathlib import Path; src=Path('adapter/http_reader.py').read_text(encoding='utf-8').splitlines(); Path('audit/qa/hde-epic028/checks/po-005/http_reader_snapshot.txt').write_text('\n'.join(src[:180])+'\n', encoding='utf-8')"
python -c "from pathlib import Path; Path('audit/qa/hde-epic028/checks/po-005/blocked_note.txt').write_text('lookup_note: /reader remains the current Reader route under review; success_endpoints is empty while /reader is marked a7_eligible:true, and PF10 addendum 2.14 treats that missing explicit designation as downstream canon drift rather than a reason to invent a second proof-surface mechanism for this step\n', encoding='utf-8')"
python - <<'PY'  # wrote PASS primary.log header + body
...
PY
```

## Evidence Outputs (Metadata)
- audit/qa/hde-epic028/checks/po-005/primary.log
  - sha256: 2543c344201eb8839738633ccc32da6eea8cb1505e76c492497e47e3d1ee3a40
  - size_bytes: 2015
  - mtime_epoch: 1775167249
- audit/qa/hde-epic028/checks/po-005/catalog_snapshot.txt
  - sha256: 4b766ec46b69df75136611a47d03fd7268fbfed1b8b18cbb44d9b3296874d143
  - size_bytes: 1749
  - mtime_epoch: 1775167248
- audit/qa/hde-epic028/checks/po-005/http_reader_snapshot.txt
  - sha256: 6e530c6f41e590f9a0174867c8a8697cd6067ba815b030aa961e639170cb4803
  - size_bytes: 6100
  - mtime_epoch: 1775167248
- audit/qa/hde-epic028/checks/po-005/blocked_note.txt
  - sha256: 4eb70a05f4c08bc0240300b2e911b365f8cd13d27b7d4d7fe84ced1de7d79592
  - size_bytes: 305
  - mtime_epoch: 1775167248

## Evidence Outputs (Full Verbatim Content)
### audit/qa/hde-epic028/checks/po-005/primary.log
```text
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"po-005","check_name":"Governed Reader proof-surface designation","claimed_tokens":[],"command":"python -c \"from pathlib import Path; src=Path('docs/ENDPOINTS_CATALOG.json').read_text(encoding='utf-8').splitlines(); Path('audit/qa/hde-epic028/checks/po-005/catalog_snapshot.txt').write_text('\\\\n'.join(src[:40])+'\\\\n', encoding='utf-8')\"; python -c \"from pathlib import Path; src=Path('adapter/http_reader.py').read_text(encoding='utf-8').splitlines(); Path('audit/qa/hde-epic028/checks/po-005/http_reader_snapshot.txt').write_text('\\\\n'.join(src[:180])+'\\\\n', encoding='utf-8')\"; python -c \"from pathlib import Path; Path('audit/qa/hde-epic028/checks/po-005/blocked_note.txt').write_text('lookup_note: /reader remains the current Reader route under review; success_endpoints is empty while /reader is marked a7_eligible:true, and PF10 addendum 2.14 treats that missing explicit designation as downstream canon drift rather than a reason to invent a second proof-surface mechanism for this step\\\\n', encoding='utf-8')\"","command_provenance":"Explicitly created","evidence_artifacts":["audit/qa/hde-epic028/checks/po-005/primary.log","audit/qa/hde-epic028/checks/po-005/catalog_snapshot.txt","audit/qa/hde-epic028/checks/po-005/http_reader_snapshot.txt","audit/qa/hde-epic028/checks/po-005/blocked_note.txt"],"fail_status":"","intended_tokens":[],"pf_refs":["PF10 — HDE-Build Notes","PF05 — HDE-CLI-API-Vendor-Ref","PF02 — HDE-Architecture","PF27 — Canon Plan Templates"],"schema_version":"pf27.step_log_header.v1","status":"PASS","timestamp_utc":"2026-04-02T22:00:49Z"}
planned_step: capture the current Reader catalog row and route ownership proof
decision_note: under PF10 addendum 2.14, /reader is the governed Reader success-proof surface for the current HDE-EPIC028 scope when the approved lookup artifact shows route existence, APP_ENV=dev gating, and a7_eligible:true
```

### audit/qa/hde-epic028/checks/po-005/catalog_snapshot.txt
```text
{"endpoints":[{"a7_eligible":false,"blueprint_module":"engine.http.compat_handler","classification":"internal_admin","description":"Compat pair endpoint (internal admin)","env_gate":"APP_ENV!=prod","method":"POST","path":"/api/compat/v1","rails_profile":"internal-admin writer no-store"},{"a7_eligible":false,"blueprint_module":"adapter.http_reader","classification":"dev_harness","description":"Conjunction reader preview route (dev-only)","env_gate":"APP_ENV in {dev,test,local}","method":"GET","path":"/dev/reader/conjunction","rails_profile":"dev-harness closed-by-default SAFE rails"},{"a7_eligible":false,"blueprint_module":"adapter.http_reader","classification":"dev_harness","description":"Conjunction writer preview route (dev-only)","env_gate":"APP_ENV in {dev,test,local}","method":"GET","path":"/dev/writer/conjunction","rails_profile":"dev-harness closed-by-default SAFE rails"},{"a7_eligible":false,"blueprint_module":"adapter.http_reader","classification":"dev_harness","description":"Conjunction sampler preview route (dev-only)","env_gate":"APP_ENV in {dev,test,local}","method":"GET","path":"/dev/sampler/conjunction","rails_profile":"dev-harness closed-by-default SAFE rails"},{"a7_eligible":false,"blueprint_module":"adapter.http_reader","classification":"internal_identity","description":"Internal version endpoint for ops evidence","env_gate":"operator-network-only","method":["GET","HEAD"],"path":"/internal/version","rails_profile":"ops-only no-store"},{"a7_eligible":true,"blueprint_module":"adapter.http_reader","classification":"dev_harness","description":"Reader success route (dev-only)","env_gate":"APP_ENV=dev","method":["GET","HEAD"],"path":"/reader","rails_profile":"dev-harness reader a7"}],"success_endpoints":[]}
```

### audit/qa/hde-epic028/checks/po-005/http_reader_snapshot.txt
```text
from __future__ import annotations
import hashlib, json, os, tempfile
from datetime import datetime, timezone
from pathlib import Path
from flask import Blueprint, Response, request, Flask, g
from threading import Lock
from engine.presenter.emitter import emit_public
from engine.serializer import canon
from engine.runtime import emit_reader_public_bytes
from engine.narratives import emit_public_aux, get_pack
from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.compat.compute import conjunction_public_resolved
from engine.sampler.core import CandidateFeatures, ViewerProfile, sample_and_rank
from adapter.no_io_guard import NoIoGuard
from engine.compat.errors import error_envelope
from engine.bodygraph.ingest import resolve_db_user_id
from engine.bodygraph.vendor_client import VendorError
from engine.http.compat_handler import compat_blueprint
from engine.db import DBAccess
from engine.db.errors import AdapterError, PrimaryUnavailable

_PROCESS_STARTED_AT = datetime.now(timezone.utc)
_PROCESS_PID = os.getpid()

# A7 helpers
def _sha256_hex(b: bytes) -> str: return hashlib.sha256(b).hexdigest()

def _set_reader_200_headers(resp: Response) -> Response:
    resp.headers["Content-Type"] = "application/json; charset=utf-8"
    resp.headers["Cache-Control"] = "private, max-age=0, must-revalidate"
    resp.headers["Vary"] = "Authorization, Accept-Encoding"
    return resp


def _collect_query_values(name: str) -> list[str]:
    values = [item.strip() for item in request.args.getlist(name) if item.strip()]
    if values:
        return values
    raw = request.args.get(name)
    if not raw:
        return []
    return [part.strip() for part in raw.split(",") if part.strip()]

_MAX_WRITER_BYTES = 32_768
_DIAGNOSTIC_ROUTE_ID = "ops.writer.diagnostic.v1"
_DEV_WRITER_CONJUNCTION_ROUTE_ID = "dev.writer.conjunction.v1"

_IDEMPOTENCE_CACHE: dict[str, dict[str, object]] = {}
_IDEMPOTENCE_CACHE_LOCK = Lock()
_ENV_UNSET = object()


class _WriterTransportResponse(Response):
    def get_wsgi_headers(self, environ):  # type: ignore[override]
        headers = super().get_wsgi_headers(environ)
        if self.status_code == 204:
            headers["Content-Length"] = "0"
        return headers

def _clear_writer_error_caching(resp: Response) -> Response:
    resp.headers["Cache-Control"] = "no-store"
    resp.headers.pop("ETag", None)
    return resp


def _emit_writer_response(
    envelope: dict[str, object],
    *,
    status: int,
    extra_headers: dict[str, str] | None = None,
    sort_keys: bool = True,
) -> Response:
    body = emit_public(envelope, sort_keys=sort_keys)
    resp = Response(body, status=status, mimetype="application/json; charset=utf-8")
    resp.headers["Content-Type"] = "application/json; charset=utf-8"
    resp.headers["Cache-Control"] = "no-store"
    resp.headers.pop("ETag", None)
    resp.headers.pop("Content-Encoding", None)
    resp.headers.pop("Vary", None)
    resp.headers["Content-Length"] = str(len(body))
    if extra_headers:
        for key, value in extra_headers.items():
            resp.headers[key] = value
    return resp


def _writer_error(
    code: str,
    *,
    status: int,
    extra_headers: dict[str, str] | None = None,
    sort_keys: bool = True,
) -> Response:
    envelope = error_envelope(code)
    return _emit_writer_response(
        envelope,
        status=status,
        extra_headers=extra_headers,
        sort_keys=sort_keys,
    )


def _json_content_type_ok(header_value: str | None) -> bool:
    if not header_value:
        return False
    normalized = header_value.strip().lower()
    return normalized == "application/json; charset=utf-8"


def _reject_request_too_large() -> Response:
    return _writer_error("ERR_WRITER_REQUEST_TOO_LARGE", status=413)


def _read_writer_json(
    *,
    allow_empty_body: bool,
    allowed_keys: set[str] | None = None,
) -> tuple[dict[str, object] | None, Response | None]:
    content_length = request.content_length
    if content_length is not None and content_length > _MAX_WRITER_BYTES:
        return None, _reject_request_too_large()

    raw = request.get_data(cache=False)
    if len(raw) > _MAX_WRITER_BYTES:
        return None, _reject_request_too_large()

    if not raw:
        if allow_empty_body:
            return {}, None
        return None, _writer_error("ERR_WRITER_INVALID_CONTENT_TYPE", status=415)

    if not _json_content_type_ok(request.headers.get("Content-Type")):
        return None, _writer_error("ERR_WRITER_INVALID_CONTENT_TYPE", status=415)

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return None, _writer_error("ERR_WRITER_INVALID_JSON", status=400)

    if text.startswith("\ufeff"):
        return None, _writer_error("ERR_WRITER_INVALID_JSON", status=400)

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return None, _writer_error("ERR_WRITER_INVALID_JSON", status=400)

    if not isinstance(data, dict):
        return None, _writer_error("ERR_WRITER_INVALID_INPUT", status=422)

    if allowed_keys is not None:
        unknown = [k for k in data.keys() if k not in allowed_keys]
        if unknown:
            return None, _writer_error("ERR_WRITER_UNKNOWN_KEY", status=422)

    return data, None


def _require_admin_scope() -> Response | None:
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return _writer_error(
            "ERR_WRITER_UNAUTHORIZED",
            status=401,
            extra_headers={"WWW-Authenticate": "Bearer"},
        )

    token = auth_header.split(" ", 1)[1].strip()
    admin_token = (os.environ.get("HDE_TEST_TOKEN_ADMIN") or "").strip()
    none_token = (os.environ.get("HDE_TEST_TOKEN_NONE") or "").strip()

    if admin_token and token == admin_token:
        return None
    if none_token and token == none_token:
        return _writer_error("ERR_WRITER_FORBIDDEN", status=403)

    return _writer_error(
        "ERR_WRITER_UNAUTHORIZED",
        status=401,
        extra_headers={"WWW-Authenticate": "Bearer"},
```

### audit/qa/hde-epic028/checks/po-005/blocked_note.txt
```text
lookup_note: /reader remains the current Reader route under review; success_endpoints is empty while /reader is marked a7_eligible:true, and PF10 addendum 2.14 treats that missing explicit designation as downstream canon drift rather than a reason to invent a second proof-surface mechanism for this step
```
