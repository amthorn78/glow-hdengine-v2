#!/usr/bin/env python3
"""Magic-10 v2 cut record (HDE-EPIC043 WU-PR-10; HDE-DIST008.2).

The writer records the v2 release cut as one governed record,
``audit/qa/hde-epic043/pr-10/v2_cut_record.txt``.  Every value is computed in
process at the head; no report file is an input:

* pass 2: ``score_distribution.run_cut()`` on the admitted release -- per
  category the score histogram, each cut's ``target_percent`` (the
  ``cut_target_percent`` it serves), ``maximum``, ``cumulative_count`` and
  ``deviation``, and the maxima; the cut rule is the tool's (HDE Math Spec
  5.3.7), never re-implemented here;
* the proof that the cut's thresholds, as canonical bytes
  (``sercanon(..., sort_keys=True)``), equal ``math/thresholds.json``;
* the realized mix per category against the target mix 30 / 35 / 25 / 10 from
  ``score_distribution.run_reference("target")``, with no category beyond the
  tolerance;
* the pass-1-equals-pass-2 proof: pass 1 is re-run over a provisional
  temporary root -- the head's release members with the two labelled non-canon
  fixtures of ``tests/fixtures/magic10_v2/`` placed at ``math/thresholds.json``
  and ``catalog/magic10_mechanics_v2.json``, and a manifest cut over it by
  ``scripts/cut_release_manifest.py`` in roster mode -- and its histograms and
  maxima must equal pass 2's;
* the corpus digest, which must be the tool's pinned corpus digest;
* the new ``release_id``, which must equal the SHA-256 of
  ``catalog/manifest.json``, and the prior ``release_id``, the SHA-256 of the
  prior release commit's manifest read from git, from which it must differ;
* the Q-02 values (version and ``built_at_utc``), which must equal the
  manifest's and the admission constants.

A failing check is a named refusal (exit status 1) and nothing is written.  The
record carries no wall-clock, git-state or host field, so a second run is byte
stable and ``--check`` re-renders it and compares the bytes, writing nothing.
It runs only under the closed determinism rails and from the repository root.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.config import registry_loader  # noqa: E402
from engine.config.registry_loader import (  # noqa: E402
    RegistryConfigError,
    _load_active_mechanics_bundle_from_root,
)
from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env  # noqa: E402
from engine.serializer.canon import sercanon  # noqa: E402
from scripts.cut_release_manifest import cut_manifest  # noqa: E402
from tools.score_distribution import score_distribution as tool  # noqa: E402

# Git history is read from the writer's own checkout, whatever input root is set.
REPOSITORY = ROOT
OUT_REL = "audit/qa/hde-epic043/pr-10/v2_cut_record.txt"
SCHEMA = "hde_epic043_v2_cut_record.v1"

MANIFEST_REL = "catalog/manifest.json"
THRESHOLDS_REL = "math/thresholds.json"
CONFIGURATION_REL = "catalog/magic10_mechanics_v2.json"
CORPUS_REL = "tools/score_distribution/reference_corpus_v1.json"
# Pass 1's provisional bytes: root path -> the labelled non-canon fixture placed there.
PASS1_FIXTURES = {
    THRESHOLDS_REL: "tests/fixtures/magic10_v2/thresholds_v2.fixture.json",
    CONFIGURATION_REL: "tests/fixtures/magic10_v2/magic10_mechanics_v2.fixture.json",
}
# The prior release: the manifest at `main` before the v2 cut (HDE-EPIC043 WU-PR-08).
PRIOR_COMMIT = "26158fcbc3c79eec311e9a802e5740076f7f57d9"
# Q-02 (HDE-EPIC043 Product Owner decision v1.0): the v2 release version and timestamp.
Q02_VERSION = "2.0.0"
Q02_BUILT_AT_UTC = "2026-11-19T05:48:28Z"

CUT_BASIS = (
    "tools/score_distribution/score_distribution.py run_cut (HDE Math Spec 5.3.7 maxima cut "
    "in exact integers) and run_reference target, in process at the head"
)
PASS1_ROOT_DESCRIPTION = (
    "temporary root: the head's release members with the labelled fixtures placed, manifest cut by "
    "scripts/cut_release_manifest.py over ADMITTED_RELEASE_ROSTER"
)

RAILS_NOT_CLOSED = "CUT_RECORD_RAILS_NOT_CLOSED"
TOOL_REFUSED = "CUT_RECORD_TOOL_REFUSED"
INPUT_UNREADABLE = "CUT_RECORD_INPUT_UNREADABLE"
PRIOR_RELEASE_UNAVAILABLE = "CUT_RECORD_PRIOR_RELEASE_UNAVAILABLE"
PASS1_ROOT_REFUSED = "CUT_RECORD_PASS1_ROOT_REFUSED"
RELEASE_ID_MISMATCH = "CUT_RECORD_RELEASE_ID_MISMATCH"
RELEASE_ID_UNCHANGED = "CUT_RECORD_RELEASE_ID_UNCHANGED"
Q02_VERSION_MISMATCH = "CUT_RECORD_Q02_VERSION_MISMATCH"
Q02_BUILT_AT_MISMATCH = "CUT_RECORD_Q02_BUILT_AT_MISMATCH"
REPORTS_INCONSISTENT = "CUT_RECORD_REPORTS_INCONSISTENT"
CORPUS_DIGEST_MISMATCH = "CUT_RECORD_CORPUS_DIGEST_MISMATCH"
THRESHOLDS_MISMATCH = "CUT_RECORD_THRESHOLDS_MISMATCH"
MIX_BEYOND_TOLERANCE = "CUT_RECORD_MIX_BEYOND_TOLERANCE"
PASS1_ROOT_INVALID = "CUT_RECORD_PASS1_ROOT_INVALID"
PASS1_MISMATCH = "CUT_RECORD_PASS1_MISMATCH"
RECORD_INVALID = "CUT_RECORD_RECORD_INVALID"


class CutRecordRefusal(RuntimeError):
    """A named refusal: no record is written."""

    def __init__(self, code: str) -> None:
        super().__init__(code)
        self.code = code


def out_path() -> Path:
    return ROOT / OUT_REL


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compact(value: object) -> str:
    """A list or mapping as one line of compact JSON, in its own order."""

    return json.dumps(value, separators=(",", ":"), ensure_ascii=True)


def flag(value: bool) -> str:
    return "true" if value else "false"


def child_env() -> dict[str, str]:
    """Closed-rails environment for the git child process."""

    environ = os.environ.copy()
    environ.update({"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"})
    ensure_determinism_env(environ=environ)
    return environ


def read_input(rel: str) -> bytes:
    try:
        return (ROOT / rel).read_bytes()
    except OSError:
        raise CutRecordRefusal(f"{INPUT_UNREADABLE}:{rel}") from None


def through_tool(call: Callable[[], object]) -> object:
    """Run one score-distribution step; its value-free refusal becomes a named refusal."""

    try:
        return call()
    except tool.Refusal as exc:
        raise CutRecordRefusal(f"{TOOL_REFUSED}:{exc.code}") from None


def identities(bundle) -> dict[str, list[object]]:
    return {identity.path: [identity.sha256, identity.size] for identity in bundle.source_identities}


# --- inputs ----------------------------------------------------------------------------------

def preconditions() -> None:
    try:
        ensure_determinism_env()
    except DeterminismEnvError:
        raise CutRecordRefusal(RAILS_NOT_CLOSED) from None
    through_tool(tool.require_repository_root)


def head_release() -> dict[str, object]:
    """The admitted release at the head, as the score-distribution tool admits it."""

    bundle = through_tool(tool.admit)
    manifest = read_input(MANIFEST_REL)
    return {
        "release_id": bundle.release_id,
        "manifest_sha256": sha256_hex(manifest),
        "version": bundle.manifest.version,
        "built_at_utc": bundle.manifest.built_at_utc,
        "config_id": bundle.mechanics["config_id"],
        "member_count": len(bundle.manifest.files),
        "admitted_version": registry_loader.ADMITTED_RELEASE_VERSION,
        "admitted_built_at_utc": registry_loader.ADMITTED_RELEASE_BUILT_AT_UTC,
        "identities": identities(bundle),
    }


def read_prior_manifest() -> bytes:
    proc = subprocess.run(
        ["git", "show", "--no-textconv", f"{PRIOR_COMMIT}:{MANIFEST_REL}"],
        cwd=REPOSITORY, env=child_env(), capture_output=True,
    )
    if proc.returncode or not proc.stdout:
        raise CutRecordRefusal(PRIOR_RELEASE_UNAVAILABLE)
    return proc.stdout


def prior_release() -> dict[str, object]:
    return {"commit": PRIOR_COMMIT, "release_id": sha256_hex(read_prior_manifest())}


def pass2_cut() -> dict:
    return through_tool(tool.run_cut)


def target_mix() -> dict:
    return through_tool(lambda: tool.run_reference("target"))


def build_provisional_root(directory: Path) -> Path:
    """The head's release members with the fixtures placed and a manifest cut over them."""

    root = directory / "provisional-pass1-root"
    for rel in registry_loader.ADMITTED_RELEASE_ROSTER:
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(read_input(PASS1_FIXTURES.get(rel, rel)))
    manifest = root / MANIFEST_REL
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_bytes(read_input(MANIFEST_REL))
    try:
        cut_manifest(
            manifest,
            version=registry_loader.ADMITTED_RELEASE_VERSION,
            built_at_utc=registry_loader.ADMITTED_RELEASE_BUILT_AT_UTC,
            roster=registry_loader.ADMITTED_RELEASE_ROSTER,
        )
    except (OSError, UnicodeError, ValueError) as exc:
        raise CutRecordRefusal(f"{PASS1_ROOT_REFUSED}:{exc}") from None
    return root


