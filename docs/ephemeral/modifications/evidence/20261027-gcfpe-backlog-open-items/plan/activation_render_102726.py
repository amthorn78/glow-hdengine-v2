#!/usr/bin/env python3
"""Activation rendering for MODIFICATION-20261027-gcfpe-backlog-open-items (PLAN assembly A4; W8 transaction and
notion_control_ops, W6 notion_control_ops, W5 NC ops; adapted from
docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/plan/activation_render.py).

  activation_render_102726.py plan  --successor-map F --parts P --phase PH [--pages ID ...] [--set @KEY=VALUE ...]
                                    [--pin ID=TS ...] [--fetched-after T] [--since-minutes N] [--emit]
        EXECUTE: on the newest fresh read of each page that has operations in phase PH: refuse a revision other than
        its pin (activation-ops.json pin_rule: a page listed under repin for PH needs --pin, else PIN_REQUIRED);
        require every earlier phase's listed operation on the page LANDED; build PH's operations (the file's own, plus
        the generated families from the successor map and the candidate graph parts: frontmatter rule and title,
        Flow Index topology and hub member rows with CL-05 before CL-20); apply them in memory, refusing an anchor
        that does not resolve exactly once (in its raw or its Notion-escaped form, C-5 Q-6) and an unsafe batch; then
        run control_check_102726.py's rules for PH on the rendered text. New pages (the catalog at candidate, the
        register entry at activation) are rendered from the map and the parts and checked the same way. --emit adds
        each operation's old_str and new_str, the new pages' content and the P5 move list: terminal only, never
        redirected into the repository.
  activation_render_102726.py plan  ... --chain
        PLAN dry run: start from the PLAN reads (each page's revision must equal its PLAN pin), and apply every phase
        up to PH in order, in memory, simulating only what Notion does on its own (a created or duplicated page appears
        as a child-page block of its parent; a retitled child shows its new title; a moved page leaves its parent).
        After each phase, the phase's control rules run on every rendered page. PE's base is the coordinator's head
        replacement (edits.json HEAD-PE), not its body (D22). With a stand-in map, every marker without a --set
        value takes a named stand-in value, and the receipt lists them.
  activation_render_102726.py check --successor-map F --parts P --phase PH [--pages ...] [--set ...] [--pin ...]
        After PH's writes, on fresh reads: every listed operation of PH LANDED, the revision moved from its pin, and
        control_check_102726.py's rules for PH pass (the generated families are verified by those rules: titles,
        links at the map's ids, no retired value).
  activation_render_102726.py selftest --successor-map F --parts P
        synthetic pages: a clean page renders and passes; a missing anchor, a doubled anchor, an unfilled marker, an
        escaped anchor, a whole-line anchor that is only a prefix, an unsafe batch, a stale pin, a missing --pin, a
        rendered page that keeps a retired value and a catalog missing a member each fail.

The successor map is the only source of successor ids, titles and dispositions (W7 successor_page_map); with a
stand-in map the ids are binding_pass.probe() synthetic ids, so retired predecessors and successors stay distinct,
and every report says stand_in: true. Control-page text is read as a transient read of this session's harness
records (control_check_102726.latest); reports carry counts, ids and booleans. Run with PYTHONDONTWRITEBYTECODE=1
and CLAUDE_CODE_SESSION_ID set.
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
sys.path.insert(0, str(HERE))
import control_check_102726 as C  # noqa: E402

OPS = json.loads((HERE / "activation-ops.json").read_text(encoding="utf-8"))
EDITS = HERE / "edits.json"
MARKER = re.compile(r"@[A-Z][A-Z0-9_]+(?::[A-Z0-9-]+)?")
PHASES = [p["id"] for p in OPS["phases"]]
CONTROL_PHASE = {"part17": None, "candidate": "candidate", "review": "candidate", "activation": "activation",
                 "activation-done": "activation", "register": "activation", "register-done": "activation",
                 "install-done": "activation", "prodval-done": "activation", "archived": "archived", "sweep": "sweep"}
REGISTER_PENDING = {"activation", "activation-done"}
PACKET_PATH = "docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/execute/PROMOTION-PACKET.md"
URL = "https://app.notion.com/p/"
VIRTUAL = {"@CATALOG_PAGE_ID": "CATALOG", "@PE_PAGE_ID": "PE", "@REGISTER_ENTRY_PAGE_ID": "ENTRY"}
# Named stand-in values for the PLAN dry run only (refused with a real map); none names a retired value.
STANDIN_VALUES = {
    "@PUBLICATION_DATE": "2026-10-27", "@ACTIVATION_DATE": "2026-10-28", "@ARCHIVAL_DATE": "2026-10-28",
    "@PRODUCTION_TOKEN": "56 nodes · 240 edges · 56 state_routes · STANDIN bytes · sha256 STANDIN…",
    "@POSTFLIGHT_VERDICT": "<code>STANDIN-REVIEW-POSTFLIGHT-A.md</code> and <code>STANDIN-REVIEW-POSTFLIGHT-B.md</code>: STANDIN",
    "@D24_RECORDS": "<code>STANDIN-REVIEW-D24-A.md</code> and <code>STANDIN-REVIEW-D24-B.md</code>: STANDIN",
    "@PROMOTION_APPROVED_AT": "2026-10-28", "@PROMOTION_D": "D31", "@PROCEDURE_PR": "0",
    "@REGISTER_SELECTED_AT": "2026-10-28T00:00:00.000Z", "@QUAL_VALIDATORS_PATH": "STANDIN/qualification-validators.json",
    "@QUAL_FIXTURES_PATH": "STANDIN/qualification-fixtures.json",
    "@QUAL_RECEIPT_PATHS": "<code>STANDIN/validators.json</code>, <code>STANDIN/fixtures.json</code>, <code>STANDIN/registry.json</code>",
    "@INSTALL_RECEIPT": "STANDIN-install.json", "@PRODVAL_RECEIPT": "STANDIN-prodval.json",
    "@ARCHIVAL_RECEIPT": "STANDIN-archival.json"}


# --- map, parts, markers ---------------------------------------------------------------------------------------
class Ctx:
    def __init__(self, map_path: str, parts: str, values: dict, standin_fill: bool):
        self.raw = json.loads(Path(map_path).read_text(encoding="utf-8"))
        self.stand_in = bool(self.raw.get("stand_in"))
        if standin_fill and not self.stand_in:
            raise SystemExit("stand-in marker values are refused with a real successor map")
        catalog = values.get("@CATALOG_PAGE_ID") or (C.probe_id("CATALOG") if self.stand_in else "")
        entry = values.get("@REGISTER_ENTRY_PAGE_ID") or (C.probe_id("ENTRY") if self.stand_in else "")
        self.cc = C.context(map_path, catalog, entry)
        self.map = self.cc["map"]
        self.nodes = {}
        for f in sorted(Path(parts, "prompts").glob("*.json")):
            n = json.loads(f.read_text(encoding="utf-8"))["node"]
            self.nodes[n["id"]] = n
        self.tsv = C.tsv_rows()
        self.errors = []
        for pid, row in self.map["members"].items():
            node = self.nodes.get(pid)
            if node is None:
                self.errors.append(f"PARTS_MISSING:{pid}")
            elif node["title"] != row["title"]:
                self.errors.append(f"TITLE_MAP_PARTS_DIFFER:{pid}")
        if len(self.map["members"]) != 56:
            self.errors.append("MAP_NOT_56")
        self.values = dict(values)
        self.values.setdefault("@CATALOG_PAGE_ID", catalog)
        self.values.setdefault("@REGISTER_ENTRY_PAGE_ID", entry)
        self.values["@PE_PAGE_ID"] = self.map["pe"]["page_id"]
        self.values["@PACKET_PATH"] = PACKET_PATH
        succ = [p for p, r in self.map["members"].items() if r["disposition"] == "SUCCESSOR"]
        kept = [p for p, r in self.map["members"].items() if r["disposition"] == "KEPT"]
        self.values["@SUCCESSOR_COUNT"] = str(len(succ))
        verb = "is" if len(kept) == 1 else "are"
        self.values["@CURRENT_VERSION_SENTENCE"] = (
            f"{', '.join(kept)} {verb} <code>{C.OLD_VER}</code>; the other {56 - len(kept)} members are "
            f"<code>{C.NEW_VER}</code>.")
        self.moves = move_list(self.raw)
        self.values["@ARCHIVED_COUNT"] = str(len(self.moves))
        self.standin_used = []
        if standin_fill:
            for k, v in STANDIN_VALUES.items():
                if k not in self.values:
                    self.values[k] = v
                    self.standin_used.append(k)

    def fill(self, text):
        if text is None:
            return None

        def one(m):
            key = m.group(0)
            if key.startswith("@SUCC_URL:"):
                row = self.map["members"].get(key.split(":", 1)[1])
                return URL + row["page_id"] if row else key
            return str(self.values[key]) if key in self.values and self.values[key] else key
        return MARKER.sub(one, text)


def move_list(raw: dict) -> list:
    out = [r["predecessor_page_id"] for r in raw["members"].values() if r["disposition"] == "SUCCESSOR"]
    return out + [raw["pe"]["predecessor_page_id"], C.OLD_CATALOG, C.CL05_CANDIDATE]


# --- escape-tolerant spans -------------------------------------------------------------------------------------
def esc(s):
    """A string as Notion's fetch renders it: every underscore outside <code>…</code> escaped."""
    if s is None:
        return None
    parts = re.split(r"(<code>.*?</code>)", s)
    return "".join(p if p.startswith("<code>") else p.replace("\\_", "_").replace("_", "\\_") for p in parts)


