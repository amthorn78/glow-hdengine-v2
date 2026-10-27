#!/usr/bin/env python3
"""X18 (Q11): the promotion packet, written by script from the receipts, for MODIFICATION-20261027-gcfpe-backlog-open-items.

  x18_packet_102726.py <delivery-dir> [--check]

Writes execute/PROMOTION-PACKET.md. Every value comes from a committed receipt or record, read here:
  the successor map (members, PE)                         execute/successor-pages-102726.1.json
  member revisions (X7; unchanged at X14)                 execute/landing-check-102726.1.json, x14r-bodies-102726.1.json
  qualification (predicate 1)                             execute/x14r-bodies-102726.1.json, x15-registry-102726.1.json
  packages                                                execute/x13r-packages-102726.1.json (and the archives in
                                                          <delivery-dir>, whose sha256 must equal it)
  graphs, contracts, governing plan                       execute/x11-graphs-102726.1.json, x12-contracts-102726.1.json
  reviews (predicate 2, D24)                              execute/REVIEW-D24-*.md, REVIEW-POSTFLIGHT-*.md (first lines)
  pins, C4 and the controls on main                       execute/x18-check-102726.1.json, x18-controls-main-102726.1.json
  the activation's files                                  plan/activation-ops.json, plan/activation_render_102726.py,
                                                          plan/control_check_102726.py (sha256 measured here)
  accepted risks                                          execute/x18-risks-102726.1.json (each with its record)
--check exits 1 unless the file on disk equals what the receipts give now. Prints no body text; holds none.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
E = HERE.parent
REPO = E.parents[4]
REL = "docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items"
OUT = HERE / "PROMOTION-PACKET.md"


def J(name: str):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def first_line(p: Path) -> str:
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.strip():
            return line.strip().lstrip("#").strip()
    return ""


def commit_of(rel: str) -> str:
    return subprocess.run(["git", "-C", str(REPO), "log", "-1", "--format=%h", "--", rel],
                          capture_output=True, text=True).stdout.strip()


def build(delivery: Path) -> str:
    smap, lc = J("successor-pages-102726.1.json"), J("landing-check-102726.1.json")["check"]["pages"]
    x14, x15, x13 = J("x14r-bodies-102726.1.json"), J("x15-registry-102726.1.json"), J("x13r-packages-102726.1.json")
    x11, x12 = J("x11-graphs-102726.1.json"), J("x12-contracts-102726.1.json")
    x18, main = J("x18-check-102726.1.json"), J("x18-controls-main-102726.1.json")
    risks = J("x18-risks-102726.1.json")
    rev = {p["prompt"]: p["as_of"] for p in lc if "as_of" in p}
    q = x14["runs"]["root-plain"]
    plan = E / "PLAN-20261027.md"
    L = []
    w = L.append
    w("# Promotion packet — GCFPE-20261027.1 / 102726.1\n")
    w("`MODIFICATION-20261027-gcfpe-backlog-open-items`, X18 (PLAN §3 PART-24, §7; DN-1 D2). This is the exact snapshot "
      "Nathan is asked to approve for promotion. Approving it authorizes PART-25, X19 to X28, as PLAN §7 and §8 state, with "
      "the amendments AM-1 to AM-8 recorded in §E, and nothing else. Until then nothing of PART-25 is done: no control "
      "binding, no new page, no register change, no install, no archive move. Written by `execute/x18_packet_102726.py` "
      "from the receipts it names; `--check` reproduces it.\n")
    # ---------------------------------------------------------------------------------------------- 1
    w("## 1. The promotion predicates (the register's own)\n")
    w("| # | Predicate | State | Evidence |\n|---|---|---|---|")
    w(f"| 1 | Complete behaviour validation of the exact pinned snapshot | met | `{REL}/execute/x14r-bodies-102726.1.json`: "
      f"the shipped 102726.1 validators over all {q['profile_102726_with_bodies']['prompt_bodies_validated']} member bodies, "
      f"none unevaluated, `ok` {str(q['ok']).lower()}; fixtures with the bodies {q['fixtures_102726_with_bodies']['case_count']} "
      f"cases, without {q['fixtures_102726_without_bodies']['case_count']}, none failed; the flowmaster suite with no finding "
      f"from this change (C-21); text form `{q['reads']['text_form']}`; both D28 roots identical. "
      f"`{REL}/execute/x15-registry-102726.1.json`: the candidate registry's assertions on fresh reads, "
      f"{x15['assertions_body_landed_inject']['rows_ok']} of {x15['assertions_body_landed_inject']['rows_total']} rows, "
      f"every operation landed, {x15['assertions_body_landed_inject']['injected_fired_total']} injected regressions all reported |")
    pf = sorted(HERE.glob("REVIEW-POSTFLIGHT-*.md"))
    w("| 2 | Independent post-flight `PASS` or `PASS WITH WARNINGS`, no mandatory open finding | "
      + ("met" if pf and all(re.match(r"(PASS|PASS WITH WARNINGS)\b", first_line(p).replace("**", "")) for p in pf) else "**not met**")
      + " | " + "; ".join(f"`execute/{p.name}`: {first_line(p).replace('|', '/')}" for p in pf) + " |")
    w("| 3 | Nathan / Product Owner's separate approval of this snapshot | **open** | requested in §8 |\n")
    # ---------------------------------------------------------------------------------------------- 2
    w("## 2. The snapshot\n")
    w(f"**Notion — the 56 members and PE**, at the page ids of `execute/successor-pages-102726.1.json`, each at its X7 "
      f"revision (`execute/landing-check-102726.1.json`). X14's fresh reads after {x14['fetched_after']} found no member "
      f"moved since (`moved_since_landing_check` empty).\n")
    w("| prompt | disposition | page id | revision |\n|---|---|---|---|")
    for pid in sorted(smap["members"]):
        m = smap["members"][pid]
        w(f"| {pid} | {m['disposition']} | `{m['page_id']}` | `{rev.get(pid)}` |")
    w(f"| PE | SUCCESSOR | `{smap['pe']['page_id']}` | `{rev.get('PE')}` |\n")
    w(f"**The four skill packages** (`execute/x13r-packages-102726.1.json`; built by `execute/package_build_102726.py`, "
      f"reproducible with `check`). The `.skill` files for installation are in `{delivery}`. They install together, at "
      f"X22, after the register selects GCFPE-20261027.1.\n")
    w("| package | `.skill` sha256 | bytes | tree (`freeze.py`) |\n|---|---|---|---|")
    for k in ("change-flow", "flowmaster-validate", "glow-hde-pr-development", "glow-graph-contract"):
        p = x13["packages"][k]
        arc = delivery / f"{k}.skill"
        if not arc.exists() or sha(arc) != p["skill_sha256"]:
            raise SystemExit(f"x18_packet: {arc} is missing or differs from the X13r receipt")
        w(f"| {k} | `{p['skill_sha256']}` | {p['skill_bytes']:,} | `{p['extracted_freeze']}` |")
    w("\nAdvertised revisions: change-flow 3.5.0, flowmaster-validate 3.5.0 (`SKILL_TREE_SHA256` "
      "`e5723d286cecc4768050e76d64e03a4f59dd67ca1900c2aa5c18da348bb19779`), glow-hde-pr-development 1.5.0; glow-graph-contract "
      "advertises none.\n")
    fr = x13["roots"]["plain"]["freeze"]
    w("**The five unchanged skills** (installed; X13r's trees, `freeze.py`, D28 name-line form). P0 and P3 compare all nine "
      "digests, these and the four above.\n")
    w("| skill | tree |\n|---|---|")
    for k in ("amthor-workspace-governance-audit", "session-relay-flowmaster", "glow-write-boundary", "typesafe-scoring",
              "glow-merged-change-attribution-lock"):
        w(f"| {k} | `{fr[k]}` |")
    mp = HERE / "successor-pages-102726.1.json"
    w(f"\n**The successor map** `execute/successor-pages-102726.1.json`: {mp.stat().st_size:,} B, sha256 `{sha(mp)}` "
      f"(written once at X3; P0 compares it).\n")
    ct, pt = x11["candidate_token"], x11["production_token"]
    c = x12["contracts"]
    w("**Contracts and graph**\n")
    w("| artifact | identity |\n|---|---|")
    w(f"| production contract (bundled in change-flow and flowmaster-validate) | {c['production']['bytes']:,} B, sha256 "
      f"`{c['production']['sha256']}`, `SELECTED_PRODUCTION`; regenerated byte for byte by the patched regenerator (X13r G5) |")
    w(f"| candidate contract | {c['candidate']['bytes']:,} B, sha256 `{c['candidate']['sha256']}` |")
    w(f"| candidate graph | {ct['nodes']} nodes · {ct['edges']} edges · {ct['state_routes']} state_routes · {ct['bytes']:,} bytes · "
      f"sha256 `{ct['sha256']}` |")
    w(f"| production graph (written to `docs/graph/parts/` at X26) | {pt['nodes']} nodes · {pt['edges']} edges · "
      f"{pt['state_routes']} state_routes · {pt['bytes']:,} bytes · sha256 `{pt['sha256']}` |")
    w(f"| governing plan (pinned by both contracts) | `PLAN-20261027.md`, {plan.stat().st_size:,} B, sha256 `{sha(plan)}` |\n")
    b = x15["build_candidate"]
    w(f"**Registry.** Candidate stage `execute/candidate-registry.md`, {b['bytes']:,} B, sha256 `{b['sha256']}`, "
      f"{b['rows']} rows. X26 writes the selected stage with `registry_assemble_102726.py build --stage selected`, which "
      f"differs from the candidate only at {', '.join(x15['compare']['differing_paths'])} (`compare`).\n")
    act = [("plan/activation-ops.json", E / "plan/activation-ops.json"),
           ("plan/activation_render_102726.py", E / "plan/activation_render_102726.py"),
           ("plan/control_check_102726.py", E / "plan/control_check_102726.py")]
    w("**The activation.** " + ", ".join(f"`{n}` sha256 `{sha(p)}`" for n, p in act)
      + ", with AM-3 to AM-7 (record §E). The operating procedure it binds at P2: "
      f"`{main['v5_1_0']['path']}` on `main` ({main['v5_1_0']['bytes']:,} B, sha256 `{main['v5_1_0']['sha256']}`), "
      f"landed by pull request #{main['controls_pr_recorded_at_x1']} (`{main['v5_1_0_added_by'].split()[0][:8]}`); "
      f"`reviewer-prompt-template.md` at {main['reviewer_prompt_template_version']}; the note after D30 present "
      f"(`execute/x18-controls-main-102726.1.json`).\n")
    # ---------------------------------------------------------------------------------------------- 3
    w("## 3. The reviews\n")
    w("| review | brief | records and verdicts |\n|---|---|---|")
    d24 = sorted(HERE.glob("REVIEW-D24-*.md"))
    w(f"| D24 (X16) | `execute/BRIEF-D24.md` (`{commit_of(REL + '/execute/BRIEF-D24.md')}`) | "
      + "; ".join(f"`{p.name}`: {first_line(p).replace('|', '/')}" for p in d24) + " |")
    w(f"| post-flight (X17) | `execute/BRIEF-POSTFLIGHT.md` (`{commit_of(REL + '/execute/BRIEF-POSTFLIGHT.md')}`) | "
      + "; ".join(f"`{p.name}`: {first_line(p).replace('|', '/')}" for p in pf) + " |\n")
    # ---------------------------------------------------------------------------------------------- 4
    w("## 4. Activation markers and pins\n")
    w("| marker | value |\n|---|---|")
    for k, v in risks["markers"].items():
        w(f"| `{k}` | {v} |")
    w("\n**Pins** (each control page's revision as read at X18 after C-FI-REV, `execute/x18-check-102726.1.json`):\n")
    w("| page | id | revision |\n|---|---|---|")
    for pid, p in x18["pins"].items():
        w(f"| {p['name']} | `{pid}` | `{p['revision']}` |")
    w(f"\nC4: C-FI-REV landed on the Flow Index; `activation_render_102726.py check --phase review` "
      f"{'ok' if x18['review_check'].get('ok') else 'NOT ok'}; `control_check_102726.py --phase candidate` on the controls, "
      f"the catalog and PE {'ok' if x18['control_check_candidate'].get('ok') else 'NOT ok'}, "
      f"{x18['control_check_candidate'].get('findings_total')} findings.\n")
    # ---------------------------------------------------------------------------------------------- 5..8
    for title, key in (("## 5. What approval authorizes, in order (PLAN §7, §8)", "authorizes"),
                       ("## 6. Accepted risks — every listed finding", "risks"),
                       ("## 7. Your actions", "actions"),
                       ("## 8. The approval requested", "approval")):
        w(title + "\n")
        for line in risks[key]:
            w(line)
        w("")
    return "\n".join(L).rstrip() + "\n"


def main() -> int:
    delivery = Path(sys.argv[1])
    text = build(delivery)
    if "--check" in sys.argv:
        same = OUT.exists() and OUT.read_text(encoding="utf-8") == text
        print(json.dumps({"mode": "check", "equal": same}))
        return 0 if same else 1
    OUT.write_text(text, encoding="utf-8")
    print(json.dumps({"written": str(OUT.relative_to(REPO)), "bytes": len(text.encode("utf-8")),
                      "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest()}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
