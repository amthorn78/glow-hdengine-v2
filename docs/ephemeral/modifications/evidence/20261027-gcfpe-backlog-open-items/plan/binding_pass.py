#!/usr/bin/env python3
"""Central binding pass for MODIFICATION-20261027-gcfpe-backlog-open-items (C-1; W7-D8; G-W7-BIND-1, G-W8-NAME-1).

Given one page's fresh read and the successor map, emit one operation per line (or per minimal group of adjacent
lines, when a line is not unique in the page) that cites a SUCCESSOR member's 100926.1 page, by URL or mention, or
names it "<title> — 100926.1", rewriting each citation to the successor: the page URL becomes @SUCC_URL_<ID> and the
title @SUCC_TITLE_<ID>, which body_check.py fills from the map. PE counts as a successor member here (its map entry
is `pe`). A line that a worker or head operation already replaces is skipped (no double edit): instead the same
rewrite is applied to that operation's replacement text, so the one edit carries current bindings. A line that
already carries 102726.1 is skipped (C-9). A KEPT member (GCFPE-MGMT-10) is never rewritten: it is not a successor.
AM-2 (Nathan, 2026-10-27, after EXECUTE's X4 stop): on a real duplicate Notion remaps the page's own self-mention to
the duplicate, which then renders the successor's "— 102726.1" title. C-9's test ignores that one mention, the page's
own successor self-mention, so a line whose only 102726.1 is that self-mention still has its stale citations
rewritten; a line carrying any other 102726.1 is skipped as before.

The map (W7 "successor_page_map", written once by EXECUTE at
execute/successor-pages-102726.1.json) is the only source of dispositions, successor ids and titles. A STAND-IN map
(`standin` below; stand_in: true) sets every successor to its predecessor page id and CL-05's to the candidate id;
then a URL-only rewrite is the identity and is reported, not applied, and G-W7-BIND-1 regenerated from the map is
vacuous, so body_check.py also runs a probe pass with synthetic successor ids that never reach Notion.

  binding_pass.py selftest                         synthetic text only; every check is shown to fail on an injection
  binding_pass.py standin --out FILE               write the stand-in map (ids and titles only)
  binding_pass.py validate --successor-map FILE    the map checks W7 states
  binding_pass.py guards --successor-map FILE      G-W7-BIND-1 and G-W8-NAME-1 regenerated from the map

Reports carry counts, ids and booleans only (D22). Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PE_PRED = "3f44590a05eb81f98b76c83465dc1960"
PE_PRED_TITLE = "PE Metaprompt 100926.1"
CL05_CANDIDATE = "4054590a05eb8155b301e2cb6dec31d5"
CL05_NAME = "CL-05 — Prepare and Publish the Close Mutation Set"
CL05_PARENT_STAND_IN = "3db4590a05eb81d59059eb6b95ed5fcf"  # the HDE Change Flow hub (C-9, C-19; stand-in only)
NEW_VERSION = "102726.1"
OLD_VERSION = "100926.1"
URL_BASE = "https://app.notion.com/p/"
SKIP_LINE = re.compile(r"^predecessor: PE Metaprompt \d{6}\.\d+$")


def tsv_members(path: Path = HERE / "members-100926.1.tsv") -> dict:
    rows = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            pid, page, title, lane = line.split("\t")
            rows[pid] = {"page_id": page, "title": title, "lane": lane}
    return rows


# --- the successor map ------------------------------------------------------------------------------------
def standin(tsv: dict | None = None) -> dict:
    """Each SUCCESSOR's successor is its predecessor page; CL-05's is the candidate; GCFPE-MGMT-10 is KEPT. Titles are
    the predecessor titles with the version moved; the revision pins are left for body_check.py to take from
    edits.json (a stand-in has no successor revision)."""
    tsv = tsv or tsv_members()
    out = {"release": "GCFPE-20261027.1", "version_family": NEW_VERSION, "baseline": "GCFPE-20261009.1 / 100926.1 / 55",
           "stand_in": True,
           "stand_in_rule": "each successor = its predecessor page id; the CL-05 successor = the candidate id",
           "members": {}, "pe": {"page_id": PE_PRED, "predecessor_page_id": PE_PRED,
                                 "title": "PE Metaprompt " + NEW_VERSION, "created_last_edited_at": None}}
    for pid, row in sorted(tsv.items()):
        if pid == "GCFPE-MGMT-10":
            out["members"][pid] = {"disposition": "KEPT", "reason": "C-1: names no member page but its own",
                                   "page_id": row["page_id"], "title": row["title"], "predecessor_page_id": None,
                                   "duplicated_from": None, "parent_id": None, "created_last_edited_at": None}
        else:
            out["members"][pid] = {"disposition": "SUCCESSOR", "reason": "C-1 cascade (stand-in)",
                                   "page_id": row["page_id"], "title": row["title"][:-len(OLD_VERSION)] + NEW_VERSION,
                                   "predecessor_page_id": row["page_id"], "duplicated_from": row["page_id"],
                                   "parent_id": None, "created_last_edited_at": None}
    # C-19: CL-05's parent_id feeds the 102726.1 contract's staged_parent_id; the stand-in is the HDE Change Flow hub
    # CL-05 is moved under before its operations (C-9; W5 RE-4 expected_parent_id). EXECUTE's map records the real one.
    out["members"]["CL-05"] = {"disposition": "ADDED", "reason": "ITEM-30, PART-13 (stand-in)",
                               "page_id": CL05_CANDIDATE, "title": f"{CL05_NAME} — {NEW_VERSION}",
                               "predecessor_page_id": None, "duplicated_from": CL05_CANDIDATE,
                               "parent_id": CL05_PARENT_STAND_IN, "created_last_edited_at": None}
    return out


def probe(smap: dict) -> dict:
    """A copy of the map whose successor ids are synthetic (sha256 of 'probe:<id>', 32 hex) and never equal a
    predecessor: used only in memory so the stand-in dry run can exercise the URL half of the binding check."""
    p = json.loads(json.dumps(smap))
    for pid, row in p["members"].items():
        if row["disposition"] in ("SUCCESSOR", "ADDED"):
            row["page_id"] = hashlib.sha256(f"probe:{pid}".encode()).hexdigest()[:32]
    p["pe"]["page_id"] = hashlib.sha256(b"probe:PE").hexdigest()[:32]
    p["probe"] = True
    return p


def validate(smap: dict, tsv: dict | None = None) -> dict:
    """W7's checks: 56 members exactly; every SUCCESSOR has a distinct new page id and the predecessor that the TSV
    names; every KEPT page id equals the TSV's; CL-05 is the only ADDED. In a stand-in map the distinctness checks are
    reported as not applicable, never as passing."""
    tsv = tsv or tsv_members()
    m = smap.get("members", {})
    stand_in = bool(smap.get("stand_in"))
    succ = {k: v for k, v in m.items() if v.get("disposition") == "SUCCESSOR"}
    kept = {k: v for k, v in m.items() if v.get("disposition") == "KEPT"}
    added = {k: v for k, v in m.items() if v.get("disposition") == "ADDED"}
    ids = [v.get("page_id") for v in m.values()] + [smap.get("pe", {}).get("page_id")]
    hexok = all(isinstance(i, str) and re.fullmatch(r"[0-9a-f]{32}", i) for i in ids)
    r = {
        "members_56": len(m) == 56,
        "members_cover_tsv_plus_cl05": set(m) == set(tsv) | {"CL-05"},
        "only_added_is_cl05": set(added) == {"CL-05"},
        "kept_ids_equal_tsv": all(v["page_id"] == tsv[k]["page_id"] for k, v in kept.items() if k in tsv),
        "successor_predecessors_equal_tsv": all(v.get("predecessor_page_id") == tsv[k]["page_id"]
                                                for k, v in succ.items() if k in tsv),
        "pe_predecessor": smap.get("pe", {}).get("predecessor_page_id") == PE_PRED,
        "page_ids_32_hex": hexok,
        "successor_titles_102726": all(str(v.get("title", "")).endswith("— " + NEW_VERSION)
                                       for v in list(succ.values()) + list(added.values())),
    }
    if stand_in:
        r["distinct_successor_ids"] = "NOT_APPLICABLE_STAND_IN"
    else:
        new = [v["page_id"] for v in list(succ.values()) + list(added.values())] + [smap["pe"]["page_id"]]
        r["distinct_successor_ids"] = (len(new) == len(set(new))
                                       and not set(new) & {row["page_id"] for row in tsv.values()}
                                       and smap["pe"]["page_id"] != PE_PRED)
        r["revision_pins_present"] = all(v.get("created_last_edited_at") for v in list(succ.values())
                                         + list(added.values())) and bool(smap["pe"].get("created_last_edited_at"))
    r["ok"] = all(v is True or v == "NOT_APPLICABLE_STAND_IN" for v in r.values())
    r["stand_in"] = stand_in
    return r


def successors(smap: dict, tsv: dict | None = None) -> list:
    """(id, predecessor page, predecessor title, successor page, successor title) for every member that has a
    successor, PE included; KEPT and ADDED members have no predecessor to rewrite."""
    tsv = tsv or tsv_members()
    out = []
    for pid, row in sorted(smap["members"].items()):
        if row["disposition"] == "SUCCESSOR":
            out.append((pid, row["predecessor_page_id"], tsv[pid]["title"], row["page_id"], row["title"]))
    pe = smap["pe"]
    out.append(("PE", pe["predecessor_page_id"], PE_PRED_TITLE, pe["page_id"], pe.get("title", "PE Metaprompt " + NEW_VERSION)))
    return out


def shared_from_map(smap: dict) -> dict:
    s = {}
    for pid, row in smap["members"].items():
        s[f"SUCC_URL_{pid}"] = URL_BASE + row["page_id"]
        s[f"SUCC_TITLE_{pid}"] = row["title"]
    s["SUCC_URL_PE"] = URL_BASE + smap["pe"]["page_id"]
    s["SUCC_TITLE_PE"] = smap["pe"].get("title", "PE Metaprompt " + NEW_VERSION)
    return s


# --- regenerated guards -----------------------------------------------------------------------------------------
def title_order(t: str) -> tuple:
    """Longest first (a longer title must be tried before a title it contains), then by text (C-22)."""
    return (-len(t), t)


def alternation_sorted(parts: list) -> bool:
    return parts == sorted(parts, key=title_order)


def regenerated_guards(smap: dict, prompts: list, tsv: dict | None = None) -> tuple[dict, dict]:
    """G-W7-BIND-1 (URL half) and G-W8-NAME-1 (title half) from the map: forbidden on every page, line units. The URL
    half names only predecessor ids whose successor differs, so under a stand-in map it is empty (vacuous) and the
    probe pass carries it."""
    rows = successors(smap, tsv)
    ids = sorted({p for _, p, _, s, _ in rows if p != s})
    # C-22: the alternation is sorted, longest first and then by text, so equal-length titles do not follow set order
    # (string hashing differs per process) and the regenerated pattern is the same on every run
    titles = sorted({t for _, _, t, _, _ in rows}, key=title_order)
    bind = {"id": "G-W7-BIND-1", "source": "W7 (regenerated from the successor map)", "kind": "forbidden",
            "unit": "line", "prompts": prompts, "except": [],
            "all": ["app\\.notion\\.com/p/(?:" + "|".join(ids) + ")" if ids else "(?!)"],
            "vacuous": not ids, "forbidden_ids": len(ids)}
    name = {"id": "G-W8-NAME-1", "source": "W8 (regenerated from the successor map)", "kind": "forbidden",
            "unit": "line", "prompts": prompts, "except": [SKIP_LINE.pattern],
            "all": ["(?:" + "|".join(re.escape(t) for t in titles) + ")(?![0-9])"], "vacuous": not titles,
            "forbidden_titles": len(titles)}
    return bind, name


# --- the pass ---------------------------------------------------------------------------------------------------
class Rewriter:
    def __init__(self, smap: dict, tsv: dict | None = None):
        rows = successors(smap, tsv)
        self.url = {p: f"@SUCC_URL_{pid}" for pid, p, _, _, _ in rows}
        self.title = sorted(((t, f"@SUCC_TITLE_{pid}") for pid, _, t, _, _ in rows), key=lambda x: -len(x[0]))
        self.url_re = re.compile(r"https://app\.notion\.com/p/(" + "|".join(sorted(self.url)) + r")(?![0-9a-f])")
        self.tok = dict(self.title)
        # a title is a citation only when no digit follows it ("— 100926.10" is not "— 100926.1")
        self.title_re = re.compile("(" + "|".join(re.escape(t) for t, _ in self.title) + ")(?![0-9])")

    def stale(self, s: str) -> bool:
        return bool(self.url_re.search(s)) or bool(self.title_re.search(s))

    def rewrite(self, s: str) -> tuple[str, int]:
        n = 0
        def sub(m):
            nonlocal n
            n += 1
            return self.url[m.group(1)]
        def subt(m):
            nonlocal n
            n += 1
            return self.tok[m.group(1)]
        s = self.url_re.sub(sub, s)
        s = self.title_re.sub(subt, s)
        return s, n


def line_spans(text: str) -> list:
    out, i = [], 0
    for ln in text.split("\n"):
        out.append((i, i + len(ln)))
        i += len(ln) + 1
    return out


def occ(text: str, s: str) -> int:
    n, i = 0, text.find(s)
    while i >= 0:
        n += 1
        i = text.find(s, i + 1)
    return n


def generate(text: str, prompt: str, smap: dict, covered: list, tsv: dict | None = None) -> dict:
    """Binding operations for one page. `covered` is the list of (start, end) character spans that worker and head
    operations replace on this same text. A stale line outside every covered span becomes one operation, grown
    upward (then downward) by whole lines until its text occurs once in the page, and merged with an overlapping
    neighbour. On a line that a covered span touches, a citation inside the span is the covering operation's to
    carry (rewrite_replacement); a citation outside it becomes an operation on the uncovered part of the line when
    that part occurs once, and is otherwise reported unresolved. A line already carrying 102726.1 is skipped (C-9).
    Returns tokenized ops and counts only."""
    rw = Rewriter(smap, tsv)
    spans = line_spans(text)
    lines = text.split("\n")
    # AM-2: the page's own successor self-mention does not count as "already carrying 102726.1" for C-9
    own = (smap.get("pe") if prompt == "PE" else (smap.get("members") or {}).get(prompt)) or {}
    own_mention = (re.compile(r'<mention url="' + re.escape(URL_BASE + str(own["page_id"])) + r'[^"]*"[^>]*>[^<]*</mention>')
                   if own.get("page_id") else None)

    def cover_of(k):
        a, b = spans[k]
        return [(max(a, cs), min(b, ce)) for cs, ce in covered if cs < b + 1 and a < ce or (a == b and cs <= a < ce)]

    # PE's frontmatter 'predecessor:' key names the predecessor by design (HEAD-PE, D-W8-9); it is not a binding
    stale = [k for k, ln in enumerate(lines) if rw.stale(ln) and not SKIP_LINE.match(ln)]
    groups, partial_ops, counts = [], [], {"skipped_covered": 0, "skipped_already_102726": 0, "unresolved": 0,
                                           "partial_line_ops": 0}
    unresolved_lines = []
    for k in stale:
        a0, b0 = spans[k]
        cov = cover_of(k)
        if NEW_VERSION in (own_mention.sub("", lines[k]) if own_mention else lines[k]):
            counts["skipped_already_102726"] += 1
            continue
        if cov:
            counts["skipped_covered"] += 1
            # the parts of the line no covering span replaces
            cuts, pos = [], a0
            for cs, ce in sorted(cov):
                if cs > pos:
                    cuts.append((pos, cs))
                pos = max(pos, ce)
            if pos < b0:
                cuts.append((pos, b0))
            for cs, ce in cuts:
                seg = text[cs:ce]
                if not rw.stale(seg):
                    continue
                if occ(text, seg) == 1:
                    partial_ops.append((cs, ce))
                    counts["partial_line_ops"] += 1
                else:
                    counts["unresolved"] += 1
                    unresolved_lines.append(k + 1)
            continue
        a = b = k
        found = None
        for direction in (-1, 1):
            a = b = k
            while True:
                seg = "\n".join(lines[a:b + 1])
                if occ(text, seg) == 1:
                    found = (a, b)
                    break
                nxt = a - 1 if direction < 0 else b + 1
                if nxt < 0 or nxt >= len(lines) or cover_of(nxt):
                    break
                a, b = (nxt, b) if direction < 0 else (a, nxt)
            if found:
                break
        if not found:
            counts["unresolved"] += 1
            unresolved_lines.append(k + 1)
            continue
        a, b = found
        if groups and groups[-1][1] >= a:  # overlaps the previous group: one operation (a superset stays unique)
            a = min(a, groups[-1][0])
            b = max(b, groups[-1][1])
            groups.pop()
        groups.append((a, b))
    ops = []
    pieces = [(spans[a][0], spans[b][1], f"lines {a + 1}-{b + 1}") for a, b in groups]
    pieces += [(cs, ce, "uncovered part of a line a worker op edits") for cs, ce in partial_ops]
    for n, (cs, ce, where) in enumerate(sorted(pieces), 1):
        old = text[cs:ce]
        new, c = rw.rewrite(old)
        ops.append({"id": f"BIND-{prompt}-{n:02d}", "part": "PART-24", "item": "ITEM-31", "prompt": prompt,
                    "section": f"binding currency, {where}", "start": old, "end": None, "new": new,
                    "source": "binding_pass", "allow_markup": True, "binding": True, "citations": c})
    return {"ops": ops, "stale_lines": len(stale), **counts, "unresolved_line_numbers": unresolved_lines}


def rewrite_replacement(new: str, smap: dict, tsv: dict | None = None) -> tuple[str, int]:
    """The binding rewrite applied to a worker operation's replacement text (the line it replaces is skipped)."""
    return Rewriter(smap, tsv).rewrite(new)


