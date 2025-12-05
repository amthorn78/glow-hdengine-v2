#!/usr/bin/env python3
"""Harden the evidence index, hash sentinel, and machine mirror.

Discovery summary (PR2 — EPIC017):
- INDEX + sentinel already existed under docs/evidence with loose schema (title/path/proof).
- The machine mirror lived at artifacts/evidence_index.jsonl with the required keys already,
  enforced partially by ci/checks/check_mirror_schema.sh.
- Path-proofs were scattered as ``*.path_proof.txt`` files with path/sha/size/mtime lines
  written by helpers such as tools/evidence/generate_rails_closed_phase1.py.
- No topology orientation demo artifact existed yet; CI only checked the sentinel hash and
  mirror schema ordering.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
from pathlib import Path
from typing import Iterable, Mapping

ROOT = Path(__file__).resolve().parents[2]
HUMAN_INDEX = ROOT / "docs/evidence/INDEX.json"
HASH_SENTINEL = ROOT / "docs/evidence/INDEX.sha256"
MIRROR_PATH = ROOT / "artifacts/evidence_index.jsonl"
MIRROR_REL = MIRROR_PATH.relative_to(ROOT).as_posix()


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _isoformat(dt: _dt.datetime) -> str:
    return dt.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _isoformat_from_timestamp(ts: float) -> str:
    return _isoformat(_dt.datetime.fromtimestamp(ts, tz=_dt.timezone.utc))


def _parse_utc_iso8601(raw: str) -> _dt.datetime:
    dt = _dt.datetime.fromisoformat(raw.replace("Z", "+00:00"))
    if dt.tzinfo != _dt.timezone.utc:
        raise ValueError("expected UTC tzinfo")
    if dt.microsecond:
        raise ValueError("expected zero microseconds")
    return dt


def _load_mirror_roles() -> dict[tuple[str, str], str]:
    roles: dict[tuple[str, str], str] = {}
    if not MIRROR_PATH.exists():
        return roles
    for raw in MIRROR_PATH.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        obj = json.loads(raw)
        roles[(obj["artifact_key"], obj["discovered_physical_path"])] = obj.get("role", "snapshot")
    return roles


def _load_existing_proof(proof_path: Path) -> dict[str, str]:
    if not proof_path.exists():
        return {}
    data: dict[str, str] = {}
    for line in proof_path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def _write_path_proof(
    rel: str,
    *,
    sha256: str,
    size_bytes: int,
    mtime_utc: str | None,
    produced_at: str | None,
    default_produced_at: str,
    check: bool,
    stat_mtime: float,
) -> tuple[str, str]:
    """Write or validate a path-proof for the given relative path.

    NEW CANON (EPIC017 WS-D4 mtime semantics): mtime_utc captures the filesystem
    mtime at evidence refresh time, truncated to seconds. It is not required to
    remain equal to future stat() values across clones. Proof checks validate
    shape and monotonicity but do not fail solely due to mtime drift.
    """

    proof_rel = f"{rel}.path_proof.txt"
    proof_path = ROOT / proof_rel
    proof_path.parent.mkdir(parents=True, exist_ok=True)

    existing = _load_existing_proof(proof_path)
    produced = produced_at or existing.get("produced_at_utc") or default_produced_at
    stat_mtime_iso = _isoformat_from_timestamp(stat_mtime)

    if check:
        if not proof_path.exists():
            raise SystemExit(f"MISSING_PROOF:{proof_rel}")
        proof = existing
        if proof.get("path") != rel:
            raise SystemExit(f"PROOF_PATH:{proof_rel}")
        if proof.get("sha256") != sha256:
            raise SystemExit(f"PROOF_SHA:{proof_rel}")
        try:
            recorded_size = int(proof.get("size_bytes", ""))
        except ValueError as exc:  # pragma: no cover - defensive
            raise SystemExit(f"PROOF_SIZE:{proof_rel}") from exc
        if recorded_size != size_bytes:
            raise SystemExit(f"PROOF_SIZE:{proof_rel}")

        mtime_raw = proof.get("mtime_utc")
        produced_raw = proof.get("produced_at_utc")
        if not mtime_raw or not produced_raw:
            raise SystemExit(f"PROOF_FIELDS:{proof_rel}")
        try:
            mtime_parsed = _parse_utc_iso8601(mtime_raw)
            _parse_utc_iso8601(produced_raw)
        except Exception as exc:  # noqa: BLE001
            raise SystemExit(f"PROOF_MTIME:{proof_rel}") from exc

        stat_mtime_dt = _dt.datetime.fromtimestamp(stat_mtime, tz=_dt.timezone.utc)
        if mtime_parsed > stat_mtime_dt:
            raise SystemExit(f"PROOF_MTIME_FUTURE:{proof_rel}")
        return proof_rel, produced

    mtime = mtime_utc or stat_mtime_iso
    proof_lines = [
        f"path: {rel}",
        f"size_bytes: {size_bytes}",
        f"sha256: {sha256}",
        f"mtime_utc: {mtime}",
        f"produced_at_utc: {produced}",
        "",
    ]
    proof_text = "\n".join(proof_lines)
    if proof_path.exists():
        existing_text = proof_path.read_text(encoding="utf-8")
        if existing_text == proof_text:
            return proof_rel, produced
    proof_path.write_text(proof_text, encoding="utf-8")
    return proof_rel, produced


def _normalize_index_entry(entry: Mapping[str, object]) -> dict[str, str]:
    key = entry.get("artifact_key") or entry.get("title")
    path = entry.get("discovered_physical_path") or entry.get("path")
    if not isinstance(key, str) or not isinstance(path, str):
        raise ValueError(f"Invalid entry: {entry!r}")
    return {"artifact_key": key, "discovered_physical_path": path}


def _load_human_index() -> list[dict[str, str]]:
    payload = json.loads(HUMAN_INDEX.read_text(encoding="utf-8"))
    entries = [_normalize_index_entry(entry) for entry in payload]
    deduped: dict[tuple[str, str], dict[str, str]] = {}
    for entry in entries:
        deduped[(entry["artifact_key"], entry["discovered_physical_path"])] = entry
    return sorted(deduped.values(), key=lambda item: (item["artifact_key"], item["discovered_physical_path"]))


def _render_human_index(entries: Iterable[Mapping[str, str]]) -> bytes:
    normalized = [
        {
            "artifact_key": entry["artifact_key"],
            "discovered_physical_path": entry["discovered_physical_path"],
        }
        for entry in entries
    ]
    return (json.dumps(normalized, separators=(",", ":"), sort_keys=True) + "\n").encode("utf-8")


def _role_for(entry: Mapping[str, str], roles: Mapping[tuple[str, str], str]) -> str:
    key = (entry["artifact_key"], entry["discovered_physical_path"])
    if key in roles:
        return roles[key]
    path = entry["discovered_physical_path"]
    if "/proofs/" in path or path.endswith(".proof.txt"):
        return "proof"
    if path.endswith(".log"):
        return "log"
    if "/audit/" in path:
        return "audit"
    return "snapshot"


def _render_mirror(
    entries: Iterable[Mapping[str, str]], *, produced_default: str, check: bool
) -> tuple[bytes, dict[str, object]]:
    """Render the machine mirror with a deterministic self-record.

    The self-record is derived only from the rendered body; it does not depend on
    any on-disk mirror or path-proof state so that a write pass followed by
    `--check` is idempotent when artifacts are unchanged.
    """

    raise_on_duplicate: set[tuple[str, str]] = set()
    records: list[dict[str, object]] = []

    for entry in entries:
        path = entry["discovered_physical_path"]
        rel_path = ROOT / path
        key = (entry["artifact_key"], path)
        if key in raise_on_duplicate:
            raise SystemExit(f"DUPLICATE_MIRROR_KEY:{key}")
        raise_on_duplicate.add(key)

        record: dict[str, object] = {
            "artifact_key": entry["artifact_key"],
            "discovered_physical_path": path,
            "produced_at_utc": None,
            "proof_anchor": f"{path}.path_proof.txt",
            "role": _role_for(entry, {}),
            "sha256": None,
            "size_bytes": None,
        }

        if rel_path == MIRROR_PATH:
            record["role"] = "self_record"
            records.append(record)
            continue

        sha = _sha256_bytes(rel_path.read_bytes())
        stat = rel_path.stat()
        proof_anchor, produced_at = _write_path_proof(
            path,
            sha256=sha,
            size_bytes=stat.st_size,
            mtime_utc=_isoformat_from_timestamp(stat.st_mtime) if not check else None,
            produced_at=None,
            default_produced_at=produced_default,
            check=check,
            stat_mtime=stat.st_mtime,
        )
        record.update({
            "sha256": sha,
            "size_bytes": stat.st_size,
            "produced_at_utc": produced_at,
            "proof_anchor": proof_anchor,
        })
        records.append(record)

    records.sort(key=lambda rec: (rec["artifact_key"], rec["discovered_physical_path"]))

    try:
        mirror_key = next(
            i
            for i, rec in enumerate(records)
            if rec["artifact_key"] == "index.machine_mirror"
            and rec["discovered_physical_path"] == MIRROR_REL
        )
    except StopIteration as exc:  # pragma: no cover - defensive
        raise SystemExit("MISSING_SELF_RECORD") from exc

    rendered_lines = [json.dumps(rec, separators=(",", ":"), sort_keys=True) for rec in records]
    body_lines = [line for i, line in enumerate(rendered_lines) if i != mirror_key]
    body_text = "\n".join(body_lines) + ("\n" if body_lines else "")

    mirror_rec = records[mirror_key]
    mirror_rec["produced_at_utc"] = produced_default
    mirror_rec["sha256"] = _sha256_bytes(body_text.encode("utf-8"))

    while True:
        rendered_lines = [json.dumps(rec, separators=(",", ":"), sort_keys=True) for rec in records]
        text = "\n".join(rendered_lines) + "\n"
        size = len(text.encode("utf-8"))
        if size == mirror_rec.get("size_bytes"):
            break
        mirror_rec["size_bytes"] = size

    return ("\n".join(rendered_lines) + "\n").encode("utf-8"), mirror_rec


def _write_if_changed(path: Path, content: bytes, *, check: bool) -> None:
    if path.exists():
        existing = path.read_bytes()
        if existing == content:
            return
        if check:
            raise SystemExit(f"STALE:{path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Maintain the evidence index and mirror")
    parser.add_argument("--check", action="store_true", help="Fail if files would change")
    args = parser.parse_args(argv)

    produced_default = _isoformat(_dt.datetime.now(tz=_dt.timezone.utc))
    mirror_proof_path = MIRROR_PATH.with_suffix(".jsonl.path_proof.txt")
    mirror_proof_existing = _load_existing_proof(mirror_proof_path)
    if mirror_proof_existing.get("produced_at_utc"):
        produced_default = mirror_proof_existing["produced_at_utc"]

    entries = _load_human_index()
    index_bytes = _render_human_index(entries)
    _write_if_changed(HUMAN_INDEX, index_bytes, check=args.check)

    hash_line = f"{_sha256_bytes(index_bytes)}  docs/evidence/INDEX.json\n".encode("utf-8")
    _write_if_changed(HASH_SENTINEL, hash_line, check=args.check)

    mirror_bytes, mirror_rec = _render_mirror(entries, produced_default=produced_default, check=args.check)
    mirror_body_sha = mirror_rec["sha256"]
    mirror_size = len(mirror_bytes)
    mirror_rec["size_bytes"] = mirror_size
    _write_if_changed(MIRROR_PATH, mirror_bytes, check=args.check)

    mirror_stat = MIRROR_PATH.stat()
    proof_anchor, produced_at = _write_path_proof(
        MIRROR_REL,
        sha256=mirror_body_sha,
        size_bytes=mirror_size,
        mtime_utc=mirror_proof_existing.get("mtime_utc"),
        produced_at=str(mirror_rec.get("produced_at_utc")),
        default_produced_at=produced_default,
        check=args.check,
        stat_mtime=mirror_stat.st_mtime,
    )
    if proof_anchor != mirror_rec["proof_anchor"]:
        mirror_rec["proof_anchor"] = proof_anchor
        if args.check:
            raise SystemExit(f"STALE_PROOF:{proof_anchor}")
    if produced_at != mirror_rec["produced_at_utc"]:
        mirror_rec["produced_at_utc"] = produced_at
        if args.check:
            raise SystemExit(f"STALE_PRODUCED_AT:{MIRROR_REL}")
    if mirror_stat.st_size != int(mirror_rec["size_bytes"]):
        if args.check:
            raise SystemExit(f"STALE_SIZE:{MIRROR_REL}")
        mirror_rec["size_bytes"] = mirror_stat.st_size


if __name__ == "__main__":
    main()