def pass1_cut() -> dict[str, object]:
    """Pass 1 reproduced: the cut over the provisional root, never written anywhere."""

    fixtures = {}
    for rel, source in PASS1_FIXTURES.items():
        data = read_input(source)
        fixtures[rel] = [sha256_hex(data), len(data)]
    with tempfile.TemporaryDirectory(prefix="hde-epic043-cut-record-pass1-") as scratch:
        root = build_provisional_root(Path(scratch))
        try:
            bundle = _load_active_mechanics_bundle_from_root(root)
        except RegistryConfigError as exc:
            raise CutRecordRefusal(f"{PASS1_ROOT_REFUSED}:{exc.code}") from None
        digest, people, pairs = through_tool(tool.load_corpus)
        parties = [through_tool(lambda person=person: tool.reference_party(person)) for person in people]
        distribution = through_tool(lambda: tool.score_pairs(bundle, parties, pairs))
        population = {"corpus_sha256": digest, "people": len(people), "pairs": len(pairs), "synthetic": True}
        report = through_tool(lambda: tool.cut_report(bundle, population, distribution))
    return {"report": report, "release_id": bundle.release_id, "identities": identities(bundle),
            "fixtures": fixtures}


def collect() -> dict[str, object]:
    preconditions()
    thresholds = read_input(THRESHOLDS_REL)
    return {
        "head": head_release(),
        "prior": prior_release(),
        "thresholds": {"sha256": sha256_hex(thresholds), "size": len(thresholds), "bytes": thresholds},
        "configuration": {"sha256": sha256_hex(read_input(CONFIGURATION_REL))},
        "cut": pass2_cut(),
        "mix": target_mix(),
        "pass1": pass1_cut(),
    }