# --- self-test ----------------------------------------------------------------------------------------------------
def _expand(s: str, shared: dict) -> str:
    for k in sorted(shared, key=len, reverse=True):
        s = s.replace("@" + k, shared[k])
    return s


def _apply(text: str, ops: list, shared: dict) -> str:
    for o in ops:
        assert text.count(o["start"]) == 1
        text = text.replace(o["start"], _expand(o["new"], shared))
    return text


def _count(text: str, g: dict) -> int:
    return sum(1 for ln in text.split("\n") if all(re.search(p, ln) for p in g["all"]))


def selftest() -> dict:
    A, B, K = "a" * 32, "b" * 32, "c" * 32
    tsv = {"AA-10": {"page_id": A, "title": "AA-10 — Alpha Stage — 100926.1", "lane": "AA"},
           "BB-20": {"page_id": B, "title": "BB-20 — Beta Stage — 100926.1", "lane": "BB"},
           "GCFPE-MGMT-10": {"page_id": K, "title": "GCFPE-MGMT-10 — Manage an Ecosystem Change — 100926.1",
                             "lane": "GCFPE-MGMT"}}
    real = {"release": "GCFPE-20261027.1", "members": {
        "AA-10": {"disposition": "SUCCESSOR", "page_id": "1" * 32, "title": "AA-10 — Alpha Stage — 102726.1",
                  "predecessor_page_id": A},
        "BB-20": {"disposition": "SUCCESSOR", "page_id": "2" * 32, "title": "BB-20 — Beta Stage — 102726.1",
                  "predecessor_page_id": B},
        "GCFPE-MGMT-10": {"disposition": "KEPT", "page_id": K, "title": tsv["GCFPE-MGMT-10"]["title"],
                          "predecessor_page_id": None}},
        "pe": {"page_id": "3" * 32, "predecessor_page_id": PE_PRED, "title": "PE Metaprompt 102726.1"}}
    text = "\n".join([
        "Intro line.",
        f"- <mention url=\"https://app.notion.com/p/{A}\" />",                                   # 2 URL only
        "",
        f"- <code>BB-20 — Beta Stage — 100926.1</code>: <code>https://app.notion.com/p/{B}?pvs=204</code>",  # 4
        "",
        f"Continue to <mention url=\"https://app.notion.com/p/{A}\">AA-10 — Alpha Stage — 100926.1</mention>.",  # 6
        "Section two",
        f"- <mention url=\"https://app.notion.com/p/{A}\" />",                                   # 8 duplicate of 2
        f"Submit to GCFPE-MGMT-10 — Manage an Ecosystem Change — 100926.1 at https://app.notion.com/p/{K}",  # 9 KEPT
        f"Covered line names AA-10 — Alpha Stage — 100926.1.",                                   # 10 covered
        "Already at AA-10 — Alpha Stage — 102726.1 and BB-20 — Beta Stage — 100926.1.",         # 11 C-9 skip
        f"PE Metaprompt 100926.1 governs authoring ({'https://app.notion.com/p/' + PE_PRED}).",  # 12 PE
        f"Longer id {A}0 is not a page and AA-10 — Alpha Stage — 100926.10 is not a title.",     # 13 near misses
    ])
    cov_start = text.find("Covered line")
    covered = [(cov_start, cov_start + len("Covered line names AA-10 — Alpha Stage — 100926.1."))]
    shared = shared_from_map(real)
    g = generate(text, "XX-10", real, covered, tsv)
    out = _apply(text, g["ops"], shared)
    bind, name = regenerated_guards(real, ["XX-10"], tsv)
    regen = generate(out, "XX-10", real, covered=[], tsv=tsv)
    rw_new, rw_n = rewrite_replacement("Covered line names AA-10 — Alpha Stage — 100926.1.", real, tsv)
    checks = {
        "ops_emitted": len(g["ops"]) == 5,  # lines 2 (grown with the line above), 4, 6, 8 (grown), 12
        "duplicate_lines_made_unique": all(text.count(o["start"]) == 1 for o in g["ops"]),
        "kept_untouched": f"https://app.notion.com/p/{K}" in out and "GCFPE-MGMT-10 — Manage an Ecosystem Change — 100926.1" in out,
        "covered_skipped": g["skipped_covered"] == 1 and "Covered line names AA-10 — Alpha Stage — 100926.1." in out,
        "already_102726_skipped": g["skipped_already_102726"] == 1,
        "near_misses_untouched": f"Longer id {A}0" in out and "100926.10 is not a title" in out,
        "bind_guard_fails_before": _count(text, bind) > 0,
        "name_guard_fails_before": _count(text, name) > 0,
        # after: only the covered line, the C-9 line and the near-miss line still name a 100926.1 page; the covered
        # line is the worker op's to carry (rewrite_replacement), so the guard must still see it here
        "bind_guard_after_counts_only_unrewritten": _count(out, bind) == 0,
        "name_guard_after_counts_covered_and_c9_lines": _count(out, name) == 2,
        "second_generation_emits_only_c9_and_covered_lines": len(regen["ops"]) == 1 and regen["skipped_already_102726"] == 1,
        "replacement_rewrite": rw_n == 1 and "@SUCC_TITLE_AA-10" in rw_new,
        "pe_rewritten": "PE Metaprompt 102726.1" in out and PE_PRED not in out,
        "code_url_query_kept": f"https://app.notion.com/p/{'2' * 32}?pvs=204" in out,
    }
    # injected failures: a generator that drops the title rewrite, and one that ignores coverage, must be caught
    broken = dict(g)
    broken_ops = [dict(o, new=o["new"].replace("@SUCC_TITLE_BB-20", "BB-20 — Beta Stage — 100926.1")) for o in g["ops"]]
    checks["injected_title_drop_caught"] = _count(_apply(text, broken_ops, shared), name) > _count(out, name)
    url_drop = [dict(o, new=o["new"].replace("@SUCC_URL_AA-10", f"https://app.notion.com/p/{A}")) for o in g["ops"]]
    checks["injected_url_drop_caught"] = _count(_apply(text, url_drop, shared), bind) > 0
    nocover = generate(text, "XX-10", real, covered=[], tsv=tsv)
    checks["injected_ignore_coverage_caught"] = len(nocover["ops"]) != len(g["ops"])
    # a line a worker op edits in part: the citation outside the op's span gets its own op on the uncovered part,
    # and a citation inside the span is left to the op's replacement (rewrite_replacement)
    pl = f"Worker edits this sentence. Then return to <mention url=\"https://app.notion.com/p/{B}\" />."
    ptext = "Head.\n" + pl + "\nTail."
    pcs = ptext.find("Worker edits this sentence.")
    pg = generate(ptext, "XX-20", real, [(pcs, pcs + len("Worker edits this sentence."))], tsv)
    pout = _apply(ptext, pg["ops"], shared)
    checks["partial_line_op_emitted"] = pg["partial_line_ops"] == 1 and len(pg["ops"]) == 1
    checks["partial_line_op_outside_span"] = "Worker edits this sentence." not in pg["ops"][0]["start"]
    checks["partial_line_current_after"] = _count(pout, bind) == 0 and "Worker edits this sentence." in pout
    inside = f"See <mention url=\"https://app.notion.com/p/{B}\" /> here."
    itext = "Head.\n" + inside + "\nTail."
    ics = itext.find(inside)
    ig = generate(itext, "XX-20", real, [(ics, ics + len(inside))], tsv)
    checks["citation_inside_span_left_to_replacement"] = len(ig["ops"]) == 0 and ig["skipped_covered"] == 1
    # C-22: G-W8-NAME-1's alternation is sorted (longest first, then by text) and so identical across processes; the
    # injected failure is a tie between equal-length titles left in reverse order, which the order check refuses
    alts = [re.sub(r"\\(.)", r"\1", t) for t in name["all"][0][3:-len(")(?![0-9])")].split("|")]
    sm_titles = [t for _, _, t, _, _ in successors(standin())]
    full = regenerated_guards(standin(), ["X"])[1]
    full_alts = [re.sub(r"\\(.)", r"\1", t) for t in full["all"][0][3:-len(")(?![0-9])")].split("|")]
    ties = sorted(full_alts, key=title_order)
    tie_pair = next(((i, i + 1) for i in range(len(ties) - 1) if len(ties[i]) == len(ties[i + 1])), None)
    injected = list(ties)
    if tie_pair:
        injected[tie_pair[0]], injected[tie_pair[1]] = injected[tie_pair[1]], injected[tie_pair[0]]
    checks["name_alternation_sorted"] = alternation_sorted(alts) and alternation_sorted(full_alts) \
        and sorted(full_alts) == sorted(set(sm_titles))
    checks["injected_unsorted_tie_refused"] = tie_pair is not None and not alternation_sorted(injected)
    # stand-in map: URL-only rewrites are identities, the URL guard is vacuous, the probe map is not
    sm = standin(); pm = probe(sm)
    checks["standin_validates"] = validate(sm)["ok"] and validate(sm)["distinct_successor_ids"] == "NOT_APPLICABLE_STAND_IN"
    checks["standin_bind_guard_vacuous"] = regenerated_guards(sm, ["X"])[0]["vacuous"]
    checks["probe_bind_guard_not_vacuous"] = not regenerated_guards(pm, ["X"])[0]["vacuous"]
    checks["probe_validates_distinct"] = validate(dict(pm, stand_in=False))["distinct_successor_ids"] is True
    bad = json.loads(json.dumps(sm)); bad["members"]["QA-10"]["predecessor_page_id"] = "f" * 32
    checks["injected_bad_predecessor_refused"] = validate(bad)["successor_predecessors_equal_tsv"] is False
    bad2 = json.loads(json.dumps(sm)); bad2["members"]["PR-50"]["disposition"] = "ADDED"
    checks["injected_second_added_refused"] = validate(bad2)["only_added_is_cl05"] is False
    # AM-2: a duplicate's own remapped self-mention renders 102726.1; a stale own title on its line is still rewritten
    own_url = f"https://app.notion.com/p/{'1' * 32}"
    am2_line = (f"- Its own record: <code>AA-10 — Alpha Stage — 100926.1</code> at <mention url=\"{own_url}\">"
                f"AA-10 — Alpha Stage — 102726.1</mention>.")
    am2_text = "Head.\n" + am2_line + "\nTail."
    a2 = generate(am2_text, "AA-10", real, [], tsv)
    a2_out = _apply(am2_text, a2["ops"], shared)
    checks["am2_own_remapped_line_rewritten"] = (len(a2["ops"]) == 1 and a2["skipped_already_102726"] == 0
                                                 and _count(a2_out, name) == 0 and own_url in a2_out)
    other_line = (f"- Already at <mention url=\"https://app.notion.com/p/{'2' * 32}\">BB-20 — Beta Stage — 102726.1"
                  f"</mention> and <code>AA-10 — Alpha Stage — 100926.1</code>.")
    o2 = generate("Head.\n" + other_line + "\nTail.", "AA-10", real, [], tsv)
    checks["am2_other_102726_still_skipped"] = len(o2["ops"]) == 0 and o2["skipped_already_102726"] == 1
    a2_again = generate(a2_out, "AA-10", real, [], tsv)
    checks["am2_current_after"] = len(a2_again["ops"]) == 0 and a2_again["unresolved"] == 0
    return {"mode": "selftest", "checks": checks, "ok": all(checks.values())}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["selftest", "standin", "validate", "guards"])
    ap.add_argument("--successor-map")
    ap.add_argument("--out")
    a = ap.parse_args()
    if a.mode == "selftest":
        res = selftest()
    elif a.mode == "standin":
        if not a.out:
            print(json.dumps({"error": "standin needs --out"}))
            return 2
        Path(a.out).write_text(json.dumps(standin(), indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        res = {"mode": "standin", "written": a.out, "ok": True}
    else:
        smap = json.loads(Path(a.successor_map).read_text(encoding="utf-8"))
        if a.mode == "validate":
            res = dict(validate(smap), mode="validate")
        else:
            b, n = regenerated_guards(smap, ["*"])
            res = {"mode": "guards", "G-W7-BIND-1": {"forbidden_ids": b["forbidden_ids"], "vacuous": b["vacuous"]},
                   "G-W8-NAME-1": {"forbidden_titles": n["forbidden_titles"]}, "ok": True}
    print(json.dumps(res, indent=1))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
