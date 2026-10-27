"""Build the 2026-10-27 R1 successor source matrix, successor oracle and successor runtime map
(MODIFICATION-20261027-gcfpe-backlog-open-items, PART-13, DN-2 (b)).

usage: PYTHONDONTWRITEBYTECODE=1 python3 build_r1_successor_20261027.py <skills-root> <repo-root> [--out-dir DIR]
           [--expect-decision-record <gcfpe.decision-record.md>]
       PYTHONDONTWRITEBYTECODE=1 python3 build_r1_successor_20261027.py selftest <skills-root> <repo-root> <scratch>

Modelled on docs/ephemeral/modifications/evidence/build_r1_successor.py (D23 Amendment 1). The successor is
cumulative over the historical oracle: it carries the three 2026-09-23 successor rows unchanged (GCF-14, GCF-17,
GCF-17.LINEAGE) and adds the close-mutation-set stage between GCF-24 and GCF-25: GCF-24 and GCF-25 change, and
GCF-24.CLOSE is inserted after GCF-24. Reads the historical oracle and map and the 2026-09-23 successor, confirms
their digests, and writes (with --out-dir, every file goes into DIR instead, for a dry run):
  <skills-root>/flowmaster-validate/references/r1-successor-source-20261027.md
  <repo-root>/docs/prompt_ecosystem_management/r1-successor-source-20261027.md            (byte-identical copy)
  <skills-root>/flowmaster-validate/references/glow-hde-canonical-change-flow-r1-20261027.json
  <skills-root>/change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map-20261027.json
Never edits the historical or 2026-09-23 files. Prints every digest it writes. Every check runs before the first
write: a failed check writes nothing.

--expect-decision-record compares the build with the decision record's "### Successor, 2026-10-27" section under
D23 (the three row digests, and the matrix, oracle and runtime-map digests and byte counts). A mismatch is reported
(decision_record_match false, exit 1) and nothing is patched. `selftest` copies the inputs into <scratch> and
shows that each check fires on its injected failure. Adapted from W5's dry-run script (W5 RE-1) for
MODIFICATION-20261027-gcfpe-backlog-open-items PLAN (A2).
"""
import copy
import re
import shutil
import hashlib
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True

HIST_ORACLE_SHA256 = "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e"
HIST_MAP_SHA256 = "5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e"
PREV_ORACLE_SHA256 = "ede635b14aa2f57c8c99e948a012e88d843338f62bc2b55349d511f52f59fb52"
PREV_MAP_SHA256 = "aa6ed8e34363b77e08e8467d9f31b4dc795c2c9fa2c2c3c7ed1cea6cf4202ee4"
OLD_PROFILE = "GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1"
NEW_PROFILE = "GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20261027_1"
OLD_COVERAGE_TOKEN = "R1_ROW_COVERAGE: 46/46"
NEW_COVERAGE_TOKEN = "R1_ROW_COVERAGE: 47/47"
CARRIED_ROWS = ("GCF-14", "GCF-17", "GCF-17.LINEAGE")          # 2026-09-23 successor rows, unchanged
NEW_ROW_ID = "GCF-24.CLOSE"
SUCCESSOR_ROWS = ("GCF-14", "GCF-17", "GCF-17.LINEAGE", "GCF-24", "GCF-24.CLOSE", "GCF-25")
SUCCESSOR_AUTHORITY = ("D23-D, D23-F; Product Owner 2026-09-23. D23 successor of 2026-10-27, the close-mutation-set "
                       "stage (PF06 §3.5.1; DN-2 of MODIFICATION-20261027-gcfpe-backlog-open-items); Product Owner "
                       "2026-10-27")
CONTENT_FIELDS = ("id", "partition", "name", "change_class", "actor", "session", "consumes",
                  "produces", "next", "approval_contract", "failure_stop_condition")
HEADER = ("# R1 successor source matrix — 2026-10-27\n\n"
          "Authority: D23-D, D23-F; Product Owner 2026-09-23. D23 successor of 2026-10-27 (PF06 §3.5.1; DN-2); "
          "Product Owner 2026-10-27. One block per row that differs from the historical R1 oracle; "
          "a row the historical oracle lacks supersedes null.\n")

