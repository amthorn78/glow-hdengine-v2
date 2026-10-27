#!/usr/bin/env python3
"""AM-5's write-form inventory and rehearsal, for EXECUTE of MODIFICATION-20261027-gcfpe-backlog-open-items
(Nathan's decision after X9a: before C-FI, inventory every distinct write form in every remaining Notion step, X9 to
X28, and rehearse all of them in one pass on one private draft page with one child page).

    am5_rehearsal_102726.py inventory --parts P --fetched-after T [--pin ID=TS ...]
    am5_rehearsal_102726.py render    --parts P --page draft|child [--draft ID]
    am5_rehearsal_102726.py plan      --parts P --stage N --draft ID --child ID --fetched-after T
    am5_rehearsal_102726.py check     --parts P --stage N --draft ID --child ID --fetched-after T

`inventory` runs the activation chain in memory (candidate .. sweep) and classifies every write the remaining steps
make: the write tool, and each content form in its text. It adds the writes the chain does not render: X9's catalog
repair, P1a's page creation, the P1 titles, the P5 moves, X25's banners and navigation corrections, and X28's
backlog dispositions (from the backlog's own structure). Each form is mapped to the rehearsal stage that covers it.

The rehearsal, in order (each write sent once; each page read back and compared after each stage):
  1  create the draft (private, workspace level): the 102726.1 catalog's text (its first three member rows) with
     its frontmatter in X9's single-break form, plus the anchors the later stages use
  2  create the child under the draft: the register entry (AM-5's template)
  3  one update_content on the draft: the catalog's frontmatter repair, C-FI, P2-REG-SEL, P6-OV-FIND (a span over
     lines), P1d-FI-ACT (a span on one line), P5-FI-DISP (a whole line), the two generated member-row operations (a
     row replaced, and a row inserted before another), a mention of the child (P1e-HUB-TW-PE's form) and a mention
     of the draft itself
  4  one update_content on the child: P1-ENTRY-DONE (a table row) and P1c-PE-5's two-paragraph insert
  5  one update_content on the draft: C-FI-REV and P1b-CAT-1 .. 8
  6  insert_content at the end of the draft: C-REG
  7  insert_content at the start of the draft: a dated banner (X25's form)
  8  update_properties: the child retitled (the P1 titles' form)
  9  move the child to the workspace level (the P5 moves' form)
The one repeat Nathan allows (rule 1), on the same two pages, after the first pass's fixes (AM-6, AM-7):
  10 replace_content of the draft: its text with the joined frontmatter paragraph as one paragraph per line, sent in
     its written form (AM-7's form for X9's catalog repair)
  11 one update_content on the draft: P1b-CAT-1 .. 8, held from stage 5 because their anchors needed the repair
  12 move the child back under the draft (a page parent, as P5's moves are)
  13 move the child to the workspace level again (AM-6's rule)
The plan's model of each stage is activation_render_102726's: as_fetched for a created page, apply() for an
update_content (page_id given, so AM-5's mention rule applies), its append rule, add_child for a created child; and,
for a retitle and a move, the chain's own rules (the child-page block's title follows the page, a moved page leaves
its parent) plus AM-5's mention rule (a mention of a child carries its current title; a page that is no longer a child
is mentioned self-closing). A read equals the model when control_check.fold of each is equal (AM-3).

Markers that exist only after promotion take activation_render's named stand-in values; the two pages are deleted
after the rehearsal, so no stand-in value reaches a page the Modification keeps. `render` and `plan` print payloads
on stdout only (D22). Run with PYTHONDONTWRITEBYTECODE=1 and CLAUDE_CODE_SESSION_ID set.
"""
from __future__ import annotations

