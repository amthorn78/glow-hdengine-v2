#!/usr/bin/env python3
"""Magic-10 v2 typed-bundle evidence (HDE-EPIC043 WU-PR-11; HDE-SEPA008.1 to .3).

The writer records the regenerated typed config bundles as one governed record,
``audit/qa/hde-epic043/pr-11/v2_bundle_evidence.txt``.  Every value is computed
in process at the head:

* the tested-source identity: each tested input's path, SHA-256 and size (both
  consumer schemas, the bundle builder, both bundles, the band-edges artifact,
  the thresholds and the release manifest) and one digest over those lines;
* the admitted release that produced the bundles (``release_id`` and
  ``config_id``);
* for each bundle: its consumer schema and identity, validation through the
  executed strict validator (``_validate_local_schema``), the keys of its
  ``bands`` block, and the absence of the v1 global keys;
* the backend ``bands`` block against the band-edges artifact;
* for each category, in catalog order: the backend and frontend maxima against
  the thresholds' maxima;
* the bundles' ``sources.band_edges`` binding against the band-edges artifact;
* the regeneration command, recorded, and the two read-only ``--check``
  commands, run here, each with its exit code.

The record also names the responsible actor, the run time and the interpreter.
``--check`` re-renders every other line and compares the bytes; it checks those
three run fields for shape only, so it is byte-stable and writes nothing.  The
record carries no git state: its tested-source identity is the input digests,
which the PR result maps to the tested commit.  A failing check is a named
refusal and nothing is written.  It runs only under the closed determinism
rails, from the repository root.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import datetime as dt
from pathlib import Path
from typing import Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.config.registry_loader import (  # noqa: E402
    RegistryConfigError,
    _LocalCapture,
    _load_active_mechanics_bundle_from_root,
    _validate_local_schema,
)
from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env  # noqa: E402

OUT_REL = "audit/qa/hde-epic043/pr-11/v2_bundle_evidence.txt"
SCHEMA = "hde_epic043_v2_bundle_evidence.v1"
GENERATOR_REL = "tools/evidence/generate_hde_epic043_v2_bundle_evidence.py"

BUNDLES = {
    "be": ("artifacts/config_bundles/be_bundle.json", "docs/schemas/config_bundle_be.json", "config_bundle.be.v1"),
    "fe": ("artifacts/config_bundles/fe_bundle.json", "docs/schemas/config_bundle_fe.json", "config_bundle.fe.v1"),
}
BAND_EDGES_REL = "artifacts/thresholds/band_edges.json"
THRESHOLDS_REL = "math/thresholds.json"
MANIFEST_REL = "catalog/manifest.json"
BUILDER_REL = "engine/config/bundles.py"
TESTED_INPUTS = (
    "docs/schemas/config_bundle_be.json",
    "docs/schemas/config_bundle_fe.json",
    BUILDER_REL,
    "artifacts/config_bundles/be_bundle.json",
    "artifacts/config_bundles/fe_bundle.json",
    BAND_EDGES_REL,
    THRESHOLDS_REL,
    MANIFEST_REL,
)
V1_GLOBAL_KEYS = ("edges", "clamp", "rounding")
REGENERATION_COMMAND = "python tools/config/generate_config_artifacts.py --publish-family"
CHECK_COMMANDS = (
    ("tools/config/generate_bundles.py", "--check"),
    ("tools/config/generate_config_artifacts.py", "--check"),
)
RUN_FIELDS = ("run.time_utc", "run.actor", "run.python")
_TIME = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
_PYTHON = re.compile(r"\d+\.\d+\.\d+")
LIMITATIONS = (
    "no live run: no production, vendor, database or network access",
    "interpreter: run.python locally; hosted CI's interpreter may differ",
    "evidence of the tested inputs named above only, not of a later state",
    "establishes no QA verdict, acceptance, Ops, deployment or closure",
)

RAILS_NOT_CLOSED = "V2_BUNDLE_EVIDENCE_RAILS_NOT_CLOSED"
INVALID_ACTOR = "V2_BUNDLE_EVIDENCE_INVALID_ACTOR"
INPUT_UNREADABLE = "V2_BUNDLE_EVIDENCE_INPUT_UNREADABLE"
RELEASE_REFUSED = "V2_BUNDLE_EVIDENCE_RELEASE_REFUSED"
SCHEMA_REFUSED = "V2_BUNDLE_EVIDENCE_SCHEMA_REFUSED"
MAXIMA_MISMATCH = "V2_BUNDLE_EVIDENCE_MAXIMA_MISMATCH"
SOURCES_MISMATCH = "V2_BUNDLE_EVIDENCE_SOURCES_MISMATCH"
CHECK_COMMAND_FAILED = "V2_BUNDLE_EVIDENCE_CHECK_COMMAND_FAILED"
RECORD_INVALID = "V2_BUNDLE_EVIDENCE_RECORD_INVALID"


class BundleEvidenceRefusal(RuntimeError):
    """A named refusal: no record is written."""

    def __init__(self, code: str) -> None:
        super().__init__(code)
        self.code = code


def out_path() -> Path:
    return ROOT / OUT_REL


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compact(value: object) -> str:
    return json.dumps(value, separators=(",", ":"), ensure_ascii=True)


def valid_actor(actor: str) -> bool:
    """The HDE-SEPA007.5 writer's actor rule."""

    return 0 < len(actor) <= 200 and actor.isprintable() and actor == actor.strip()


