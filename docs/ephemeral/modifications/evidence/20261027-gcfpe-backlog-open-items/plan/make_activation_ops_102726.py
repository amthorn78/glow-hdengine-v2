#!/usr/bin/env python3
"""Builds plan/activation-ops.json for MODIFICATION-20261027-gcfpe-backlog-open-items (PLAN assembly A4).

The operations are copied by script, never retyped, from the design returns:
  W8 "notion_control_ops" and "transaction" (candidate publication C1 to C4, promotion P1 to P6),
  W6 "notion_control_ops" (PART-17's Hub and register operations, PART-21's Hub label, PART-19's bindings),
  W5 "notion_control_ops" (NC-1 to NC-3),
and arranged per page and per phase in the precedent's format
(docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/plan/activation-ops.json), with the
coordinator's decisions applied (plan/coordinator-decisions.md):
  C-10 Q-5  adds the one-sentence scope label on the Hub's "Earlier PF10 drafting/reference controls" section
            (W6 Q-W6-5 option (a), in PE's citation form, D-W6-10) as op C10-HUB-Q5;
  C-12      the CL-05 candidate is moved only (W5 NC-3's banner dropped); the 100926.1 catalog is archived by move;
            the hub candidate notes and the register's unselected-candidate record are written at publication (C3);
  D-W8-7    W6-BIND-4 folded into P1d-FI-BIND-P; W6-BIND-5 runs in the Flow Index's P1 batch; W6-BIND-1/2/3 are
            carried verbatim inside P2-REG-SEL/-SRC/-PROC (checked here: each binding text occurs in its host);
  D-W8-4    W5 NC-1 (the catalog's CL-05 row) is a generated catalog row, not a separate write.
Generated families (catalog rows, Flow Index topology rows, hub member rows, frontmatter, titles, the archive move
list) are NOT written here: activation_render_102726.py generates them from the successor map and the candidate
graph parts at render time.

  C-22      (repair R2) W8's P1c-PE-* anchors (and their replacements) take the escaped fetch form: PE's candidate
            frontmatter is written by the coordinator's HEAD-PE operation (edits.json) in the fetch's own form, where a
            plain-text underscore reads `\\_`, and update_content matches that form (C-15). Markers and <code> spans are
            left as they are; each escaped anchor must normalize back to W8's text (normalize_fetch.normalize) and
            occur exactly once in HEAD-PE's replacement.

  make_activation_ops_102726.py build     write plan/activation-ops.json
  make_activation_ops_102726.py check     rebuild in memory and compare with the file on disk (exit 1 on drift)
  make_activation_ops_102726.py selftest  each C-22 check refuses its injected defect

Reads the W files and coordinator-decisions.md beside it, and edits.json's HEAD-PE replacement (C-22); writes only
activation-ops.json. Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import normalize_fetch as nf  # noqa: E402
OUT = HERE / "activation-ops.json"
W = {k: json.loads((HERE / "work" / f"{k}.json").read_text(encoding="utf-8")) for k in ("W5", "W6", "W8")}

REGISTER = "3d24590a05eb81ce942ad994cfca9fa1"
FLOW_INDEX = "3db4590a05eb81de9736ea69bac61016"
HUBS = {"3db4590a05eb81d59059eb6b95ed5fcf": ("HDE Change Flow", "CF"),
        "3db4590a05eb8195a2ccf7c0959a8b6e": ("HDE IA", "IA"),
        "3db4590a05eb814d96d3dcfa8835f96d": ("HDE QA", "QA"),
        "3db4590a05eb81cd938de84cfffead9c": ("Escalation", "ESC"),
        "3db4590a05eb811b9c14f2ae89c28df7": ("HDE TW", "TW")}
CHECKLIST = "3db4590a05eb812f87caed515836687f"
OPS_HUB = "3ce4590a05eb814f8892f88ff8539308"
OVERVIEW = "3c74590a05eb811d8433e7022629e213"
OLD_CATALOG = "3f74590a05eb812db385c2544d7570f7"
ARCHIVE_PARENT = "3c94590a05eb811cb145cd010e3b3fcf"
PE_PRED = "3f44590a05eb81f98b76c83465dc1960"
CL05_CANDIDATE = "4054590a05eb8155b301e2cb6dec31d5"
OLD_REL, OLD_VER, NEW_REL, NEW_VER = "GCFPE-20261009.1", "100926.1", "GCFPE-20261027.1", "102726.1"

# PLAN pins: each page's revision ("as of") on A4's fresh reads of 2026-10-27 (recorded in the A4 receipt too)
PLAN_PINS = {
    REGISTER: "2026-10-12T17:17:45.991Z",
    FLOW_INDEX: "2026-10-12T17:17:19.872Z",
    "3db4590a05eb81d59059eb6b95ed5fcf": "2026-10-12T17:34:42.176Z",
    "3db4590a05eb8195a2ccf7c0959a8b6e": "2026-10-12T13:36:35.304Z",
    "3db4590a05eb814d96d3dcfa8835f96d": "2026-10-12T13:37:02.911Z",
    "3db4590a05eb81cd938de84cfffead9c": "2026-10-12T13:37:22.723Z",
    "3db4590a05eb811b9c14f2ae89c28df7": "2026-10-12T13:37:45.218Z",
    CHECKLIST: "2026-10-12T13:37:58.821Z",
    OPS_HUB: "2026-10-27T03:02:37.191Z",
    OVERVIEW: "2026-10-12T17:34:33.909Z",
    OLD_CATALOG: "2026-10-12T13:28:07.573Z",
}

PHASES = [
    {"id": "part17", "step": "PART-17 (EXECUTE body stage, before candidate publication)", "authority": "PLAN approval"},
    {"id": "candidate", "step": "C3", "authority": "PLAN approval"},
    {"id": "review", "step": "C4", "authority": "PLAN approval"},
    {"id": "activation", "step": "P1", "authority": "Nathan's exact promotion approval"},
    {"id": "activation-done", "step": "P1 verified", "authority": "Nathan's exact promotion approval"},
    {"id": "register", "step": "P2", "authority": "Nathan's exact promotion approval"},
    {"id": "register-done", "step": "P2 verified", "authority": "Nathan's exact promotion approval"},
    {"id": "install-done", "step": "P3 verified", "authority": "Nathan's exact promotion approval"},
    {"id": "prodval-done", "step": "P4 verified", "authority": "Nathan's exact promotion approval"},
    {"id": "archived", "step": "P5", "authority": "Nathan's exact promotion approval"},
    {"id": "sweep", "step": "P6", "authority": "Nathan's exact promotion approval"},
]


MARKER = re.compile(r"@[A-Z][A-Z0-9_]+(?::[A-Z0-9-]+)?")  # activation_render_102726.py's marker form
ESC_KEEP = re.compile(r"(<code>.*?</code>|@[A-Z][A-Z0-9_]+(?::[A-Z0-9-]+)?)")


def esc_fetch(s):
    """C-22: a string in Notion's fetch form: each plain-text underscore escaped (`\\_`); <code> spans and @MARKERs
    (activation_render_102726.py fills them before writing) are left as they are."""
    if s is None:
        return None
    return "".join(p if ESC_KEEP.fullmatch(p) else p.replace("\\_", "_").replace("_", "\\_") for p in ESC_KEEP.split(s))


def pe_fetch_form(ops: list, head_pe: str) -> list:
    """C-22: W8's P1c-PE-* ops in the escaped fetch form, checked against the PE head the coordinator writes."""
    out = []
    for o in ops:
        e = {**o, "start": esc_fetch(o["start"]), "end": esc_fetch(o.get("end")), "new": esc_fetch(o["new"])}
        for k in ("start", "end", "new"):
            if o.get(k) is not None and nf.normalize(e[k]) != o[k]:
                raise SystemExit(f"C-22: {o['id']} {k}: the escaped form does not normalize back to W8's text")
            if o.get(k) is not None and MARKER.findall(e[k]) != MARKER.findall(o[k]):
                raise SystemExit(f"C-22: {o['id']} {k}: escaping changed a marker")
        if head_pe.count(e["start"]) != 1:
            raise SystemExit(f"C-22: {o['id']}: the escaped anchor does not occur exactly once in HEAD-PE's replacement")
        e["why"] = (o.get("why") or "") + " C-22: anchor and replacement in the escaped fetch form."
        out.append(e)
    return out