def occ(text: str, s: str, whole_line: bool = False) -> int:
    if not s:
        return 0
    if whole_line:
        return sum(1 for line in text.split("\n") if line == s)
    n, i = 0, text.find(s)
    while i >= 0:
        n += 1
        i = text.find(s, i + 1)
    return n


def find(text: str, s: str, whole_line: bool) -> int:
    if not whole_line:
        return text.find(s)
    pos = 0
    for line in text.split("\n"):
        if line == s:
            return pos
        pos += len(line) + 1
    return -1


def form(text: str, op: dict) -> tuple:
    """(start, end, new, form name) in the form the page carries, or (None, reason)."""
    wl = op.get("whole_line", False)
    raw_n, esc_n = occ(text, op["start"], wl), occ(text, esc(op["start"]), wl)
    same = esc(op["start"]) == op["start"]
    if raw_n == 1 and (same or esc_n == 0):
        return op["start"], op.get("end"), op["new"], "raw"
    if esc_n == 1 and raw_n == 0:
        return esc(op["start"]), esc(op.get("end")), esc(op["new"]), "escaped"
    return None, f"START_COUNT_{raw_n if same else raw_n + esc_n}"


def resolve(text: str, op: dict):
    got = form(text, op)
    if got[0] is None:
        return None, got[1], None
    start, end, new, name = got
    wl = op.get("whole_line", False)
    i = find(text, start, wl)
    if end is None:
        return (i, i + len(start)), None, (new, name)
    j = text.find(end, i + len(start))
    if op.get("lines") is not None:
        if j < 0 or occ(text[i + len(start):], end) != 1:
            return None, "END_NOT_UNIQUE_AFTER_START", None
        span_lines = text[i:j + len(end)].count("\n")
        if span_lines != op["lines"]:
            return None, f"SPAN_LINES_{span_lines}", None
        return (i, j + len(end)), None, (new, name)
    line_end = text.find("\n", i)
    line_end = len(text) if line_end < 0 else line_end
    if j < 0 or j + len(end) > line_end:
        return None, "END_NOT_ON_LINE", None
    return (i, j + len(end)), None, (new, name)