# --- checks ----------------------------------------------------------------------------------

def _categories(report: Mapping[str, object]) -> list[str]:
    return [row["category_id"] for row in report["categories"]]


def _cut_rows(report: Mapping[str, object]) -> list[list[object]]:
    return [[row["category_id"], row["results"], list(row["score_histogram"]), [dict(c) for c in row["cuts"]],
             list(row["maxima"])] for row in report["categories"]]


def _histograms_sha256(report: Mapping[str, object]) -> str:
    return sha256_hex(sercanon([{"category_id": row["category_id"], "score_histogram": list(row["score_histogram"])}
                                for row in report["categories"]], sort_keys=True))


def _thresholds_bytes(report: Mapping[str, object]) -> bytes:
    return sercanon(report["thresholds"], sort_keys=True)


def check_results(facts: Mapping[str, object]) -> list[tuple[str, str, bool]]:
    """Every check as (record key, refusal code, passed), in record order."""

    head, prior, cut, mix, pass1 = facts["head"], facts["prior"], facts["cut"], facts["mix"], facts["pass1"]
    pass1_report = pass1["report"]
    release = {"release_id": head["release_id"], "version": head["version"], "config_id": head["config_id"]}
    populations = [cut["population"], mix["population"], pass1_report["population"]]
    # Pass 1's members are the head's, except the two placed fixtures.
    expected_identities = {rel: list(value) for rel, value in head["identities"].items()}
    expected_identities.update({rel: list(value) for rel, value in pass1["fixtures"].items()})
    pass1_identities = {rel: list(value) for rel, value in pass1["identities"].items()}
    return [
        ("release_id_equals_manifest_digest", RELEASE_ID_MISMATCH,
         head["release_id"] == head["manifest_sha256"]),
        ("release_id_differs_from_prior", RELEASE_ID_UNCHANGED, head["release_id"] != prior["release_id"]),
        ("q02_version_equal", Q02_VERSION_MISMATCH,
         Q02_VERSION == head["version"] == head["admitted_version"]),
        ("q02_built_at_utc_equal", Q02_BUILT_AT_MISMATCH,
         Q02_BUILT_AT_UTC == head["built_at_utc"] == head["admitted_built_at_utc"]),
        ("reports_bind_the_head_release", REPORTS_INCONSISTENT,
         dict(cut["release"]) == release == dict(mix["release"])
         and cut.get("schema") == tool.CUT_SCHEMA and mix.get("schema") == tool.REPORT_SCHEMA
         and mix["comparison"].get("against") == "target"
         and list(mix["comparison"]["per_category"]) == _categories(cut)),
        ("corpus_digest_pinned", CORPUS_DIGEST_MISMATCH,
         all(dict(population) == dict(populations[0]) for population in populations)
         and populations[0].get("corpus_sha256") == tool.REFERENCE_CORPUS_SHA256),
        ("thresholds_equal_committed", THRESHOLDS_MISMATCH, _thresholds_bytes(cut) == facts["thresholds"]["bytes"]),
        ("categories_within_tolerance", MIX_BEYOND_TOLERANCE,
         list(mix["comparison"]["categories_beyond_tolerance"]) == []),
        ("pass1_root_provisional", PASS1_ROOT_INVALID,
         pass1_identities == expected_identities and pass1["release_id"] != head["release_id"]
         and dict(pass1_report["release"]).get("release_id") == pass1["release_id"]),
        ("pass1_equals_pass2", PASS1_MISMATCH,
         _cut_rows(pass1_report) == _cut_rows(cut) and _thresholds_bytes(pass1_report) == _thresholds_bytes(cut)),
    ]


