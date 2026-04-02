# HDE-EPIC028 - PO-002 Full Action Report and Evidence Output

## Scope
- Epic: HDE-EPIC028 (Conjunction Pass 4)
- Check ID: po-002
- Check Name: One governed emission path across CLI, Reader, and internal compatibility
- Step intent: prove that CLI, Reader/public assembly, and internal compatibility posture remain aligned to one governed emission path
- Status: PASS

## Proof Obligation (Verbatim)
"The CLI, the public success surface, and the internal compatibility surface must all rely on one governed emission path rather than alternate serialization paths."

## Pass Criteria (Verbatim)
- All snapshots exist.
- The snapshots show Reader/public routing through the governed emitter path.
- Both CLI guard artifacts show PASS.

## Rails and Determinism Pins
- SAFE_MODE=1
- ALLOW_NETWORK=0
- APP_ENV=dev
- LC_ALL=C
- LANG=C
- TZ=UTC

## Repo Loci in Scope
- presenter/reader_v1/emitter.py
- engine/runtime/public.py
- artifacts/cli/guards/emitter_symbol_proof.txt
- artifacts/cli/guards/serializer_grep_guard.log

## Executed Actions
1. Wrote po-002 primary step log header (PF27 schema) with captured env and artifact list.
2. Captured Reader emitter locus snapshot from presenter/reader_v1/emitter.py.
3. Captured runtime public assembly snapshot from engine/runtime/public.py.
4. Captured governed CLI emitter symbol proof snapshot.
5. Captured governed CLI serializer grep guard snapshot.

## Validation Checks Performed
1. Confirmed all required deliverables exist at the governed po-002 path.
2. Confirmed Reader-side snapshot includes calls to emit_public.
3. Confirmed runtime public snapshot imports and calls emit_reader_v1.
4. Confirmed emitter symbol guard snapshot reports summary:PASS.
5. Confirmed serializer grep guard snapshot reports summary: PASS.

## Findings Trace (Line-Level)
- reader_v1_emitter_snapshot.txt
  - emit_public found at line 60
  - emit_public found at line 64
- runtime_public_snapshot.txt
  - emit_reader_v1 import found at line 6
  - emit_reader_v1 call found at line 51
- emitter_symbol_proof_snapshot.txt
  - summary:PASS found at line 4
- serializer_grep_guard_snapshot.txt
  - summary: PASS found at line 3

## Evidence Integrity Snapshot
- audit/qa/hde-epic028/checks/po-002/primary.log
  - size_bytes: 1980
  - lines: 2
  - sha256: 47981deff94f0f052331f26ee0dfd1662a33832b1e56f59ca3ade98ec3247dcd
- audit/qa/hde-epic028/checks/po-002/reader_v1_emitter_snapshot.txt
  - size_bytes: 2379
  - lines: 65
  - sha256: 431bb58488d658e4b028f27af55d30cc3f043c187153e212abcbedb240a59fc2
- audit/qa/hde-epic028/checks/po-002/runtime_public_snapshot.txt
  - size_bytes: 1756
  - lines: 70
  - sha256: 9668bd2a8b488bc6b0b7c89c379d8b4a9c3767cdfa2eeb63185ebaa5342d5f76
- audit/qa/hde-epic028/checks/po-002/emitter_symbol_proof_snapshot.txt
  - size_bytes: 392
  - lines: 7
  - sha256: 6120d745ff554e12d9bc4b731a597f60264e6f5c8fff60c1939a71f35652bfc4
- audit/qa/hde-epic028/checks/po-002/serializer_grep_guard_snapshot.txt
  - size_bytes: 137
  - lines: 3
  - sha256: 3d5902ce7fd49185b22c2d5f51735e83017c8e38246ed5e3adc716051b8f528a

## Full Evidence Outputs

### 1) primary.log
Path: audit/qa/hde-epic028/checks/po-002/primary.log

