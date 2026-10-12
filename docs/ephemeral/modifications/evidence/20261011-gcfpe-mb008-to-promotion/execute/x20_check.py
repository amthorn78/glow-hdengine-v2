#!/usr/bin/env python3
"""X20: the corrections and banners written to pages the sweep found asserting 091426.1 as current.

  x20_check.py --fetched-after T

On the newest fresh read of each page after T: every text written (as written; Notion's stored form must equal it,
decision 4 of 2026-10-12), every replaced text absent, and control_check.py's retired-value scan of the page
(lines outside a historical section that name a 091426.1 page id or literal with no predecessor marker), reported by
section heading only. Transient reads of this session's harness records; prints counts, headings and booleans only.
"""
import argparse, json, os, sys
from pathlib import Path
sys.dont_write_bytecode = True
E = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(E / "plan"))
import control_check as C

CAT, FI, MGMT = "3f74590a05eb812db385c2544d7570f7", "3db4590a05eb81de9736ea69bac61016", "3f74590a05eb81b69bd8c27106f7a59d"
PAGES = {
    "3ce4590a05eb814f8892f88ff8539308": {
        "name": "Glow Operations Hub",
        "present": ["## Current selection — GCFPE-20261009.1 / 100926.1",
                    "**Selected GCFPE contract:** `GCFPE-20261009.1` / `100926.1`, exactly **55 members**. Selected 2026-10-12 by Product Owner approval (`D29`); the register selects it from 14:23:57Z.",
                    "**Sections on this page headed \"Current … — 091426.1\" were written for the predecessor** and are kept as written; where they differ from the selected 100926.1 prompts or the register, those govern.",
                    "## Historical selection — GCFPE-20260914.1 / 091426.1",
                    "## Find a selected GCFPE prompt — 100926.1",
                    f"Use [Glow HDE Complete Prompt Set — GCFPE-20261009.1 — 100926.1](https://app.notion.com/p/{CAT}) and the release register for every actual selected destination. Submit governance changes to [GCFPE-MGMT-10 — 100926.1](https://app.notion.com/p/{MGMT})",
                    "Optional [MGR-10 — 100926.1](https://app.notion.com/p/3f44590a05eb813ea53ac959e7a4e597)",
                    "The final [CL-40 — 100926.1](https://app.notion.com/p/3f44590a05eb8155934dd1c4c2b5d1eb) scan"],
        "absent": ["## Current selection — GCFPE-20260914.1", "## Find a selected GCFPE prompt — 091426.1",
                   "Use [Glow HDE Complete Prompt Set — 091426.1](https://app.notion.com/p/3db4590a05eb81738ef1d846e3c0df8c)"],
    },
    "3c74590a05eb811d8433e7022629e213": {
        "name": "HDE Change Flow Overview",
        "present": ["## Current GCFPE selection — GCFPE-20261009.1 / 100926.1 / 55",
                    "It is `REGISTER_CONTROLLED` navigation and is operative if and only if the register selects `GCFPE-20261009.1 / 100926.1 / 55`.",
                    "**Completed promotion and archival — 2026-10-12.**",
                    "## Historical GCFPE selection — GCFPE-20260914.1 / 091426.1 / 55",
                    "## Find a selected GCFPE prompt — 100926.1",
                    "Corrected 2026-10-12 from `091426.1`, and 2026-09-22 from `091326.2`; both releases' pages are archived."],
        "absent": ["## Current GCFPE selection — GCFPE-20260914.1", "## Find a selected GCFPE prompt — 091426.1",
                   "operative if and only if the register selects `GCFPE-20260914.1 / 091426.1 / 55`. Navigation grants no execution authority.\n**Completed promotion and archival — 2026-10-12"],
    },
    "3cc4590a05eb8101b5ded32c12616eb6": {
        "name": "Glow HDE Prompt Flow Index (un-versioned)",
        "present": [f"Current selection: `GCFPE-20261009.1` / `100926.1` / **55**, resolved only from the [GCFPE Membership and Release Register](https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1). Operational index: [Glow HDE Prompt Flow Index — GCFPE-20261009.1 — 100926.1](https://app.notion.com/p/{FI})."],
        "absent": ["Current selection: `GCFPE-20260914.1`"],
    },
    "3d94590a05eb81c6ab8fe343b9d2ae67": {
        "name": "GCFPE Next Iteration — Alpha Feedback Update Plan — 20260912.1",
        "present": [f"the lane map is the [Glow HDE Prompt Flow Index — GCFPE-20261009.1 — 100926.1](https://app.notion.com/p/{FI})."],
        "absent": ["the lane map is the [Glow HDE Prompt Flow Index — GCFPE-20260914.1"],
    },
    "3db4590a05eb8182ade0c1eb46c7e80f": {
        "name": "GCFPE — Epic Alpha Run Notes — HDE-EPIC040 — 20260914.1",
        "present": ["**Not operative since 2026-10-12.** This record is bound to GCFPE-20260914.1 / 091426.1. The register selects GCFPE-20261009.1 / 100926.1 / 55 from 2026-10-12, and the 091426.1 prompts are archived. The text below is kept as written."],
        "absent": [],
    },
    "3e34590a05eb811b93d2da9b4ef8106d": {
        "name": "GCFPE-MGMT-10 — PROPOSED BODY (D20 redesign)",
        "present": [f"**Promoted 2026-10-12.** This proposed body was duplicated as [GCFPE-MGMT-10 — Manage an Ecosystem Change — 100926.1](https://app.notion.com/p/{MGMT}), which the register selects with GCFPE-20261009.1 / 100926.1 / 55."],
        "absent": [],
    },
    "3e34590a05eb81e7927efe0541258916": {
        "name": "GCFPE MGMT Change-Process Redesign — Tracking",
        "present": [f"**2026-10-12: promoted.** The proposed body was duplicated as [GCFPE-MGMT-10 — Manage an Ecosystem Change — 100926.1](https://app.notion.com/p/{MGMT}) and selected with GCFPE-20261009.1 / 100926.1 / 55"],
        "absent": [],
    },
    "3df4590a05eb81e09144c1c36ffad28b": {
        "name": "GCFPE Workflow Skill Repair — Round Tracking — 091426.1",
        "present": ["**Historical record.** This page tracks the 091426.1 skill-repair rounds and is kept as written. Since 2026-10-12 the register selects GCFPE-20261009.1 / 100926.1 / 55, and the 091426.1 prompts are archived."],
        "absent": [],
    },
    "3df4590a05eb8111a6a5f67cb82f96f6": {
        "name": "GCFPE Alpha Feedback — Deferred Items — 091426.1",
        "present": ["**2026-10-12: GCFPE-20261009.1 / 100926.1 / 55 is selected** (the register; record `docs/ephemeral/modifications/MODIFICATION-20261011-gcfpe-mb008-to-promotion.md`). The 2026-10-09 cycle below was promoted; its statement that selected-release behaviour remains 091426.1 until a separate selection is superseded."],
        "absent": [],
    },
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetched-after", required=True)
    a = ap.parse_args()
    root, session = os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"]
    archive = C.archive_set(str(E / "execute/candidate-graph-parts"))
    rows, ok = [], True
    for pid, spec in PAGES.items():
        got = C.latest(pid, root, session, 120, a.fetched_after)
        if got is None:
            rows.append({"page": pid, "name": spec["name"], "error": "NO_FETCH_FOUND", "ok": False}); ok = False
            continue
        _, as_of, title, text = got
        missing = [s[:90] for s in spec["present"] if s not in text]
        survived = [s[:90] for s in spec["absent"] if s in text]
        f = C.findings(text, archive, "archived")
        sections = sorted({x["section"] for x in f})
        row = {"page": pid, "name": spec["name"], "as_of": as_of, "written_present": len(spec["present"]) - len(missing),
               "written_expected": len(spec["present"]), "missing": missing, "replaced_still_present": survived,
               "retired_value_lines_outside_historical": len(f), "their_sections": sections}
        row["ok"] = not missing and not survived
        ok &= row["ok"]
        rows.append(row)
    print(json.dumps({"mode": "x20_check", "fetched_after": a.fetched_after, "pages": rows, "ok": ok}, indent=1, ensure_ascii=False))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