def failed_checks(facts: Mapping[str, object]) -> list[str]:
    return [code for _key, code, passed in check_results(facts) if not passed]


# --- the record ------------------------------------------------------------------------------

def record_lines(facts: Mapping[str, object]) -> list[tuple[str, str]]:
    head, prior, cut, mix, pass1 = facts["head"], facts["prior"], facts["cut"], facts["mix"], facts["pass1"]
    pass1_report = pass1["report"]
    population = cut["population"]
    lines: list[tuple[str, str]] = [
        ("schema", SCHEMA),
        ("epic_id", "HDE-EPIC043"),
        ("task_id", "HDE-DIST008"),
        ("subtask_id", "HDE-DIST008.2"),
        ("work_unit_id", "WU-PR-10"),
        ("cut_basis", CUT_BASIS),
        ("release.release_id", head["release_id"]),
        ("release.manifest_path", MANIFEST_REL),
        ("release.manifest_sha256", head["manifest_sha256"]),
        ("release.version", head["version"]),
        ("release.built_at_utc", head["built_at_utc"]),
        ("release.config_id", head["config_id"]),
        ("release.member_count", str(head["member_count"])),
        ("release.prior_commit", prior["commit"]),
        ("release.prior_release_id", prior["release_id"]),
        ("q02.version", Q02_VERSION),
        ("q02.built_at_utc", Q02_BUILT_AT_UTC),
        ("q02.admitted_release_version", head["admitted_version"]),
        ("q02.admitted_release_built_at_utc", head["admitted_built_at_utc"]),
        ("corpus.path", CORPUS_REL),
        ("corpus.sha256", str(population.get("corpus_sha256"))),
        ("corpus.pinned_sha256", tool.REFERENCE_CORPUS_SHA256),
        ("corpus.people", str(population.get("people"))),
        ("corpus.pairs", str(population.get("pairs"))),
        ("thresholds.path", THRESHOLDS_REL),
        ("thresholds.sha256", facts["thresholds"]["sha256"]),
        ("thresholds.size_bytes", str(facts["thresholds"]["size"])),
        ("configuration.path", CONFIGURATION_REL),
        ("configuration.sha256", facts["configuration"]["sha256"]),
        ("cut.schema", str(cut.get("schema"))),
        ("cut.target_mix_percent", compact(dict(cut["target_mix_percent"]))),
        ("cut.cut_target_percent", compact(list(cut["cut_target_percent"]))),
        ("cut.category_order", compact(_categories(cut))),
    ]
    for row in cut["categories"]:
        prefix = f"cut.{row['category_id']}"
        lines += [(f"{prefix}.results", str(row["results"])),
                  (f"{prefix}.score_histogram", compact(list(row["score_histogram"])))]
        for index, rule in enumerate(row["cuts"], start=1):
            lines += [(f"{prefix}.cut.{index}.{key}", str(rule[key]))
                      for key in ("target_percent", "maximum", "cumulative_count", "deviation")]
        lines.append((f"{prefix}.maxima", compact(list(row["maxima"]))))
    lines += [
        ("cut.score_histograms_sha256", _histograms_sha256(cut)),
        ("cut.thresholds_sha256", sha256_hex(_thresholds_bytes(cut))),
    ]
    comparison = mix["comparison"]
    lines += [
        ("mix.schema", str(mix.get("schema"))),
        ("mix.against", str(comparison.get("against"))),
        ("mix.target_mix_percent", compact(dict(comparison["target_mix_percent"]))),
        ("mix.tolerance_points", str(comparison["tolerance_points"])),
    ]
    for band in tool.BANDS:
        row = comparison["overall"][band]
        lines += [(f"mix.overall.{band}.share_points", row["share_points"]),
                  (f"mix.overall.{band}.difference_points", row["difference_points"])]
    for category, bands in comparison["per_category"].items():
        for band in tool.BANDS:
            row = bands[band]
            lines += [(f"mix.{category}.{band}.share_points", row["share_points"]),
                      (f"mix.{category}.{band}.difference_points", row["difference_points"]),
                      (f"mix.{category}.{band}.beyond_tolerance", flag(row["beyond_tolerance"]))]
    lines.append(("mix.categories_beyond_tolerance", compact(list(comparison["categories_beyond_tolerance"]))))
    lines += [
        ("pass1.root", PASS1_ROOT_DESCRIPTION),
        ("pass1.thresholds_source", PASS1_FIXTURES[THRESHOLDS_REL]),
        ("pass1.thresholds_source_sha256", pass1["fixtures"][THRESHOLDS_REL][0]),
        ("pass1.configuration_source", PASS1_FIXTURES[CONFIGURATION_REL]),
        ("pass1.configuration_source_sha256", pass1["fixtures"][CONFIGURATION_REL][0]),
        ("pass1.release_id", pass1["release_id"]),
        ("pass1.corpus_sha256", str(pass1_report["population"].get("corpus_sha256"))),
        ("pass1.score_histograms_sha256", _histograms_sha256(pass1_report)),
        ("pass1.thresholds_sha256", sha256_hex(_thresholds_bytes(pass1_report))),
    ]
    results = check_results(facts)
    lines += [(f"check.{key}", flag(passed)) for key, _code, passed in results]
    lines.append(("status", "PASS" if all(passed for _key, _code, passed in results) else "FAIL"))
    return lines


