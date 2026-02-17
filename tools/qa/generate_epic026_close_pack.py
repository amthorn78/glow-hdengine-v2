#!/usr/bin/env python3
"""Generate EPIC026 close-pack artifacts and QA step logs manifest."""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.evidence import update_evidence_index

EPIC_ID = "HDE-EPIC026"
EPIC_SLUG = "hde-epic026"
QA_ROOT = ROOT / "audit" / "qa" / EPIC_SLUG
QA_CHECKS_ROOT = QA_ROOT / "checks"
QA_META_DOC_DELTAS_PATH = QA_ROOT / "00_meta" / "doc_deltas.md"
DOC_DELTAS_PATH = ROOT / "audit" / "docdeltas" / "hde-epic026_doc_deltas.md"
CLOSE_REPORT_PATH = ROOT / "audit" / "EPIC-026_close_report.md"
CLOSE_MANIFEST_PATH = ROOT / "audit" / "EPIC-026_MANIFEST.json"
QA_STEP_MANIFEST_PATH = QA_ROOT / "qa_step_logs_manifest.json"
PF23_PATH = ROOT / "docs" / "pfcanon" / "PF23-Canon-Reality-Audits-v1.0.3.md"


def _utc_now() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _announce_write(path: Path) -> None:
    rel = path.relative_to(ROOT).as_posix()
    print(f"WROTE {rel}")


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    _announce_write(path)