def apply(text: str, ops: list, ctx: Ctx):
    rows = []
    for op in ops:
        op = {**op, "new": ctx.fill(op["new"])}
        row = {"id": op["id"], "applied": False, "refusal": None, "generated": op.get("generated", False)}
        if MARKER.findall(op["new"] or ""):
            row["refusal"] = "UNFILLED_MARKER"
            row["markers"] = sorted(set(MARKER.findall(op["new"])))
            rows.append(row)
            continue
        if op.get("append"):
            if occ(text, op["new"]) or occ(text, esc(op["new"])):
                row["refusal"] = "APPEND_ALREADY_PRESENT"
            else:
                text = text.rstrip("\n") + "\n\n" + op["new"] + "\n"
                row["applied"] = True
                row["old_str"], row["new_str"] = None, op["new"]
                row["append"] = True
            rows.append(row)
            continue
        span, why, got = resolve(text, op)
        if span is None:
            row["refusal"] = why
            rows.append(row)
            continue
        new, name = got
        old = text[span[0]:span[1]]
        after = text[:span[0]] + new + text[span[1]:]
        row["form"] = name
        row["old_str_once_at_application"] = occ(text, old) == 1
        row["old_str_only_in_own_new_after"] = occ(after, old) == occ(new, old)
        row["applied"] = row["old_str_once_at_application"] and row["old_str_only_in_own_new_after"]
        if row["applied"]:
            text = after
            row["old_str"], row["new_str"] = old, new
        else:
            row["refusal"] = "BATCH_UNSAFE"
        rows.append(row)
    return text, rows


def landed(text: str, op: dict, page_ops: list, ctx: Ctx) -> bool:
    """LANDED: the start anchor occurs only inside the replacements this page carries, and the replacement is
    present (a deletion: the anchor gone). Raw and escaped forms are counted together."""
    new = ctx.fill(op["new"]) or ""
    if op.get("append"):
        return occ(text, new) + occ(text, esc(new)) >= 1
    news = [ctx.fill(o["new"]) or "" for o in page_ops]
    s, wl = op["start"], op.get("whole_line", False)
    n_text = occ(text, s, wl) + (occ(text, esc(s), wl) if esc(s) != s else 0)
    n_want = sum(occ(x, s, wl) + (occ(x, esc(s), wl) if esc(s) != s else 0) for x in news)
    if n_text != n_want:
        return False
    return new == "" or occ(text, new) + (occ(text, esc(new)) if esc(new) != new else 0) >= 1


# --- generated families ----------------------------------------------------------------------------------------
def row_line(pid: str, title: str, lane: str, page_id: str) -> str:
    return f"| <code>{pid}</code> | {title} | <code>{lane}</code> | <code>{URL}{page_id}?pvs=204</code> |"


