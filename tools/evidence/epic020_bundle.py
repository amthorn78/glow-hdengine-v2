#!/usr/bin/env python3
"""EPIC020 bundle and manifest generator (Candidate 1, PR1 scope).

The tool groups EPIC020 evidence families into bundles plus manifests without
touching Index/Mirror artifacts. It is intentionally conservative: artifact
and bundle keys must be provided by canon (PF10/PF12/PF19/PF20). Missing keys
surface as explicit errors rather than implicit invention.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import ensure_determinism_env
from engine.serializer.canon import sercanon


DEFAULT_ACCEPTANCE_MAP = ROOT / "docs" / "acceptance_map_epic020.json"
DEFAULT_MANIFEST = ROOT / "audit" / "EPIC020_MANIFEST.json"
DEFAULT_OUT_DIR = ROOT / "artifacts" / "epic020" / "bundles"


class Epic020BundleError(RuntimeError):
    """Raised for canonicality gaps or bundle validation failures."""


@dataclass(frozen=True)
class ArtifactDescriptor:
    artifact_key: str
    bundle_artifact_key: str
    relative_path: Path


@dataclass(frozen=True)
class MemberRecord:
    artifact_key: str
    bundle_artifact_key: str
    discovered_physical_path: str
    sha256: str
    size_bytes: int


def _iso_now() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _rails_env() -> dict[str, str]:
    env = os.environ
    env.setdefault("APP_ENV", "dev")
    ensure_determinism_env(environ=env, apply=True)
    return dict(env)


def _canonical_write(path: Path, payload: Mapping[str, object]) -> bytes:
    payload_bytes = sercanon(payload, sort_keys=True)
    if not payload_bytes.endswith(b"\n"):
        payload_bytes += b"\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload_bytes)
    return payload_bytes


def _canonical_dump(payload: Mapping[str, object]) -> bytes:
    payload_bytes = sercanon(payload, sort_keys=True)
    if not payload_bytes.endswith(b"\n"):
        payload_bytes += b"\n"
    return payload_bytes


def _load_json(path: Path) -> Mapping[str, object]:
    with path.open("rb") as f:
        return json.load(f)


def _discover_artifacts(
    epic_id: str,
    acceptance_map_path: Path,
    audit_manifest_path: Path,
    base_dir: Path,
) -> list[ArtifactDescriptor]:
    acceptance = _load_json(acceptance_map_path)
    if acceptance.get("epic_id") != epic_id:
        raise Epic020BundleError(
            f"Acceptance map {acceptance_map_path} has epic_id={acceptance.get('epic_id')} but expected {epic_id}"
        )

    audit_manifest = _load_json(audit_manifest_path)
    if audit_manifest.get("epic_id") != epic_id:
        raise Epic020BundleError(
            f"Audit manifest {audit_manifest_path} has epic_id={audit_manifest.get('epic_id')} but expected {epic_id}"
        )

    token_status = acceptance.get("token_status", {})
    descriptors: list[ArtifactDescriptor] = []
    for token, entry in sorted(token_status.items()):
        artifacts = entry.get("artifacts", []) if isinstance(entry, Mapping) else []
        for raw in artifacts:
            if not isinstance(raw, Mapping):
                raise Epic020BundleError(
                    f"Artifact entry for token {token} must include artifact_key/bundle_artifact_key; missing in {raw!r}"
                )
            artifact_key = raw.get("artifact_key")
            bundle_key = raw.get("bundle_artifact_key")
            path_value = raw.get("path") or raw.get("artifact_path")
            if not artifact_key:
                raise Epic020BundleError(
                    f"Artifact entry for token {token} is missing artifact_key (PF10/PF12 canon gap)"
                )
            if not bundle_key:
                raise Epic020BundleError(
                    f"Artifact {artifact_key} is missing bundle_artifact_key (PF10/PF12 canon gap)"
                )
            if not path_value:
                raise Epic020BundleError(f"Artifact {artifact_key} is missing physical path")
            rel_path = Path(path_value)
            physical_path = base_dir / rel_path
            if not physical_path.is_file():
                raise Epic020BundleError(f"Artifact path {physical_path} not found for {artifact_key}")
            descriptors.append(
                ArtifactDescriptor(
                    artifact_key=str(artifact_key),
                    bundle_artifact_key=str(bundle_key),
                    relative_path=rel_path,
                )
            )
    descriptors.sort(key=lambda d: (d.bundle_artifact_key, d.artifact_key, str(d.relative_path)))
    if not descriptors:
        raise Epic020BundleError("No EPIC020 artifacts discovered; ensure acceptance map lists bundle members")
    return descriptors


def _digest(path: Path) -> tuple[str, int]:
    import hashlib

    h = hashlib.sha256()
    data = path.read_bytes()
    h.update(data)
    return h.hexdigest(), len(data)


def _build_member_records(descriptors: Iterable[ArtifactDescriptor], base_dir: Path) -> list[MemberRecord]:
    records: list[MemberRecord] = []
    for desc in descriptors:
        physical_path = base_dir / desc.relative_path
        sha, size = _digest(physical_path)
        records.append(
            MemberRecord(
                artifact_key=desc.artifact_key,
                bundle_artifact_key=desc.bundle_artifact_key,
                discovered_physical_path=str(desc.relative_path.as_posix()),
                sha256=sha,
                size_bytes=size,
            )
        )
    records.sort(key=lambda r: (r.bundle_artifact_key, r.artifact_key, r.discovered_physical_path))
    return records


def _write_bundle(bundle_key: str, epic_id: str, members: Sequence[MemberRecord], out_dir: Path) -> Path:
    bundle_path = out_dir / f"{bundle_key}.bundle.json"
    payload = {
        "artifact_key": bundle_key,
        "epic_id": epic_id,
        "members": [
            {
                "artifact_key": m.artifact_key,
                "bundle_artifact_key": m.bundle_artifact_key,
                "discovered_physical_path": m.discovered_physical_path,
                "record_type": "epic020_bundle_member",
                "schema_version": "1.0",
                "sha256": m.sha256,
                "size_bytes": m.size_bytes,
            }
            for m in members
            if m.bundle_artifact_key == bundle_key
        ],
        "record_type": "epic020_bundle",
        "schema_version": "1.0",
    }
    _canonical_write(bundle_path, payload)
    return bundle_path


def _relative_path(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:  # pragma: no cover - defensive for external out_dir
        return str(path)


def _render_bundle_payload(bundle_key: str, epic_id: str, members: Sequence[MemberRecord]) -> bytes:
    payload = {
        "artifact_key": bundle_key,
        "epic_id": epic_id,
        "members": [
            {
                "artifact_key": m.artifact_key,
                "bundle_artifact_key": m.bundle_artifact_key,
                "discovered_physical_path": m.discovered_physical_path,
                "record_type": "epic020_bundle_member",
                "schema_version": "1.0",
                "sha256": m.sha256,
                "size_bytes": m.size_bytes,
            }
            for m in members
            if m.bundle_artifact_key == bundle_key
        ],
        "record_type": "epic020_bundle",
        "schema_version": "1.0",
    }
    return _canonical_dump(payload)


def _render_manifest_payload(
    bundle_key: str,
    epic_id: str,
    members: Sequence[MemberRecord],
    bundle_path: Path,
    root: Path,
    produced_at_utc: str,
) -> bytes:
    payload = {
        "artifact_key": bundle_key,
        "bundle_path": _relative_path(bundle_path, root),
        "epic_id": epic_id,
        "members": [
            {
                "artifact_key": m.artifact_key,
                "bundle_artifact_key": m.bundle_artifact_key,
                "discovered_physical_path": m.discovered_physical_path,
                "record_type": "epic020_bundle_member",
                "schema_version": "1.0",
                "sha256": m.sha256,
                "size_bytes": m.size_bytes,
            }
            for m in members
            if m.bundle_artifact_key == bundle_key
        ],
        "produced_at_utc": produced_at_utc,
        "record_type": "epic020_bundle_manifest",
        "schema_version": "1.0",
    }
    return _canonical_dump(payload)


def build_epic020_bundles(
    epic_id: str,
    acceptance_map: Path = DEFAULT_ACCEPTANCE_MAP,
    audit_manifest: Path = DEFAULT_MANIFEST,
    out_dir: Path = DEFAULT_OUT_DIR,
    mode: str = "build",
    base_dir: Path | None = None,
    dry_run: bool = False,
) -> None:
    if epic_id != "HDE-EPIC020":
        raise Epic020BundleError(f"Unsupported epic_id {epic_id}; only HDE-EPIC020 is allowed in PR1")

    _rails_env()
    base_dir = base_dir or ROOT
    descriptors = _discover_artifacts(epic_id, acceptance_map, audit_manifest, base_dir)
    members = _build_member_records(descriptors, base_dir)
    bundles = {}
    for member in members:
        bundles.setdefault(member.bundle_artifact_key, []).append(member)

    out_dir.mkdir(parents=True, exist_ok=True)

    if mode == "check":
        for bundle_key, bundle_members in sorted(bundles.items()):
            bundle_path = out_dir / f"{bundle_key}.bundle.json"
            manifest_path = out_dir / f"{bundle_key}.manifest.json"
            expected_bundle = _render_bundle_payload(bundle_key, epic_id, bundle_members)
            existing_manifest_ts = None
            if manifest_path.is_file():
                try:
                    existing_manifest_ts = json.loads(manifest_path.read_bytes()).get("produced_at_utc")
                except Exception:  # pragma: no cover - defensive
                    existing_manifest_ts = None
            expected_manifest = _render_manifest_payload(
                bundle_key,
                epic_id,
                bundle_members,
                bundle_path,
                ROOT,
                existing_manifest_ts or _iso_now(),
            )
            if not bundle_path.is_file() or not manifest_path.is_file():
                raise Epic020BundleError(
                    f"Bundle or manifest missing for {bundle_key}; run build mode to create them"
                )
            if bundle_path.read_bytes() != expected_bundle:
                raise Epic020BundleError(f"Bundle content mismatch for {bundle_key}; regenerate under build mode")
            if manifest_path.read_bytes() != expected_manifest:
                raise Epic020BundleError(f"Manifest content mismatch for {bundle_key}; regenerate under build mode")
        return

    if mode != "build":
        raise Epic020BundleError(f"Unknown mode {mode}; expected 'build' or 'check'")

    for bundle_key, bundle_members in sorted(bundles.items()):
        bundle_path = out_dir / f"{bundle_key}.bundle.json"
        manifest_path = out_dir / f"{bundle_key}.manifest.json"
        bundle_bytes = _render_bundle_payload(bundle_key, epic_id, bundle_members)
        prior_manifest_ts = None
        if manifest_path.is_file():
            try:
                prior_manifest_ts = json.loads(manifest_path.read_bytes()).get("produced_at_utc")
            except Exception:  # pragma: no cover - defensive
                prior_manifest_ts = None
        manifest_bytes = _render_manifest_payload(
            bundle_key,
            epic_id,
            bundle_members,
            bundle_path,
            ROOT,
            prior_manifest_ts or _iso_now(),
        )
        if dry_run:
            continue
        bundle_path.write_bytes(bundle_bytes)
        manifest_path.write_bytes(manifest_bytes)


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["build", "check"], help="Action to perform")
    parser.add_argument("--epic-id", required=True, help="Epic ID (must be HDE-EPIC020)")
    parser.add_argument("--acceptance-map", type=Path, default=DEFAULT_ACCEPTANCE_MAP)
    parser.add_argument("--audit-manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    parser.add_argument("--base-dir", type=Path, default=ROOT)
    parser.add_argument("--dry-run", action="store_true", help="Build without writing files")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    args = _parse_args(argv)
    try:
        build_epic020_bundles(
            epic_id=args.epic_id,
            acceptance_map=args.acceptance_map,
            audit_manifest=args.audit_manifest,
            out_dir=args.out_dir,
            mode=args.mode,
            base_dir=args.base_dir,
            dry_run=args.dry_run,
        )
    except Epic020BundleError as exc:  # pragma: no cover - CLI surface
        sys.stderr.write(f"epic020_bundle: {exc}\n")
        sys.exit(1)


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    main()