def render(lines: Sequence[tuple[str, str]]) -> bytes:
    keys = [key for key, _value in lines]
    if len(keys) != len(set(keys)) or keys[0] != "schema" or keys[-1] != "status":
        raise CutRecordRefusal(RECORD_INVALID)
    for key, value in lines:
        if (not isinstance(value, str) or not key or ": " in key
                or any(char in f"{key}{value}" for char in "\r\n")):
            raise CutRecordRefusal(RECORD_INVALID)
    return "".join(f"{key}: {value}\n" for key, value in lines).encode("utf-8")


def build() -> tuple[list[str], bytes]:
    """Collect every input at the head and return (failing refusal codes, record bytes)."""

    facts = collect()
    return failed_checks(facts), render(record_lines(facts))


def first_difference(stored: bytes, expected: bytes) -> str:
    try:
        have = stored.decode("utf-8").split("\n")
    except UnicodeDecodeError:
        return "layout"
    for have_line, want_line in zip(have, expected.decode("utf-8").split("\n")):
        if have_line != want_line:
            return want_line.partition(": ")[0] or "layout"
    return "layout"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    parser.add_argument("--check", action="store_true",
                        help="re-render the record and compare it with the stored bytes; write nothing")
    args = parser.parse_args(argv)
    try:
        failing, record = build()
    except CutRecordRefusal as exc:
        raise SystemExit(exc.code) from None
    if failing:
        for code in failing[1:]:
            print(code, file=sys.stderr)
        raise SystemExit(failing[0])
    out = out_path()
    if args.check:
        if not out.is_file():
            raise SystemExit(f"DRIFT:{OUT_REL}:missing")
        stored = out.read_bytes()
        if stored != record:
            raise SystemExit(f"DRIFT:{OUT_REL}:{first_difference(stored, record)}")
        print("v2 cut record check ok")
        return 0
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(record)
    print("v2 cut record written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