import argparse
import collections
import contextlib
import importlib.util
import io
import json
import os
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PLAN = HERE.parent / "plan"
sys.path.insert(0, str(PLAN))
DRAFT_TITLE = "AM-5 write-form rehearsal — draft, to be deleted"
CHILD_TITLE = "AM-5 rehearsal child — to be deleted"
CHILD_RETITLE = "AM-5 rehearsal child — retitled, to be deleted"
BANNER = ("<b>Historical record, superseded 2026-10-28.</b> The selected release is <code>GCFPE-20261027.1</code> / "
          "<code>102726.1</code>; see the [release register](https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1).")
PE_PRED = "3f44590a05eb81f98b76c83465dc1960"
STAGES = range(1, 14)


def load():
    spec = importlib.util.spec_from_file_location("ar", PLAN / "activation_render_102726.py")
    ar = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ar)
    return ar


def op_by_id(ar, oid):
    return next(o for p in ar.OPS["pages"].values() for o in p["ops"] if o["id"] == oid)


def context(ar, parts, draft="d" * 32, child="e" * 32):
    ctx = ar.Ctx(str(HERE / "successor-pages-102726.1.json"), parts,
                 {"@CATALOG_PAGE_ID": child, "@REGISTER_ENTRY_PAGE_ID": child, "@CONTROLS_PR": "770",
                  "@PUBLICATION_DATE": "2026-10-27"}, True, read_only=True)
    return ctx


def draft_content(ar, ctx) -> str:
    cat = ar.catalog_text(ctx)
    rows_seen = [0]

    def keep(line):   # the catalog's first three member rows: the forms are the same, the page shorter
        if line.startswith("| <code>"):
            rows_seen[0] += 1
            return rows_seen[0] <= 3
        return True
    ls = [x for x in cat.split("\n") if keep(x)]
    j = ls.index("---", 1)
    rest = ls[j + 1:]
    while rest and rest[0] == "":
        rest = rest[1:]
    single = "\n".join(["---", *[x for x in ls[1:j] if x], "---"]) + "\n" + "\n".join(rest)   # X9's form
    tsv = {r[0]: r for r in ctx.tsv}
    rows = [ar.row_line(pid, tsv[pid][2], tsv[pid][3], tsv[pid][1]) for pid in ("PR-30", "CL-20")]
    extra = [
        "## Historical — Alpha feedback candidate — 2026-10-09",
        "The earlier candidate is a dated record.",
        "## Current selection — GCFPE-20261009.1 / 100926.1",
        "The register selects the 100926.1 release.",
        "## Find a selected GCFPE prompt — 100926.1",
        "Use the 100926.1 catalog.",
        "After promotion both releases' pages are archived.",
        "<b>This index is operative only while the register selects </b><code>GCFPE-20261009.1</code> and members.",
        "predecessor_disposition: SUPERSEDED",
        "| ID | title | lane | page |\n| --- | --- | --- | --- |\n" + "\n".join(rows),
        f'<mention url="{ar.URL}{PE_PRED}" /> is the authoring control for this release.',
        "Self reference: rehearsal.",
    ]
    return single.rstrip("\n") + "\n\n" + "\n\n".join(extra) + "\n"


def stage_ops(ar, ctx, stage, draft, child, text):
    """The operations of an update_content stage, in the plan's own texts (rehearsal anchors where a real page's
    anchor cannot exist on the draft)."""
    if stage == 3:
        old, new = ar.frontmatter_paragraph_repair(text)
        p1e = op_by_id(ar, "P1e-HUB-TW-PE")
        ops = [{"id": "X9-CAT-REPAIR", "start": old, "end": None, "new": new},
               op_by_id(ar, "C-FI"), op_by_id(ar, "P2-REG-SEL"), op_by_id(ar, "P6-OV-FIND"),
               op_by_id(ar, "P1d-FI-ACT"), op_by_id(ar, "P5-FI-DISP"),
               {**p1e, "id": "P1e-HUB-TW-PE (child form)",
                "start": f'<mention url="{ar.URL}{PE_PRED}" /> is the authoring control for this release.',
                "new": p1e["new"].replace("@PE_PAGE_ID", child).replace("PE Metaprompt 102726.1", CHILD_TITLE)},
               {"id": "SELF-MENTION", "start": "Self reference: rehearsal.", "end": None,
                "new": f'Self reference: <mention url="{ar.URL}{draft}">{DRAFT_TITLE}</mention>.'}]
        page = {"member_rows": True}
        return ops + ar.generated(ar.C.FLOW_INDEX, page, text, "activation", ctx)
    if stage == 4:
        p1c5 = op_by_id(ar, "P1c-PE-5")
        return [op_by_id(ar, "P1-ENTRY-DONE"),
                {"id": "P1c-PE-5 (on the entry)", "start": "validation\\_status: VALIDATED", "end": None,
                 "new": p1c5["new"]}]
    if stage == 5:
        return [op_by_id(ar, "C-FI-REV")] + [op_by_id(ar, f"P1b-CAT-{i}") for i in range(1, 9)]
    if stage == 6:
        return [op_by_id(ar, "C-REG")]
    return []


