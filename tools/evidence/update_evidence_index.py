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


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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


def _write_path_proof(rel: str, *, sha256: str, size_bytes: int, produced_at: str | None = None) -> tuple[str, str]:
    proof_rel = f"{rel}.path_proof.txt"
    proof_path = ROOT / proof_rel
    proof_path.parent.mkdir(parents=True, exist_ok=True)

    existing = _load_existing_proof(proof_path)
    produced = produced_at or existing.get("produced_at_utc")
    if produced:
        try:
            _dt.datetime.fromisoformat(produced.replace("Z", "+00:00"))
        except ValueError:
            produced = None
    if not produced:
        produced = _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    proof_lines = [
        f"path: {rel}",
        f"size_bytes: {size_bytes}",
        f"sha256: {sha256}",
        f"produced_at_utc: {produced}",
        "",
    ]
    proof_text = "\n".join(proof_lines)
    if proof_path.read_text(encoding="utf-8") if proof_path.exists() else None != proof_text:
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


def _render_mirror(entries: Iterable[Mapping[str, str]]) -> bytes:
    roles = _load_mirror_roles()
    records: list[dict[str, object]] = []
    mirror_key = None
    for entry in entries:
        path = entry["discovered_physical_path"]
        rel_path = ROOT / path
        record: dict[str, object] = {
            "artifact_key": entry["artifact_key"],
            "discovered_physical_path": path,
            "produced_at_utc": None,
            "proof_anchor": f"{path}.path_proof.txt",
            "role": _role_for(entry, roles),
            "sha256": None,
            "size_bytes": None,
        }
        if rel_path == MIRROR_PATH:
            record["_mirror_marker"] = True
            existing_proof = _load_existing_proof(rel_path.with_suffix(".jsonl.path_proof.txt"))
            record["produced_at_utc"] = existing_proof.get("produced_at_utc") or _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
            record["sha256"] = existing_proof.get("sha256") or ""
            size_val = existing_proof.get("size_bytes")
            try:
                size_val = int(size_val) if size_val is not None else None
            except ValueError:
                size_val = None
            fallback_size = rel_path.stat().st_size if rel_path.exists() else 0
            record["size_bytes"] = size_val or fallback_size
        else:
            sha = _sha256_bytes(rel_path.read_bytes())
            size = rel_path.stat().st_size
            proof_anchor, produced_at = _write_path_proof(path, sha256=sha, size_bytes=size)
            record.update({
                "sha256": sha,
                "size_bytes": size,
                "produced_at_utc": produced_at,
                "proof_anchor": proof_anchor,
            })
        records.append(record)

    records.sort(key=lambda rec: (rec["artifact_key"], rec["discovered_physical_path"]))
    for idx, rec in enumerate(records):
        if rec.pop("_mirror_marker", False):
            mirror_key = idx
            break

    rendered_lines = [json.dumps(rec, separators=(",", ":"), sort_keys=True) for rec in records]

    if mirror_key is not None:
        body_lines = [line for i, line in enumerate(rendered_lines) if i != mirror_key]
        body_text = "\n".join(body_lines) + ("\n" if body_lines else "")
        mirror_rec = records[mirror_key]
        mirror_rec["sha256"] = _sha256_bytes(body_text.encode("utf-8"))
        for _ in range(5):
            rendered_lines = [json.dumps(rec, separators=(",", ":"), sort_keys=True) for rec in records]
            text = "\n".join(rendered_lines) + "\n"
            size = len(text.encode("utf-8"))
            if mirror_rec["size_bytes"] == size:
                break
            mirror_rec["size_bytes"] = size
        proof_anchor, produced_at = _write_path_proof(
            "artifacts/evidence_index.jsonl",
            sha256=str(mirror_rec["sha256"]),
            size_bytes=int(mirror_rec["size_bytes"]),
            produced_at=str(mirror_rec["produced_at_utc"]),
        )
        mirror_rec["proof_anchor"] = proof_anchor
        mirror_rec["produced_at_utc"] = produced_at
        rendered_lines = [json.dumps(rec, separators=(",", ":"), sort_keys=True) for rec in records]

    return ("\n".join(rendered_lines) + "\n").encode("utf-8")


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

    entries = _load_human_index()
    index_bytes = _render_human_index(entries)
    _write_if_changed(HUMAN_INDEX, index_bytes, check=args.check)

    hash_line = f"{_sha256_bytes(index_bytes)}  docs/evidence/INDEX.json\n".encode("utf-8")
    _write_if_changed(HASH_SENTINEL, hash_line, check=args.check)

    mirror_bytes = _render_mirror(entries)
    _write_if_changed(MIRROR_PATH, mirror_bytes, check=args.check)


if __name__ == "__main__":
    main()
