from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL_MODULE = "tools.evidence.epic020_bundle"


def _env_with_rails() -> dict[str, str]:
    env = os.environ.copy()
    env.update(
        {
            "SAFE_MODE": "1",
            "ALLOW_NETWORK": "0",
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
            "APP_ENV": env.get("APP_ENV", "dev"),
        }
    )
    return env


def _fixture_root(name: str) -> Path:
    return REPO_ROOT / "tests" / "fixtures" / "epic020" / "bundles" / name


def _run_tool(
    tmp_path: Path,
    mode: str,
    *,
    acceptance_map: Path | None = None,
    audit_manifest: Path | None = None,
    base_dir: Path | None = None,
    extra_env: dict[str, str] | None = None,
    dry_run: bool = False,
) -> subprocess.CompletedProcess:
    env = _env_with_rails()
    if extra_env:
        env.update(extra_env)
    acceptance_map = acceptance_map or _fixture_root("docs/acceptance_map_epic020.json")
    audit_manifest = audit_manifest or _fixture_root("audit/EPIC020_MANIFEST.json")
    base_dir = base_dir or _fixture_root("")
    args = [
        "python",
        "-m",
        TOOL_MODULE,
        mode,
        "--epic-id",
        "HDE-EPIC020",
        "--acceptance-map",
        str(acceptance_map),
        "--audit-manifest",
        str(audit_manifest),
        "--out-dir",
        str(tmp_path / "artifacts"),
        "--base-dir",
        str(base_dir),
    ]
    if dry_run:
        args.append("--dry-run")
    return subprocess.run(args, env=env, capture_output=True, text=True, check=False)


def _load_json(path: Path) -> dict:
    with path.open("rb") as f:
        return json.load(f)


def _assert_lf_terminated(path: Path) -> None:
    data = path.read_bytes()
    assert data.endswith(b"\n"), f"{path} must end with newline"


def test_epic020_bundle_build_produces_bundle_and_manifest(tmp_path: Path) -> None:
    result = _run_tool(tmp_path, "build")
    assert result.returncode == 0, result.stderr

    bundle_path = tmp_path / "artifacts" / "EPIC020.D1.HTTP_COMPAT_HTTP_BUNDLE.bundle.json"
    manifest_path = tmp_path / "artifacts" / "EPIC020.D1.HTTP_COMPAT_HTTP_BUNDLE.manifest.json"

    assert bundle_path.is_file()
    assert manifest_path.is_file()

    bundle = _load_json(bundle_path)
    manifest = _load_json(manifest_path)

    assert bundle["artifact_key"] == "EPIC020.D1.HTTP_COMPAT_HTTP_BUNDLE"
    assert manifest["artifact_key"] == "EPIC020.D1.HTTP_COMPAT_HTTP_BUNDLE"
    assert bundle["members"] == manifest["members"]
    assert bundle["record_type"] == "epic020_bundle"
    assert manifest["record_type"] == "epic020_bundle_manifest"
    assert bundle["schema_version"] == "1.0"
    assert manifest["schema_version"] == "1.0"

    _assert_lf_terminated(bundle_path)
    _assert_lf_terminated(manifest_path)


def test_epic020_bundle_build_is_deterministic(tmp_path: Path) -> None:
    first = _run_tool(tmp_path, "build")
    assert first.returncode == 0, first.stderr

    bundle_path = tmp_path / "artifacts" / "EPIC020.D1.HTTP_COMPAT_HTTP_BUNDLE.bundle.json"
    manifest_path = tmp_path / "artifacts" / "EPIC020.D1.HTTP_COMPAT_HTTP_BUNDLE.manifest.json"
    bundle_bytes = bundle_path.read_bytes()
    manifest_bytes = manifest_path.read_bytes()

    second = _run_tool(tmp_path, "build")
    assert second.returncode == 0, second.stderr
    assert bundle_path.read_bytes() == bundle_bytes
    assert manifest_path.read_bytes() == manifest_bytes