def remention(ar, text, page_id, children):
    """AM-5's rule on a page after a retitle or a move: a mention of a child carries its current title; a mention of
    a page that is neither the page nor a child is self-closing."""
    def sub(m):
        t = m.group(1)
        if t == page_id:
            return m.group(0)
        if t in children:
            return f'<mention url="{ar.URL}{t}">{children[t]}</mention>'
        return f'<mention url="{ar.URL}{t}" />'
    return re.sub(r'<mention url="https://app\.notion\.com/p/([0-9a-f]{32})"(?: />|>[^<]*</mention>)', sub, text)


def models(ar, ctx, draft, child, upto, held=()):
    """[(stage, draft_text, child_text, child_title, payload)] up to `upto`, each stage applied to the previous model.
    `held`: operation ids left out of this pass (the X9b first pass: the catalog repair, which Notion did not match,
    and the catalog operations whose anchors it creates)."""
    d = ar.as_fetched(draft_content(ar, ctx))
    out = [(1, d, None, None, {"title": DRAFT_TITLE, "content": draft_content(ar, ctx)})]
    k, ktitle = None, CHILD_TITLE
    for st in range(2, upto + 1):
        pay = None
        if st == 2:
            pay = {"parent": draft, "title": CHILD_TITLE, "content": ar.entry_text(ctx)}
            k = ar.as_fetched(ar.entry_text(ctx))
            d = ar.add_child(d, child, CHILD_TITLE)
        elif st in (3, 5):
            ops = [o for o in stage_ops(ar, ctx, st, draft, child, d) if o["id"] not in held]
            d, rows = ar.apply(d, ops, ctx, draft)
            pay = {"page_id": draft, "rows": rows}
        elif st == 4:
            ops = stage_ops(ar, ctx, st, draft, child, k)
            k, rows = ar.apply(k, ops, ctx, child)
            pay = {"page_id": child, "rows": rows}
        elif st == 6:
            ops = stage_ops(ar, ctx, st, draft, child, d)
            d, rows = ar.apply(d, ops, ctx, draft)
            pay = {"page_id": draft, "rows": rows, "insert": "end"}
        elif st == 7:
            d = BANNER + "\n\n" + d
            pay = {"page_id": draft, "insert": "start", "content": BANNER}
        elif st == 8:
            d = d.replace(f"\n{CHILD_TITLE}\n</page>", f"\n{CHILD_RETITLE}\n</page>")
            ktitle = CHILD_RETITLE
            d = remention(ar, d, draft, {child: CHILD_RETITLE})
            pay = {"page_id": child, "title": CHILD_RETITLE}
        elif st in (9, 13):
            d = ar.remove_children(d, {child})   # AM-6
            pay = {"page_id": child, "new_parent": "workspace"}
        elif st == 10:
            joined = [x for x in d.split("\n") if "<br />" in x]
            assert len(joined) == 1 and d.count(joined[0]) == 1
            d = d.replace(joined[0], "\n\n".join(s.strip() for s in joined[0].split("<br />")))
            pay = {"page_id": draft, "replace": True, "new_str": ar.C.unescape(d)}
        elif st == 11:
            ops = [op_by_id(ar, f"P1b-CAT-{i}") for i in range(1, 9)]
            d, rows = ar.apply(d, ops, ctx, draft)
            pay = {"page_id": draft, "rows": rows}
        elif st == 12:
            d = remention(ar, ar.add_child(d, child, ktitle), draft, {child: ktitle})
            pay = {"page_id": child, "new_parent": draft}
        out.append((st, d, k, ktitle, pay))
    return out