def generated(key: str, page: dict, text: str, phase: str, ctx: Ctx) -> list:
    out = []
    if phase != "activation":
        return out
    if page.get("frontmatter_rule"):
        fm = [C.unescape(l).strip() for p, l, _ in C.sections(text) if p == ("<frontmatter>",)]
        for old, new in OPS["frontmatter_rule"].items():
            whole = not old.startswith("GCFPE-")  # every rule key is a whole line but the selection_rule fragment
            present = old in fm if whole else any(old in l for l in fm)
            if present:
                out.append({"id": f"FM:{old.split(':')[0]}", "start": old, "end": None, "new": new,
                            "whole_line": whole, "generated": True})
        if page.get("frontmatter_title"):
            old, new = page["frontmatter_title"]
            out.append({"id": "FM:title", "start": old, "end": None, "new": new, "whole_line": True, "generated": True})
    if page.get("member_rows"):
        members = ctx.map["members"]
        cl05 = members["CL-05"]
        for pid, pred, old_title, lane in ctx.tsv:
            old = row_line(pid, old_title, lane, pred)
            if occ(text, old) + occ(text, esc(old)) == 0:
                continue
            row = members[pid]
            new = old if row["disposition"] == "KEPT" else row_line(pid, row["title"], ctx.nodes[pid]["lane"], row["page_id"])
            if pid == "CL-20" and key in (C.CF_HUB, C.FLOW_INDEX):
                new = row_line("CL-05", cl05["title"], ctx.nodes["CL-05"]["lane"], cl05["page_id"]) + "\n" + new
            if new != old:
                out.append({"id": f"ROW:{pid}", "start": old, "end": None, "new": new, "whole_line": True,
                            "generated": True})
    return out


def catalog_text(ctx: Ctx) -> str:
    spec = OPS["new_pages"]["CATALOG"]
    members = ctx.map["members"]
    order = [pid for pid, *_ in ctx.tsv]
    order.insert(order.index("CL-20"), "CL-05")
    rows = []
    for pid in order:
        r = members[pid]
        ver = C.OLD_VER if r["disposition"] == "KEPT" else C.NEW_VER
        rows.append(f"| <code>{pid}</code> | {r['title']} | <code>{ctx.nodes[pid]['lane']}</code> | "
                    f"<code>{URL}{r['page_id']}?pvs=204</code> | <code>{ver}</code> |")
    blocks = ["---", *spec["frontmatter"], "---"]
    body = []
    for line in spec["body"]:
        if line.startswith("@ROWS"):
            body[-1] = body[-1] + "\n" + "\n".join(rows)
        elif line.startswith("| --- |"):
            body[-1] = body[-1] + "\n" + line
        else:
            body.append(line)
    return ctx.fill("\n".join(blocks) + "\n" + "\n\n".join(body) + "\n")


def entry_text(ctx: Ctx) -> str:
    spec = OPS["new_pages"]["REGISTER_ENTRY"]
    body, table = [], []
    for line in spec["body"]:
        if line.startswith("|"):
            table.append(line)
        else:
            body.append(line)
    return ctx.fill("---\n" + "\n".join(spec["frontmatter"]) + "\n---\n" + "\n\n".join(body) + "\n\n"
                    + "\n".join(table) + "\n")


def pe_head(ctx: Ctx) -> str:
    """The coordinator's PE head replacement (edits.json HEAD-PE), the only PE text the dry run uses (D22)."""
    e = json.loads(EDITS.read_text(encoding="utf-8"))
    head = next(o for o in e["ops"] if o["id"] == "HEAD-PE")["new"]
    return head.replace("@SUCC_TITLE_PE", ctx.map["pe"]["title"])


def as_fetched(content: str) -> str:
    """How Notion's fetch renders a page written from `content`: frontmatter lines as paragraphs, underscores
    outside code escaped (observed on the 100926.1 catalog the precedent created from unescaped text)."""
    lines = content.split("\n")
    if lines and lines[0] == "---":
        j = lines.index("---", 1)
        fm = "\n\n".join(lines[: j + 1])
        content = fm + "\n\n" + "\n".join(lines[j + 1:])
    return esc(content)


# --- pins ------------------------------------------------------------------------------------------------------
def repin_required(key: str, phase: str) -> bool:
    rp = OPS["pin_rule"]["repin"]
    entries = rp.get(key, []) + (rp.get("hubs", []) if key in C.HUB_NAMES else [])
    return any(e.split(":", 1)[0].strip() == phase for e in entries)


# --- render -----------------------------------------------------------------------------------------------------
def page_ops(key: str, phase: str) -> list:
    return [o for o in OPS["pages"][key]["ops"] if o["phase"] == phase]


REPORT_LINES = {"on": False}


def control(key: str, title: str, text: str, ctx: Ctx, phase: str) -> dict:
    cphase = CONTROL_PHASE[phase]
    if cphase is None:
        return {"ok": True, "judged": False}
    name = VIRTUAL.get(key, key)
    if cphase == "sweep" and key not in C.SWEEP_PAGES:
        cphase = "archived"
    if cphase != "sweep" and key in C.SWEEP_PAGES:
        return {"ok": True, "judged": False}
    if name == "ENTRY":
        left = MARKER.findall(text)
        return {"ok": not left, "judged": True, "markers_left": len(left)}
    if name == "PE" and cphase == "candidate":
        return {"ok": True, "judged": False}
    res = C.check_text(name, title, text, ctx.cc, cphase, phase in REGISTER_PENDING)
    out = {"ok": res["ok"], "judged": True, "findings": res["findings"], "failed_checks": res["failed_checks"],
           "finding_sections": sorted({f["section"] for f in res["finding_rows"]})}
    if REPORT_LINES["on"]:  # terminal only; never redirect into the repository
        out["excerpts"] = [f["excerpt"] for f in res["finding_rows"]]
    return out


