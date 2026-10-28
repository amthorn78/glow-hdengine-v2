#!/usr/bin/env python3
"""X18 (C4 and Q11, before the packet) for EXECUTE of MODIFICATION-20261027-gcfpe-backlog-open-items.

  x18_record_102726.py check <fetched-after> --parts P --set @POSTFLIGHT_VERDICT=... --set @D24_RECORDS=... --out R
        after C-FI-REV's one write: activation_render_102726.py check --phase review on this session's reads after
        <fetched-after> (the Flow Index), and control_check_102726.py check --phase candidate on the ten control
        pages, the catalog and PE; each page's revision as read becomes its pin for P1 (written to R with the checks)
  x18_record_102726.py main --out R
        on origin/main, the controls merge detected by files (PLAN X18): v5.1.0 present (its sha256 and bytes),
        reviewer-prompt-template.md at artifact_version 1.3, the decision record's note after D30, and the commit
        that added v5.1.0 with its pull request number (execute/controls-pr-102726.1.json)

D22: control pages only, transient reads of this session's harness records; revisions, counts and booleans.
Run with PYTHONDONTWRITEBYTECODE=1; CLAUDE_CODE_SESSION_ID names the session.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
E = HERE.parent
REPO = E.parents[4]
sys.path.insert(0, str(E / "plan"))
import body_check as B  # noqa: E402

MAP = HERE / "successor-pages-102726.1.json"
PAGES = {
    "3d24590a05eb81ce942ad994cfca9fa1": "register", "3db4590a05eb81de9736ea69bac61016": "Flow Index",
    "3db4590a05eb81d59059eb6b95ed5fcf": "hub HDE Change Flow", "3db4590a05eb8195a2ccf7c0959a8b6e": "hub HDE IA",
    "3db4590a05eb814d96d3dcfa8835f96d": "hub HDE QA", "3db4590a05eb81cd938de84cfffead9c": "hub Escalation",
    "3db4590a05eb811b9c14f2ae89c28df7": "hub HDE TW", "3db4590a05eb812f87caed515836687f": "Alpha checklist",
    "3ce4590a05eb814f8892f88ff8539308": "Glow Operations Hub", "3c74590a05eb811d8433e7022629e213": "HDE Change Flow Overview",
    "4064590a05eb8113ae7de73041631c00": "catalog 102726.1", "4064590a05eb8173b2e7d37929e7fe4d": "PE Metaprompt 102726.1",
    "3f74590a05eb812db385c2544d7570f7": "catalog 100926.1 (read only)",
}
V510 = "docs/ephemeral/GCFPE-Direct-Handoff-and-Runtime-Artifact-Operating-Procedure-v5.1.0-20261027.md"
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}


def py(args) -> tuple[int, dict]:
    r = subprocess.run([sys.executable, *map(str, args)], capture_output=True, text=True, env=ENV, cwd=REPO)
    try:
        return r.returncode, json.loads(r.stdout)
    except ValueError:
        return r.returncode, {"_unparsed": (r.stdout + r.stderr)[-400:]}


def git(*args) -> str:
    return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True).stdout


def check(argv: list) -> dict:
    t, out = argv[0], Path(argv[argv.index("--out") + 1])
    parts = argv[argv.index("--parts") + 1]
    sets = [argv[i + 1] for i, x in enumerate(argv) if x == "--set"]
    setargs = [y for s in sets for y in ("--set", s)]
    rc1, rev = py([E / "plan/activation_render_102726.py", "check", "--successor-map", MAP, "--parts", parts,
                   "--phase", "review", "--fetched-after", t, "--set", "@CATALOG_PAGE_ID=4064590a05eb8113ae7de73041631c00",
                   "--set", "@PUBLICATION_DATE=2026-10-27", "--set", "@CONTROLS_PR=770", *setargs])
    rc2, cc = py([E / "plan/control_check_102726.py", "check", "--successor-map", MAP, "--phase", "candidate",
                  "--catalog", "4064590a05eb8113ae7de73041631c00", "--with-pe", "--fetched-after", t])
    root, session = os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"]
    pins = {}
    for pid, name in PAGES.items():
        got = B.latest_fetch(pid, root, session, 900, t)
        pins[pid] = {"name": name, "revision": got[1] if got else None}
    rec = {"record_type": "GCFPE_102726_X18_CHECK", "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
           "step": "X18", "fetched_after": t,
           "review_check": {"exit": rc1, **{k: v for k, v in rev.items() if k != "pages"},
                            "pages": [{k: v for k, v in p.items() if k not in ("control_rows",)} for p in rev.get("pages", [])]},
           "control_check_candidate": {"exit": rc2, "ok": cc.get("ok"), "findings_total": cc.get("findings_total"),
                                       "failed_checks_total": cc.get("failed_checks_total"),
                                       "pages": [{k: p.get(k) for k in ("page", "as_of", "ok", "findings", "current_selection_ok",
                                                                        "catalog_staging_ok", "title_ok") if k in p}
                                                 for p in cc.get("pages", [])]},
           "pins": pins,
           "d22": "control pages only; transient reads of this session's harness records; revisions, counts and booleans"}
    rec["ok"] = (rc1 == 0 and rev.get("ok") is True and rc2 == 0 and cc.get("ok") is True
                 and all(v["revision"] for v in pins.values()))
    out.write_text(json.dumps(rec, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    return {"ok": rec["ok"], "review_check_ok": rev.get("ok"), "control_check_ok": cc.get("ok")}


def main_check(argv: list) -> dict:
    out = Path(argv[argv.index("--out") + 1])
    subprocess.run(["git", "-C", str(REPO), "fetch", "-q", "origin", "main"], check=False)
    head = git("rev-parse", "origin/main").strip()
    v510 = subprocess.run(["git", "-C", str(REPO), "show", f"origin/main:{V510}"], capture_output=True).stdout
    tpl = git("show", "origin/main:docs/prompt_ecosystem_management/reviewer-prompt-template.md")
    dr = git("show", "origin/main:docs/prompt_ecosystem_management/gcfpe.decision-record.md")
    heads = [m.group(0) for m in re.finditer(r"(?m)^## .+$", dr)]
    d30 = next((i for i, h in enumerate(heads) if h.startswith("## D30 ")), None)
    note_after_d30 = heads[d30 + 1] if d30 is not None and d30 + 1 < len(heads) else None
    added = git("log", "origin/main", "--diff-filter=A", "--format=%H %s", "--", V510).strip().splitlines()
    pr_in_subject = [int(x) for x in re.findall(r"\(#(\d+)\)", added[-1])] if added else []
    recorded = json.loads((HERE / "controls-pr-102726.1.json").read_text(encoding="utf-8"))["controls_pr"]
    rec = {"record_type": "GCFPE_102726_X18_CONTROLS_ON_MAIN", "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
           "step": "X18", "origin_main": head,
           "v5_1_0": {"path": V510, "present": bool(v510), "sha256": hashlib.sha256(v510).hexdigest() if v510 else None,
                      "bytes": len(v510)},
           "reviewer_prompt_template_version": (re.search(r'(?m)^artifact_version: "([^"]+)"', tpl) or [None, None])[1],
           "decision_record_heading_after_d30": note_after_d30,
           "v5_1_0_added_by": added[-1] if added else None, "pull_request_in_commit": pr_in_subject,
           "controls_pr_recorded_at_x1": recorded}
    rec["ok"] = (rec["v5_1_0"]["present"] and rec["reviewer_prompt_template_version"] == "1.3"
                 and bool(note_after_d30) and note_after_d30.startswith("## Note, 2026-10-27")
                 and pr_in_subject == [recorded])
    out.write_text(json.dumps(rec, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    return rec


if __name__ == "__main__":
    mode = sys.argv[1]
    res = check(sys.argv[2:]) if mode == "check" else main_check(sys.argv[2:])
    print(json.dumps(res, indent=1, ensure_ascii=False))
    sys.exit(0 if res.get("ok") else 1)
