"""Build the R1 successor source matrix, successor oracle and successor runtime map (spec v2 §5).

usage: PYTHONDONTWRITEBYTECODE=1 python3 build_r1_successor.py <skills-root> <repo-root>

Reads the historical oracle and runtime map from <skills-root>, confirms their digests, and writes:
  <skills-root>/flowmaster-validate/references/r1-successor-source-20260923.md          (matrix, §5.4)
  <repo-root>/docs/prompt_ecosystem_management/r1-successor-source-20260923.md           (byte-identical copy, §12 OQ-6)
  <skills-root>/flowmaster-validate/references/glow-hde-canonical-change-flow-r1-20260923.json      (oracle, §5.3/§5.5)
  <skills-root>/change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json (map, §5.6)
Pin order (§5.11 steps 1-3): matrix first, then the oracle carrying the matrix digest, then the map.
Never edits the historical files. Prints every digest it writes.
"""
import copy
import hashlib
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True

HIST_ORACLE_SHA256 = "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e"
HIST_MAP_SHA256 = "5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e"
OLD_PROFILE = "GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1"
NEW_PROFILE = "GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260923_1"
SUCCESSOR_ROWS = ("GCF-14", "GCF-17", "GCF-17.LINEAGE")
SUCCESSOR_AUTHORITY = "D23-D, D23-F; Product Owner 2026-09-23"
CONTENT_FIELDS = ("id", "partition", "name", "change_class", "actor", "session", "consumes",
                  "produces", "next", "approval_contract", "failure_stop_condition")
HEADER = ("# R1 successor source matrix — 2026-09-23\n\n"
          "Authority: D23-D, D23-F; Product Owner 2026-09-23. One block per changed row.\n")

# §5.3 changed row fields (final values), with the values they replace for a guard.
CHANGES = {
    "GCF-17": {
        "name": ("Dedicated PR session implements and creates PR lineage; PR-35 continues it in its own session", None),
        "actor": ("Dedicated PR session (PR-30 phase) and dedicated PR-35 session (PR-35 phase)", None),
        "session": ("PR-30: exactly the GCF-14 planning session, continuing for implementation of its one authorized "
                    "work unit. PR-35: its own dedicated top-level session for the same work unit and pull request, "
                    "entered from PR-30's handoff; never a subagent of another session.", None),
        "failure_stop_condition": (
            "STOP_SESSION_MISMATCH, STOP_SCOPE_CHANGE, STOP_REMOTE_INTEGRITY_DRIFT, or STOP_VALIDATION_FAILURE; "
            "recovery owner: the phase's own PR session/IA rescope.",
            "STOP_SESSION_MISMATCH, STOP_SCOPE_CHANGE, STOP_REMOTE_INTEGRITY_DRIFT, or STOP_VALIDATION_FAILURE; "
            "recovery owner: same PR session/IA rescope."),
    },
    "GCF-17.LINEAGE": {
        "next": (["GCF-14", "GCF-19", "GCF-20"], ["GCF-19", "GCF-20"]),
        "failure_stop_condition": (
            "STOP_LINEAGE_INCOMPLETE, STOP_UNATTRIBUTABLE_CHANGE, or STOP_WORK_UNIT_NOT_TO_SPEC; recovery owner: "
            "a new top-level PR session Nathan creates for a re-plan (GCF-14), the reviewer, or IA.",
            "STOP_LINEAGE_INCOMPLETE, STOP_UNATTRIBUTABLE_CHANGE, or STOP_WORK_UNIT_NOT_TO_SPEC; recovery owner: "
            "PR session/reviewer/IA."),
    },
    "GCF-14": {
        "consumes": (["pr_instruction", "approved_implementation_plan_lineage", "current_repository",
                      "pr_work_unit_lineage_review"],
                     ["pr_instruction", "approved_implementation_plan_lineage", "current_repository"]),
    },
}


def ser(obj) -> bytes:
    """§5.3 recipe for the oracle and the runtime map."""
    return (json.dumps(obj, indent=2, sort_keys=False, ensure_ascii=False) + "\n").encode("utf-8")