def chain(a, ctx: Ctx) -> dict:
    root, session = os.path.expanduser("~/.claude/projects"), os.environ.get("CLAUDE_CODE_SESSION_ID")
    upto = PHASES.index(a.phase)
    state, report, ok = {}, {"pages": {}, "phases": []}, True
    keys = [k for k in OPS["pages"] if not a.pages or k in a.pages or VIRTUAL.get(k) in a.pages]
    for key in keys:
        page = OPS["pages"][key]
        if key in VIRTUAL:
            continue
        got = C.latest(key, root, session, a.since_minutes, a.fetched_after)
        if got is None:
            report["pages"][key] = {"error": "NO_FETCH_FOUND"}
            ok = False
            continue
        pin = dict(x.split("=", 1) for x in a.pin).get(key, page["pin"])
        state[key] = {"text": got[3], "title": got[2]}
        report["pages"][key] = {"name": page["name"], "as_of": got[1], "pin": pin, "revision_matches_pin": got[1] == pin}
        ok &= got[1] == pin
    # pins of pages only read (not written) by the transaction: the 100926.1 catalog
    old_cat = C.latest(C.OLD_CATALOG, root, session, a.since_minutes, a.fetched_after)
    report["read_only_pins"] = {C.OLD_CATALOG: {"as_of": old_cat[1] if old_cat else None,
                                                "pin": OPS["pin_rule"]["plan_pins"][C.OLD_CATALOG],
                                                "revision_matches_pin": bool(old_cat) and old_cat[1] == OPS["pin_rule"]["plan_pins"][C.OLD_CATALOG]}}
    ok &= report["read_only_pins"][C.OLD_CATALOG]["revision_matches_pin"]
    totals = {"listed": 0, "generated": 0, "applied": 0, "refused": 0}
    for ph in PHASES[: upto + 1]:
        prow = {"phase": ph, "pages": {}}
        # what Notion does on its own before or at this phase
        if ph == "candidate":
            for pid, r in ctx.map["members"].items():  # C1: successors appear under their parents
                if r["disposition"] in ("SUCCESSOR", "ADDED"):
                    parent = C.registry_parents().get(pid, C.CF_HUB)
                    if parent in state:
                        state[parent]["text"] += f'\n<page url="{URL}{r["page_id"]}">\n{r["title"]}\n</page>\n'
            if C.TW_HUB in state:
                state[C.TW_HUB]["text"] += f'\n<page url="{URL}{ctx.map["pe"]["page_id"]}">\n{ctx.map["pe"]["title"]}\n</page>\n'
            if "@CATALOG_PAGE_ID" in keys:
                cat = catalog_text(ctx)
                state["@CATALOG_PAGE_ID"] = {"text": as_fetched(cat), "title": OPS["new_pages"]["CATALOG"]["title"]}
                report["new_pages"] = {"CATALOG": {"markers_left": len(MARKER.findall(cat)),
                                                   "rows": cat.count("\n| <code>"), "chars": len(cat)}}
                if C.FLOW_INDEX in state:
                    state[C.FLOW_INDEX]["text"] += f'\n<page url="{URL}{ctx.values["@CATALOG_PAGE_ID"]}">\n{OPS["new_pages"]["CATALOG"]["title"]}\n</page>\n'
            if "@PE_PAGE_ID" in keys:
                state["@PE_PAGE_ID"] = {"text": pe_head(ctx), "title": ctx.map["pe"]["title"]}
        if ph == "activation" and "@REGISTER_ENTRY_PAGE_ID" in keys:
            ent = entry_text(ctx)
            state["@REGISTER_ENTRY_PAGE_ID"] = {"text": as_fetched(ent), "title": OPS["new_pages"]["REGISTER_ENTRY"]["title"]}
            report.setdefault("new_pages", {})["REGISTER_ENTRY"] = {"markers_left": len(MARKER.findall(ent))}
            if C.REGISTER in state:
                state[C.REGISTER]["text"] += f'\n<page url="{URL}{ctx.values["@REGISTER_ENTRY_PAGE_ID"]}">\n{OPS["new_pages"]["REGISTER_ENTRY"]["title"]}\n</page>\n'
        if ph == "archived":
            gone = set(ctx.moves)
            for st in state.values():
                st["text"] = re.sub(r'\n?<page url="https://app\.notion\.com/p/([0-9a-f]{32})">\n[^\n]*\n</page>\n?',
                                    lambda m: "\n" if m.group(1) in gone else m.group(0), st["text"])
        for key in keys:
            if key not in state:
                continue
            page = OPS["pages"][key]
            ops = page_ops(key, ph)
            gen = generated(key, page, state[key]["text"], ph, ctx)
            if ops or gen:
                text, rows = apply(state[key]["text"], ops + gen, ctx)
                state[key]["text"] = text
                refused = [{"id": r["id"], "refusal": r["refusal"], **({"markers": r["markers"]} if "markers" in r else {})}
                           for r in rows if not r["applied"]]
                totals["listed"] += len(ops)
                totals["generated"] += len(gen)
                totals["applied"] += sum(r["applied"] for r in rows)
                totals["refused"] += len(refused)
                prow["pages"][key] = {"listed": len(ops), "generated": len(gen), "applied": sum(r["applied"] for r in rows),
                                      "escaped_form": sum(r.get("form") == "escaped" for r in rows), "refused": refused}
                ok &= not refused
            new_title = page.get("titles", {}).get(ph)
            if new_title:
                old_title = state[key]["title"]
                state[key]["title"] = new_title
                for st in state.values():  # a retitled child shows its new title in its parent
                    st["text"] = st["text"].replace(f"\n{old_title}\n</page>", f"\n{new_title}\n</page>")
        checks = {}
        for key in keys:
            if key in state:
                res = control(key, state[key]["title"], state[key]["text"], ctx, ph)
                if res.get("judged"):
                    checks[key] = res
                    ok &= res["ok"]
        prow["control"] = {"phase_rules": CONTROL_PHASE[ph], "register_pending": ph in REGISTER_PENDING,
                           "pages_judged": len(checks), "pages_ok": sum(r["ok"] for r in checks.values()),
                           "findings": sum(r.get("findings", 0) for r in checks.values()),
                           "failing": {k: {x: r[x] for x in ("findings", "failed_checks", "finding_sections", "markers_left", "excerpts") if x in r}
                                       for k, r in checks.items() if not r["ok"]}}
        report["phases"].append(prow)
    report["moves"] = {"P5": len(ctx.moves), "distinct": len(set(ctx.moves)),
                       "equal_to_control_archive_set": set(ctx.moves) == set(ctx.cc["archive_102726"])}
    ok &= report["moves"]["equal_to_control_archive_set"] and len(ctx.moves) == 57
    report["totals"] = totals
    return report, ok


