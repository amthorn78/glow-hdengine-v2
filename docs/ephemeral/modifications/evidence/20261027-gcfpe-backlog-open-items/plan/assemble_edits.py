#!/usr/bin/env python3
"""Assemble plan/edits.json for MODIFICATION-20261027-gcfpe-backlog-open-items (MODE = PLAN, assembly A1).

Merges the body operations of the design returns W1, W2, W3a, W3b, W4, W5 and W6 (plan/work/W*.json) into the
precedent's edits.json format (MODIFICATION-20261011-gcfpe-mb008-to-promotion plan/edits.json: record_type,
modification, date, scope, d22, span_rule, shared_texts, pages, ops), applies the coordinator's decisions
(plan/coordinator-decisions.md, C-2 to C-6, C-8, C-9, C-10, C-13, and C-16, C-17 and C-24 of the repairs) where they
bear on body operations, and adds the
central head operations (one per successor: 54 runtime members, PE and CL-05). The binding currency edits (C-1) are
not stored: binding_pass.py generates them from each fresh read and the successor map.

Every value comes from a worker file, members-100926.1.tsv or a decision named in the comment beside it; no
successor id is typed. The head operations carry @SUCC_TITLE_<ID> and @SUCC_URL_<ID>, which body_check.py fills from
the successor map (W7 "successor_page_map"). No prompt body is read or written here: anchors are the workers'.

  PYTHONDONTWRITEBYTECODE=1 python3 assemble_edits.py          write edits.json beside this file
  PYTHONDONTWRITEBYTECODE=1 python3 assemble_edits.py --check  rebuild in memory and compare with edits.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE))
from assemble_guards import markdown_form  # noqa: E402  (C-15)
WORK = HERE / "work"
WORKERS = ["W1", "W2", "W3a", "W3b", "W4", "W5", "W6"]
PE_ID = "3f44590a05eb81f98b76c83465dc1960"
CL05_CANDIDATE = "4054590a05eb8155b301e2cb6dec31d5"
CL05_CANDIDATE_TITLE = "CL-05 — Prepare and Publish the Close Mutation Set — 102626.2 (candidate)"
KEPT = {"GCFPE-MGMT-10"}  # C-1: the only member kept
MIDSPAN_MARKUP = {"HP-OPS-10-04"}
DROPS = {"W1-DOC20-01": ["PR-40"], "QA120-02": ["CL-E-10"], "QA120-03": ["CL-C-10"]}
OP_KEYS = ("id", "part", "item", "prompt", "section", "start", "end", "lines", "new")

# C-24 (repair of PLAN review round 1, R-2; coordinator-decisions.md): the coordinator's override set for IA-30's two
# delta-review operations. Each pair is (the worker's widening text, the frozen per-work-unit text); the assertion in
# build() refuses a pair whose old text is not in the worker's replacement exactly once.
C24_OVERRIDES = {
    "W2-IA-30-BC-2": (
        "For every work unit the delta adds or changes, including a unit whose acceptance criterion or outcome the "
        "delta changes without editing the unit, check its business case",
        "For every work unit the delta adds or changes, check its business case"),
    "W2-IA-30-EM-2": (
        "An acceptance criterion the delta adds or changes that depends on emulating an external system is a ground "
        "for this decision",
        "For every work unit the delta adds or changes, an acceptance criterion that depends on emulating an external "
        "system is a ground for this decision"),
}
C24_WHY = {
    "W2-IA-30-BC-2": ("PF04 §9.7.7 names no review mode, so IA-30's business-case check applies to its material "
                      "Plan-delta review too (R-A1), for every work unit the delta adds or changes (ITEM-14). C-24: "
                      "L-C1 is an accepted risk, not repaired here."),
    "W2-IA-30-EM-2": ("D30-A in the material Plan-delta review, for every work unit the delta adds or changes "
                      "(ITEM-15). C-24: L-C1 is an accepted risk, not repaired here."),
}

# C-16 (repair R1): the A5 failing rows judged by PART-07's stated test (scope-measurement.md section 2; D23-B; D27).
# A line that tells an agent a handoff or package carries lineage, session identity, manual prerequisites, recovery
# context, branch or commit, or a complete native input package gets a PART-07 operation built from W3a's canonical
# family (W3a canonical_texts: HP_HOLD, HP_SESSION, and the "naming its input artifacts by repository path" form of
# W3a's change-flow redlines); the conforming rows get named exceptions in assemble_guards.py (C16_EXCEPTIONS).
# Anchors were checked on the A5 reads: each start occurs once in its page and overlaps no other operation's span.
_C16_STOP = ("A source, authority, or Product Owner decision stop without a complete receiver package remains terminal "
             "to its actual owner.",
             "A source, authority, or Product Owner decision stop that cannot hand off to a receiver, naming its input "
             "artifacts by repository path, remains terminal to its actual owner.",
             "G-HP-1: routing is made to depend on a 'complete receiver package', so the handoff is told to carry a "
             "complete package (ITEM-08; D23-B). Rewritten to the canonical form: a handoff names its input artifacts "
             "by repository path.")
_C16_IA10 = ("The complete package names the exact approved Specification and Thoth decision by repository path, and the "
             "required IA/session binding or its truthful unassigned state; the artifacts hold the rest.",
             "The handoff names the exact approved Specification and Thoth decision by repository path; the artifacts "
             "hold the rest. The receiving side chooses or recovers the session.",
             "G-HP-1: a 'complete package' label, and the handoff is told to carry the IA/session binding (session "
             "identity), which D27 Continuity reverses. Rewritten with the canonical lead's naming form and HP_SESSION "
             "('The receiving side chooses or recovers the session').")
C16_OPS = [
    {"id": "C16-CF-C-20-01", "prompt": "CF-C-20", "section": "Required result and routing",
     "start": _C16_STOP[0], "new": _C16_STOP[1], "why": _C16_STOP[2]},
    {"id": "C16-CF-E-20-01", "prompt": "CF-E-20", "section": "Required result and routing",
     "start": _C16_STOP[0], "new": _C16_STOP[1], "why": _C16_STOP[2]},
    {"id": "C16-CF-C-30-01", "prompt": "CF-C-30", "section": "Required result and routing",
     "start": _C16_IA10[0], "new": _C16_IA10[1], "why": _C16_IA10[2]},
    {"id": "C16-CF-E-30-01", "prompt": "CF-E-30", "section": "Required result and routing",
     "start": _C16_IA10[0], "new": _C16_IA10[1], "why": _C16_IA10[2]},
    {"id": "C16-DOC-10-01", "prompt": "DOC-10", "section": "Execute, step 6",
     "start": "create one complete evidence package and RS-10 intake with the exact native return phase;",
     "new": "record the evidence in one artifact and hand off to RS-10, naming that artifact by repository path; the "
            "artifact records the exact native return phase;",
     "why": "G-HP-1: the RS-10 handoff is told to be built as 'one complete evidence package' (ITEM-08; D23-B), as "
            "DOC-20's 'one complete package' was (W3b HP-DOC-20-01). Rewritten: the evidence is an artifact the "
            "handoff names by repository path, and the artifact records the return phase (D23-A)."},
    {"id": "C16-ESC-25-01", "prompt": "ESC-25", "section": "Result routing",
     "start": "or producing a complete lawful return package is terminal to Nathan",
     "new": "or a lawful return that names its input artifacts by repository path is terminal to Nathan",
     "why": "G-HP-1: the terminal condition is the absence of a 'complete lawful return package', so the return "
            "handoff is told to carry a complete package (ITEM-08; D23-B). Rewritten to the canonical naming form."},
    {"id": "C16-RS-30-01", "prompt": "RS-30", "section": "Controlled sources and boundaries",
     "start": "preserve the bases unchanged, and carry exact lineage into the revised request/proposal and handoff.",
     "new": "preserve the bases unchanged, and record exact lineage in the revised request/proposal. The handoff names "
            "its input artifacts by repository path; they hold their lineage, owners, recovery point and the rest.",
     "why": "G-HP-2: the handoff is told to carry exact lineage (ITEM-08; D23-B). The lineage goes into the artifact "
            "(D23-A), and the handoff sentence is W3a's HP_HOLD verbatim."},
]


def members() -> dict:
    rows = {}
    for line in (HERE / "members-100926.1.tsv").read_text(encoding="utf-8").splitlines():
        if line.strip():
            pid, page, title, lane = line.split("\t")
            rows[pid] = {"page_id": page, "title": title, "lane": lane}
    return rows


def load(w: str) -> dict:
    return json.loads((WORK / f"{w}.json").read_text(encoding="utf-8"))


def norm(op: dict, worker: str, why_note: str = "") -> dict:
    out = {k: op[k] for k in OP_KEYS if k in op}
    out.setdefault("end", None)
    out["source"] = worker
    # A worker that found mention, link, code or escape markup in its span said so (span_has_markup); the
    # replacement is written for that markup, so the op is allowed to replace it (body_check refuses markup
    # in every span that is not flagged).
    if op.get("span_has_markup"):
        out["allow_markup"] = True
    if why_note:
        out["coordinator"] = why_note
    return out


def head_ops(m: dict) -> list:
    """The central head operations (task step 2), two per member. Member heads were inspected on this session's
    fetches: line 1 the title, then 'Prompt ID: <ID>' (or 'Prompt ID: <code><ID></code>'), then
    'Notion URL: <mention url="https://app.notion.com/p/<page>"><title></mention>', each separated by one blank line.
    Each op names its text exactly, so a page whose head differs is refused (START_COUNT_0), never guessed."""
    ops = []
    for pid, row in sorted(m.items()):
        if pid in KEPT:
            continue
        url = f"https://app.notion.com/p/{row['page_id']}"
        # the Prompt ID line renders as 'Prompt ID: X' on some pages and 'Prompt ID: <code>X</code>' on others, so it
        # is not part of either span: the title op ends at the line's label, the URL op is the whole Notion URL line
        ops.append({"id": f"HEAD-{pid}-T", "part": "PART-24", "item": "ITEM-31", "prompt": pid,
                    "section": "head: title line", "start": f"{row['title']}\n\nPrompt ID: ", "end": None,
                    "new": f"@SUCC_TITLE_{pid}\n\nPrompt ID: ", "source": "A1", "head": True})
        ops.append({"id": f"HEAD-{pid}-U", "part": "PART-24", "item": "ITEM-31", "prompt": pid,
                    "section": "head: Notion URL self-mention",
                    "start": f"Notion URL: <mention url=\"{url}\">{row['title']}</mention>", "end": None,
                    "new": f"Notion URL: <mention url=\"@SUCC_URL_{pid}\">@SUCC_TITLE_{pid}</mention>",
                    "source": "A1", "allow_markup": True, "head": True})
    # CL-05: the candidate body has no title line and no Notion URL line (it opens 'Prompt ID: CL-05'; its title is
    # the page property 'CL-05 — ... — 102626.2 (candidate)', which W8 retitles at duplication, D-W8-1). The shipped
    # identity check needs the title as the first non-blank line and exactly one 'Notion URL:' line naming the page
    # (flowmaster-validate validate_gcfpe_20261009.py prompt_identity_header_valid), so the head op inserts both
    # around the existing 'Prompt ID: CL-05' line.
    ops.append({"id": "HEAD-CL-05", "part": "PART-24", "item": "ITEM-31", "prompt": "CL-05",
                "section": "head: title line and Notion URL self-mention inserted around Prompt ID",
                "start": "Prompt ID: CL-05", "end": None,
                "new": ("@SUCC_TITLE_CL-05\n\nPrompt ID: CL-05\n\n"
                        "Notion URL: <mention url=\"@SUCC_URL_CL-05\">@SUCC_TITLE_CL-05</mention>"),
                "source": "A1", "allow_markup": True, "head": True})
    # PE: the frontmatter, title line and 'Prompt Version:' line, 32 line breaks (lines 1 to 33 of the 100926.1
    # read). The candidate frontmatter carries exactly the keys W8's activation operations P1c-PE-1..5 anchor on
    # (D-W8-9): candidate_release, status UNSELECTED_CANDIDATE, the candidate selection_rule, promotion_authorized
    # false, validation_status QUALIFICATION_PENDING. activated_at and validation_scope are absent because
    # P1c-PE-3 and P1c-PE-5 add them. Underscores are written escaped, as the page renders them (C-5 Q-6), so the
    # read-back equals the replacement.
    fm = [
        "---",
        "artifact\\_type: PE\\_METAPROMPT",
        "artifact\\_version: \"102726.1\"",
        "title: \"@SUCC_TITLE_PE\"",
        "candidate\\_release: GCFPE-20261027.1",
        "status: UNSELECTED\\_CANDIDATE",
        "selection\\_authority: GCFPE Membership and Release Register",
        "selection\\_rule: \"This version is operative while the register binds it as the prompt-authoring control "
        "of GCFPE-20261027.1 / 102726.1 / 56, once selected. It does not assert its own selection.\"",
        "predecessor: PE Metaprompt 100926.1",
        "promotion\\_authorized: false",
        "validation\\_status: QUALIFICATION\\_PENDING",
        "source\\_modification: MODIFICATION-20261027-gcfpe-backlog-open-items",
        "---",
        "@SUCC_TITLE_PE",
        "Prompt Version: 102726.1",
    ]
    ops.append({"id": "HEAD-PE", "part": "PART-24", "item": "ITEM-31", "prompt": "PE",
                "section": "frontmatter, title line and Prompt Version line",
                "start": "---\n\nartifact\\_type: PE\\_METAPROMPT", "end": "Prompt Version: 100926.1", "lines": 32,
                "new": "\n\n".join(fm), "source": "A1", "allow_markup": True, "head": True})
    return ops


def build() -> tuple[dict, dict]:
    m = members()
    W = {w: load(w) for w in WORKERS}
    notes = {"applied": [], "flags": []}
    ops = []
    for w in WORKERS:
        for op in W[w]["ops"]:
            o = norm(op, w)
            # C-5 Q-2: W1's DOC-20 operation takes HP-DOC-20-02's wording
            if o["id"] == "W1-DOC20-01":
                old = "and complete recovery package are known"
                assert o["new"].count(old) == 1, "C-5 Q-2 anchor"
                o["new"] = o["new"].replace(old, "and the artifacts its handoff names are known")
                o["coordinator"] = "C-5 Q-2: takes HP-DOC-20-02's wording"
                notes["applied"].append("C-5 Q-2 W1-DOC20-01")
            # A replacement that retargets a route drops the old destination's page reference by design; body_check
            # refuses a dropped reference unless the op lists it (PART-08: DOC-20 no longer enters PR-40; PART-13:
            # QA-120 PASS continues to CL-05 instead of the closure decisions)
            # HP-OPS-10-04's span carries <code> formatting markup in its middle, which its worker's anchors did not
            # show (span_has_markup unset); it names no page, and the replacement is W3b's HP_ACCESS_FORM for the whole
            # field, so it is flagged here, visibly, rather than accepted silently
            # C-6: the PR Instruction quotes PF04 §9.7.7's stop rule verbatim (canon: "A work unit whose business
            # case is met stops; further work on it needs a new business case."); W2 paraphrased it
            if o["id"] == "W2-PR-10-BC-1":
                old = ("The instruction also states that a work unit whose business case is met stops, and that "
                       "further work on it needs a new business case.")
                assert o["new"].count(old) == 1, "C-6 anchor"
                o["new"] = o["new"].replace(old, "The instruction also states <code>PF04-Canon-HDE-Governance</code> "
                                            "§9.7.7's rule: \"A work unit whose business case is met stops; further "
                                            "work on it needs a new business case.\"")
                o["coordinator"] = "C-6: canon's sentence quoted verbatim"
                notes["applied"].append("C-6 W2-PR-10-BC-1 verbatim")
            # C-9: W3b's QA-120 PASS sentence names CL-05 and the inputs its intake lists (W5 Q-7 (a): the change ID,
            # the QA Report and the RCA); the tail, which says the artifacts hold the rest, is W3b's
            if o["id"] == "HP-QA-120-01":
                o["new"] = ("For either PASS branch, the handoff names CL-05's Close Implementer and the inputs CL-05's "
                            "intake reads: the change ID and, by repository path, the separate <code>QA_REPORT</code> "
                            "and <code>QA_RCA</code> with their IDs; the artifacts hold the PF10 and addendum lineage, "
                            "the Product Owner publication state and the rescope, remediation and unresolved-finding "
                            "lineage.")
                o["coordinator"] = "C-9: names CL-05 and its intake (W5 Q-7 (a)); this wording is A1's, for review"
                notes["applied"].append("C-9 HP-QA-120-01 names CL-05")
            # C-17: "as the instruction carries it" collides with G-HP-5 (a carry verb in the Required result sentence
            # that also names session identity); reworded, with G-W2-BC-7 moved to match in assemble_guards.py
            if o["id"] == "W2-PR-20-BC-1":
                old = "as the instruction carries it"
                assert o["new"].count(old) == 1, "C-17 anchor"
                o["new"] = o["new"].replace(old, "as the PR Instruction states it")
                o["coordinator"] = "C-17: reworded to 'as the PR Instruction states it' (G-HP-5 collision)"
                notes["applied"].append("C-17 W2-PR-20-BC-1")
            # C-24 (repair of PLAN review round 1, R-2): L-C1 is an accepted risk (§A.13, §A.14), so IA-30's
            # delta-review texts return to the frozen cut of ITEM-14 and ITEM-15, "every work unit a material Plan
            # delta adds or changes"; the widening clauses are gone and L-C1 stays listed (D26-A rule 4)
            if o["id"] in C24_OVERRIDES:
                old, new = C24_OVERRIDES[o["id"]]
                assert o["new"].count(old) == 1, f"C-24 anchor {o['id']}"
                o["new"] = o["new"].replace(old, new)
                o["why"] = C24_WHY[o["id"]]
                o["coordinator"] = "C-24: reverted to the frozen per-work-unit cut of ITEM-14 / ITEM-15 (L-C1 stays listed)"
                notes["applied"].append(f"C-24 {o['id']}")
            if o["id"] in MIDSPAN_MARKUP:
                o["allow_markup"] = True
                o["coordinator"] = "A1: allow_markup for mid-span <code> formatting markup (no page reference)"
                notes["applied"].append(f"A1 allow_markup {o['id']}")
            if o["id"] in DROPS:
                o["drops_refs"] = [m[x]["page_id"] for x in DROPS[o["id"]]]
                o["drops_refs_members"] = DROPS[o["id"]]
            ops.append(o)
        # C-8 Q1: QA-10's two sentences (W4 EH-1) join PART-10
        if w == "W4":
            for eh in W[w]["escape_hatch"]:
                if eh["id"] == "EH-1":
                    for op in eh["proposed_ops"]:
                        ops.append(norm(op, "W4", "C-8 Q1: W4 EH-1 joins PART-10"))
                        notes["applied"].append(f"C-8 {op['id']}")
    # C-16: the coordinator's PART-07 operations for the contradicting A5 rows (set "C16")
    for op in C16_OPS:
        ops.append(dict({"part": "PART-07", "item": "ITEM-08"}, **{k: op[k] for k in ("id", "prompt", "section", "start")},
                        end=None, new=op["new"], source="C16", why=op["why"],
                        coordinator="C-16: PART-07's test applied to an A5 failing row; contradicting"))
    notes["applied"].append(f"C-16 {len(C16_OPS)} PART-07 operations (set C16)")
    # C-2: all of W3a's 109 and W3b's 98 operations are kept
    n3a = sum(1 for o in ops if o["source"] == "W3a")
    n3b = sum(1 for o in ops if o["source"] == "W3b")
    assert (n3a, n3b) == (109, 98), (n3a, n3b)
    notes["applied"].append("C-2 W3a 109, W3b 98 kept")
    # C-9 and C-10 Q-1: W5's ops (CL-05 anchored on the candidate's text) and W6-PE-13a..c stay as written
    ops += head_ops(m)
    ids = [o["id"] for o in ops]
    assert len(ids) == len(set(ids)), "duplicate op id"

    # C-13: R-P2 is Nathan's, prepared as a conditional set and excluded from the normal path. Its text is C-13's
    # ("which should read 091426.1"); W6-Q-4 (a) would delete the clause instead, and C-13 governs.
    conditional = [
        {"set": "R-P1", "ops": [],
         "note": "R-P1 is skill text only (flowmaster-validate SKILL.md:168 and run_gcfpe_20261009_fixtures.py:320; "
                 "change-flow SKILL.md:305 and line 10): no prompt-body operation; its redlines belong in the "
                 "package redlines, not here"},
        {"set": "R-P2", "ops": [{
            "id": "RP2-PE", "part": "R-P2", "item": "R-P2 (conditional, Nathan)", "prompt": "PE",
            "section": "GCFPE bounded implementation phase labels",
            "start": "(C-VERSION, <code>D23-G</code>, from the release after 100926.1)", "end": None,
            "new": "(C-VERSION, <code>D23-G</code>, from the release after 091426.1)",
            "source": "W6 (Q-W6-4) / C-13", "allow_markup": True,
            "coordinator": "C-13: conditional; applied only with --with-conditional R-P2"}],
         # C-13's wording names 091426.1, which W6's PART-14 guard G-W6-PE-14L forbids on PE; the set carries the
         # named exception its own sentence needs, so the guard holds everywhere else (W6-Q-4 (a), dropping the
         # clause, needs none)
         # C-15: guards run on the normalized read, so the amendment pattern is translated to the Markdown form by
         # assemble_guards.markdown_form (the same translation every guard pattern gets), not retyped
         "guard_amendments": {"G-W6-PE-14L": {"except_add": [markdown_form(
             "\\(C-VERSION, <code>D23-G</code>, from the release after 091426\\.1\\)")]}}},
    ]

    # pages: every page an op touches, pinned to the as_of of the worker's fresh read (the later if two differ)
    reads: dict = {}
    for w in WORKERS + ["W7", "W8"]:
        d = W[w] if w in W else load(w)
        for fr in d.get("fresh_reads", []):
            pid = fr.get("page_id")
            as_of = str(fr.get("as_of", "")).split(" ")[0]
            if pid and len(as_of) >= 20 and as_of[:4] == "2026":
                reads.setdefault(pid, []).append((as_of, w))
    page_of = {pid: row["page_id"] for pid, row in m.items()}
    page_of["PE"] = PE_ID
    page_of["CL-05"] = CL05_CANDIDATE
    pages = {}
    touched = sorted({o["prompt"] for o in ops} | {o["prompt"] for c in conditional for o in c["ops"]})
    for prompt in touched + sorted(KEPT):
        page = page_of[prompt]
        got = sorted(reads.get(page, []))
        entry = {"page_id": page, "expected_last_edited": got[-1][0] if got else None,
                 "pin_from": sorted({w for _, w in got})}
        if prompt in KEPT:
            entry["guards_only"] = True
            entry["note"] = "KEPT (C-1): no operation; read for the binding guards and G-HP-6 (C-5 Q-3)"
        if prompt == "CL-05":
            entry["note"] = ("the 102626.2 candidate; EXECUTE's successor map points the entry at the duplicate "
                             "under the HDE Change Flow hub (C-9)")
        if len({a for a, _ in got}) > 1:
            notes["flags"].append({"page": prompt, "as_of_values": sorted({a for a, _ in got}),
                                   "used": got[-1][0]})
        if not got:
            notes["flags"].append({"page": prompt, "error": "NO_WORKER_FRESH_READ"})
        pages[prompt] = entry

    edits = {
        "record_type": "GCFPE_102726_PLAN_BODY_OPERATIONS",
        "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
        "date": "2026-10-27",
        "scope": ("Successor GCFPE-20261027.1 / 102726.1 / 56 pages (C-1): the 54 runtime members and PE, each a "
                  "duplicate of its 100926.1 page, and CL-05, a duplicate of the 102626.2 candidate "
                  f"{CL05_CANDIDATE}; GCFPE-MGMT-10 is kept and only read. No selected 100926.1 page is written. The "
                  "entries point at the 100926.1 pages (CL-05 at the candidate) for the PLAN dry run; EXECUTE points "
                  "them at the successors with body_check.py --successor-map execute/successor-pages-102726.1.json, "
                  "which also fills every @SUCC_TITLE_<ID> and @SUCC_URL_<ID>. Binding currency edits (C-1) are "
                  "generated by binding_pass.py from each fresh read and the map, never stored."),
        "d22": ("Operations name spans by anchors and carry replacement text; no prompt body is stored. Pins are the "
                "as_of of the design workers' fresh reads (plan/work/W*.json fresh_reads)."),
        "span_rule": ("start must occur exactly once in the unedited page; end, when present, on the same line after "
                      "start, or `lines` line breaks after it; an op may replace mention, link, code or escape "
                      "markup only when it carries allow_markup"),
        "shared_texts": {
            # C-9: PART-13's cross-member destination tokens are the successor map's own values
            "CL05_URL": "@SUCC_URL_CL-05",
            "CLC10_URL": "@SUCC_URL_CL-C-10",
            "CLE10_URL": "@SUCC_URL_CL-E-10",
        },
        "shared_texts_from_map": ("SUCC_URL_<ID> = https://app.notion.com/p/<successor page_id>; SUCC_TITLE_<ID> = "
                                  "the successor's exact title; PE's are the map's pe entry"),
        "pages": pages,
        "ops": ops,
        "conditional_ops": conditional,
        "decisions_applied": notes["applied"],
        "pin_flags": notes["flags"],
    }
    return edits, notes


def main() -> int:
    edits, notes = build()
    text = json.dumps(edits, indent=1, ensure_ascii=False) + "\n"
    target = HERE / "edits.json"
    if "--check" in sys.argv:
        same = target.exists() and target.read_text(encoding="utf-8") == text
        print(json.dumps({"mode": "check", "edits_json_current": same}))
        return 0 if same else 1
    target.write_text(text, encoding="utf-8")
    by = {}
    for o in edits["ops"]:
        by[o["source"]] = by.get(o["source"], 0) + 1
    print(json.dumps({"mode": "write", "ops": len(edits["ops"]), "by_source": by, "pages": len(edits["pages"]),
                      "conditional_sets": [c["set"] for c in edits["conditional_ops"]],
                      "pin_flags": notes["flags"]}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
