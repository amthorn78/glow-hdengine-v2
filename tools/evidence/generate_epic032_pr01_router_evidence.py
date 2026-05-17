#!/usr/bin/env python3
"""Generate HDE-EPIC032 PR-01 narrative-router evidence artifacts."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from adapter.http_reader import app
from engine.serializer.canon import sercanon
from engine.narratives import MISSING_NARRATIVE_KEY, get_pack, route_keys
from engine.narratives.constants import BANDS, PERSPECTIVES
from engine.runtime.determinism_env import ensure_determinism_env

KEY_TABLE_PATH = ROOT / "audit/gates/narratives/keys_10x4.table.json"
ABBA_LOG_PATH = ROOT / "artifacts/narratives/router/parity_abba.log"
CLI_HTTP_LOG_PATH = ROOT / "artifacts/narratives/router/cli_http_parity.log"
EXPECTED_CATEGORIES: tuple[str, ...] = (
    "heat",
    "harmony",
    "communication",
    "alignment",
    "comfort",
    "consistency",
    "expansion",
    "creativity",
    "drive",
    "balance",
)
EXPECTED_KEY_TABLE_ROWS = 40
RELEASE_ID = "0" * 64


def _canonical_json_bytes(value: object) -> bytes:
    return (
        json.dumps(value, separators=(",", ":"), sort_keys=True) + "\n"
    ).encode("utf-8")


def _write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _write_text(path: Path, lines: Iterable[str]) -> None:
    text = "\n".join(lines) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _supported_cases() -> list[tuple[str, str, str]]:
    return [
        (category, band, perspective)
        for category in EXPECTED_CATEGORIES
        for band in BANDS
        for perspective in PERSPECTIVES
    ]


def _validate_pack_roster() -> None:
    pack = get_pack()
    actual = tuple(category for category in EXPECTED_CATEGORIES if category in pack.categories)
    missing = sorted(set(EXPECTED_CATEGORIES) - pack.categories)
    extra = sorted(pack.categories - set(EXPECTED_CATEGORIES))
    if missing or extra or actual != EXPECTED_CATEGORIES:
        raise SystemExit(
            "ROUTER_CATEGORY_ROSTER_MISMATCH:"
            f"missing={','.join(missing) or '-'};extra={','.join(extra) or '-'}"
        )


def _key_table() -> list[dict[str, str]]:
    pack = get_pack()
    _validate_pack_roster()
    rows: list[dict[str, str]] = []
    for category in EXPECTED_CATEGORIES:
        for band in BANDS:
            routed = route_keys(category, band, "shared", viewer_top=None, flags=None)
            if MISSING_NARRATIVE_KEY in routed.values():
                raise SystemExit(f"ROUTER_KEY_TABLE_MISSING:{category}:{band}")
            rows.append(
                {
                    "band": band,
                    "category": category,
                    "personal_key": routed["personal_key"],
                    "shared_key": routed["shared_key"],
                }
            )
    if len(rows) != EXPECTED_KEY_TABLE_ROWS:
        raise SystemExit(f"ROUTER_KEY_TABLE_ROW_COUNT:{len(rows)}")
    return rows


def _generate_abba_log() -> None:
    _validate_pack_roster()
    cases: list[tuple[str, str, str]] = [
        *_supported_cases(),
        ("unknown", "Cool", "shared"),
        ("harmony", "Unknown", "shared"),
        ("harmony", "Cool", "unknown"),
    ]

    lines = [
        "schema=hde_epic032.pr01.router_abba.v1",
        "epic_id=HDE-EPIC032",
        "subtask_id=HDE-FERM002.2",
        "tokens=TWO_RUN_IDENTITY_OK,COMPOSITE_ABBA_IDENTITY_OK",
    ]
    two_run_ok = True
    for idx, (category, band, perspective) in enumerate(cases, start=1):
        first = route_keys(
            category, band, perspective, viewer_top=None, flags=["b", "a", "b"]
        )
        second = route_keys(
            category, band, perspective, viewer_top=None, flags=["b", "a", "b"]
        )
        equal = first == second
        two_run_ok = two_run_ok and equal
        lines.append(
            "case={idx:03d} category={category} band={band} perspective={perspective} "
            "personal_key={personal_key} shared_key={shared_key} two_run_equal={equal}".format(
                idx=idx,
                category=category,
                band=band,
                perspective=perspective,
                personal_key=first["personal_key"],
                shared_key=first["shared_key"],
                equal=str(equal).lower(),
            )
        )

    abba_ok = True
    for category in EXPECTED_CATEGORIES:
        for band in BANDS:
            ab = route_keys(category, band, "a_to_b", viewer_top=None, flags=None)
            ba = route_keys(category, band, "b_to_a", viewer_top=None, flags=None)
            equal = ab == ba
            abba_ok = abba_ok and equal
            lines.append(
                "abba category={category} band={band} ab_personal_key={ab_personal} "
                "ba_personal_key={ba_personal} ab_shared_key={ab_shared} ba_shared_key={ba_shared} "
                "normalized_equal={equal}".format(
                    category=category,
                    band=band,
                    ab_personal=ab["personal_key"],
                    ba_personal=ba["personal_key"],
                    ab_shared=ab["shared_key"],
                    ba_shared=ba["shared_key"],
                    equal=str(equal).lower(),
                )
            )

    missing_ok = True
    for category, band, perspective in [
        ("unknown", "Cool", "shared"),
        ("harmony", "Unknown", "shared"),
        ("harmony", "Cool", "unknown"),
        ("unknown", "Unknown", "unknown"),
    ]:
        routed = route_keys(category, band, perspective, viewer_top=None, flags=None)
        equal = routed == {
            "personal_key": MISSING_NARRATIVE_KEY,
            "shared_key": MISSING_NARRATIVE_KEY,
        }
        missing_ok = missing_ok and equal
        lines.append(
            "missing category={category} band={band} perspective={perspective} "
            "personal_key={personal_key} shared_key={shared_key} missing_equal={equal}".format(
                category=category,
                band=band,
                perspective=perspective,
                personal_key=routed["personal_key"],
                shared_key=routed["shared_key"],
                equal=str(equal).lower(),
            )
        )

    status = two_run_ok and abba_ok and missing_ok
    lines.extend(
        [
            f"two_run_identity={str(two_run_ok).lower()}",
            f"abba_identity={str(abba_ok).lower()}",
            f"missing_key_identity={str(missing_ok).lower()}",
            "status=PASS" if status else "status=FAIL",
        ]
    )
    _write_text(ABBA_LOG_PATH, lines)
    if not status:
        raise SystemExit("ROUTER_ABBA_EVIDENCE_FAILED")


def _run_cli_admin(category: str, band: str, perspective: str, admin_out: Path) -> dict[str, object]:
    env = os.environ.copy()
    env.update(
        {
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
            "SAFE_MODE": "1",
            "ALLOW_NETWORK": "0",
            "RELEASE_ID": RELEASE_ID,
        }
    )
    cmd = [
        sys.executable,
        "-c",
        "import sys; from engine.cli.main import cli; raise SystemExit(cli(sys.argv[1:]))",
        "aux-preview",
        "--category",
        category,
        "--band",
        band,
        "--perspective",
        perspective,
        "--admin-out",
        str(admin_out),
    ]
    result = subprocess.run(cmd, cwd=ROOT, env=env, capture_output=True, check=False)
    if result.returncode != 0:
        raise SystemExit(f"CLI_AUX_PREVIEW_FAILED:{result.returncode}")
    return json.loads(admin_out.read_text(encoding="utf-8"))


def _generate_cli_http_log() -> None:
    _validate_pack_roster()
    cases = _supported_cases()
    client = app.test_client()
    lines = [
        "schema=hde_epic032.pr01.router_cli_http_parity.v1",
        "epic_id=HDE-EPIC032",
        "subtask_id=HDE-FERM002.2",
        "surface=hdctl_aux_preview_admin_out_to_api_aux_narrative_headers",
        "tokens=CLI_READER_PARITY_OK",
    ]
    parity_ok = True
    with tempfile.TemporaryDirectory(prefix="hde_epic032_router_") as tmp:
        tmp_path = Path(tmp)
        for idx, (category, band, perspective) in enumerate(cases, start=1):
            admin_out = tmp_path / f"case_{idx:03d}.json"
            cli_payload = _run_cli_admin(category, band, perspective, admin_out)
            resp = client.get(
                "/api/aux/narrative",
                query_string={
                    "category": category,
                    "band": band,
                    "perspective": perspective,
                    "release_id": RELEASE_ID,
                    "v": "1",
                },
            )
            key_header = resp.headers.get("X-Narrative-Key")
            composition_id = resp.headers.get("X-Narrative-Composition") or ""
            suppressed = resp.headers.get("X-Narrative-Policy") == "suppressed"
            if suppressed:
                http_key = composition_id
                key_header_ok = key_header is None
            else:
                http_key = key_header or ""
                key_header_ok = bool(key_header)
            http_payload = {
                "composition_id": composition_id,
                "key": http_key,
                "pack_sha": resp.headers.get("X-Narrative-Pack-Sha") or "",
                "release_id": RELEASE_ID,
            }
            expected_fields = {"composition_id", "key", "pack_sha", "release_id"}
            fields_equal = (
                set(cli_payload) == expected_fields and cli_payload == http_payload
            )
            cli_bytes = admin_out.read_bytes()
            cli_canonical = cli_bytes == sercanon(cli_payload)
            sidecar = admin_out.with_name(f"{admin_out.name}.sha256")
            if sidecar.exists():
                sidecar_digest = sidecar.read_text(encoding="utf-8").strip()
            else:
                sidecar_digest = ""
            sidecar_equal = sidecar_digest == hashlib.sha256(cli_bytes).hexdigest()
            equal = (
                resp.status_code == 200
                and key_header_ok
                and fields_equal
                and cli_canonical
                and sidecar_equal
            )
            parity_ok = parity_ok and equal
            lines.append(
                "case={idx:03d} category={category} band={band} perspective={perspective} "
                "key={key} composition_id={composition_id} suppressed={suppressed} "
                "key_header_ok={key_header_ok} pack_sha_equal={pack_sha_equal} "
                "release_id_equal={release_id_equal} fields_equal={fields_equal} "
                "cli_canonical={cli_canonical} sidecar_equal={sidecar_equal} parity_equal={equal}".format(
                    idx=idx,
                    category=category,
                    band=band,
                    perspective=perspective,
                    key=http_payload["key"],
                    composition_id=http_payload["composition_id"],
                    suppressed=str(suppressed).lower(),
                    key_header_ok=str(key_header_ok).lower(),
                    pack_sha_equal=str(
                        cli_payload.get("pack_sha") == http_payload["pack_sha"]
                    ).lower(),
                    release_id_equal=str(
                        cli_payload.get("release_id") == RELEASE_ID
                    ).lower(),
                    fields_equal=str(fields_equal).lower(),
                    cli_canonical=str(cli_canonical).lower(),
                    sidecar_equal=str(sidecar_equal).lower(),
                    equal=str(equal).lower(),
                )
            )
    lines.extend(
        [
            f"cli_http_parity={str(parity_ok).lower()}",
            "status=PASS" if parity_ok else "status=FAIL",
        ]
    )
    _write_text(CLI_HTTP_LOG_PATH, lines)
    if not parity_ok:
        raise SystemExit("ROUTER_CLI_HTTP_PARITY_FAILED")


def main() -> None:
    ensure_determinism_env()
    _write_bytes(KEY_TABLE_PATH, _canonical_json_bytes(_key_table()))
    _generate_abba_log()
    _generate_cli_http_log()


if __name__ == "__main__":
    main()
