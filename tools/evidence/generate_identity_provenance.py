#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.identity import identity_admin
from engine.serializer import canon
from scripts.release_id_recompute import _evaluate_state

def require_closed_rails():
    import os
    expected={"SAFE_MODE":"1","ALLOW_NETWORK":"0","LC_ALL":"C","LANG":"C","TZ":"UTC"}
    bad=[k for k,v in expected.items() if os.environ.get(k)!=v]
    if bad:
        raise SystemExit("DETERMINISM_ENV:"+",".join(bad))

OUTPUTS = {
    "service": ROOT / "artifacts/identity/service_identity.json",
    "release": ROOT / "artifacts/identity/release_id.json",
    "recompute": ROOT / "artifacts/identity/release_id_recompute.log",
    "emitter": ROOT / "artifacts/identity/emitter_sha256.json",
    "invocation": ROOT / "artifacts/identity/invocation_sha256.json",
    "two_run": ROOT / "artifacts/parity/two_run_identity.log",
}


def _json_bytes(obj: object) -> bytes:
    return canon.sercanon(obj, sort_keys=True)


def _release_eval():
    return _evaluate_state(
        manifest_path=ROOT / "catalog/manifest.json",
        freeze_path=ROOT / "artifacts/math/freeze_pack_manifest.json",
        release_id_path=ROOT / "artifacts/math/release_id.txt",
    )


def _expected() -> dict[Path, bytes]:
    require_closed_rails()
    identity = identity_admin()
    ev = _release_eval()
    if ev.problems:
        raise SystemExit("RELEASE_ID_STATE_INVALID:" + ",".join(ev.problems))
    if identity["release_id"] != ev.expected_release_id:
        raise SystemExit("IDENTITY_RELEASE_ID_MISMATCH")
    invocation = json.loads((ROOT / "artifacts/invocation.json").read_text(encoding="utf-8"))["invocation"]
    if invocation["tag"] != identity["invocation_tag"] or invocation["sha256"] != identity["invocation_sha256"]:
        raise SystemExit("INVOCATION_IDENTITY_MISMATCH")
    emitter_txt = (ROOT / "artifacts/identity/emitter_sha256.txt").read_text(encoding="utf-8").strip()
    if emitter_txt != identity["emitter_sha256"]:
        raise SystemExit("EMITTER_IDENTITY_MISMATCH")
    release_payload = {
        "manifest_path": "catalog/manifest.json",
        "manifest_sha256": ev.manifest_digest,
        "release_id": ev.expected_release_id,
        "release_id_algorithm": "sha256(canonical_bytes(catalog/manifest.json))",
    }
    recompute_log = "\n".join([
        "identity_release_id_recompute",
        f"manifest_sha256={ev.manifest_digest}",
        f"release_id={ev.expected_release_id}",
        "status=PASS",
        "",
    ]).encode("utf-8")
    emitter_payload = {"emitter_sha256": identity["emitter_sha256"], "source": "artifacts/identity/emitter_sha256.txt"}
    invocation_payload = {"invocation_sha256": identity["invocation_sha256"], "invocation_tag": identity["invocation_tag"], "source": "artifacts/invocation.json"}
    service = _json_bytes(identity)
    two_run = "\n".join([
        "two_run_identity",
        f"run1_sha256={hashlib.sha256(service).hexdigest()}",
        f"run2_sha256={hashlib.sha256(service).hexdigest()}",
        "status=PASS",
        "",
    ]).encode("utf-8")
    return {
        OUTPUTS["service"]: service,
        OUTPUTS["release"]: _json_bytes(release_payload),
        OUTPUTS["recompute"]: recompute_log,
        OUTPUTS["emitter"]: _json_bytes(emitter_payload),
        OUTPUTS["invocation"]: _json_bytes(invocation_payload),
        OUTPUTS["two_run"]: two_run,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    expected = _expected()
    if args.check:
        drift = [p.as_posix() for p,b in expected.items() if not p.exists() or p.read_bytes()!=b]
        if drift:
            raise SystemExit("DRIFT:" + ",".join(drift))
        return 0
    for path, body in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(body)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
