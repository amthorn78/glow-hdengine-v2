#!/usr/bin/env python3
"""A3's PLAN dry run of the GCFPE-PCR-20261027.1 registry (MODIFICATION-20261027-gcfpe-backlog-open-items, PART-24; W7 Q8
in PLAN form).

  a3_registry_dryrun_102726.py <installed-skills-root> <scratch> --a2 <A2 scratch dir> --map <stand-in map>
                               [--receipt R]

Base: the selected GCFPE-PCR-20261009.1 registry read from `main` with `git show` (W7-D9). Derived fields from A2's
candidate parts. Stand-ins: the map, the page revisions (edits.json's fresh-read pins), the catalog id (the 100926.1
catalog's) and the promotion approval date. Gates, each by its own flag: build (candidate) and its byte-identical
rebuild; check (the audit's validator 0 errors, no derivation drift, 56 rows, 56 ACTIVE, header values); synthetic
assertions --inject on every row; the selected stage's build and check; compare; selftest. Writes only <scratch> and,
with --receipt, that file. Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[5]
TOOL = HERE / "registry_assemble_102726.py"
REG = "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"
ENV = {"PYTHONDONTWRITEBYTECODE": "1", "PATH": os.environ.get("PATH", "/usr/bin:/bin")}
CATALOG_STAND_IN = "3f74590a05eb812db385c2544d7570f7"  # the 100926.1 catalog (D-W8-3: the 102726.1 one exists only in EXECUTE)


def run(args) -> tuple[int, dict | None, str]:
    p = subprocess.run([sys.executable, str(TOOL), *map(str, args)], capture_output=True, text=True, env=ENV)
    try:
        return p.returncode, json.loads(p.stdout), p.stderr[-400:]
    except json.JSONDecodeError:
        return p.returncode, None, (p.stdout + p.stderr)[-400:]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("installed"); ap.add_argument("scratch")
    ap.add_argument("--a2", required=True); ap.add_argument("--map", required=True)
    ap.add_argument("--receipt")
    a = ap.parse_args()
    SK, W, A2 = Path(a.installed), Path(a.scratch).resolve() / "registry-dryrun", Path(a.a2)
    if W.exists():
        shutil.rmtree(W)
    W.mkdir(parents=True)
    for k in ("amthor-workspace-governance-audit", "glow-graph-contract"):
        shutil.copytree(SK / k, W / k, ignore=shutil.ignore_patterns("__pycache__"))
    main_rev = subprocess.run(["git", "-C", str(REPO), "rev-parse", "origin/main"], capture_output=True, text=True).stdout.strip()
    base = W / "base-registry-main.md"
    base.write_bytes(subprocess.run(["git", "-C", str(REPO), "show", f"origin/main:{REG}"], capture_output=True).stdout)
    edits = json.loads((HERE / "edits.json").read_text(encoding="utf-8"))
    smap = json.loads(Path(a.map).read_text(encoding="utf-8"))
    rev = W / "revisions-standin.json"
    rev.write_text(json.dumps({"stand_in": True, "revisions": {k: edits["pages"][k]["expected_last_edited"] for k in smap["members"]}},
                              indent=1), encoding="utf-8")
    # C-22: @CATALOG_ID comes from the activation record of the catalog created at candidate publication; in PLAN
    # that record is a stand-in naming the 100926.1 catalog
    catrec = W / "catalog-record-standin.json"
    catrec.write_text(json.dumps({"record_type": "GCFPE_102726_CANDIDATE_CATALOG_RECORD_STAND_IN", "stand_in": True,
                                  "step": "C3 C-CAT", "values": {"@CATALOG_PAGE_ID": CATALOG_STAND_IN}}, indent=1) + "\n",
                      encoding="utf-8")
    common = ["--base-registry", base, "--audit-root", W / "amthor-workspace-governance-audit",
              "--graph-contract", W / "glow-graph-contract", "--parts", A2 / "candidate-parts", "--map", a.map,
              "--revisions", rev, "--stand-in-ok", "--catalog-record", catrec]
    ck = ["--audit-root", W / "amthor-workspace-governance-audit", "--graph-contract", W / "glow-graph-contract",
          "--parts", A2 / "candidate-parts"]
    rec = {"record_type": "A3_PLAN_REGISTRY_RECEIPT", "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
           "worker": "A3", "date": "2026-10-27", "stand_in_used": True,
           "stand_ins": ["successor map " + Path(a.map).name, "page revisions: edits.json pages[*].expected_last_edited",
                         f"@CATALOG_ID {CATALOG_STAND_IN} (the 100926.1 catalog), from a stand-in catalog record (C-22)", "@PROMOTION_APPROVAL_DATE 2026-10-27",
                         "derived fields from A2's stand-in candidate parts (counts do not depend on the map)"],
           "base": {"source": f"git show origin/main:{REG}", "origin_main": main_rev,
                    "sha256": hashlib.sha256(base.read_bytes()).hexdigest(), "bytes": base.stat().st_size}}
    cand, cand2, sel = W / "candidate-registry.md", W / "candidate-registry-again.md", W / "selected-registry.md"
    rc, b, err = run(["build", "--stage", "candidate", "--out", cand, *common])
    rec["build_candidate"] = {"exit": rc, "ok": (b or {}).get("ok"), "error": None if rc == 0 else err,
                              **{k: (b or {}).get(k) for k in ("rows", "bytes", "read_back_equal", "successor_rows", "kept_rows",
                                                               "added_rows", "hand_edits", "plan_assertions_added", "stand_in_used")}}
    if rc == 0:
        rec["build_candidate"]["sha256"] = hashlib.sha256(cand.read_bytes()).hexdigest()
    rc2, _, _ = run(["build", "--stage", "candidate", "--out", cand2, *common])
    rec["rebuild_byte_identical"] = rc == 0 and rc2 == 0 and cand.read_bytes() == cand2.read_bytes()
    rc, c, err = run(["check", "--stage", "candidate", "--registry", cand, *ck])
    rec["check_candidate"] = {"exit": rc, **(c or {"error": err})}
    rc, s, err = run(["assertions", "--registry", cand, "--audit-root", W / "amthor-workspace-governance-audit", "--synthetic", "--inject"])
    rec["assertions_candidate_synthetic_inject"] = {"exit": rc, **({k: v for k, v in (s or {}).items() if k != "per_row"} if s else {"error": err}),
                                                    "required_reported_total": sum(r["required_reported"] for r in (s or {}).get("per_row", [])),
                                                    "forbidden_injected_reported_total": sum(r["forbidden_injected_reported"] for r in (s or {}).get("per_row", [])),
                                                    "min_required_per_row": min((r["required"] for r in (s or {}).get("per_row", [])), default=None)}
    rc, b, err = run(["build", "--stage", "selected", "--out", sel, *common, "--set", "@PROMOTION_APPROVAL_DATE=2026-10-27"])
    rec["build_selected"] = {"exit": rc, "ok": (b or {}).get("ok"), "error": None if rc == 0 else err}
    rc, c, err = run(["check", "--stage", "selected", "--registry", sel, *ck])
    rec["check_selected"] = {"exit": rc, **{k: (c or {}).get(k) for k in ("ok", "validator_errors", "deriver_drift", "rows", "rows_active", "header_values_ok")}}
    rc, m, err = run(["compare", cand, sel, "--audit-root", W / "amthor-workspace-governance-audit"])
    rec["compare"] = {"exit": rc, **(m or {"error": err})}
    rc, t, err = run(["selftest", "--scratch", W / "selftest", *common])
    rec["selftest"] = {"exit": rc, **(t or {"error": err})}
    rec["ok"] = all([rec["build_candidate"]["ok"] is True, rec["rebuild_byte_identical"], rec["check_candidate"].get("ok") is True,
                     rec["assertions_candidate_synthetic_inject"].get("ok") is True, rec["build_selected"]["ok"] is True,
                     rec["check_selected"].get("ok") is True, rec["compare"].get("ok") is True,
                     rec["selftest"].get("selftest_ok") is True])
    rec["not_run_here"] = ["body-level assertions on every page as read, with every operation LANDED (A5; EXECUTE --landed)",
                           "page_last_edited_at from EXECUTE's landing-check report"]
    for p in (cand2,):
        p.unlink(missing_ok=True)
    if a.receipt:
        Path(a.receipt).write_text(json.dumps(rec, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    print(json.dumps({k: (v.get("ok") if isinstance(v, dict) and "ok" in v else v) for k, v in rec.items()
                      if k in ("build_candidate", "rebuild_byte_identical", "check_candidate", "assertions_candidate_synthetic_inject",
                               "build_selected", "check_selected", "compare", "ok")}
                     | {"selftest": rec["selftest"].get("selftest_ok")}, indent=1))
    return 0 if rec["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