def head_pe_text() -> str:
    edits = json.loads((HERE / "edits.json").read_text(encoding="utf-8"))
    return next(o for o in edits["ops"] if o["id"] == "HEAD-PE")["new"]


def phase_of(op_id: str) -> str:
    for pre, ph in (("C-FI-REV", "review"), ("C-", "candidate"), ("P1-ENTRY-DONE", "activation-done"),
                    ("P1", "activation"), ("P2-ENTRY-DONE", "register-done"), ("P2", "register"),
                    ("P3-ENTRY-DONE", "install-done"), ("P4-ENTRY-DONE", "prodval-done"), ("P5", "archived"),
                    ("P6", "sweep"), ("W6-BIND-5", "activation"), ("W6-", "part17")):
        if op_id.startswith(pre):
            return ph
    raise SystemExit(f"no phase for {op_id}")


def norm(o: dict, source: str) -> dict:
    out = {"id": o["id"], "phase": phase_of(o["id"]), "source": source, "part": o.get("part"),
           "item": o.get("item"), "start": o.get("start"), "end": o.get("end"), "new": o.get("new")}
    if o.get("lines") is not None:
        out["lines"] = o["lines"]
    if str(o.get("action", "")).startswith("APPEND"):
        out["append"] = True
        out["start"] = None
    if o["id"] == "P5-FI-DISP":
        out["whole_line"] = True  # "predecessor_disposition: SUPERSEDED" is a prefix of the longer value
    out["why"] = o.get("why")
    return out