def _write_json(path: Path, payload: object) -> None:
    _write_text(path, json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n")


def _write_path_proof(path: Path, produced_at: str) -> None:
    rel = path.relative_to(ROOT).as_posix()
    stat = path.stat()
    update_evidence_index._write_path_proof(
        rel=rel,
        sha256=_sha256(path),
        size_bytes=stat.st_size,
        mtime_utc=update_evidence_index._isoformat_from_timestamp(stat.st_mtime),
        produced_at=produced_at,
        default_produced_at=produced_at,
        check=False,
        stat_mtime=stat.st_mtime,
    )
    _announce_write(ROOT / f"{rel}.path_proof.txt")


def _discover_qa_step_logs() -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    for primary in sorted(QA_CHECKS_ROOT.glob("**/primary.log")):
        rel = primary.relative_to(QA_ROOT).as_posix()
        parts = rel.split("/")
        if len(parts) < 3:
            continue
        check_id = parts[1]
        record: dict[str, object] = {
            "check_id": check_id,
            "log_path": rel,
            "sha256": _sha256(primary),
            "size_bytes": primary.stat().st_size,
        }
        transcript = primary.parent / "transcript.txt"
        if transcript.exists():
            record["transcript_path"] = transcript.relative_to(QA_ROOT).as_posix()
            record["transcript_sha256"] = _sha256(transcript)
            record["transcript_size_bytes"] = transcript.stat().st_size
        entries.append(record)
    return entries


def write_step_manifest(produced_at: str) -> None:
    QA_ROOT.mkdir(parents=True, exist_ok=True)
    QA_CHECKS_ROOT.mkdir(parents=True, exist_ok=True)
    payload = {
        "epic_id": EPIC_SLUG,
        "generated_utc": produced_at,
        "checks": _discover_qa_step_logs(),
    }
    _write_json(QA_STEP_MANIFEST_PATH, payload)
    _write_path_proof(QA_STEP_MANIFEST_PATH, produced_at)


def write_doc_deltas() -> None:
    content = """# HDE-EPIC026 Doc Delta Ledger

## TI-002 PF09 coverage mapping
- HDE-FERM001.3: `audit/qa/hde-epic026/qa_step_logs_manifest.json`, `audit/qa/hde-epic026/00_meta/doc_deltas.md`
- HDE-COAG007.3: `audit/EPIC-026_close_report.md`, `audit/EPIC-026_MANIFEST.json`, `audit/docdeltas/hde-epic026_doc_deltas.md`

## ADR status
- ADR-TI002-EPIC026-001: Not required for PR08 baseline; supplied PF09 pointers cover committed close-pack baseline artifacts.
"""
    _write_text(DOC_DELTAS_PATH, content)
    _write_text(QA_META_DOC_DELTAS_PATH, content)


def _load_pf23_excerpt() -> tuple[str, list[str]]:
    lines = PF23_PATH.read_text(encoding="utf-8").splitlines()
    excerpt: list[str] = []
    capture = False
    for raw in lines:
        line = raw.strip()
        if line == "### **9.1 Evidence homes inventory (new; required)**":
            capture = True
            continue
        if capture and line.startswith("### **9.2"):
            break
        if capture and line in {"* docs/\\*\\*", "* artifacts/\\*\\*", "* audit/\\*\\* (including audit/qa/\\*\\* if present)"}:
            excerpt.append(line)
        if len(excerpt) == 2:
            break
    if len(excerpt) < 2:
        raise SystemExit("MISSING:PF23_9_1_EXCERPT")
    return PF23_PATH.relative_to(ROOT).as_posix(), excerpt


def _collect_index_epic026_outputs() -> dict[str, str]:
    index_path = ROOT / "docs" / "evidence" / "INDEX.json"
    rows = json.loads(index_path.read_text(encoding="utf-8"))
    outputs: dict[str, str] = {}
    hit_count = 0
    for row in rows:
        rel = str(row.get("discovered_physical_path", "")).strip()
        if not rel:
            continue
        epic_id = str(row.get("epic_id", "")).strip()
        lower_rel = rel.lower()
        if epic_id == EPIC_ID or "epic026" in lower_rel or "epic-026" in lower_rel or "hde-epic026" in lower_rel:
            key = str(row.get("artifact_key", "")).strip() or f"index_epic026_{hit_count:03d}"
            key = "index_" + key.replace("/", "_").replace(".", "_")
            while key in outputs:
                key = f"{key}_dup"
            outputs[key] = rel
            hit_count += 1
    return outputs


def _collect_gate_outputs() -> dict[str, str]:
    outputs: dict[str, str] = {}
    gate_roots = [ROOT / "audit" / "gates" / "json_gate" / "canonical", ROOT / "audit" / "gates" / "topology"]
    for root in gate_roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.name.endswith(".path_proof.txt"):
                continue
            rel = path.relative_to(ROOT).as_posix()
            outputs[f"gate_{rel.replace('/', '_').replace('.', '_')}"] = rel
    return outputs


def _collect_cli_outputs() -> dict[str, str]:
    outputs: dict[str, str] = {}
    root = ROOT / "artifacts" / "audit" / "cli"
    if not root.exists():
        return outputs
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.name.endswith(".path_proof.txt"):
            continue
        rel = path.relative_to(ROOT).as_posix()
        outputs[f"cli_{rel.replace('/', '_').replace('.', '_')}"] = rel
    return outputs


def _collect_qa_outputs() -> dict[str, str]:
    outputs: dict[str, str] = {}
    if not QA_ROOT.exists():
        return outputs
    for path in sorted(QA_ROOT.rglob("*")):
        if not path.is_file() or path.name.endswith(".path_proof.txt"):
            continue
        rel = path.relative_to(ROOT).as_posix()
        outputs[f"qa_{rel.replace('/', '_').replace('.', '_')}"] = rel
    return outputs


def _required_paths() -> list[Path]:
    return [
        CLOSE_REPORT_PATH,
        CLOSE_MANIFEST_PATH,
        QA_STEP_MANIFEST_PATH,
        DOC_DELTAS_PATH,
        QA_META_DOC_DELTAS_PATH,
        ROOT / "docs" / "evidence" / "INDEX.json",
        ROOT / "docs" / "evidence" / "INDEX.sha256",
        ROOT / "artifacts" / "evidence_index.jsonl",
        ROOT / "audit" / "gates" / "json_gate" / "canonical" / "json_gate_check_log.ndjson",
        ROOT / "audit" / "gates" / "json_gate" / "canonical" / "json_gate_compare_log.ndjson",
        ROOT / "audit" / "gates" / "json_gate" / "canonical" / "json_gate_structured_record.json",
        ROOT / "audit" / "gates" / "topology" / "orientation_demo.txt",
        PF23_PATH,
    ]


def _ensure_paths(paths: list[Path]) -> None:
    missing = [path.as_posix() for path in paths if not path.exists()]
    if missing:
        raise SystemExit(f"MISSING:{','.join(sorted(missing))}")


def _key_output_entries() -> dict[str, str]:
    outputs: dict[str, str] = {
        "close_report": "audit/EPIC-026_close_report.md",
        "close_manifest": "audit/EPIC-026_MANIFEST.json",
        "qa_step_manifest": "audit/qa/hde-epic026/qa_step_logs_manifest.json",
        "doc_deltas": "audit/docdeltas/hde-epic026_doc_deltas.md",
        "qa_doc_deltas": "audit/qa/hde-epic026/00_meta/doc_deltas.md",
        "evidence_index": "docs/evidence/INDEX.json",
        "evidence_index_sha256": "docs/evidence/INDEX.sha256",
        "evidence_index_mirror": "artifacts/evidence_index.jsonl",
        "pf23_canon": PF23_PATH.relative_to(ROOT).as_posix(),
    }
    outputs.update(_collect_index_epic026_outputs())
    outputs.update(_collect_gate_outputs())
    outputs.update(_collect_cli_outputs())
    outputs.update(_collect_qa_outputs())
    return dict(sorted(outputs.items()))


def write_close_report(captured_at: str, key_outputs: dict[str, str], pf23_excerpt: list[str], pf23_rel: str) -> None:
    key_output_paths = sorted(set(key_outputs.values()))
    key_output_lines = "\n".join(f"- `{path}`" for path in key_output_paths)
    gate_paths = sorted(
        path for path in key_output_paths if path.startswith("audit/gates/json_gate/") or path.startswith("audit/gates/topology/")
    )
    gate_lines = "\n".join(f"- `{path}`" for path in gate_paths)
    content = f"""# HDE-EPIC026 — Close Report

## Overview
HDE-EPIC026 close-pack scaffolds canonical closure outputs by summarizing currently-governed evidence and QA/gate artifacts already present in-repo, without changing product behavior.

## Capture timestamp
- `{captured_at}`

## Key Outputs
- Canonical manifest: `audit/EPIC-026_MANIFEST.json`
- Canonical step log manifest: `audit/qa/hde-epic026/qa_step_logs_manifest.json`
- Canonical doc delta ledgers: `audit/docdeltas/hde-epic026_doc_deltas.md`, `audit/qa/hde-epic026/00_meta/doc_deltas.md`
- Manifest-backed outputs ({len(key_output_paths)} paths):
{key_output_lines}

## Gate posture snapshot (present-on-disk)
{gate_lines}

## PF23 existence/path-family confirmation
- Canon source file: `{pf23_rel}`
- Canon SHA256: `{_sha256(PF23_PATH)}`
- Section reference: PF23 — Canon — Reality Audits v1.0.3, §9.1 “Evidence homes inventory”.

### PF23 §9.1 excerpt (minimal)
> {pf23_excerpt[0]}
> {pf23_excerpt[1]}


## TI-002 PF09 baseline mapping
- HDE-FERM001.3
  - `audit/qa/hde-epic026/qa_step_logs_manifest.json`
  - `audit/qa/hde-epic026/00_meta/doc_deltas.md`
- HDE-COAG007.3
  - `audit/EPIC-026_close_report.md`
  - `audit/EPIC-026_MANIFEST.json`
  - `audit/docdeltas/hde-epic026_doc_deltas.md`

## TI-002 ADR status
- ADR-TI002-EPIC026-001: Not required for PR08 baseline; supplied PF09 pointers cover committed close-pack baseline artifacts.

## Manifest reference
All paths and closure outputs above are bound in `audit/EPIC-026_MANIFEST.json` under `key_outputs`.
"""
    _write_text(CLOSE_REPORT_PATH, content)


def write_close_manifest(captured_at: str, key_outputs: dict[str, str], pf23_rel: str) -> None:
    payload = {
        "captured_at_utc": captured_at,
        "closeout_dir": "audit/qa/hde-epic026",
        "epic_id": EPIC_ID,
        "key_outputs": key_outputs,
        "pf23_ref": pf23_rel,
        "pf23_sha256": _sha256(PF23_PATH),
        "qa_epic_root": "audit/qa/hde-epic026",
        "qa_root": "audit/qa/hde-epic026",
        "qa_step_manifest_path": "audit/qa/hde-epic026/qa_step_logs_manifest.json",
        "run_id": "epic026-close",
    }
    _write_json(CLOSE_MANIFEST_PATH, payload)


def _validate_manifest_paths(key_outputs: dict[str, str]) -> None:
    missing: list[str] = []
    for rel in sorted(set(key_outputs.values())):
        if not (ROOT / rel).exists():
            missing.append(rel)
    if missing:
        raise SystemExit(f"DANGLING_MANIFEST_PATHS:{','.join(missing)}")


def main() -> int:
    try:
        ensure_determinism_env(apply=True)
    except DeterminismEnvError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    produced_at = _utc_now()
    write_step_manifest(produced_at)
    write_doc_deltas()
    _ensure_paths([path for path in _required_paths() if path not in {CLOSE_REPORT_PATH, CLOSE_MANIFEST_PATH}])
    pf23_rel, pf23_excerpt = _load_pf23_excerpt()
    key_outputs = _key_output_entries()
    write_close_manifest(produced_at, key_outputs, pf23_rel)
    write_close_report(produced_at, key_outputs, pf23_excerpt, pf23_rel)
    _write_path_proof(CLOSE_MANIFEST_PATH, produced_at)
    _write_path_proof(CLOSE_REPORT_PATH, produced_at)
    _validate_manifest_paths(key_outputs)
    _ensure_paths(_required_paths())
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