```text
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"po-002","check_name":"One governed emission path across CLI, Reader, and internal compatibility","claimed_tokens":[],"command":"python -c \"from pathlib import Path; src=Path('presenter/reader_v1/emitter.py').read_text(encoding='utf-8').splitlines(); Path('audit/qa/hde-epic028/checks/po-002/reader_v1_emitter_snapshot.txt').write_text('\\n'.join(src[:240])+'\\n', encoding='utf-8')\"; python -c \"from pathlib import Path; src=Path('engine/runtime/public.py').read_text(encoding='utf-8').splitlines(); Path('audit/qa/hde-epic028/checks/po-002/runtime_public_snapshot.txt').write_text('\\n'.join(src[:220])+'\\n', encoding='utf-8')\"; python -c \"from pathlib import Path; src=Path('artifacts/cli/guards/emitter_symbol_proof.txt').read_text(encoding='utf-8').splitlines(); Path('audit/qa/hde-epic028/checks/po-002/emitter_symbol_proof_snapshot.txt').write_text('\\n'.join(src[:40])+'\\n', encoding='utf-8')\"; python -c \"from pathlib import Path; src=Path('artifacts/cli/guards/serializer_grep_guard.log').read_text(encoding='utf-8').splitlines(); Path('audit/qa/hde-epic028/checks/po-002/serializer_grep_guard_snapshot.txt').write_text('\\n'.join(src[:40])+'\\n', encoding='utf-8')\"","command_provenance":"Explicitly created","evidence_artifacts":["audit/qa/hde-epic028/checks/po-002/primary.log","audit/qa/hde-epic028/checks/po-002/reader_v1_emitter_snapshot.txt","audit/qa/hde-epic028/checks/po-002/runtime_public_snapshot.txt","audit/qa/hde-epic028/checks/po-002/emitter_symbol_proof_snapshot.txt","audit/qa/hde-epic028/checks/po-002/serializer_grep_guard_snapshot.txt"],"fail_status":"","intended_tokens":[],"pf_refs":["PF19 — Glow QA Guide","PF27 — Canon Plan Templates"],"schema_version":"pf27.step_log_header.v1","status":"PASS","timestamp_utc":"2026-04-01T20:48:20Z"}
planned_step: capture Reader-side emitter loci and governed CLI guard artifacts
```

### 2) reader_v1_emitter_snapshot.txt
Path: audit/qa/hde-epic028/checks/po-002/reader_v1_emitter_snapshot.txt

```text
from __future__ import annotations
import hashlib
from typing import Dict, List, Any, Tuple

from engine.presenter import emitter  # emits UTF-8 with exactly one trailing LF

_CATEGORY_BANDS = {"Cool","Open","Warm","Glow"}

def _dedupe_and_sort_categories(categories: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Enforce 'categories is a set' and sort by id.
    - Reject duplicate ids (explicitly fail-closed rather than arbitrary pick).
    - Preserve only allowed keys ('id','band','prompt') if present; do not inject anything new.
    """
    seen = set()
    cleaned: List[Dict[str, Any]] = []
    for c in categories or []:
        cid = c.get("id")
        if cid in seen:
            raise ValueError(f"Duplicate category id: {cid}")
        seen.add(cid)
        band = c.get("band")
        # Basic band sanity (schema will also enforce; keep this light)
        if band not in _CATEGORY_BANDS:
            raise ValueError(f"Invalid band for {cid}: {band}")
        item = {"id": cid, "band": band}
        if "prompt" in c:
            item["prompt"] = c["prompt"]
        cleaned.append(item)
    cleaned.sort(key=lambda x: x["id"])
    return cleaned

def _build_preimage(enriched: Dict[str, Any]) -> Dict[str, Any]:
    """
    Build success envelope WITHOUT idempotence_hash (preimage).
    Required in enriched:
      eligible: bool
      categories: list[{id,band[,prompt]}]
      meta: {engine_tag, invocation_tag}
      release_id: hex64
    """
    pre = {
        "reader_version": "v1",
        "eligible": bool(enriched.get("eligible", False)),
        "categories": _dedupe_and_sort_categories(enriched.get("categories", [])),
        "meta": {
            "engine_tag": enriched["meta"]["engine_tag"],
            "invocation_tag": enriched["meta"]["invocation_tag"],
        },
        "release_id": enriched["release_id"],
    }
    return pre

def emit_reader_v1(enriched: Dict[str, Any]) -> Tuple[bytes, Dict[str, Any]]:
    """
    Returns (public_bytes, final_envelope_dict).
    public_bytes are LF-terminated, produced by sercanon.serialize.
    """
    preimage = _build_preimage(enriched)
    pre_bytes = emitter.emit_public(preimage)
    digest = hashlib.sha256(pre_bytes).hexdigest()
    final = dict(preimage)
    final["idempotence_hash"] = digest
    public_bytes = emitter.emit_public(final)
    return public_bytes, final
```