def build(head_pe: str | None = None) -> dict:
    w8 = {o["id"]: o for o in W["W8"]["notion_control_ops"]}
    head_pe = head_pe_text() if head_pe is None else head_pe
    w6 = {o["id"]: o for o in W["W6"]["notion_control_ops"]}
    tx = W["W8"]["transaction"]
    pages: dict = {}

    def page(key: str, **meta):
        p = pages.setdefault(key, {"ops": []})
        p.update({k: v for k, v in meta.items() if k not in p})
        return p

    page(REGISTER, name="register", titles={}, pin=PLAN_PINS[REGISTER])
    page(FLOW_INDEX, name="Flow Index", pin=PLAN_PINS[FLOW_INDEX], frontmatter_rule=True, member_rows=True,
         titles={"activation": f"Glow HDE Prompt Flow Index — {NEW_REL} — {NEW_VER}"},
         frontmatter_title=[f'title: "Glow HDE Prompt Flow Index — {OLD_REL} — {OLD_VER}"',
                            f'title: "Glow HDE Prompt Flow Index — {NEW_REL} — {NEW_VER}"'])
    for hid, (name, _) in HUBS.items():
        page(hid, name=f"hub {name}", pin=PLAN_PINS[hid], frontmatter_rule=True, member_rows=True,
             titles={"activation": f"{name} — {NEW_REL} — {NEW_VER}"},
             frontmatter_title=[f'title: "{name} — {OLD_REL} — {OLD_VER}"', f'title: "{name} — {NEW_REL} — {NEW_VER}"'])
    page(CHECKLIST, name="Alpha checklist", pin=PLAN_PINS[CHECKLIST], frontmatter_rule=True,
         titles={"activation": f"GCFPE Alpha Establishment and Change Management Checklist — {NEW_VER}"},
         frontmatter_title=[f'title: "GCFPE Alpha Establishment and Change Management Checklist — {OLD_VER}"',
                            f'title: "GCFPE Alpha Establishment and Change Management Checklist — {NEW_VER}"'])
    page(OPS_HUB, name="Glow Operations Hub", pin=PLAN_PINS[OPS_HUB], titles={})
    page(OVERVIEW, name="HDE Change Flow Overview", pin=PLAN_PINS[OVERVIEW], titles={})
    page("@CATALOG_PAGE_ID", name="catalog 102726.1 (created at C3)", virtual="CATALOG",
         titles={"candidate": f"Glow HDE Complete Prompt Set — {NEW_REL} — {NEW_VER}"})
    page("@PE_PAGE_ID", name="PE Metaprompt 102726.1 (successor; head written by the coordinator)", virtual="PE",
         titles={"activation": f"PE Metaprompt {NEW_VER}"})
    page("@REGISTER_ENTRY_PAGE_ID", name="register entry 20261027.1 (created at P1(a))", virtual="REGISTER_ENTRY",
         titles={"activation": f"GCFPE Membership and Release Register Entry — {NEW_REL}"})

    # W6: PART-17 Hub and register ops, PART-21's Hub label; W6-BIND-5 in the Flow Index's P1 batch
    for oid, o in w6.items():
        if oid.startswith(("W6-HUB-", "W6-REG-")) or oid == "W6-BIND-5":
            page(o["page_id"])["ops"].append(norm(o, "W6"))
    # C-10 Q-5: the scope label W6 Q-W6-5 (a) proposed, in PE's citation form (D-W6-10)
    anchor = ("The following earlier instructions are preserved historical text for GCFPE.")
    page(OPS_HUB)["ops"].append({
        "id": "C10-HUB-Q5", "phase": "part17", "source": "C-10 Q-5 (W6 Q-W6-5 option (a))", "part": "PART-17",
        "item": "ITEM-10", "start": anchor, "end": None,
        "new": anchor + " Its addendum-numbering bullet is superseded everywhere by "
                        "<code>PF06-Canon-Change-Process-Guide</code> §0.1A.",
        "why": "C-10 Q-5: one-sentence scope label on the Hub's historical drafting section (SCOPE-002); "
               "PF06 §0.1A makes no ecosystem exception."})

    # W8: every op with a span or an append
    skip = {"C-DUP", "C-CAT", "P1a-ENTRY", "P5-MOVE", "P6-SWEEP", "P1d-FI-W6"}
    for oid, o in w8.items():
        if oid in skip or o.get("action") == "GENERATED":
            continue
        key = o["page_id"]
        page(key)["ops"].append(norm(o, "W8"))
    # C-22: PE's P1c ops in the escaped fetch form
    pe_ops = page("@PE_PAGE_ID")["ops"]
    p1c = [o for o in pe_ops if o["id"].startswith("P1c-PE-")]
    if len(p1c) != 5:
        raise SystemExit(f"C-22: expected W8's five P1c-PE ops, found {len(p1c)}")
    escaped = {o["id"]: o for o in pe_fetch_form(p1c, head_pe)}
    page("@PE_PAGE_ID")["ops"] = [escaped.get(o["id"], o) for o in pe_ops]

    # D-W8-7 / CD-9: W6-BIND-1..3 carried verbatim in P2-REG-*; W6-BIND-4 folded into P1d-FI-BIND-P
    carried = []
    hosts = {"W6-BIND-1": "P2-REG-SEL", "W6-BIND-2": "P2-REG-SRC", "W6-BIND-3": "P2-REG-PROC",
             "W6-BIND-4": "P1d-FI-BIND-P"}
    for b, host in hosts.items():
        carried.append({"binding": b, "host": host, "text_in_host": w6[b]["new"] in w8[host]["new"]})
    w6reg2 = w6["W6-REG-2"]["new"].split("\n\n## Historical")[0]
    carried.append({"binding": "W6-REG-2 (PF10 paragraph)", "host": "P2-REG-SRC",
                    "text_in_host": w6reg2 in w8["P2-REG-SRC"]["new"]})

    # phase order inside a page follows the W files' order; sort only by phase index
    order = {p["id"]: i for i, p in enumerate(PHASES)}
    for p in pages.values():
        p["ops"].sort(key=lambda o: order[o["phase"]])

    cand = tx["candidate_records"]
    act = tx["activation_records"]
    return {
        "record_type": "MODIFICATION_20261027_PLAN_ACTIVATION_OPS",
        "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
        "date": "2026-10-27",
        "sources": "W8 notion_control_ops and transaction; W6 notion_control_ops; W5 NC-1 to NC-3; coordinator "
                   "decisions C-1, C-9, C-10, C-12 (plan/coordinator-decisions.md); precedent format "
                   "20261011-gcfpe-mb008-to-promotion/plan/activation-ops.json. Built by "
                   "make_activation_ops_102726.py; no operation text is typed here.",
        "purpose": "The exact operations EXECUTE applies to the control pages at PART-17, candidate publication "
                   "(C3, C4) and the promotion transaction (P1 to P6), and the content specs of the two pages it "
                   "creates. Each operation names its span by anchors and carries its replacement; "
                   "activation_render_102726.py adds the generated families from the successor map and the "
                   "candidate graph parts, applies everything in memory to fresh reads, refuses an anchor that does "
                   "not resolve exactly once and an unsafe batch, and runs control_check_102726.py on the result.",
        "successor_map": {
            "execute": "docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/execute/"
                       "successor-pages-102726.1.json",
            "plan_stand_in": "docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/plan/"
                             "successor-map-standin.json",
            "rule": "every successor id, URL, title and revision pin comes from the map; none is typed. A stand-in "
                    "map (stand_in: true) is rendered with binding_pass.probe() synthetic ids so retired and "
                    "successor ids stay distinct, and every receipt says stand-ins were used."},
        "phases": PHASES,
        "markers": tx["markers"],
        "generated_markers": {
            "@SUCC_URL:<ID>": "https://app.notion.com/p/<map page_id>",
            "@PE_PAGE_ID": "map pe.page_id",
            "@SUCCESSOR_COUNT": "SUCCESSOR rows of the map (54 under C-1)",
            "@CURRENT_VERSION_SENTENCE": "from the map's KEPT rows",
            "@ARCHIVED_COUNT": "length of the generated move list (57 under C-1)",
            "@PACKET_PATH": "constant (W8)"},
        "frontmatter_rule": tx["frontmatter_rule"],
        "frontmatter_rule_pages": tx["frontmatter_rule_pages"],
        "generated_families": {
            "frontmatter": "the frontmatter rule on every listed page (only keys present in its frontmatter), plus "
                           "the page's frontmatter_title pair; escape-tolerant (Notion fetches show \\_)",
            "member_rows": "Flow Index topology and each hub's family rows: a predecessor row "
                           "'| <code>ID</code> | <100926.1 title> | <code>LANE</code> | <code>URL?pvs=204</code> |' "
                           "becomes the successor title and map URL; KEPT rows are unchanged; on the Change Flow hub "
                           "and the Flow Index the CL-05 row is inserted before the CL-20 row (C-9; W5 NC-1)",
            "titles": "each page's title per phase (pages.<id>.titles)",
            "catalog": "new_pages.CATALOG, 56 rows from the map and the candidate graph parts (lane, title)",
            "register_entry": "new_pages.REGISTER_ENTRY",
            "archive_moves": "moves.P5"},
        "pages": pages,
        "new_pages": {
            "CATALOG": {"phase": "candidate", "step": "C3 (C-CAT)", "parent": FLOW_INDEX, "title": cand["catalog"]["title"],
                        "frontmatter": cand["catalog"]["frontmatter"], "body": cand["catalog"]["body"],
                        "rows_rule": "one row per map member in members-100926.1.tsv order with CL-05 before CL-20: "
                                     "| <code>ID</code> | title | <code>LANE</code> | <code>https://app.notion.com/p/<id>?pvs=204</code> | "
                                     "<code>current_version</code> | (KEPT: its 100926.1 page and 100926.1)",
                        "note": cand["catalog"]["note"]},
            "REGISTER_ENTRY": {"phase": "activation", "step": "P1(a) (P1a-ENTRY)", "parent": REGISTER,
                               "title": act["register_entry"]["title"],
                               "frontmatter": act["register_entry"]["frontmatter"],
                               "body": act["register_entry"]["body"]}},
        "duplication": {"step": "C1 (C-DUP; W5 NC-2)", "rule": w8["C-DUP"]["why"],
                        "members": "transaction.candidate_publication.members of W8, read from the map at EXECUTE",
                        "cl05": f"duplicated from {CL05_CANDIDATE} and moved under 3db4590a05eb81d59059eb6b95ed5fcf",
                        "pe": f"duplicated from {PE_PRED} under the TW hub"},
        "moves": {"P5": {"new_parent": ARCHIVE_PARENT,
                         "pages": "every predecessor_page_id of a SUCCESSOR row in the map, plus "
                                  f"{PE_PRED} (PE 100926.1), {OLD_CATALOG} (the 100926.1 catalog, C-12) and "
                                  f"{CL05_CANDIDATE} (the CL-05 candidate, moved only, no banner: C-12, D-W8-10)",
                         "kept": "GCFPE-MGMT-10's 100926.1 page, the 20261009.1 register entry, the previous candidate "
                                 "inventory and every control page stay where they are",
                         "batch_limit": 100, "check_children_first": True}},
        "sweep": {"P6-SWEEP": {k: w8["P6-SWEEP"][k] for k in ("new", "starting_list", "why")}},
        "folded_and_dropped": {
            "W6-BIND-4": "folded into P1d-FI-BIND-P (D-W8-7)",
            "W6-BIND-1/2/3": "carried verbatim in P2-REG-SEL/-SRC/-PROC (D-W8-7; CD-9 under Nathan's condition)",
            "W5 NC-1": "generated catalog row (D-W8-4)",
            "W5 NC-2": "= C-DUP for CL-05",
            "W5 NC-3": "banner dropped; the candidate is moved only (C-12)",
            "carried_check": carried},
        "pin_rule": {
            "basis": "precedent PIN-1-A: a fetch's revision is the newest edit anywhere in the page's subtree, so a "
                     "page moves before its own write whenever this Modification edits it or a page under it",
            "plan_pins": PLAN_PINS,
            "repin": {
                REGISTER: ["candidate: after PART-17's W6-REG write is read back",
                           "register: after P1(a) creates the entry and P1-ENTRY-DONE is written"],
                FLOW_INDEX: ["candidate: after C-CAT creates the catalog under it",
                             "review: after C3's C-FI write", "activation: after P1(b)'s catalog write",
                             "archived: after P1(d)/P1(f) and the P5 moves"],
                "hubs": ["candidate: after C1 duplicates and C2b writes the successors under each hub (TW: and PE)",
                         "archived: after P1(e) and the P5 moves"],
                CHECKLIST: ["activation: PLAN pin, unless the C4 packet pins it later"],
                OPS_HUB: ["part17: the revision read immediately before the write (its subtree moved on 2026-10-27 "
                          "with no page edit since 2026-10-22; treat as volatile)", "sweep: likewise, after P5"],
                OVERVIEW: ["sweep: PLAN pin unless moved; a move stops P6 for a re-plan"],
                OLD_CATALOG: ["archived: PLAN pin (it is moved, not written)"],
                "@CATALOG_PAGE_ID": ["activation: its revision read back after C3 creates it, recorded in the C4 packet"],
                "@PE_PAGE_ID": ["activation: its revision after C2b's landing check, recorded in the C4 packet"],
                "@REGISTER_ENTRY_PAGE_ID": ["activation-done: after P1(a) creates it", "register-done: after P1-ENTRY-DONE",
                                            "install-done: after P2-ENTRY-DONE", "prodval-done: after P3-ENTRY-DONE",
                                            "archived: after P4-ENTRY-DONE"]},
            "renderer": "activation_render_102726.py plan --phase X compares each page's fresh revision with "
                        "--pin ID=TS when the page is listed under repin for that phase (and refuses with "
                        "PIN_REQUIRED when none is given), otherwise with plan_pins; C4's packet records each "
                        "control page's pin after its last pre-promotion write, and P0 compares them"},
    }