# --- inventory --------------------------------------------------------------------------------------------------
STEP = {"candidate": "X9", "review": "X18", "activation": "X20", "activation-done": "X20", "register": "X21",
        "register-done": "X21", "install-done": "X22", "prodval-done": "X23", "archived": "X24", "sweep": "X25"}
FORMS = [
    ("inline code", r"<code>", 3), ("bold", r"<b>", 3), ("code inside bold", r"<b>(?:(?!</b>).)*<code>|</b><b><code>", 3),
    ("italic", r"<i>", 3), ("escaped underscore (plain-text _)", None, 3), ("separate-line paragraphs", r"\n\n", 3),
    ("heading", r"(?:^|\n)#{1,6} ", 3), ("bulleted list item", r"(?:^|\n)\s*- ", 3),
    ("numbered list item", r"(?:^|\n)\s*\d+\. ", 3), ("table row", r"(?:^|\n)\|", 4),
    ("Markdown link to a Notion page", r"\]\(https://app\.notion\.com/p/", 3),
    ("external link", r"\]\(https?://(?!app\.notion\.com)", 6), ("page mention", r"<mention", 3),
    ("typographic characters (— § ’ “)", r"[—§’“”]", 3), ("double quotes", r'"', 4)]


def classify(ar, text):
    found = []
    for name, rx, _ in FORMS:
        if rx is None:
            if "_" in re.sub(r"<code>.*?</code>", "", text):
                found.append(name)
        elif re.search(rx, text, re.S):
            found.append(name)
    return found