### 3) runtime_public_snapshot.txt
Path: audit/qa/hde-epic028/checks/po-002/runtime_public_snapshot.txt

```text
from __future__ import annotations

from typing import Dict, Tuple

from engine.compat import ts_v0
from presenter.reader_v1.emitter import emit_reader_v1

_HARMONY_ID = "harmony"


def _build_enriched_envelope(
    band: str,
    *,
    eligible: bool,
    engine_tag: str,
    invocation_tag: str,
    release_id: str,
) -> Dict[str, object]:
    return {
        "eligible": bool(eligible),
        "categories": [{"id": _HARMONY_ID, "band": band}],
        "meta": {"engine_tag": engine_tag, "invocation_tag": invocation_tag},
        "release_id": release_id,
    }


def _compute_harmony_band(a_chart: Dict[str, object], b_chart: Dict[str, object]) -> str:
    a_ts = ts_v0.extract_ts(a_chart)
    b_ts = ts_v0.extract_ts(b_chart)
    features = ts_v0.compute_features(a_ts, b_ts)
    return ts_v0.band_v0(features)


def emit_reader_public_envelope(
    a_chart: Dict[str, object],
    b_chart: Dict[str, object],
    *,
    engine_tag: str,
    invocation_tag: str,
    release_id: str,
    eligible: bool = True,
) -> Tuple[bytes, Dict[str, object]]:
    band = _compute_harmony_band(a_chart, b_chart)
    enriched = _build_enriched_envelope(
        band,
        eligible=eligible,
        engine_tag=engine_tag,
        invocation_tag=invocation_tag,
        release_id=release_id,
    )
    return emit_reader_v1(enriched)


def emit_reader_public_bytes(
    a_chart: Dict[str, object],
    b_chart: Dict[str, object],
    *,
    engine_tag: str,
    invocation_tag: str,
    release_id: str,
    eligible: bool = True,
) -> bytes:
    return emit_reader_public_envelope(
        a_chart,
        b_chart,
        engine_tag=engine_tag,
        invocation_tag=invocation_tag,
        release_id=release_id,
        eligible=eligible,
    )[0]
```

### 4) emitter_symbol_proof_snapshot.txt
Path: audit/qa/hde-epic028/checks/po-002/emitter_symbol_proof_snapshot.txt

```text
CLI Emitter Symbol Proof
canonical_emitters:emit_reader_public_envelope,emitter.emit_public
handler_emitter_allowlist:aux-preview=<none>,bg:resolve=emitter.emit_public,showcompat=emit_reader_public_envelope|emitter.emit_public
summary:PASS
aux-preview:aux_preview:<none> (exempt)
bg:resolve:bg_resolve:emitter.emit_public
showcompat:showcompat:emit_reader_public_envelope,emitter.emit_public
```

### 5) serializer_grep_guard_snapshot.txt
Path: audit/qa/hde-epic028/checks/po-002/serializer_grep_guard_snapshot.txt

```text
CLI Serializer Grep Guard
scope:adapter/http_reader.py,engine/cli
summary: PASS (no disallowed json serialization in governed CLI scope)
```

## Final Step Result
PASS. The complete evidence set for PO-002 is present in one governed location and supports the single governed emission path posture across Reader/public assembly and CLI guard artifacts.