def selftest() -> dict:
    head = head_pe_text()
    rows = {"clean_build_passes": bool(build(head)["pages"]["@PE_PAGE_ID"]["ops"])}
    ops = build(head)["pages"]["@PE_PAGE_ID"]["ops"]
    rows["p1c_anchors_escaped"] = all("\\_" in o["start"] for o in ops if o["id"].startswith("P1c-PE-"))
    rows["p1c_marker_kept"] = any("@ACTIVATION_DATE" in o["new"] for o in ops if o["id"] == "P1c-PE-3")

    def refused(fn) -> bool:
        try:
            fn()
        except SystemExit:
            return True
        return False
    # the head written unescaped (an anchor that only the raw form would match) is refused
    rows["rejects_head_without_escaped_anchor"] = refused(lambda: build(head.replace("candidate\\_release", "candidate_release")))
    # an anchor occurring twice in the head is refused
    rows["rejects_anchor_twice_in_head"] = refused(lambda: build(head + "\npromotion\\_authorized: false\n"))
    # escaping a marker would break its fill: the round trip through the normalizer refuses it
    bad = [{"id": "P1c-PE-X", "start": "promotion_authorized: false", "end": None, "new": "activated_at: @ACTIVATION_DATE"}]
    global esc_fetch
    keep = esc_fetch
    try:
        esc_fetch = lambda s: None if s is None else s.replace("_", "\\_")  # noqa: E731  (escapes inside markers)
        rows["rejects_escaped_marker"] = refused(lambda: pe_fetch_form(bad, head))
    finally:
        esc_fetch = keep
    rows["esc_fetch_keeps_markers_and_code"] = esc_fetch("a_b <code>c_d</code> @SUCC_URL:QA-10 @ACTIVATION_DATE") == \
        "a\\_b <code>c_d</code> @SUCC_URL:QA-10 @ACTIVATION_DATE"
    return {"mode": "selftest", "rows": rows, "ok": all(rows.values())}


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "build"
    if mode == "selftest":
        res = selftest()
        print(json.dumps(res, indent=1))
        return 0 if res["ok"] else 1
    data = build()
    text = json.dumps(data, indent=1, ensure_ascii=False) + "\n"
    carried_ok = all(c["text_in_host"] for c in data["folded_and_dropped"]["carried_check"])
    if mode == "build":
        OUT.write_text(text, encoding="utf-8")
        print(json.dumps({"written": str(OUT.name), "pages": len(data["pages"]),
                          "ops": sum(len(p["ops"]) for p in data["pages"].values()),
                          "w6_bindings_carried_verbatim": carried_ok, "ok": carried_ok}, indent=1))
        return 0 if carried_ok else 1
    same = OUT.exists() and OUT.read_text(encoding="utf-8") == text
    print(json.dumps({"mode": "check", "file_equals_rebuild": same, "w6_bindings_carried_verbatim": carried_ok,
                      "ok": same and carried_ok}, indent=1))
    return 0 if same and carried_ok else 1


if __name__ == "__main__":
    sys.exit(main())