# Changed fields of existing rows (final values), each with the historical value it replaces, as a guard.
CHANGES = {
    "GCF-24": {
        "next": (["GCF-24.CLOSE"], ["GCF-25"]),
    },
    "GCF-25": {
        "consumes": (["approved_specification_ia_intake", "approved_change_wide_implementation_plan",
                      "complete_work_unit_results", "final_qa_report", "qa_rca", "close_mutation_set",
                      "close_mutation_set_result", "outstanding_blocker_ledger"],
                     ["approved_specification_ia_intake", "approved_change_wide_implementation_plan",
                      "complete_work_unit_results", "final_qa_report", "qa_rca", "outstanding_blocker_ledger"]),
        "next": (["GCF-24.CLOSE", "GCF-26", "REENTER_EXACT_OWNER"], ["GCF-26", "REENTER_EXACT_OWNER"]),
        "failure_stop_condition": (
            "STOP_CLOSURE_EVIDENCE_INCOMPLETE or CLOSE_DENIED_WITH_EXACT_OWNER_AND_REENTRY; recovery owner: "
            "Isis/named stage owner, and the close-mutation-set stage (GCF-24.CLOSE) when the return work is a "
            "missing, incomplete or defective close mutation set, a close-tooling defect included.",
            "STOP_CLOSURE_EVIDENCE_INCOMPLETE or CLOSE_DENIED_WITH_EXACT_OWNER_AND_REENTRY; recovery owner: "
            "Isis/named stage owner."),
    },
}
# The inserted row (PF06 §3.5.1 "Close-mutation-set stage"; PF27 §3B; PF19 §3.1.3).
NEW_ROW = {
    "id": NEW_ROW_ID,
    "partition": "MATERIAL_BRANCH_LOOP_OR_UTILITY",
    "name": "Close-mutation-set stage prepares and publishes the close mutation set",
    "change_class": "Closure prerequisite (PR work unit)",
    "actor": "Close Implementer (CL-05); the Product Owner invokes the stage and alone merges the close pull request",
    "session": ("A standalone top-level session that the Product Owner starts with the stage prompt and the change ID; "
                "it needs no handoff to start, resolves its inputs from the change's records, and is never a "
                "subagent of another session."),
    "consumes": ["change_identity", "final_qa_report", "qa_rca", "isis_closure_decision", "current_repository",
                 "applicable_canon"],
    "produces": ["close_mutation_set", "close_mutation_set_result"],
    "next": ["GCF-25"],
    "approval_contract": ("The Product Owner's invocation of the stage for a change authorizes that change's close "
                          "mutation set and any close-tooling repair it needs, and is the Proceed for both. The "
                          "closure authority judges its result at the closure decision; the Product Owner alone "
                          "merges. It never reopens implementation, QA or the closure decision."),
    "failure_stop_condition": ("STOP_CLOSE_INTAKE_FAILED, STOP_APPROVED_QA_EVIDENCE_WOULD_CHANGE, "
                               "STOP_DEFECT_OUTSIDE_CLOSE_TOOLING, STOP_CLOSE_RUN_FAMILY_NOT_ADMITTED or "
                               "STOP_CANON_CONFLICT; recovery owner: the Close Implementer for close-tooling repair, "
                               "with no escalation, rescope or PR-chain stage; otherwise the Product Owner."),
}


def ser(obj) -> bytes:
    return (json.dumps(obj, indent=2, sort_keys=False, ensure_ascii=False) + "\n").encode("utf-8")