def run_plan(a) -> dict:
    values = dict(x.split("=", 1) for x in a.set)
    REPORT_LINES["on"] = getattr(a, "report_lines", False)
    ctx = Ctx(a.successor_map, a.parts, values, a.chain and a.standin_values)
    base = {"mode": "plan-chain" if a.chain else "plan", "phase": a.phase, "stand_in": ctx.stand_in,
            "stand_in_ids": "binding_pass.probe() synthetic ids" if ctx.stand_in else None,
            "stand_in_marker_values": ctx.standin_used, "map_parts_errors": ctx.errors}
    if a.chain:
        rep, ok = chain(a, ctx)
        res = {**base, **rep}
        res["ok"] = ok and not ctx.errors
        return res
    root, session = os.path.expanduser("~/.claude/projects"), os.environ.get("CLAUDE_CODE_SESSION_ID")
    pins = dict(x.split("=", 1) for x in a.pin)
    out, ok = [], not ctx.errors
    for key, page in OPS["pages"].items():
        ops = page_ops(key, a.phase)
        real = ctx.values.get(key, key) if key in VIRTUAL else key
        if a.pages and key not in a.pages and real not in a.pages:
            continue
        if not ops and not (page.get("frontmatter_rule") or page.get("member_rows")) or (not ops and a.phase != "activation"):
            continue
        got = C.latest(real, root, session, a.since_minutes, a.fetched_after) if real and not real.startswith("@") else None
        if got is None:
            out.append({"page": key, "error": "NO_FETCH_FOUND"})
            ok = False
            continue
        row = {"page": key, "id": real, "name": page["name"], "as_of": got[1]}
        if repin_required(key, a.phase) and key not in pins and real not in pins:
            row["refusal"] = "PIN_REQUIRED"
            out.append(row)
            ok = False
            continue
        pin = pins.get(key, pins.get(real, page.get("pin")))
        row["revision_matches_pin"] = pin is None or got[1] == pin
        prior = [o for o in page["ops"] if PHASES.index(o["phase"]) < PHASES.index(a.phase)]
        row["prior_not_landed"] = [o["id"] for o in prior if not landed(got[3], o, prior, ctx)]
        gen = generated(key, page, got[3], a.phase, ctx)
        text, rows = apply(got[3], ops + gen, ctx)
        row.update({"ops_listed": len(ops), "ops_generated": len(gen), "applied": sum(r["applied"] for r in rows),
                    "refused": [{"id": r["id"], "refusal": r["refusal"]} for r in rows if not r["applied"]]})
        title = page.get("titles", {}).get(a.phase) or got[2]
        row["control"] = control(key, title, text, ctx, a.phase)
        if a.emit:
            row["ops_payload_for_execute"] = [{"id": r["id"], "old_str": r.get("old_str"), "new_str": r.get("new_str"),
                                               "append": r.get("append", False)} for r in rows if r["applied"]]
            row["title_for_execute"] = page.get("titles", {}).get(a.phase)
        row["ok"] = (row["revision_matches_pin"] and not row["prior_not_landed"] and not row["refused"]
                     and row["control"]["ok"])
        ok &= row["ok"]
        out.append(row)
    res = {**base, "pages": out}
    if a.phase == "candidate":
        cat = catalog_text(ctx)
        chk = C.check_text("CATALOG", OPS["new_pages"]["CATALOG"]["title"], as_fetched(cat), ctx.cc, "candidate")
        res["new_pages"] = {"CATALOG": {"markers_left": len(MARKER.findall(cat)), "ok": chk["ok"] and not MARKER.findall(cat),
                                        "parent": OPS["new_pages"]["CATALOG"]["parent"]}}
        if a.emit:
            res["new_pages"]["CATALOG"]["content"] = cat
        ok &= res["new_pages"]["CATALOG"]["ok"]
    if a.phase == "activation":
        ent = entry_text(ctx)
        res["new_pages"] = {"REGISTER_ENTRY": {"markers_left": len(MARKER.findall(ent)), "ok": not MARKER.findall(ent),
                                               "parent": OPS["new_pages"]["REGISTER_ENTRY"]["parent"]}}
        if a.emit:
            res["new_pages"]["REGISTER_ENTRY"]["content"] = ent
        ok &= res["new_pages"]["REGISTER_ENTRY"]["ok"]
    if a.phase == "archived":
        res["moves"] = {"new_parent": OPS["moves"]["P5"]["new_parent"], "count": len(ctx.moves)}
        if a.emit:
            res["moves"]["pages"] = ctx.moves
    res["ok"] = ok
    res["d22"] = "transient reads of this session's harness records; control pages only; counts, ids and booleans"
    return res


