#!/usr/bin/env python3
"""X28, the close, for MODIFICATION-20261027-gcfpe-backlog-open-items (PLAN §5 X28): the backlog writes.

  x28_backlog_102726.py plan  --fetched-after T --out PAYLOAD
  x28_backlog_102726.py check --fetched-after T --payload PAYLOAD --out R

On this session's newest read of the GCFPE Modification Backlog after T:
  dispositions  every entry whose heading ends "— TAKEN" (the backlog's own count; the plan's X28 row says 28, and
                the backlog holds 29, MB-042 taken by ITEM-35 under DN-12 rider 3): its index row's status cell,
                its heading's status, and a dated closing paragraph after the section's last paragraph, naming the
                item's disposition and the record. The dispositions are the plan's (§3, PART-01 to PART-28)
  listed        the promotion packet's §6 listed findings not opted in, which "go to the backlog at X28" (Nathan's
                approval: "PF-A F-1 and PF-A F-2 stay listed, and D24-B LISTED-2 goes to the backlog"): six new
                entries, MB-053 to MB-058, in the page's entry form, their index rows after MB-052's. Two whose
                condition no longer holds (PF-A F-1, ended at X27; D24-A F1, no ecosystem defect) are recorded
                CLOSED with the reason
`plan` writes PAYLOAD: one update_content (each old_str from the read, at count 1) and one insert_content at the
end. `check` reads the page again: each new string once (as written or with Notion's underscore escaping), each
replaced string gone, no heading left "— TAKEN". The backlog is a record page, not a prompt body (D22).
Run with PYTHONDONTWRITEBYTECODE=1; CLAUDE_CODE_SESSION_ID names the session.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "plan"))
sys.path.insert(0, str(HERE))
import activation_render_102726 as R  # noqa: E402  (occ, esc)
import page_facts_102726 as PF  # noqa: E402

PAGE = "3e54590a05eb81eb818fd0f42045167a"
MOD = "<code>MODIFICATION-20261027-gcfpe-backlog-open-items</code>"
REC = "§E of <code>docs/ephemeral/modifications/MODIFICATION-20261027-gcfpe-backlog-open-items.md</code>"
WHEN = ("after the promotion: GCFPE-20261027.1 / 102726.1 / 56 is selected from 2026-10-28 00:21:59Z, and the "
        "repository step merged to <code>main</code> as <code>c3afb921</code>")
DATE = "2026-10-28"

# entry -> (disposition kind, the record's words); every other taken entry is APPLIED (PLAN §3)
SPECIAL = {
    "MB-007": ("NOT_APPLICABLE", "<code>NOT_APPLICABLE</code> under Nathan's DN-8 (c), with no edit: no producer outside "
                                 "GCFPE authors an addendum (GTWPE-D3; L-B18 accepted)"),
    "MB-009": ("WONT_DO", "closes WON'T DO under Nathan's DN-7 (a), with no edit, and this entry's risk is an accepted "
                          "risk"),
    "MB-025": ("NOT_APPLICABLE", "is settled under Nathan's DN-10 (b), with no edit: the clause is kept, and the repeated "
                                 "PENDING row is an accepted risk"),
    "MB-028": ("NOT_APPLICABLE", "<code>NOT_APPLICABLE</code> under Nathan's DN-8 (c), with no edit: TW already keeps "
                                 "unchanged members' pages"),
    "MB-029": ("VERIFIED", "closes delivered under Nathan's DN-11, with no edit: \"close MB-029 as delivered. Its "
                           "quantified relay reading is the typesafe-scoring skill, which every GCFPE handoff runs "
                           "(PF04 §9.1.3); its qualitative Claude recommendation is withdrawn by my direction of "
                           "2026-10-11 that no AI model recommendation is given.\""),
}
INDEX_STATUS = {"APPLIED": "CLOSED — {items} of " + MOD + ", APPLIED, " + DATE,
                "NOT_APPLICABLE": "CLOSED — {items} of " + MOD + ", {why}, " + DATE,
                "VERIFIED": "CLOSED — {items} of " + MOD + ", delivered (DN-11), " + DATE,
                "WONT_DO": "WON'T DO — {items} of " + MOD + ", Nathan's DN-7 (a), recorded " + DATE}
INDEX_WHY = {"MB-007": "not applicable (DN-8 (c))", "MB-025": "settled with no edit (DN-10 (b))",
             "MB-028": "not applicable (DN-8 (c))"}
FRONTMATTER_WORD = {"NOT_APPLICABLE": "NOT_APPLICABLE", "VERIFIED": "VERIFIED", "WONT_DO": "NOT_APPLICABLE"}

FIELD = "|  |  |\n| --- | --- |\n"
NOT_RATED = "Not rated: a listed finding (D26-A rule 4); the Product Owner rates it"
FOUND = ("2026-10-27, EXECUTE of " + MOD + ", {step} ({src}); listed in the promotion packet's §6 and not opted in, "
         "so it goes to the backlog at X28; recorded " + DATE)
NEW = [
    {"id": "MB-053", "title": "No package gate checks what CL-05's handoff to the closure receiver carries", "status": "OPEN",
     "found_by": "(EXECUTE, X16, D24-B LISTED-2)", "step": "X16, the D24 skill review",
     "src": "<code>execute/REVIEW-D24-B.md</code> LISTED-2; Nathan's promotion approval: \"D24-B LISTED-2 goes to the backlog\"",
     "affects": "flowmaster-validate <code>scripts/validate_gcfpe_20261027.py</code> (<code>validate_qa_closure_bodies</code>, "
                "<code>QA_PASS_INTAKE_MARKERS</code>); the 102726.1 contract's CL-05 → CL-E-10 and CL-05 → CL-C-10 branches",
     "conflicts": "None. 100926.1 checked QA-120's PASS handoff to Isis for its intake markers; with CL-05 between them "
                  "(PF06 §3.5.1), nothing checks the handoff Isis now receives",
     "body": [("What is wrong.", "No validator rule, runner case or registry guard checks what CL-05's <code>CLOSE_PR_READY</code> "
                                 "handoff names. The contract's CL-05 → Isis branches require <code>CLOSE_MUTATION_SET_RESULT</code> "
                                 "only, while CL-E-10 and CL-C-10 still read <code>QA_REPORT_ID</code> and <code>QA_RCA_ID</code>."),
              ("What breaks.", "If CL-05's handoff ever omitted the QA Report or the RCA, CL-E-10 or CL-C-10 would stop at intake "
                               "(<code>STOP_CLOSURE_EVIDENCE_INCOMPLETE</code>): a loud stop, not a wrong action. CL-05's body names "
                               "the result record, the QA-120 Report and the RCA by repository path."),
              ("Why not fixed where found.", "A new check is a new design element, outside the frozen scope."),
              ("What closing it involves.", "A Modification that packages flowmaster-validate adds a check on CL-05's exit "
                                            "handoff, fired by regression.")]},
    {"id": "MB-054", "title": "The Flow Index's and QA hub's CL-05 navigation lines omit the Epic close-run condition", "status": "OPEN",
     "found_by": "(EXECUTE, X17, PF-A F-2)", "step": "X17, the post-flight",
     "src": "<code>execute/REVIEW-POSTFLIGHT-A.md</code> F-2; Nathan: \"PF-A F-1 and PF-A F-2 stay listed\"",
     "affects": "Glow HDE Prompt Flow Index — GCFPE-20261027.1 — 102726.1 (P1d-FI-FLOW-QA) and HDE QA — GCFPE-20261027.1 — "
                "102726.1 (P1e-HUB-QA-PASS)",
     "conflicts": "P-L18 of that Modification's plan, accepted: until canon admits an Epic close-run family, an Epic close "
                  "stops <code>BLOCKED</code> after its rehearsal. CL-05's body and the graph carry the condition",
     "body": [("What is wrong.", "Both lines say CL-05 hands a verified <code>EPIC</code> to CL-E-10, without that condition."),
              ("What breaks.", "A reader of the navigation expects an Epic close to reach CL-E-10; CL-05's body stops it "
                               "<code>BLOCKED</code>, a loud stop."),
              ("Why not fixed where found.", "The one-line correction was an opt-in in the promotion packet; Nathan kept it listed."),
              ("What closing it involves.", "Append \"for an Epic whose close-run family canon admits; otherwise CL-05 returns "
                                            "<code>BLOCKED</code> after its rehearsal\" to both lines in a Modification that "
                                            "writes those controls, or close the entry when canon admits the family.")]},
    {"id": "MB-055", "title": "<code>activation_render_102726.py plan --chain</code> ignores <code>--emit</code>", "status": "OPEN",
     "found_by": "(EXECUTE, X17, PF-A F-3 = PF-B W-2)", "step": "X17, the post-flight",
     "src": "<code>execute/REVIEW-POSTFLIGHT-A.md</code> F-3 and <code>execute/REVIEW-POSTFLIGHT-B.md</code> W-2; the packet: "
            "\"A tool fix goes to the backlog\"",
     "affects": "<code>docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/plan/activation_render_102726.py</code>, "
                "its chain mode, and any later Modification that adapts it",
     "conflicts": "The tool's own usage, which says <code>--emit</code> prints each operation's text",
     "body": [("What is wrong.", "With <code>--chain</code>, the renderer prints the same report with or without "
                                 "<code>--emit</code>; it never reads the flag."),
              ("What breaks.", "Whoever runs the chain with <code>--emit</code> sees counts, not operation text. The "
                               "transaction wrote from the non-chain <code>plan --phase PH --emit</code>, which emits, so no "
                               "write was affected."),
              ("Why not fixed where found.", "A tool fix, outside the frozen scope."),
              ("What closing it involves.", "When a later Modification adapts the renderer, its chain mode honours "
                                            "<code>--emit</code> or refuses it.")]},
    {"id": "MB-056", "title": "PE Metaprompt's page carries release and selection state, with no ruling on its head", "status": "OPEN",
     "found_by": "(EXECUTE, X17, PF-B W-3)", "step": "X17, the post-flight",
     "src": "<code>execute/REVIEW-POSTFLIGHT-B.md</code> W-3; the packet: \"To the backlog for a ruling\"",
     "affects": "PE Metaprompt 102726.1's page head (<code>status</code>, <code>candidate_release</code>, "
                "<code>promotion_authorized</code>, <code>validation_status</code>, a <code>Prompt Version</code> line), as "
                "PE Metaprompt 100926.1's did",
     "conflicts": "None: <code>prompt-body-content-policy.md</code> does not say whether PE's head is a control head or a "
                  "prompt body",
     "body": [("What is wrong.", "PE carries release and selection state that the content policy keeps out of a member body, "
                                 "and no ruling says whether that applies to PE's head."),
              ("What breaks.", "Nothing on the normal path; an auditor cannot say whether those lines are permitted."),
              ("Why not fixed where found.", "It needs a ruling."),
              ("What closing it involves.", "Nathan rules whether PE's head is a control head; a Modification then aligns "
                                            "PE or the policy.")]},
    {"id": "MB-057", "title": "Control text named repository surfaces before the promotion pull request merged", "status": "CLOSED",
     "index_status": "CLOSED — ended when the promotion pull request merged; verified at X27 of " + MOD + ", " + DATE,
     "found_by": "(EXECUTE, X17, PF-A F-1 = PF-B W-1)", "step": "X17, the post-flight",
     "src": "<code>execute/REVIEW-POSTFLIGHT-A.md</code> F-1 and <code>execute/REVIEW-POSTFLIGHT-B.md</code> W-1; Nathan: "
            "\"PF-A F-1 and PF-A F-2 stay listed\"",
     "affects": "The Flow Index (P1d-FI-B-TOKEN); the register (P2-REG-SEL's machine contract and per-prompt contracts rows); "
                "the Glow Operations Hub and the HDE Change Flow Overview (P6-HUB-SEL, P6-OV-SEL)",
     "conflicts": "None: D17's order puts the repository step last, as D29's promotion did",
     "body": [("What was wrong.", "From P1 until the promotion pull request merged, those lines named <code>docs/graph/parts/</code> "
                                  "with the 102726.1 token, <code>GCFPE-PCR-20261027.1</code> and D31 before <code>main</code> held them."),
              ("Closed, " + DATE + ".", "The promotion pull request merged as <code>c3afb921</code>, and X27 verified from "
                                        "<code>main</code> that the parts reproduce the token, the registry check passes and D31 "
                                        "is present once. No text needs a change. Record: " + REC + ".")]},
    {"id": "MB-058", "title": "The D24 brief's expected <code>package_apply.py --check</code> result did not reproduce", "status": "CLOSED",
     "index_status": "CLOSED — no ecosystem defect; disclosed in the record of " + MOD + ", " + DATE,
     "found_by": "(EXECUTE, X16, D24-A F1 = D24-B LISTED-1)", "step": "X16, the D24 skill review",
     "src": "<code>execute/REVIEW-D24-A.md</code> F1 and <code>execute/REVIEW-D24-B.md</code> LISTED-1",
     "affects": "<code>execute/BRIEF-D24.md</code> §8 b of that Modification: a record, not an ecosystem surface",
     "conflicts": "None",
     "body": [("What was wrong.", "The brief expected 105 <code>LANDED</code>. On the extracted trees the check reports 104 "
                                  "<code>LANDED</code> and <code>SR-W7-CF-04</code> <code>UNTOUCHED</code>, because R-P1's "
                                  "<code>RP1-CF-02</code> extends the note that operation inserts."),
              ("Closed, " + DATE + ".", "No package byte or behaviour is affected, and the author's error is disclosed in "
                                        "the record. Record: " + REC + ".")]},
]


def sections(text: str) -> dict:
    lines, out, cur = text.split("\n"), {}, None
    for line in lines:
        m = re.match(r"^## (MB-\d{3}) — ", line)
        if m:
            cur = m.group(1)
            out[cur] = [line]
        elif line.startswith("## ") or line.startswith("# "):
            cur = None
        elif cur:
            out[cur].append(line)
    return out


def count(text: str, s: str) -> int:
    return R.occ(text, s) + (R.occ(text, R.esc(s)) if R.esc(s) != s else 0)


def read(after: str) -> tuple:
    got = PF.newest(PAGE, os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"], 900, after)
    if not got:
        raise SystemExit("x28: no read of the backlog after the cutoff")
    m = PF.CONTENT.search(got[2])
    return got[1], m.group(1) if m else ""


def entry_text(e: dict) -> str:
    rows = [("Severity", "Not rated: closed when recorded" if e["status"] == "CLOSED" else NOT_RATED),
            ("Found", FOUND.format(step=e["step"], src=e["src"])), ("Affects", e["affects"]),
            ("Ruling or text it conflicts with", e["conflicts"])]
    table = FIELD + "\n".join(f"| <b>{k}</b> | {v} |" for k, v in rows)
    body = "\n\n".join(f"<b>{h}</b> {p}" for h, p in e["body"])
    return f"## {e['id']} — {e['title']} — {e['status']}\n\n{table}\n\n{body}"


def plan(a) -> int:
    as_of, text = read(a.fetched_after)
    secs = sections(text)
    taken = [k for k, v in secs.items() if v[0].endswith(" — TAKEN")]
    ops, rows = [], []
    for k in taken:
        sec = secs[k]
        idx = [ln for ln in text.split("\n") if ln.startswith(f"| {k} |")]
        assert len(idx) == 1, k
        cells = idx[0].split(" | ")
        m = re.fullmatch(r"TAKEN — (.+) of <code>MODIFICATION-20261027-gcfpe-backlog-open-items</code>", cells[3])
        assert m, (k, cells[3])
        items = m.group(1)
        kind, words = SPECIAL.get(k, ("APPLIED", None))
        tk = [ln for ln in sec if ln.startswith("<b>Taken, 2026-10-27.</b> ")]
        parts = re.match(r"<b>Taken, 2026-10-27\.</b> (ITEM-[^()]+\([^)]+\)) of ", tk[0]).group(1) if tk else None
        if k == "MB-042":
            parts = "ITEM-35 (PART-28)"
        last = [ln for ln in sec if ln.strip()][-1]
        if kind == "APPLIED":
            para = f"<b>Closed, {DATE}.</b> {parts} of {MOD}: <code>APPLIED</code>, recorded by its EXECUTE at X28, {WHEN}. Record: {REC}."
        elif kind == "WONT_DO":
            para = (f"<b>WON'T DO, 2026-10-27; recorded {DATE}.</b> {parts} of {MOD} {words}. Record: {REC} "
                    f"(<code>NOT_APPLICABLE</code> in its frontmatter).")
        else:
            tail = "" if words.startswith("<code>") else f" (<code>{FRONTMATTER_WORD[kind]}</code> in its frontmatter)"
            stop = "" if words.endswith('."') else "."
            para = f"<b>Closed, {DATE}.</b> {parts} of {MOD}{':' if words.startswith('<code>') else ''} {words}{stop} Record: {REC}{tail}."
        new_cells = cells[:3] + [INDEX_STATUS[kind].format(items=items, why=INDEX_WHY.get(k, ""))] + cells[4:]
        heading = sec[0][: -len(" — TAKEN")] + (" — WON'T DO" if kind == "WONT_DO" else " — CLOSED")
        for old, new, what in ((idx[0], " | ".join(new_cells), "index"), (sec[0], heading, "heading"),
                               (last, last + "\n\n" + para, "closing")):
            assert count(text, old) == 1, (k, what)
            ops.append({"old_str": old, "new_str": new})
        rows.append({"entry": k, "items": items, "parts": parts, "kind": kind,
                     "frontmatter": FRONTMATTER_WORD.get(kind, "APPLIED")})
    anchor = [ln for ln in text.split("\n") if ln.startswith("| MB-052 |")]
    assert len(anchor) == 1 and not any(ln.startswith(f"| {e['id']} |") for e in NEW for ln in text.split("\n"))
    new_rows = [f"| {e['id']} | {e['title']} | Not rated | {e.get('index_status', 'OPEN')} | {MOD} {e['found_by']} |" for e in NEW]
    ops.append({"old_str": anchor[0], "new_str": anchor[0] + "\n" + "\n".join(new_rows)})
    append = "\n\n".join(entry_text(e) for e in NEW)
    assert len(ops) <= 100 and not any(count(text, f"## {e['id']} — ") for e in NEW)
    pay = {"record_type": "GCFPE_102726_X28_BACKLOG_PAYLOAD", "page": PAGE, "read_as_of": as_of, "taken": len(taken),
           "rows": rows, "update_content": ops, "insert_content_end": append, "new_entries": [e["id"] for e in NEW]}
    Path(a.out).write_text(json.dumps(pay, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"read_as_of": as_of, "taken": len(taken), "operations": len(ops), "append_chars": len(append),
                      "kinds": {k: sum(r["kind"] == k for r in rows) for k in ("APPLIED", "NOT_APPLICABLE", "VERIFIED", "WONT_DO")},
                      "new_entries": pay["new_entries"]}, indent=1))
    return 0


def check(a) -> int:
    as_of, text = read(a.fetched_after)
    pay = json.loads(Path(a.payload).read_text(encoding="utf-8"))
    rows = []
    for op in pay["update_content"]:
        rows.append({"new_once": count(text, op["new_str"]) == 1,
                     "old_only_in_new": count(text, op["old_str"]) == R.occ(op["new_str"], op["old_str"])})
    app = [count(text, s) == 1 for s in pay["insert_content_end"].split("\n\n")]
    secs = sections(text)
    rec = {"record_type": "GCFPE_102726_X28_BACKLOG", "page": PAGE, "fetched_after": a.fetched_after, "as_of": as_of,
           "operations": len(rows), "operations_ok": sum(r["new_once"] and r["old_only_in_new"] for r in rows),
           "append_blocks": len(app), "append_blocks_ok": sum(app),
           "headings_taken_left": [k for k, v in secs.items() if v[0].endswith(" — TAKEN")],
           "closed_by_this_run": [r["entry"] for r in pay["rows"]],
           "new_entries_present": [e for e in pay["new_entries"] if e in secs]}
    rec["ok"] = (rec["operations_ok"] == rec["operations"] and rec["append_blocks_ok"] == rec["append_blocks"]
                 and not rec["headings_taken_left"] and rec["new_entries_present"] == pay["new_entries"])
    Path(a.out).write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(rec, indent=1, ensure_ascii=False))
    return 0 if rec["ok"] else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["plan", "check"])
    ap.add_argument("--fetched-after", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--payload")
    a = ap.parse_args()
    return plan(a) if a.mode == "plan" else check(a)


if __name__ == "__main__":
    sys.exit(main())