def read_input(rel: str) -> bytes:
    try:
        return (ROOT / rel).read_bytes()
    except OSError:
        raise BundleEvidenceRefusal(f"{INPUT_UNREADABLE}:{rel}") from None


def read_json(rel: str) -> object:
    try:
        return json.loads(read_input(rel).decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise BundleEvidenceRefusal(f"{INPUT_UNREADABLE}:{rel}") from None


def child_env() -> dict[str, str]:
    environ = os.environ.copy()
    environ.update({"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"})
    return environ


def run_check_command(command: Sequence[str]) -> int:
    """Run one read-only ``--check`` command from the repository root; its own exit code."""

    return subprocess.run([sys.executable, *command], cwd=ROOT, env=child_env(),
                          capture_output=True).returncode


def head_release() -> dict[str, str]:
    try:
        bundle = _load_active_mechanics_bundle_from_root(ROOT)
    except RegistryConfigError:
        raise BundleEvidenceRefusal(RELEASE_REFUSED) from None
    return {"release_id": bundle.release_id, "config_id": bundle.mechanics["config_id"]}


def validate_bundle(schema_rel: str, payload: object) -> None:
    try:
        _validate_local_schema(_LocalCapture(ROOT), schema_rel, payload)
    except RegistryConfigError:
        raise BundleEvidenceRefusal(f"{SCHEMA_REFUSED}:{schema_rel}") from None


# --- collection --------------------------------------------------------------------------------

def collect() -> list[tuple[str, str]]:
    """Every line of the record except the run fields, in record order."""

    lines: list[tuple[str, str]] = []
    digests = []
    for rel in TESTED_INPUTS:
        data = read_input(rel)
        digests.append(f"{rel} {sha256_hex(data)} {len(data)}")
        lines += [(f"input.{rel}.sha256", sha256_hex(data)), (f"input.{rel}.size_bytes", str(len(data)))]
    lines += [
        ("tested_inputs.count", str(len(TESTED_INPUTS))),
        ("tested_inputs.sha256", sha256_hex(("\n".join(digests) + "\n").encode("utf-8"))),
    ]
    release = head_release()
    lines += [("release.release_id", release["release_id"]), ("release.config_id", release["config_id"])]

    band_edges = read_json(BAND_EDGES_REL)
    thresholds = read_json(THRESHOLDS_REL)
    expected = {entry["category_id"]: entry["maxima"] for entry in thresholds["categories"]}
    edges_raw = read_input(BAND_EDGES_REL)
    edges_binding = {"path": BAND_EDGES_REL, "sha256": sha256_hex(edges_raw), "size_bytes": len(edges_raw)}
    carried: dict[str, dict[str, list[int]]] = {}
    order: list[str] = []
    for side, (bundle_rel, schema_rel, identity) in BUNDLES.items():
        payload = read_json(bundle_rel)
        # The closed consumer schema fixes the band keys, the catalog order and each set's shape.
        validate_bundle(schema_rel, payload)
        bands = payload["bands"]
        if payload["sources"]["band_edges"] != edges_binding:
            raise BundleEvidenceRefusal(f"{SOURCES_MISMATCH}:{side}")
        order = [entry["category_id"] for entry in bands["categories"]]
        carried[side] = {entry["category_id"]: entry["maxima"] for entry in bands["categories"]}
        lines += [
            (f"bundle.{side}.path", bundle_rel),
            (f"bundle.{side}.schema_path", schema_rel),
            (f"bundle.{side}.schema_identity", identity),
            (f"bundle.{side}.validated", "true"),
            (f"bundle.{side}.bands_keys", compact(sorted(bands))),
            (f"bundle.{side}.v1_global_keys_absent", compact(not any(key in bands for key in V1_GLOBAL_KEYS))),
            (f"bundle.{side}.sources_band_edges_equal", "true"),
        ]
    if read_json(BUNDLES["be"][0])["bands"] != band_edges:
        raise BundleEvidenceRefusal(f"{MAXIMA_MISMATCH}:be:{BAND_EDGES_REL}")
    if set(expected) != set(order):
        raise BundleEvidenceRefusal(f"{MAXIMA_MISMATCH}:{THRESHOLDS_REL}")
    for category in order:
        for side in ("be", "fe"):
            if carried[side][category] != expected[category]:
                raise BundleEvidenceRefusal(f"{MAXIMA_MISMATCH}:{side}:{category}")
        lines += [
            (f"category.{category}.thresholds_maxima", compact(expected[category])),
            (f"category.{category}.be_maxima", compact(carried["be"][category])),
            (f"category.{category}.fe_maxima", compact(carried["fe"][category])),
            (f"category.{category}.equal", "true"),
        ]

    lines.append(("command.regeneration", REGENERATION_COMMAND))
    for index, command in enumerate(CHECK_COMMANDS, start=1):
        code = run_check_command(command)
        if code:
            raise BundleEvidenceRefusal(f"{CHECK_COMMAND_FAILED}:{command[0]}")
        lines += [(f"command.check_{index}", "python " + " ".join(command)), (f"command.check_{index}.exit", str(code))]
    lines.append(("command.writer", f"python {GENERATOR_REL} --actor <run.actor>"))
    lines += [(f"limitation.{index}", text) for index, text in enumerate(LIMITATIONS, start=1)]
    lines.append(("status", "PASS"))
    return lines


def header(run: Mapping[str, str]) -> list[tuple[str, str]]:
    return [
        ("schema", SCHEMA),
        ("epic_id", "HDE-EPIC043"),
        ("task_id", "HDE-SEPA008"),
        ("subtask_ids", "HDE-SEPA008.1,HDE-SEPA008.2,HDE-SEPA008.3"),
        ("work_unit_id", "WU-PR-11"),
        *((key, run[key]) for key in RUN_FIELDS),
    ]


def render(lines: Sequence[tuple[str, str]]) -> bytes:
    keys = [key for key, _value in lines]
    if len(keys) != len(set(keys)) or keys[0] != "schema" or keys[-1] != "status":
        raise BundleEvidenceRefusal(RECORD_INVALID)
    for key, value in lines:
        if (not isinstance(value, str) or not key or ": " in key
                or any(char in f"{key}{value}" for char in "\r\n")):
            raise BundleEvidenceRefusal(RECORD_INVALID)
    return "".join(f"{key}: {value}\n" for key, value in lines).encode("utf-8")


def parse_record(data: bytes) -> list[tuple[str, str]]:
    text = data.decode("utf-8")
    if not text.endswith("\n"):
        raise ValueError("record without a final LF")
    parsed = []
    for line in text.split("\n")[:-1]:
        key, separator, value = line.partition(": ")
        if not separator:
            raise ValueError("record line without a key")
        parsed.append((key, value))
    return parsed


def run_fields_problem(run: Mapping[str, str]) -> str | None:
    if _TIME.fullmatch(run.get("run.time_utc", "")) is None:
        return "run.time_utc"
    if not valid_actor(run.get("run.actor", "")):
        return "run.actor"
    if _PYTHON.fullmatch(run.get("run.python", "")) is None:
        return "run.python"
    return None


def preconditions() -> None:
    try:
        ensure_determinism_env()
    except DeterminismEnvError:
        raise BundleEvidenceRefusal(RAILS_NOT_CLOSED) from None


def write(actor: str) -> bytes:
    if not valid_actor(actor):
        raise BundleEvidenceRefusal(INVALID_ACTOR)
    preconditions()
    run = {
        "run.time_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "run.actor": actor,
        "run.python": platform.python_version(),
    }
    record = render([*header(run), *collect()])
    out = out_path()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(record)
    return record


def check() -> None:
    preconditions()
    out = out_path()
    if not out.is_file():
        raise SystemExit(f"DRIFT:{OUT_REL}:missing")
    stored = out.read_bytes()
    try:
        parsed = parse_record(stored)
    except (UnicodeDecodeError, ValueError):
        raise SystemExit(f"DRIFT:{OUT_REL}:layout") from None
    run = {key: value for key, value in parsed if key in RUN_FIELDS}
    if [key for key, _ in parsed[5:8]] != list(RUN_FIELDS) or len(run) != len(RUN_FIELDS):
        raise SystemExit(f"DRIFT:{OUT_REL}:run")
    problem = run_fields_problem(run)
    if problem:
        raise SystemExit(f"DRIFT:{OUT_REL}:{problem}")
    expected = [*header(run), *collect()]
    for (want_key, want), (have_key, have) in zip(expected, parsed):
        if (want_key, want) != (have_key, have):
            raise SystemExit(f"DRIFT:{OUT_REL}:{want_key}")
    if render(expected) != stored:
        raise SystemExit(f"DRIFT:{OUT_REL}:layout")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--actor", help="the responsible actor of this run; writes the record")
    mode.add_argument("--check", action="store_true",
                      help="re-render the record and compare it with the stored bytes; write nothing")
    args = parser.parse_args(argv)
    try:
        if args.check:
            check()
            print("v2 bundle evidence check ok")
            return 0
        write(args.actor)
    except BundleEvidenceRefusal as exc:
        raise SystemExit(exc.code) from None
    print("v2 bundle evidence written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