def run_check(a) -> dict:
    values = dict(x.split("=", 1) for x in a.set)
    ctx = Ctx(a.successor_map, a.parts, values, False)
    root, session = os.path.expanduser("~/.claude/projects"), os.environ.get("CLAUDE_CODE_SESSION_ID")
    pins = dict(x.split("=", 1) for x in a.pin)
    out, ok = [], not ctx.errors
    for key, page in OPS["pages"].items():
        ops = page_ops(key, a.phase)
        real = ctx.values.get(key, key) if key in VIRTUAL else key
        if (a.pages and key not in a.pages and real not in a.pages) or not (ops or (a.phase == "activation" and page.get("titles", {}).get("activation"))):
            continue
        got = C.latest(real, root, session, a.since_minutes, a.fetched_after)
        if got is None:
            out.append({"page": key, "error": "NO_FETCH_FOUND"})
            ok = False
            continue
        upto = [o for o in page["ops"] if PHASES.index(o["phase"]) <= PHASES.index(a.phase)]
        not_landed = [o["id"] for o in ops if not landed(got[3], o, upto, ctx)]
        pin = pins.get(key, pins.get(real, page.get("pin")))
        row = {"page": key, "id": real, "as_of": got[1], "landed": len(ops) - len(not_landed), "not_landed": not_landed,
               "revision_moved": pin is None or got[1] != pin, "control": control(key, got[2], got[3], ctx, a.phase)}
        row["ok"] = not not_landed and row["revision_moved"] and row["control"]["ok"]
        ok &= row["ok"]
        out.append(row)
    return {"mode": "check", "phase": a.phase, "stand_in": ctx.stand_in, "pages": out, "ok": ok,
            "d22": "transient reads of this session's harness records; counts, ids and booleans"}