def row_digest(row) -> str:
    """§5.4 row digest formula."""
    content = {k: row[k] for k in CONTENT_FIELDS}
    return hashlib.sha256(
        json.dumps(content, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def project_map(oracle):
    """§5.6 runtime-map projection."""
    return {key: oracle[key] for key in ("profile_id", "authority", "coverage", "runtime_rows")}


def main() -> int:
    skills, repo = Path(sys.argv[1]), Path(sys.argv[2])
    hist_path = skills / "flowmaster-validate/references/glow-hde-canonical-change-flow-r1.json"
    hist_map_path = skills / "change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map.json"
    hist_bytes, hist_map_bytes = hist_path.read_bytes(), hist_map_path.read_bytes()
    assert hashlib.sha256(hist_bytes).hexdigest() == HIST_ORACLE_SHA256, "historical oracle digest"
    assert hashlib.sha256(hist_map_bytes).hexdigest() == HIST_MAP_SHA256, "historical map digest"
    hist = json.loads(hist_bytes)
    assert ser(hist) == hist_bytes, "recipe does not reproduce the historical oracle"
    assert ser(project_map(hist)) == hist_map_bytes, "recipe does not reproduce the historical map"

    succ = copy.deepcopy(hist)
    succ["profile_id"] = NEW_PROFILE
    tokens = succ["required_global_tokens"]
    assert tokens.count(OLD_PROFILE) == 1
    tokens[tokens.index(OLD_PROFILE)] = NEW_PROFILE
    rows = {r["id"]: r for r in succ["runtime_rows"]}
    hist_rows = {r["id"]: r for r in hist["runtime_rows"]}
    for rid, fields in CHANGES.items():
        for key, (new, old) in fields.items():
            if old is not None:
                assert rows[rid][key] == old, (rid, key, rows[rid][key])
            rows[rid][key] = new
    order = [r["id"] for r in succ["runtime_rows"] if r["id"] in SUCCESSOR_ROWS]
    assert order == list(SUCCESSOR_ROWS), order

    # §5.11 step 1: the matrix.
    blocks = []
    for rid in order:
        row = rows[rid]
        assert list(row)[:11] == list(CONTENT_FIELDS) and list(row)[11] == "source_row_sha256"
        row["source_row_sha256"] = row_digest(row)
        block = {k: row[k] for k in CONTENT_FIELDS}
        block["supersedes_source_row_sha256"] = hist_rows[rid]["source_row_sha256"]
        blocks.append("```json\n" + json.dumps(block, indent=2, ensure_ascii=False) + "\n```\n"
                      + "source_row_sha256: " + row["source_row_sha256"] + "\n")
    matrix = (HEADER + "\n".join(blocks)).encode("utf-8")
    assert matrix.endswith(b"\n") and not matrix.endswith(b"\n\n")
    matrix_sha = hashlib.sha256(matrix).hexdigest()
    for path in (skills / "flowmaster-validate/references/r1-successor-source-20260923.md",
                 repo / "docs/prompt_ecosystem_management/r1-successor-source-20260923.md"):
        path.write_bytes(matrix)

    # §5.11 step 2: the oracle, authority appended (§5.5).
    authority = succ["authority"]
    assert list(authority) == ["r1_source_manifest_library_id", "r1_contract_matrix_library_id",
                               "r1_contract_matrix_sha256", "r1_frozen_snapshot_sha256", "r1_verdict"]
    authority["successor_source_matrix_sha256"] = matrix_sha
    authority["successor_rows"] = list(order)
    authority["successor_authority"] = SUCCESSOR_AUTHORITY
    oracle = ser(succ)
    oracle_sha = hashlib.sha256(oracle).hexdigest()
    (skills / "flowmaster-validate/references/glow-hde-canonical-change-flow-r1-20260923.json").write_bytes(oracle)

    # §5.11 step 3: the map.
    runtime_map = ser(project_map(succ))
    map_sha = hashlib.sha256(runtime_map).hexdigest()
    (skills / "change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json").write_bytes(runtime_map)

    # Self-checks: only the declared differences from the historical oracle.
    assert len(succ["runtime_rows"]) == 46
    assert sum(r["partition"] == "CORE" for r in succ["runtime_rows"]) == 26
    diffs = sorted((r["id"], k) for r in succ["runtime_rows"] for k in r if r[k] != hist_rows[r["id"]][k])
    assert [r["id"] for r in succ["runtime_rows"]] == [r["id"] for r in hist["runtime_rows"]]
    top = sorted(k for k in succ if succ[k] != hist[k])
    assert top == ["authority", "profile_id", "required_global_tokens", "runtime_rows"], top
    assert hashlib.sha256(hist_path.read_bytes()).hexdigest() == HIST_ORACLE_SHA256
    assert hashlib.sha256(hist_map_path.read_bytes()).hexdigest() == HIST_MAP_SHA256
    print(json.dumps({
        "matrix": {"bytes": len(matrix), "sha256": matrix_sha},
        "oracle": {"bytes": len(oracle), "sha256": oracle_sha},
        "runtime_map": {"bytes": len(runtime_map), "sha256": map_sha},
        "row_digests": {rid: rows[rid]["source_row_sha256"] for rid in order},
        "changed_row_fields": diffs,
        "changed_top_level_keys": top,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
