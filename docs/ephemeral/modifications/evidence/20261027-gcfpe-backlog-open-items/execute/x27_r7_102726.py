#!/usr/bin/env python3
"""X27, R7, after Nathan merges the promotion pull request, for MODIFICATION-20261027-gcfpe-backlog-open-items
(PLAN §5 X27, §7 step 8; D26-C: started from `main`, the merge detected by files, never by commit subjects).

  x27_r7_102726.py <installed-skills-root> <work> --out R

On the checkout at origin/main (refused unless HEAD's tree equals origin/main's):
  merge     docs/graph/parts/global.json's candidate.release is GCFPE-20261027.1, prompts/CL-05.json exists, and the
            registry's registry_id is GCFPE-PCR-20261027.1
  build     the installed glow-graph-contract graph_parts.py build of docs/graph/parts into <work> reproduces the
            production token (execute/x26-102726.1.json's R1 build)
  registry  plan/registry_assemble_102726.py check --stage selected on main's registry, with copies of the installed
            governance audit and graph contract and main's parts
  d31       the decision record carries the promotion heading once
  surfaces  authoritative-surfaces.md's graph proof token row equals the build, in @PROD_TOKEN's form
  digests   execute/x22_install_102726.py on the installed root: the nine freeze digests equal the packet's
Read-only outside <work> and R; tokens, ids, counts and digests only. Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
E = HERE.parent
REPO = HERE.parents[5]
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
PARTS = REPO / "docs/graph/parts"
REG = REPO / "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"
DR = REPO / "docs/prompt_ecosystem_management/gcfpe.decision-record.md"
SURF = REPO / "docs/prompt_ecosystem_management/authoritative-surfaces.md"
D31 = re.compile(r"(?m)^## D31 — `GCFPE-20261027\.1 / 102726\.1 / 56` is promoted")


def run(cmd: list, env: dict | None = None) -> subprocess.CompletedProcess:
    return subprocess.run([str(c) for c in cmd], capture_output=True, text=True, env=env or ENV)


def main() -> int:
    installed, work = Path(sys.argv[1]), Path(sys.argv[2])
    out = Path(sys.argv[sys.argv.index("--out") + 1])
    head = run(["git", "-C", REPO, "rev-parse", "HEAD^{tree}", "origin/main^{tree}", "origin/main"]).stdout.split()
    if len(head) != 3 or head[0] != head[1]:
        raise SystemExit("x27: HEAD's tree is not origin/main's; start from main")
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)
    rec = {"record_type": "GCFPE_102726_X27_R7", "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
           "step": "X27, R7", "main": head[2], "tree": head[0]}

    g = json.loads((PARTS / "global.json").read_text(encoding="utf-8"))
    rid = re.search(r"(?m)^registry_id: (\S+)$", REG.read_text(encoding="utf-8"))
    rec["merge"] = {"candidate_release": g.get("candidate", {}).get("release"), "cl05_part": (PARTS / "prompts/CL-05.json").exists(),
                    "registry_id": rid.group(1) if rid else None}
    rec["merge"]["detected"] = (rec["merge"]["candidate_release"] == "GCFPE-20261027.1" and rec["merge"]["cl05_part"]
                                and rec["merge"]["registry_id"] == "GCFPE-PCR-20261027.1")

    want = json.loads((HERE / "x26-102726.1.json").read_text(encoding="utf-8"))["r1"]["build"]
    b = run([sys.executable, installed / "glow-graph-contract/scripts/graph_parts.py", "build", PARTS, work / "graph.md"],
            env={**ENV, "TMPDIR": str(work)})
    m = re.search(r"build: (\d+) nodes, (\d+) edges, (\d+) state_routes\s+embedded JSON (\d+) bytes\s+sha256 ([0-9a-f]{64})\s+"
                  r"validation (\w+)", b.stdout + b.stderr)
    got = {"nodes": int(m[1]), "edges": int(m[2]), "state_routes": int(m[3]), "embedded_json_bytes": int(m[4]),
           "sha256": m[5], "validation": m[6]} if m else None
    rec["build"] = {"exit": b.returncode, "token": got, "production_token": want, "reproduced": got == want}

    for s in ("amthor-workspace-governance-audit", "glow-graph-contract"):
        shutil.copytree(installed / s, work / s)
    c = run([sys.executable, E / "plan/registry_assemble_102726.py", "check", "--stage", "selected", "--registry", REG,
             "--audit-root", work / "amthor-workspace-governance-audit", "--graph-contract", work / "glow-graph-contract",
             "--parts", PARTS])
    cj = json.loads(c.stdout) if c.stdout.strip().startswith("{") else {}
    rec["registry"] = {"exit": c.returncode, **{k: cj.get(k) for k in ("ok", "validator_errors", "deriver_drift", "rows",
                                                                         "rows_active", "header_values_ok")}}

    rec["d31_heading_count"] = len(D31.findall(DR.read_text(encoding="utf-8")))

    row = re.search(r"(?m)^\| Graph proof token \| `([^`]+)`", SURF.read_text(encoding="utf-8"))
    form = (f"{got['nodes']} nodes · {got['edges']} edges · {got['state_routes']} state_routes · "
            f"{got['embedded_json_bytes']:,} bytes · sha256 {got['sha256'][:8]}…") if got else None
    rec["surfaces"] = {"token_row": row.group(1) if row else None, "build_form": form,
                       "equal": bool(row) and row.group(1) == form}

    d = run([sys.executable, HERE / "x22_install_102726.py", installed, "--out", work / "digests.json"])
    dj = json.loads((work / "digests.json").read_text(encoding="utf-8")) if (work / "digests.json").exists() else {}
    rec["digests"] = {"exit": d.returncode, "nine_equal": dj.get("nine_equal"),
                      "skills": [{k: r[k] for k in ("skill", "kind", "installed", "ok")} for r in dj.get("skills", [])]}

    rec["checks"] = {"merge_detected_by_files": rec["merge"]["detected"],
                     "build_reproduces_production_token": rec["build"]["reproduced"],
                     "registry_check_ok": rec["registry"]["ok"] is True and rec["registry"]["exit"] == 0,
                     "d31_heading_once": rec["d31_heading_count"] == 1,
                     "surfaces_token_equals_build": rec["surfaces"]["equal"],
                     "installed_digests_equal_reviewed": dj.get("nine_equal") is True}
    rec["ok"] = all(rec["checks"].values())
    out.write_text(json.dumps(rec, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"ok": rec["ok"], **rec["checks"], "registry": rec["registry"]}, indent=1))
    return 0 if rec["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