def row_digest(row) -> str:
    content = {k: row[k] for k in CONTENT_FIELDS}
    return hashlib.sha256(
        json.dumps(content, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def project_map(oracle):
    return {key: oracle[key] for key in ("profile_id", "authority", "coverage", "runtime_rows")}


DR_HEADING = "### Successor, 2026-10-27 \u2014 the R1 oracle gains the close-mutation-set stage (DN-2)"


def decision_record_digests(path: Path) -> dict:
    """The digests and byte counts the decision record's D23 successor of 2026-10-27 states."""
    text = path.read_text(encoding="utf-8")
    assert text.count(DR_HEADING) == 1, "decision record: the 2026-10-27 successor heading must occur exactly once"
    sec = text[text.index(DR_HEADING) + len(DR_HEADING):]
    ends = [i for i in (sec.find("\n### "), sec.find("\n## ")) if i >= 0]
    sec = sec[:min(ends)] if ends else sec
    line = next(l for l in sec.split("\n") if l.startswith("- **Row digests"))
    out = {}
    for rid in ("GCF-24.CLOSE", "GCF-24", "GCF-25"):
        m = re.search(re.escape(rid) + r" `([0-9a-f]{64})`", line)
        out["row:" + rid] = m.group(1) if m else None
    for kind, label in (("matrix", "Matrix"), ("oracle", "oracle"), ("runtime_map", "runtime map")):
        m = re.search(label + r" `([0-9a-f]{64})` \(([0-9,]+) B\)", line)
        out[kind] = {"sha256": m.group(1), "bytes": int(m.group(2).replace(",", ""))} if m else None
    return out


def build(skills: Path, repo: Path) -> tuple[dict, dict, dict]:
    """(payloads, targets, report); raises AssertionError on any failed check; writes nothing."""

    fv, cf = skills / "flowmaster-validate/references", skills / "change-flow/references"
    hist_bytes = (fv / "glow-hde-canonical-change-flow-r1.json").read_bytes()
    hist_map_bytes = (cf / "glow-hde-canonical-change-flow-r1-runtime-map.json").read_bytes()
    prev_bytes = (fv / "glow-hde-canonical-change-flow-r1-20260923.json").read_bytes()
    prev_map_bytes = (cf / "glow-hde-canonical-change-flow-r1-runtime-map-20260923.json").read_bytes()
    assert hashlib.sha256(hist_bytes).hexdigest() == HIST_ORACLE_SHA256, "historical oracle digest"
    assert hashlib.sha256(hist_map_bytes).hexdigest() == HIST_MAP_SHA256, "historical map digest"
    assert hashlib.sha256(prev_bytes).hexdigest() == PREV_ORACLE_SHA256, "2026-09-23 oracle digest"
    assert hashlib.sha256(prev_map_bytes).hexdigest() == PREV_MAP_SHA256, "2026-09-23 map digest"
    hist, prev = json.loads(hist_bytes), json.loads(prev_bytes)
    assert ser(prev) == prev_bytes and ser(project_map(prev)) == prev_map_bytes, "recipe"

    succ = copy.deepcopy(hist)
    succ["profile_id"] = NEW_PROFILE
    tokens = succ["required_global_tokens"]
    assert tokens.count(OLD_PROFILE) == 1 and tokens.count(OLD_COVERAGE_TOKEN) == 1
    tokens[tokens.index(OLD_PROFILE)] = NEW_PROFILE
    tokens[tokens.index(OLD_COVERAGE_TOKEN)] = NEW_COVERAGE_TOKEN
    prev_rows = {r["id"]: r for r in prev["runtime_rows"]}
    hist_rows = {r["id"]: r for r in hist["runtime_rows"]}
    rows = succ["runtime_rows"]
    for i, r in enumerate(rows):  # the three 2026-09-23 rows, byte-for-byte as approved then
        if r["id"] in CARRIED_ROWS:
            rows[i] = copy.deepcopy(prev_rows[r["id"]])
    by_id = {r["id"]: r for r in rows}
    for rid, fields in CHANGES.items():
        for key, (new, old) in fields.items():
            assert by_id[rid][key] == old, (rid, key, by_id[rid][key])
            by_id[rid][key] = new
    new_row = dict(NEW_ROW)
    new_row["source_row_sha256"] = ""
    rows.insert([r["id"] for r in rows].index("GCF-24") + 1, new_row)
    succ["coverage"] = {"rows": 47, "core_rows": 26, "material_rows": 21}
    order = [r["id"] for r in rows if r["id"] in SUCCESSOR_ROWS]
    assert order == list(SUCCESSOR_ROWS), order

    blocks = []
    for r in rows:
        if r["id"] not in SUCCESSOR_ROWS:
            continue
        assert list(r)[:11] == list(CONTENT_FIELDS) and list(r)[11] == "source_row_sha256"
        r["source_row_sha256"] = row_digest(r)
        if r["id"] in CARRIED_ROWS:
            assert r["source_row_sha256"] == prev_rows[r["id"]]["source_row_sha256"]
        block = {k: r[k] for k in CONTENT_FIELDS}
        block["supersedes_source_row_sha256"] = hist_rows[r["id"]]["source_row_sha256"] if r["id"] in hist_rows else None
        blocks.append("```json\n" + json.dumps(block, indent=2, ensure_ascii=False) + "\n```\n"
                      + "source_row_sha256: " + r["source_row_sha256"] + "\n")
    matrix = (HEADER + "\n".join(blocks)).encode("utf-8")
    assert matrix.endswith(b"\n") and not matrix.endswith(b"\n\n")
    matrix_sha = hashlib.sha256(matrix).hexdigest()

    authority = succ["authority"]
    assert list(authority) == ["r1_source_manifest_library_id", "r1_contract_matrix_library_id",
                               "r1_contract_matrix_sha256", "r1_frozen_snapshot_sha256", "r1_verdict"]
    authority["successor_source_matrix_sha256"] = matrix_sha
    authority["successor_rows"] = list(order)
    authority["successor_authority"] = SUCCESSOR_AUTHORITY
    oracle = ser(succ)
    runtime_map = ser(project_map(succ))

    targets = {
        "matrix": [fv / "r1-successor-source-20261027.md",
                   repo / "docs/prompt_ecosystem_management/r1-successor-source-20261027.md"],
        "oracle": [fv / "glow-hde-canonical-change-flow-r1-20261027.json"],
        "map": [cf / "glow-hde-canonical-change-flow-r1-runtime-map-20261027.json"],
    }
    payload = {"matrix": matrix, "oracle": oracle, "map": runtime_map}

    # Self-checks: 47 rows, 26 core, the historical order with one insertion, only declared differences.
    assert len(rows) == 47 and sum(r["partition"] == "CORE" for r in rows) == 26
    assert [r["id"] for r in rows if r["id"] != NEW_ROW_ID] == [r["id"] for r in hist["runtime_rows"]]
    diffs_vs_prev = sorted((r["id"], k) for r in rows if r["id"] in prev_rows
                           for k in r if r[k] != prev_rows[r["id"]][k])
    top_vs_prev = sorted(k for k in succ if succ[k] != prev[k])
    assert top_vs_prev == ["authority", "coverage", "profile_id", "required_global_tokens", "runtime_rows"], top_vs_prev
    for p, sha in ((fv / "glow-hde-canonical-change-flow-r1.json", HIST_ORACLE_SHA256),
                   (fv / "glow-hde-canonical-change-flow-r1-20260923.json", PREV_ORACLE_SHA256)):
        assert hashlib.sha256(p.read_bytes()).hexdigest() == sha
    report = {
        "matrix": {"bytes": len(matrix), "sha256": matrix_sha},
        "oracle": {"bytes": len(oracle), "sha256": hashlib.sha256(oracle).hexdigest()},
        "runtime_map": {"bytes": len(runtime_map), "sha256": hashlib.sha256(runtime_map).hexdigest()},
        "row_digests": {r["id"]: r["source_row_sha256"] for r in rows if r["id"] in SUCCESSOR_ROWS},
        "rows": len(rows), "core_rows": sum(r["partition"] == "CORE" for r in rows),
        "material_rows": sum(r["partition"] != "CORE" for r in rows),
        "changed_row_fields_vs_20260923": diffs_vs_prev,
        "changed_top_level_keys_vs_20260923": top_vs_prev,
    }
    return payload, targets, report


def compare_dr(report: dict, dr: dict) -> dict:
    got = {"row:" + k: v for k, v in report["row_digests"].items() if k in ("GCF-24", "GCF-24.CLOSE", "GCF-25")}
    for kind in ("matrix", "oracle", "runtime_map"):
        got[kind] = report[kind]
    return {k: {"decision_record": dr.get(k), "built": got[k]} for k in got if dr.get(k) != got[k]}


def run(skills: Path, repo: Path, out_dir, dr_path) -> int:
    payload, targets, report = build(skills, repo)
    if dr_path is not None:
        mism = compare_dr(report, decision_record_digests(Path(dr_path)))
        report["decision_record_match"] = not mism
        report["decision_record_mismatches"] = mism
    written = []
    for kind, paths in targets.items():
        for p in paths:
            if out_dir is not None:
                p = Path(out_dir) / (kind + "-" + p.name)
            p.write_bytes(payload[kind])
            written.append(str(p))
    report["written"] = written
    report["build_ok"] = True
    print(json.dumps(report, indent=2))
    return 0 if report.get("decision_record_match", True) else 1


def selftest(skills: Path, repo: Path, scratch: Path) -> int:
    """Each check fires on its injected failure, on copies of the inputs under <scratch>."""
    work = scratch / "r1-selftest"
    if work.exists():
        shutil.rmtree(work)
    names = {"flowmaster-validate/references": ("glow-hde-canonical-change-flow-r1.json",
                                                "glow-hde-canonical-change-flow-r1-20260923.json"),
             "change-flow/references": ("glow-hde-canonical-change-flow-r1-runtime-map.json",
                                        "glow-hde-canonical-change-flow-r1-runtime-map-20260923.json")}

    def fresh(tag: str) -> Path:
        root = work / tag
        for d, files in names.items():
            (root / d).mkdir(parents=True)
            for f in files:
                shutil.copyfile(skills / d / f, root / d / f)
        return root

    def fails(fn) -> bool:
        try:
            fn()
        except AssertionError:
            return True
        return False

    rows = {}
    clean = fresh("clean")
    payload, _, report = build(clean, repo)
    rows["clean_build_passes"] = report["rows"] == 47
    dr = repo / "docs/prompt_ecosystem_management/gcfpe.decision-record.md"
    rows["decision_record_compare_runs"] = isinstance(compare_dr(report, decision_record_digests(dr)), dict)
    for tag, rel in (("hist", "flowmaster-validate/references/glow-hde-canonical-change-flow-r1.json"),
                     ("prev", "flowmaster-validate/references/glow-hde-canonical-change-flow-r1-20260923.json"),
                     ("hmap", "change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map.json"),
                     ("pmap", "change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json")):
        root = fresh(tag)
        p = root / rel
        p.write_bytes(p.read_bytes().replace(b"Kronos", b"Kronoz", 1))
        rows[f"rejects_changed_{tag}_input"] = fails(lambda: build(root, repo))
    saved = copy.deepcopy(CHANGES)
    try:
        CHANGES["GCF-24"]["next"] = (["GCF-24.CLOSE"], ["GCF-99"])
        rows["rejects_guarded_old_value_mismatch"] = fails(lambda: build(clean, repo))
    finally:
        CHANGES.clear(); CHANGES.update(saved)
    fake = dict(report)
    fake["row_digests"] = dict(report["row_digests"], **{"GCF-24": "0" * 64})
    rows["decision_record_mismatch_reported"] = "row:GCF-24" in compare_dr(fake, decision_record_digests(dr))
    fake_dr = work / "dr.md"
    fake_dr.write_text("no heading\n", encoding="utf-8")
    rows["rejects_decision_record_without_heading"] = fails(lambda: decision_record_digests(fake_dr))
    ok = all(rows.values())
    shutil.rmtree(work)
    print(json.dumps({"mode": "selftest", "rows": rows, "selftest_ok": ok}, indent=2))
    return 0 if ok else 1


def main() -> int:
    a = sys.argv[1:]
    if a and a[0] == "selftest":
        return selftest(Path(a[1]), Path(a[2]), Path(a[3]))
    if len(a) < 2:
        raise SystemExit(__doc__)
    out_dir = a[a.index("--out-dir") + 1] if "--out-dir" in a else None
    dr = a[a.index("--expect-decision-record") + 1] if "--expect-decision-record" in a else None
    return run(Path(a[0]), Path(a[1]), out_dir, dr)


if __name__ == "__main__":
    raise SystemExit(main())
