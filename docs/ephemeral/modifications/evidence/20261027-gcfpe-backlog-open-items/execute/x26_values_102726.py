#!/usr/bin/env python3
"""X26's values file for plan/repo_edits_102726.py --set X26, for MODIFICATION-20261027-gcfpe-backlog-open-items
(PLAN §5 X26, C-23: "the values file carries each @ marker from the receipts, written by script"; AM-11 and the
values as Nathan approved them at X26, §E).

  x26_values_102726.py --build R1-BUILD --out VALUES --sources SOURCES

R1-BUILD is the installed graph_parts.py build output of docs/graph/parts (R1). Each value is read from its source,
never typed:
  @PROMOTION_D              the next free D-number on origin/main's decision record
  @PROMOTION_DATE           the date of the register's selection (x21-register-102726.1.json register_selected_at)
  @PROMOTION_APPROVED_AT    Nathan's approval date, as X20 wrote it on the register entry (x20-entry-102726.1.json; AM-11)
  @REGISTER_TIME            register_selected_at as "YYYY-MM-DD HH:MM:SSZ" (with its date, as D29 wrote it)
  @N_ARCHIVED               x24-archived-102726.1.json present_under_archive
  @N_SUCCESSOR, @N_KEPT     the successor map's SUCCESSOR and KEPT member rows
  @MAIN_SHA                 the merge base of HEAD and origin/main, 7 characters
  @PROD_TOKEN               R1-BUILD: "<n> nodes · <e> edges · <s> state_routes · <bytes> bytes · sha256 <8 hex>…"
  @POSTFLIGHT_VERDICT       PROMOTION-PACKET.md's value, its <code> spans written as Markdown code spans
  @PROMOTION_APPROVAL_WORDS §E's quote of the approval, "Nathan approves promotion" through "Go on to PART-25."
  @REGISTER_ENTRY_PAGE_ID   x20-entry-102726.1.json
  @CATALOG_PAGE_ID          notion-controls-102726.1.json values
  @PE_PAGE_ID               the successor map's pe.page_id
  @ACTIVATION_DATE          x20-entry-102726.1.json values
VALUES holds the markers only (repo_edits_102726.py replaces every key it is given); SOURCES records each value's
source. Read-only outside the two outputs. Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[5]
RECORD = REPO / "docs/ephemeral/modifications/MODIFICATION-20261027-gcfpe-backlog-open-items.md"
DR = "docs/prompt_ecosystem_management/gcfpe.decision-record.md"


def j(name: str) -> dict:
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True, check=True).stdout


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--sources", required=True)
    a = ap.parse_args()
    v, src = {}, {}

    nums = [int(n) for n in re.findall(r"(?m)^## D(\d+) — ", git("show", f"origin/main:{DR}"))]
    v["@PROMOTION_D"] = f"D{max(nums) + 1}"
    src["@PROMOTION_D"] = f"origin/main:{DR}, highest heading D{max(nums)}"

    sel = j("x21-register-102726.1.json")["register_selected_at"]
    m = re.fullmatch(r"(\d{4}-\d\d-\d\d)T(\d\d:\d\d:\d\d)(?:\.\d+)?Z", sel)
    v["@PROMOTION_DATE"], v["@REGISTER_TIME"] = m.group(1), f"{m.group(1)} {m.group(2)}Z"
    src["@PROMOTION_DATE"] = src["@REGISTER_TIME"] = f"execute/x21-register-102726.1.json register_selected_at {sel}"

    entry = j("x20-entry-102726.1.json")
    v["@PROMOTION_APPROVED_AT"] = entry["values"]["@PROMOTION_APPROVED_AT"]
    v["@ACTIVATION_DATE"] = entry["values"]["@ACTIVATION_DATE"]
    v["@REGISTER_ENTRY_PAGE_ID"] = entry["register_entry_page_id"]
    for k in ("@PROMOTION_APPROVED_AT", "@ACTIVATION_DATE", "@REGISTER_ENTRY_PAGE_ID"):
        src[k] = "execute/x20-entry-102726.1.json"

    arch = j("x24-archived-102726.1.json")
    assert arch["ok"] and arch["present_under_archive"] == arch["reread"]
    v["@N_ARCHIVED"] = str(arch["present_under_archive"])
    src["@N_ARCHIVED"] = "execute/x24-archived-102726.1.json present_under_archive"

    mp = j("successor-pages-102726.1.json")
    disp = [r["disposition"] for r in mp["members"].values()]
    v["@N_SUCCESSOR"], v["@N_KEPT"] = str(disp.count("SUCCESSOR")), str(disp.count("KEPT"))
    v["@PE_PAGE_ID"] = mp["pe"]["page_id"]
    src["@N_SUCCESSOR"] = src["@N_KEPT"] = "execute/successor-pages-102726.1.json members' dispositions"
    src["@PE_PAGE_ID"] = "execute/successor-pages-102726.1.json pe.page_id"

    v["@CATALOG_PAGE_ID"] = j("notion-controls-102726.1.json")["values"]["@CATALOG_PAGE_ID"]
    src["@CATALOG_PAGE_ID"] = "execute/notion-controls-102726.1.json values"

    v["@MAIN_SHA"] = git("merge-base", "HEAD", "origin/main").strip()[:7]
    src["@MAIN_SHA"] = "git merge-base HEAD origin/main"

    out = Path(a.build).read_text(encoding="utf-8") if Path(a.build).suffix == ".txt" else ""
    b = re.search(r"build: (\d+) nodes, (\d+) edges, (\d+) state_routes\s+embedded JSON (\d+) bytes\s+sha256 ([0-9a-f]{64})", out)
    assert b, "R1 build output"
    v["@PROD_TOKEN"] = f"{b[1]} nodes · {b[2]} edges · {b[3]} state_routes · {int(b[4]):,} bytes · sha256 {b[5][:8]}…"
    src["@PROD_TOKEN"] = f"R1's build output, sha256 {b[5]}"

    pk = (HERE / "PROMOTION-PACKET.md").read_text(encoding="utf-8")
    pv = re.search(r"^\| `@POSTFLIGHT_VERDICT` \| `(.+)` \|$", pk, re.M).group(1)
    v["@POSTFLIGHT_VERDICT"] = re.sub(r"<code>(.*?)</code>", r"`\1`", pv)
    src["@POSTFLIGHT_VERDICT"] = "execute/PROMOTION-PACKET.md, <code> spans as Markdown code spans"

    rec = RECORD.read_text(encoding="utf-8")
    sec = rec.split("### Nathan's decisions after X18", 1)[1].split("\n### ", 1)[0]
    q = re.search(r"(Nathan approves promotion .*? Go on to PART-25\.)", sec)
    v["@PROMOTION_APPROVAL_WORDS"] = q.group(1)
    src["@PROMOTION_APPROVAL_WORDS"] = "the record's §E, Nathan's decisions after X18, the approval sentence"

    assert all(re.fullmatch(r"@[A-Z][A-Z0-9_]+", k) for k in v) and not any("@" in x for x in v.values())
    Path(a.out).write_text(json.dumps(v, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    Path(a.sources).write_text(json.dumps({"record_type": "GCFPE_102726_X26_VALUES_SOURCES", "values_file": Path(a.out).name,
                                           "sources": src}, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(v, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