# --- self-test --------------------------------------------------------------------------------------------------
def selftest(a) -> dict:
    ctx = Ctx(a.successor_map, a.parts, {}, True)
    pid, pred, old_title, lane = next(r for r in ctx.tsv if r[0] == "PR-30")
    page = {"member_rows": True, "frontmatter_rule": True, "frontmatter_title": ['title: "X — old"', 'title: "X — new"']}
    base = ("---\n\nartifact\\_version: \"100926.1\"\n\ntitle: \"X — old\"\n\n---\n## Selected topology\n"
            + row_line(pid, old_title, lane, pred) + "\n## Native flow changes\nThe register selected `GCFPE-20261009.1` once.\n")
    good = {"id": "S1", "start": "The register selected `GCFPE-20261009.1` once.", "end": None,
            "new": "The register selects `GCFPE-20261027.1` (@ACTIVATION_DATE)."}

    def render(text, ops, c=ctx):
        return apply(text, ops + generated("SYN", page, text, "activation", c), c)
    t1, r1 = render(base, [good])
    succ_id = ctx.map["members"]["PR-30"]["page_id"]
    clean = (all(r["applied"] for r in r1) and len(r1) == 4 and succ_id in t1 and pred not in t1
             and 'artifact\\_version: "102726.1"' in t1 and not C.findings(t1, ctx.cc, "activation"))
    nomark = Ctx(a.successor_map, a.parts, {}, False)
    nomark.values.pop("@ACTIVATION_DATE", None)
    unsafe_new = {"id": "U", "start": "cb", "end": None, "new": "c"}  # the replacement re-forms the span after it
    dup_text = base + "The register selected `GCFPE-20261009.1` once.\n"
    wl_op = {"id": "W", "start": "predecessor_disposition: SUPERSEDED", "end": None, "new": "x", "whole_line": True}
    prefix_text = "---\npredecessor_disposition: SUPERSEDED_ARCHIVED_INTACT\n---\n"
    esc_op = {"id": "E", "start": "status: UNSELECTED_CANDIDATE", "end": None, "new": "status: REGISTER_CONTROLLED"}
    esc_text = "---\nstatus: UNSELECTED\\_CANDIDATE\n---\n"
    t_esc, r_esc = apply(esc_text, [esc_op], ctx)
    cat = catalog_text(ctx)
    cat_missing = cat.replace(f"{URL}{succ_id}?pvs=204", f"{URL}{'0' * 32}?pvs=204")
    cases = {
        "clean_page_renders_and_passes": clean,
        "missing_anchor_refused": not render(base, [{**good, "start": "absent anchor"}])[1][0]["applied"],
        "doubled_anchor_refused": not render(dup_text, [good])[1][0]["applied"],
        "unfilled_marker_refused": apply(base, [good], nomark)[1][0]["refusal"] == "UNFILLED_MARKER",
        "unsafe_batch_refused": apply("Qcbb\n", [unsafe_new], ctx)[1][0]["refusal"] == "BATCH_UNSAFE",
        "escaped_anchor_resolves_and_writes_escaped": r_esc[0]["applied"] and r_esc[0]["form"] == "escaped"
                                                      and "status: REGISTER\\_CONTROLLED" in t_esc,
        "whole_line_prefix_refused": apply(prefix_text, [wl_op], ctx)[1][0]["refusal"] == "START_COUNT_0",
        "kept_retired_value_fails": len(C.findings(render(base, [])[0], ctx.cc, "activation")) > 0,
        "second_render_changes_nothing": not any(r["applied"] for r in render(t1, [good])[1]),
        "landed_after_render": landed(t1, good, [good], ctx) and not landed(base, good, [good], ctx),
        "catalog_56_rows_passes_candidate_rules": C.check_text("CATALOG", OPS["new_pages"]["CATALOG"]["title"],
                                                               as_fetched(cat), ctx.cc, "candidate")["ok"]
                                                  and cat.count("\n| <code>") == 56,
        "catalog_missing_member_fails": not C.check_text("CATALOG", OPS["new_pages"]["CATALOG"]["title"],
                                                         as_fetched(cat_missing), ctx.cc, "candidate")["ok"],
        "repin_required_for_moved_page": repin_required(C.CF_HUB, "candidate") and repin_required(C.REGISTER, "register")
                                         and repin_required("@PE_PAGE_ID", "activation")
                                         and repin_required("@REGISTER_ENTRY_PAGE_ID", "archived")
                                         and not repin_required(C.CHECKLIST, "candidate"),
        "move_list_is_archive_set": set(ctx.moves) == set(ctx.cc["archive_102726"]) and len(ctx.moves) == 57,
        "standin_values_refused_with_real_map": _real_map_refuses(a),
    }
    return {"mode": "selftest", "stand_in": ctx.stand_in, "cases": cases, "cases_passed": sum(cases.values()),
            "cases_total": len(cases), "ok": all(cases.values())}


def _real_map_refuses(a) -> bool:
    import tempfile
    raw = json.loads(Path(a.successor_map).read_text(encoding="utf-8"))
    raw["stand_in"] = False
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "real.json"
        p.write_text(json.dumps(raw), encoding="utf-8")
        try:
            Ctx(str(p), a.parts, {}, True)
        except SystemExit:
            return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser(prog="activation_render_102726.py")
    sub = ap.add_subparsers(dest="mode", required=True)
    for name in ("plan", "check"):
        p = sub.add_parser(name)
        p.add_argument("--successor-map", required=True)
        p.add_argument("--parts", required=True)
        p.add_argument("--phase", choices=PHASES, required=True)
        p.add_argument("--pages", nargs="*")
        p.add_argument("--set", action="append", default=[], help="@KEY=VALUE")
        p.add_argument("--pin", action="append", default=[], help="PAGE_ID=REVISION")
        p.add_argument("--fetched-after", default="")
        p.add_argument("--since-minutes", type=int, default=600)
        p.add_argument("--emit", action="store_true")
        if name == "plan":
            p.add_argument("--chain", action="store_true")
            p.add_argument("--standin-values", action="store_true")
            p.add_argument("--report-lines", action="store_true", help="80-character excerpts, terminal only")
    s = sub.add_parser("selftest")
    s.add_argument("--successor-map", required=True)
    s.add_argument("--parts", required=True)
    a = ap.parse_args()
    res = selftest(a) if a.mode == "selftest" else (run_plan(a) if a.mode == "plan" else run_check(a))
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