def inventory(ar, a) -> dict:
    steps = collections.defaultdict(lambda: {"tools": collections.Counter(), "forms": collections.Counter(), "ops": 0})
    orig = ar.apply

    def spy(text, ops, ctx, page_id=None):
        kids = dict(ar.CHILD_BLOCK.findall(text))
        for o in ops:
            st = STEP.get(o.get("phase") or spy.phase, "?")
            row = steps[st]
            row["ops"] += 1
            new = ctx.fill(o["new"]) or ""
            row["tools"]["insert_content (append)" if o.get("append") else "update_content"] += 1
            shape = ("span over lines" if o.get("lines") else "span within a line" if o.get("end")
                     else "whole line" if o.get("whole_line") else None)
            if shape:
                row["forms"][shape] += 1
            if o.get("generated") and o["id"].startswith("ROW:") and "\n" in new:
                row["forms"]["table row inserted before another"] += 1
            for f in classify(ar, new):
                row["forms"][f] += 1
            for m in ar.MENTION.finditer(new):
                rel = "self" if m.group(1) == (page_id or "") else "child" if m.group(1) in kids else "other"
                row["forms"][f"mention of {rel} page"] += 1
            for m in re.finditer(r"\]\(https://app\.notion\.com/p/([0-9a-f]{32})", new):
                row["forms"]["Markdown link to a child page" if m.group(1) in kids else
                            "Markdown link to another page"] += 1
        return orig(text, ops, ctx, page_id)
    spy.phase = ""
    gen = ar.generated

    def gen_spy(key, page, text, phase, ctx):   # the chain renders each phase's generated ops just before apply
        spy.phase = phase
        return gen(key, page, text, phase, ctx)
    ar.apply, ar.generated = spy, gen_spy
    argv = ["ar", "plan", "--successor-map", str(HERE / "successor-pages-102726.1.json"), "--parts", a.parts,
            "--phase", "sweep", "--chain", "--standin-values", "--from-phase", "candidate",
            "--set", "@CONTROLS_PR=770", "--set", "@PUBLICATION_DATE=2026-10-27",
            "--set", "@CATALOG_PAGE_ID=4064590a05eb8113ae7de73041631c00",
            "--fetched-after", a.fetched_after, "--since-minutes", "900"] + sum((["--pin", p] for p in a.pin), [])
    sys.argv = argv
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            ar.main()
        except SystemExit:
            pass
    chain = json.loads(buf.getvalue())
    ar.apply, ar.generated = orig, gen
    ctx = context(ar, a.parts)
    # writes the chain does not render
    x9 = steps["X9"]
    x9["tools"]["update_content (frontmatter repair)"] += 1
    x9["forms"]["joined paragraph replaced by separate-line paragraphs"] += 1
    x20 = steps["X20"]
    x20["tools"]["create page under a parent (P1a)"] += 1
    for f in classify(ar, ar.entry_text(ctx)) + ["divider (frontmatter ---)", "mention of other page"]:
        x20["forms"][f"created page: {f}"] += 1
    titles = [p for p in ar.OPS["pages"].values() if p.get("titles", {}).get("activation")]
    x20["tools"]["update_properties (title)"] += len(titles)
    steps["X24"]["tools"]["move pages (P5)"] += len(ctx.moves)
    steps["X25"]["tools"]["insert_content (start: a dated record's banner)"] += 1
    steps["X25"]["forms"]["bold"] += 1
    steps["X25"]["tools"]["update_content (navigation corrected)"] += 1
    steps["X25"]["forms"]["Markdown link to another page"] += 1
    x28 = steps["X28"]
    x28["tools"]["update_content (backlog dispositions)"] += 1
    for f in ("heading", "bold", "inline code", "external link", "table row", "separate-line paragraphs"):
        x28["forms"][f] += 1
    cover = {
        "update_content": 3, "insert_content (append)": 6, "insert_content (start: a dated record's banner)": 7,
        "create page under a parent (P1a)": 2, "update_properties (title)": 8, "move pages (P5)": 9,
        "update_content (frontmatter repair)": 3, "update_content (navigation corrected)": 3,
        "update_content (backlog dispositions)": 3,
        "joined paragraph replaced by separate-line paragraphs": 3, "span over lines": 3, "span within a line": 3,
        "whole line": 3, "table row inserted before another": 3, "mention of child page": 3, "mention of self page": 3,
        "mention of other page": 1, "Markdown link to a child page": 3, "Markdown link to another page": 3,
        "external link": 6, "table row": 4, "divider (frontmatter ---)": 1, "created page": 2}
    for name, _, stg in FORMS:
        cover.setdefault(name, stg)
    out, uncovered = {}, []
    for st in sorted(steps, key=lambda s: int(s[1:]) if s[1:].isdigit() else 99):
        r = steps[st]
        out[st] = {"ops": r["ops"], "tools": dict(r["tools"]), "forms": dict(sorted(r["forms"].items()))}
        for k in list(r["tools"]) + list(r["forms"]):
            key = k.split(": ", 1)[0] if k.startswith("created page") else k
            if key not in cover and k.split(": ", 1)[-1] not in cover:
                uncovered.append(f"{st}: {k}")
    return {"mode": "inventory", "chain_ok": chain.get("ok"), "chain_totals": chain.get("totals"), "steps": out,
            "covered_by_stage": cover, "uncovered": uncovered, "ok": bool(chain.get("ok")) and not uncovered,
            "d22": "transient reads of this session's harness records; counts and form names only"}