def test_epic020_bundle_check_mode_validates_without_writing(tmp_path: Path) -> None:
    build = _run_tool(tmp_path, "build")
    assert build.returncode == 0, build.stderr

    bundle_path = tmp_path / "artifacts" / "EPIC020.D1.HTTP_COMPAT_HTTP_BUNDLE.bundle.json"
    before_mtime = bundle_path.stat().st_mtime

    check = _run_tool(tmp_path, "check")
    assert check.returncode == 0, check.stderr
    assert bundle_path.stat().st_mtime == before_mtime

    # Introduce mismatch
    bundle_path.write_text("corrupted\n")
    failure = _run_tool(tmp_path, "check")
    assert failure.returncode != 0
    assert "mismatch" in failure.stderr.lower()


def test_epic020_bundle_handles_string_artifact_entries(tmp_path: Path) -> None:
    result = _run_tool(
        tmp_path,
        "build",
        acceptance_map=REPO_ROOT / "docs" / "acceptance_map_epic020.json",
        audit_manifest=REPO_ROOT / "audit" / "EPIC020_MANIFEST.json",
        base_dir=REPO_ROOT,
        dry_run=True,
    )
    assert result.returncode == 0, result.stderr


def test_epic020_bundle_accepts_discovered_physical_path_entries(tmp_path: Path) -> None:
    acceptance_map = tmp_path / "acceptance_map_epic020.json"
    acceptance_map.write_text(
        json.dumps(
            {
                "epic_id": "HDE-EPIC020",
                "token_status": {
                    "EPIC020.D1.HTTP_COMPAT_MALFORMED_JSON": {
                        "artifacts": [
                            {
                                "artifact_key": "EPIC020.D1.HTTP_COMPAT_MALFORMED_JSON",
                                "bundle_artifact_key": "EPIC020.D1.HTTP_COMPAT_HTTP_BUNDLE",
                                "discovered_physical_path": "artifacts/compat/invalid_payload.json",
                            }
                        ]
                    }
                },
            }
        )
        + "\n"
    )

    result = _run_tool(
        tmp_path,
        "build",
        acceptance_map=acceptance_map,
        audit_manifest=_fixture_root("audit/EPIC020_MANIFEST.json"),
        base_dir=_fixture_root(""),
        dry_run=True,
    )

    assert result.returncode == 0, result.stderr


def test_epic020_bundle_ignores_outputs_listed_as_artifacts(tmp_path: Path) -> None:
    acceptance_map = tmp_path / "acceptance_map_epic020.json"
    acceptance_map.write_text(
        json.dumps(
            {
                "epic_id": "HDE-EPIC020",
                "token_status": {
                    "EPIC020.D1.HTTP_COMPAT_MALFORMED_JSON": {
                        "artifacts": [
                            {
                                "artifact_key": "EPIC020.D1.HTTP_COMPAT_MALFORMED_JSON",
                                "bundle_artifact_key": "EPIC020.D1.HTTP_COMPAT_HTTP_BUNDLE",
                                "discovered_physical_path": "artifacts/compat/invalid_payload.json",
                            },
                            {
                                "artifact_key": "EPIC020.D1.HTTP_COMPAT_HTTP_BUNDLE",
                                "bundle_artifact_key": "EPIC020.D1.HTTP_COMPAT_HTTP_BUNDLE",
                                "discovered_physical_path": "artifacts/epic020/bundles/EPIC020.D1.HTTP_COMPAT_HTTP_BUNDLE.bundle.json",
                            },
                            {
                                "artifact_key": "EPIC020.D1.HTTP_COMPAT_HTTP_BUNDLE",
                                "bundle_artifact_key": "EPIC020.D1.HTTP_COMPAT_HTTP_BUNDLE",
                                "discovered_physical_path": "artifacts/epic020/bundles/EPIC020.D1.HTTP_COMPAT_HTTP_BUNDLE.manifest.json",
                            },
                        ]
                    }
                },
            }
        )
        + "\n",
    )

    result = _run_tool(
        tmp_path,
        "build",
        acceptance_map=acceptance_map,
        audit_manifest=_fixture_root("audit/EPIC020_MANIFEST.json"),
        base_dir=_fixture_root(""),
    )

    assert result.returncode == 0, result.stderr

    bundle_path = tmp_path / "artifacts" / "EPIC020.D1.HTTP_COMPAT_HTTP_BUNDLE.bundle.json"
    bundle = _load_json(bundle_path)
    assert len(bundle["members"]) == 1
    assert all("/epic020/bundles/" not in member["discovered_physical_path"] for member in bundle["members"])
