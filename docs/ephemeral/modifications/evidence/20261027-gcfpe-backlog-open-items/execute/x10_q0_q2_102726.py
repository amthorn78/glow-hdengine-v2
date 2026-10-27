#!/usr/bin/env python3
"""X10 (Q0 to Q2) for EXECUTE of MODIFICATION-20261027-gcfpe-backlog-open-items.

    x10_q0_q2_102726.py <installed-skills-root> <build-root> [--q2]

Q0: the nine installed skills' freeze digests equal W7's, and the selected graph parts build D29's token (the
register's selection is read from X9's control check, execute/x9-control-check-102726.1.json). Q1: a copy of the
installed glow-graph-contract is patched (contracts_102726.py patch-ggc) and its contract_recipe.py regenerates the
shipped 100926.1 contract byte for byte against both bundled copies (W7 graph_measurement's predecessor command).
With --q2, Q2: build_r1_successor_20261027.py on <build-root> (a copy of the installed skills) and the repository,
with --expect-decision-record, which writes the three R1 files into <build-root> and
docs/prompt_ecosystem_management/r1-successor-source-20261027.md into the repository; then the repository matrix is
compared byte for byte with <build-root>'s. <build-root> is created as a copy of the installed tree when absent; the
installed tree is only read. Prints a JSON receipt (digests and counts only). Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PLAN = HERE.parent / "plan"
EVID = HERE.parent
sys.path.insert(0, str(PLAN))


def main() -> int:
    installed, build = Path(sys.argv[1]), Path(sys.argv[2])
    q2 = "--q2" in sys.argv
    if "/skills/synced/" in str(build.resolve()):
        raise SystemExit("refusing a build root under the synced install directory")
    spec = importlib.util.spec_from_file_location("dr", PLAN / "dry_run_102726.py")
    dr = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dr)
    if not build.exists():
        build.mkdir(parents=True)
        for d in sorted(installed.iterdir()):
            if d.is_dir():
                shutil.copytree(d, build / d.name, ignore=shutil.ignore_patterns("__pycache__"))
    rec: dict = {}
    # Q0 ---------------------------------------------------------------------------------------------------------
    want = dr.expected_digests()
    rows = [{"skill": k, "expected": v, "installed": dr.freeze(installed / k), "build_copy": dr.freeze(build / k)}
            for k, v in want.items()]
    for r in rows:
        r["ok"] = r["expected"] == r["installed"] == r["build_copy"]
    scratch = build.parent / (build.name + "-x10")
    if scratch.exists():
        shutil.rmtree(scratch)
    scratch.mkdir(parents=True)
    c, o, e = dr.run([dr.PY, build / "glow-graph-contract/scripts/graph_parts.py", "build", dr.REPO / "docs/graph/parts",
                      scratch / "graph-100926.1.md"], env_extra={"TMPDIR": str(scratch)})
    tok, d29 = dr.build_token(o), dr.d29_token()
    x9 = json.loads((HERE / "x9-control-check-102726.1.json").read_text(encoding="utf-8"))
    reg = next(p for p in x9["pages"] if p["page"] == "3d24590a05eb81ce942ad994cfca9fa1")
    rec["Q0"] = {"skills": rows, "skills_9_equal": len(rows) == 9 and all(r["ok"] for r in rows),
                 "graph_token": tok, "d29_token": d29, "graph_token_equals_d29": dr.token_matches(tok, d29),
                 "register_current_selection_ok_at_x9": reg.get("current_selection_ok"),
                 "register_read_as_of": reg.get("as_of")}
    rec["Q0"]["ok"] = rec["Q0"]["skills_9_equal"] and rec["Q0"]["graph_token_equals_d29"] and reg.get("current_selection_ok") is True
    # Q1 ---------------------------------------------------------------------------------------------------------
    ctr = importlib.util.spec_from_file_location("ct", PLAN / "contracts_102726.py")
    ct = importlib.util.module_from_spec(ctr)
    ctr.loader.exec_module(ct)
    ggc = scratch / "glow-graph-contract"
    cp, po, pe = dr.run([dr.PY, PLAN / "contracts_102726.py", "patch-ggc", build / "glow-graph-contract", ggc])
    shipped = [build / "change-flow" / ct.PRED_CONTRACT, build / "flowmaster-validate" / ct.PRED_CONTRACT]
    out = scratch / "contract-100926.1.json"
    c1, o1, e1 = dr.run([dr.PY, ggc / "scripts/contract_recipe.py", scratch / "graph-100926.1.md", dr.REPO / ct.TEMPLATE,
                         build / "flowmaster-validate" / ct.ORACLE_0923, dr.REPO / ct.DECISIONS, out,
                         "--contract-revision", "4.2.0", "--primary-skill-revision", "1.4.0",
                         "--release-values", dr.REPO / ct.PRED_VALUES, "--check", *shipped],
                        cwd=dr.REPO, env_extra={"TMPDIR": str(scratch)})
    text = o1 + e1
    rec["Q1"] = {"patch_exit": cp, "recipe_exit": c1, "equal_lines": text.count("EQUAL    "),
                 "different_lines": text.count("DIFFERENT"),
                 "sha256": hashlib.sha256(out.read_bytes()).hexdigest() if out.exists() else None,
                 "bytes": out.stat().st_size if out.exists() else None}
    rec["Q1"]["ok"] = (cp == 0 and c1 == 0 and rec["Q1"]["equal_lines"] == 2 and rec["Q1"]["sha256"] == ct.PRED_SHA
                       and rec["Q1"]["bytes"] == ct.PRED_BYTES)
    # Q2 ---------------------------------------------------------------------------------------------------------
    if q2:
        c2, r2 = dr.jrun([dr.PY, EVID / "build_r1_successor_20261027.py", build, dr.REPO,
                          "--expect-decision-record", dr.DECISIONS])
        repo_m = dr.REPO / "docs/prompt_ecosystem_management/r1-successor-source-20261027.md"
        fv_m = build / "flowmaster-validate/references/r1-successor-source-20261027.md"
        rec["Q2"] = {"exit": c2, "receipt": r2,
                     "repo_matrix_byte_identical_to_flowmaster_validate": repo_m.exists() and fv_m.exists()
                     and repo_m.read_bytes() == fv_m.read_bytes(),
                     "repo_matrix_sha256": hashlib.sha256(repo_m.read_bytes()).hexdigest() if repo_m.exists() else None}
        rec["Q2"]["ok"] = c2 == 0 and rec["Q2"]["repo_matrix_byte_identical_to_flowmaster_validate"]
    rec["ok"] = all(rec[k]["ok"] for k in rec)
    print(json.dumps(rec, indent=1, ensure_ascii=False))
    return 0 if rec["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