# --- reads and checks -------------------------------------------------------------------------------------------
def newest(ar, pid, after):
    return ar.C.latest(pid, os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"], 600, after)


def compare(ar, real, want) -> dict:
    a, b = ar.C.fold(real).split("\n"), ar.C.fold(want).split("\n")
    diff = [i for i in range(min(len(a), len(b))) if a[i] != b[i]]
    return {"real_lines": len(a), "model_lines": len(b), "equal": a == b, "differing_line_indexes": diff[:6],
            "line_count_difference": len(a) - len(b)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("inventory", "render", "plan", "check"))
    ap.add_argument("--parts", required=True)
    ap.add_argument("--page", choices=("draft", "child"))
    ap.add_argument("--stage", type=int)
    ap.add_argument("--draft", default="d" * 32)
    ap.add_argument("--child", default="e" * 32)
    ap.add_argument("--fetched-after", default="")
    ap.add_argument("--pin", action="append", default=[])
    ap.add_argument("--held", nargs="*", default=[])
    a = ap.parse_args()
    ar = load()
    if a.mode == "inventory":
        res = inventory(ar, a)
        print(json.dumps(res, indent=1, ensure_ascii=False))
        return 0 if res["ok"] else 1
    ctx = context(ar, a.parts, a.draft, a.child)
    if a.mode == "render":
        m = models(ar, ctx, a.draft, a.child, 2, set(a.held))
        print(json.dumps(m[0][4] if a.page == "draft" else m[1][4], ensure_ascii=False, indent=1))
        return 0
    held = set(a.held)
    if "X9-CAT-REPAIR" in held:
        held |= {f"P1b-CAT-{i}" for i in range(1, 9)}
    ms = models(ar, ctx, a.draft, a.child, max(a.stage, 1), held)
    if a.mode == "plan" and a.stage < 2:
        print(json.dumps({"ok": False, "error": "STAGE_1_IS_RENDER"}))
        return 1
    if a.mode == "plan":
        prev = ms[a.stage - 2]
        rd, rk = newest(ar, a.draft, a.fetched_after), newest(ar, a.child, a.fetched_after) if a.stage > 2 else None
        before = {"draft": compare(ar, rd[3], prev[1]) if rd else None,
                  "child": compare(ar, rk[3], prev[2]) if rk and prev[2] is not None else None}
        if not rd or not before["draft"]["equal"] or (a.stage > 2 and not (before["child"] or {}).get("equal")):
            print(json.dumps({"ok": False, "error": "READ_NOT_AT_PREVIOUS_MODEL", "before": before}))
            return 1
        pay = ms[a.stage - 1][4]
        if "rows" in pay:
            refused = [(r["id"], r["refusal"]) for r in pay["rows"] if not r["applied"]]
            if refused:
                print(json.dumps({"ok": False, "error": "OPERATION_REFUSED", "refused": refused}))
                return 1
            pay = {"page_id": pay["page_id"], **({"insert": pay["insert"]} if pay.get("insert") else {}),
                   "ops": [r["id"] for r in pay["rows"]],
                   **({"content": pay["rows"][0]["new_str"]} if pay.get("insert") else
                      {"content_updates": [{"old_str": r["old_str"], "new_str": r["new_str"]} for r in pay["rows"]]})}
        print(json.dumps({"ok": True, "stage": a.stage, **pay}, ensure_ascii=False, indent=1))
        return 0
    st = ms[a.stage - 1]
    rd = newest(ar, a.draft, a.fetched_after)
    out = {"stage": a.stage, "draft": None, "child": None}
    if rd:
        out["draft"] = {"as_of": rd[1], "title": rd[2], "title_ok": rd[2] == DRAFT_TITLE, **compare(ar, rd[3], st[1])}
    if st[2] is not None:
        rk = newest(ar, a.child, a.fetched_after)
        if rk:
            out["child"] = {"as_of": rk[1], "title": rk[2], "title_ok": rk[2] == st[3], **compare(ar, rk[3], st[2])}
    out["ok"] = bool(out["draft"] and out["draft"]["equal"] and out["draft"]["title_ok"]
                     and (st[2] is None or (out["child"] and out["child"]["equal"] and out["child"]["title_ok"])))
    out["d22"] = "transient reads of this session's harness records; counts, titles and line indexes only"
    print(json.dumps(out, indent=1, ensure_ascii=False))
    return 0 if out["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
