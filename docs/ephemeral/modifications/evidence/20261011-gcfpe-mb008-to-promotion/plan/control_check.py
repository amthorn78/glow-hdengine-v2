#!/usr/bin/env python3
"""Activation check for the in-place controls of MODIFICATION-20261011-gcfpe-mb008-to-promotion (PLAN §7; P-B1 of
PLAN review round 1). It runs on fresh reads of the control pages and fails while any of them still states the
091426.1 release, or a fact of it, as current.

  control_check.py check --parts P --phase activation|archived [--fetched-after T] [--since-minutes N]
                         [--catalog ID] [--report-lines]
  control_check.py selftest

On each control page (the register, the Flow Index, the five hubs, the Alpha checklist and PE Metaprompt 100926.1)
every frontmatter line (PE: only its frontmatter, which is all X15(b) writes) keeping a staging value (an UNSELECTED status or posture, `promotion_authorized: false`, a
`candidate_release` key) is a finding, and every line outside a historical section is a finding when it names a
retired value and carries no predecessor marker:
  - a retired value: one of the 57 archive-set page ids (the 55 predecessors in the candidate parts, the 091426.1
    catalog and PE Metaprompt 091426.1), in either id form; the literals `091426.1` and `GCFPE-20260914.1`; the
    091426.1 MGMT-10 vocabulary (GCFPE_ECOSYSTEM_CHANGE_REPORT, GCFPE_SUCCESSOR_RELEASE,
    READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION); 091426.1's promotion evidence directory (gcfpe.round27); or a
    statement of the 091426.1 member set ("sole new member" or "sole added member").
  - a historical section: decided by the innermost heading that names history, a predecessor, a supersession or
    an archive (historical) or begins "Current" (current); with neither, current. The frontmatter block at the
    top of a page is a section of its own and is never historical.
  - a predecessor marker: "predecessor", "supersede", "historical" or "archive" (any case) within the 100
    characters before the retired value on the same line, or the value struck through (~~…~~); each retired
    value on a line is judged on its own.
In the activation phase (X15, X16) a line that is only a child-page block (<page url=...>...</page>) is not counted,
because the 091426.1 pages stay children until X19 moves them; the archived phase (X19 onwards) counts it.
Positive checks: each page's title equals TITLES (the Flow Index and hubs from registry-header-100926.1.json's
control_titles, the register's unchanged, the Alpha checklist's at 100926.1, PE's at 100926.1); each hub and
the Flow Index link every successor whose candidate registry row names it as parent (by the parts'
candidate_url, compared by page id); the register's "Current selection" section names GCFPE-20261009.1, 100926.1
and 55; with --catalog, the catalog page links all 55 successors, and its lines are judged like any control's.

Bodies are D22 transient reads of this session's harness records (body_check.py's reader, extended to keep the
title). The report carries counts, ids and section headings; --report-lines adds an 80-character excerpt of each
finding's line for the terminal only. Never redirect a --report-lines run into the repository.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
HEADER = json.loads((HERE / "registry-header-100926.1.json").read_text(encoding="utf-8"))
MGMT_ROW = json.loads((HERE / "mgmt10-registry-row.json").read_text(encoding="utf-8"))
REGISTER = "3d24590a05eb81ce942ad994cfca9fa1"
FLOW_INDEX = "3db4590a05eb81de9736ea69bac61016"
ALPHA_CHECKLIST = "3db4590a05eb812f87caed515836687f"
PE_SUCCESSOR = "3f44590a05eb81f98b76c83465dc1960"
EXTRA_ARCHIVE = {"3db4590a05eb81738ef1d846e3c0df8c": "Glow HDE Complete Prompt Set — 091426.1",
                 "3db4590a05eb8174be35d9e35acb3f77": "PE Metaprompt 091426.1"}
CONTROLS = [REGISTER, *HEADER["control_titles"], ALPHA_CHECKLIST, PE_SUCCESSOR]
TITLES = {**HEADER["control_titles"], REGISTER: "GCFPE Membership and Release Register",
          ALPHA_CHECKLIST: "GCFPE Alpha Establishment and Change Management Checklist — 100926.1",
          PE_SUCCESSOR: "PE Metaprompt 100926.1"}
STRUCK = re.compile(r"~~.*?~~")
# staging values a selected control's frontmatter must not keep (X15(b), X15(d)): a candidate status or posture, an
# unauthorized promotion, and the stale `candidate_release` key
STAGING = re.compile(r"^(?:status: \S*UNSELECTED\S*|mutation_posture: \S*UNSELECTED\S*|promotion_authorized: false|"
                     r"candidate_release:.*)$")
LITERALS = re.compile(r"091426\.1|GCFPE-20260914\.1|GCFPE_ECOSYSTEM_CHANGE_REPORT|GCFPE_SUCCESSOR_RELEASE|"
                      r"READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION|gcfpe\.round27|(?i:sole (?:new|added) member)")
MARKER = re.compile(r"(?i)predecessor|supersed|historical|archive")
WINDOW = 100  # a predecessor marker excuses a retired value only within this many characters before it
CHILD_PAGE = re.compile(r'^\s*<page url="[^"]+">.*</page>\s*$')
HEX = re.compile(r"[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}")
FETCH_HEAD = re.compile(r'Here is the result of "fetch" for the Page with URL https://[^/\s]+/p/([0-9a-f-]{32,36}) '
                        r'as of (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z):')
TITLE = re.compile(r'<properties>\s*(\{.*?\})\s*</properties>', re.S)


def _body_check():
    sys.path.insert(0, str(HERE))
    import body_check  # noqa: E402
    return body_check


def latest(page_id: str, root: str, session: str, since: int, fetched_after: str):
    """(captured, as_of, title, content) of the newest fetch at or after the cutoff, or None. The same transient
    read as body_check.all_fetches, keeping the page title."""
    B = _body_check()
    page = page_id.replace("-", "")
    cutoff = datetime.now(timezone.utc).timestamp() - since * 60
    if fetched_after:
        cutoff = max(cutoff, datetime.strptime(fetched_after, "%Y-%m-%dT%H:%M:%S.%fZ")
                     .replace(tzinfo=timezone.utc).timestamp())
    cutoff_iso = datetime.fromtimestamp(cutoff, timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    base = os.path.join(root, "*", session)
    files = glob.glob(base + ".jsonl") + glob.glob(base + "/tool-results/*") \
        + glob.glob(base + "/subagents/**/*.jsonl", recursive=True) \
        + glob.glob(base + "/subagents/**/tool-results/*", recursive=True)
    best = None
    for f in files:
        if os.path.getmtime(f) < cutoff:
            continue
        if f.endswith(".jsonl"):
            entries = B._recent_lines(f, cutoff_iso)
        else:
            try:
                raw = open(f, encoding="utf-8").read()
                entries = [json.loads(raw)] if page in raw else []
            except (OSError, ValueError):
                continue
        for obj in entries:
            ts = obj.get("timestamp") if isinstance(obj, dict) else None
            for t in B._texts(obj):
                inner = t
                if not inner.startswith("Here is the result of"):
                    try:
                        inner = json.loads(t)["text"]
                    except (ValueError, KeyError, TypeError):
                        continue
                head = FETCH_HEAD.match(inner)
                if not head or head.group(1).replace("-", "") != page:
                    continue
                m = re.search(r"<content>\n?(.*)</content>", inner, re.S)
                tm = TITLE.search(inner)
                if not m:
                    continue
                captured = ts if f.endswith(".jsonl") else datetime.fromtimestamp(
                    os.path.getmtime(f), timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
                if not captured or captured < cutoff_iso:
                    continue
                title = json.loads(tm.group(1)).get("title", "") if tm else ""
                if best is None or captured > best[0]:
                    best = (captured, head.group(2), title, m.group(1))
    return best


def archive_set(parts_dir: str) -> dict:
    out = dict(EXTRA_ARCHIVE)
    for f in sorted(Path(parts_dir, "prompts").glob("*.json")):
        node = json.loads(f.read_text(encoding="utf-8"))["node"]
        out[node["predecessor"]["notion_page_id"].replace("-", "")] = node["predecessor"]["title"]
    return out


def successors(parts_dir: str) -> dict:
    out = {}
    for f in sorted(Path(parts_dir, "prompts").glob("*.json")):
        part = json.loads(f.read_text(encoding="utf-8"))
        m = HEX.search(part["node"]["candidate_url"])
        out[part["id"]] = m.group(0).replace("-", "")
    return out


def sections(text: str):
    """(heading path, line) for every line; the leading frontmatter block is its own section."""
    lines = text.split("\n")
    stack, out, i = [], [], 0
    if lines and lines[0].strip() == "---":
        j = next((k for k in range(1, len(lines)) if lines[k].strip() == "---"), 0)
        for k in range(0, j + 1):
            out.append((("<frontmatter>",), lines[k]))
        i = j + 1
    for line in lines[i:]:
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            stack = [s for s in stack if s[0] < level] + [(level, m.group(2).strip())]
        out.append((tuple(h for _, h in stack), line))
    return out


def historical(path: tuple) -> bool:
    """The innermost heading that decides: one naming history, a predecessor, a supersession or an archive makes
    the section historical; one beginning "Current" makes it current, whatever encloses it (the register's
    "Current …" sections sit under an H1 "Historical register profile"). No deciding heading: current."""
    if path == ("<frontmatter>",):
        return False
    for h in reversed(path):
        if MARKER.search(h):
            return True
        if h.lower().startswith("current"):
            return False
    return False


def findings(text: str, archive: dict, phase: str):
    ids = set(archive)
    out = []
    for path, line in sections(text):
        if path == ("<frontmatter>",) and STAGING.match(line.strip()):
            out.append({"section": "<frontmatter>", "archive_ids": [], "literals": ["STAGING_VALUE"],
                        "excerpt": line.strip()[:80]})
            continue
        if historical(path):
            continue
        if phase == "activation" and CHILD_PAGE.match(line):
            continue
        hits, lit = set(), set()
        for m in list(HEX.finditer(line)) + list(LITERALS.finditer(line)):
            value = m.group(0)
            is_id = HEX.fullmatch(value) is not None
            if is_id and value.replace("-", "") not in ids:
                continue
            if MARKER.search(line[max(0, m.start() - WINDOW):m.start()]):
                continue
            if any(k.start() <= m.start() < k.end() for k in STRUCK.finditer(line)):
                continue  # struck through: visibly retired text
            (hits if is_id else lit).add(value.replace("-", "") if is_id else value)
        if hits or lit:
            out.append({"section": path[-1] if path else "<top>", "archive_ids": sorted(hits),
                        "literals": sorted(lit), "excerpt": line.strip()[:80]})
    return out


def hub_members(parts_dir: str) -> dict:
    """parent page id -> successor ids whose candidate registry row names it (the 2026-10-09 proposal's
    expected_parent_id, MGMT-10's from its successor row)."""
    evidence = HERE.parent.parent
    prop = json.loads((evidence / "20261009-gcfpe-latest-alpha-analysis/execute/candidate-registry-nonderived.json")
                      .read_text(encoding="utf-8"))["prompts"]
    succ = successors(parts_dir)
    out = {}
    for row in prop:
        parent = MGMT_ROW["row"]["expected_parent_id"] if row["prompt_key"] == "GCFPE-MGMT-10" else row["expected_parent_id"]
        out.setdefault(parent, set()).add(succ[row["prompt_key"]])
    return out


def check_text(page: str, title: str, text: str, archive: dict, members: dict, phase: str, catalog: str) -> dict:
    f = findings(text, archive, phase)
    if page == PE_SUCCESSOR:
        # X15(b) writes PE's header block only; its body is a reviewed candidate body, whose passages scoped to the
        # 20260914 repair are recorded as P-L8 rather than edited after the post-flight
        f = [r for r in f if r["section"] == "<frontmatter>"]
    linked = {h.replace("-", "") for h in HEX.findall(text)}
    row = {"page": page, "title": title, "findings": len(f), "finding_rows": f}
    want_title = TITLES.get(page)
    if want_title is not None:
        row["title_ok"] = title == want_title
    if page in members:
        missing = sorted(members[page] - linked)
        row["successors_expected"], row["successors_missing"] = len(members[page]), len(missing)
    if page == REGISTER:
        cur = [line for path, line in sections(text) if path and path[-1].lower().startswith("current selection")]
        joined = "\n".join(cur)
        row["current_selection_ok"] = all(t in joined for t in ("GCFPE-20261009.1", "100926.1", "55"))
    if page == catalog:
        allsucc = set().union(*members.values())
        row["catalog_successors_missing"] = len(allsucc - linked)
    row["ok"] = (not f and row.get("title_ok", True) and not row.get("successors_missing")
                 and row.get("current_selection_ok", True) and not row.get("catalog_successors_missing"))
    return row


def check(a) -> dict:
    archive, members = archive_set(a.parts), hub_members(a.parts)
    root, session = os.path.expanduser("~/.claude/projects"), os.environ.get("CLAUDE_CODE_SESSION_ID")
    pages = (a.pages or list(CONTROLS)) + ([a.catalog] if a.catalog else [])
    rows, ok = [], True
    for page in pages:
        got = latest(page, root, session, a.since_minutes, a.fetched_after)
        if got is None:
            rows.append({"page": page, "error": "NO_FETCH_FOUND", "ok": False})
            ok = False
            continue
        row = check_text(page, got[2], got[3], archive, members, a.phase, a.catalog)
        row["as_of"] = got[1]
        if not a.report_lines:
            for r in row["finding_rows"]:
                r.pop("excerpt")
        ok &= row["ok"]
        rows.append(row)
    return {"mode": "check", "phase": a.phase, "archive_set": len(archive), "pages": rows, "ok": ok,
            "d22": "transient reads of this session's harness records; counts, ids and headings only"
                   + ("; excerpts for the terminal" if a.report_lines else "")}


def selftest(parts_dir: str) -> dict:
    archive, members = archive_set(parts_dir), hub_members(parts_dir)
    old = next(iter(sorted(archive)))
    succ_ids = sorted(members.get(FLOW_INDEX, set()))
    new_link = "".join(f'<mention-page url="https://app.notion.com/p/{s}">m</mention-page>\n' for s in succ_ids)
    fi_title = HEADER["control_titles"][FLOW_INDEX]
    cases = {
        "current_line_fails": (f"## Selected topology\nThe catalog is <mention-page url=\"https://app.notion.com/p/{old}\">x</mention-page>.\n{new_link}", False),
        "literal_fails": ("## Activation contract\nThe register selected `GCFPE-20260914.1` / `091426.1` / `55`.\n" + new_link, False),
        "sole_member_fails": ("## Current explicit membership\n`PR-35` is the sole new member.\n" + new_link, False),
        "retired_vocab_fails": ("## Native flow changes\nGCFPE-MGMT-10 returns `READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION`.\n" + new_link, False),
        "historical_section_passes": ("## Historical selection — GCFPE-20260914.1 / 091426.1\nThe catalog was 091426.1.\n" + new_link, True),
        "distant_marker_fails": ("## Activation contract\n**This index is operative**, because the register selected "
                                 "`GCFPE-20260914.1` on 2026-09-21. The predecessor index is superseded and archived.\n"
                                 + new_link, False),
        "predecessor_line_passes": ("---\npredecessor_release: GCFPE-20260914.1\n---\n## Selected topology\n" + new_link, True),
        "child_page_activation_passes": (f'<page url="https://app.notion.com/p/{old}">x</page>\n' + new_link, True),
        "missing_successor_fails": ("## Selected topology\nnothing linked\n", False),
        "struck_line_passes": ("## Governance repair checklist\n- [ ] ~~All 55 are 091426.1 siblings~~\n" + new_link, True),
        "staging_frontmatter_fails": ("---\nstatus: UNSELECTED_CANDIDATE\n---\n" + new_link, False),
        "candidate_release_key_fails": ("---\ncandidate_release: GCFPE-20261009.1\n---\n" + new_link, False),
        "current_under_historical_h1_fails": ("# Historical register profile\n## Current explicit membership — 091426.1\n"
                                              "all 55 are 091426.1\n" + new_link, False),
        "subsection_of_historical_passes": ("## Historical selection — GCFPE-20260914.1\n### Release provenance\n"
                                            "091426.1 was selected\n" + new_link, True),
    }
    rows, ok = {}, True
    for name, (text, want) in cases.items():
        got = check_text(FLOW_INDEX, fi_title, text, archive, members, "activation", "")["ok"]
        rows[name] = got == want
        ok &= got == want
    arch = check_text(FLOW_INDEX, fi_title, f'<page url="https://app.notion.com/p/{old}">x</page>\n' + new_link,
                      archive, members, "archived", "")["ok"]
    rows["child_page_archived_fails"] = arch is False
    ok &= arch is False
    rows["wrong_title_fails"] = check_text(FLOW_INDEX, "Glow HDE Prompt Flow Index — GCFPE-20260914.1 — 091426.1",
                                           new_link, archive, members, "activation", "")["ok"] is False
    ok &= rows["wrong_title_fails"]
    return {"mode": "selftest", "archive_set": len(archive), "cases": rows, "ok": ok and len(archive) == 57}


def main() -> int:
    ap = argparse.ArgumentParser(prog="control_check.py")
    sub = ap.add_subparsers(dest="mode", required=True)
    c = sub.add_parser("check")
    c.add_argument("--parts", required=True)
    c.add_argument("--phase", choices=["activation", "archived"], required=True)
    c.add_argument("--fetched-after", default="")
    c.add_argument("--since-minutes", type=int, default=600)
    c.add_argument("--catalog", default="")
    c.add_argument("--report-lines", action="store_true")
    c.add_argument("--pages", nargs="*", help="only these control page ids (X15 checks its own pages before X16)")
    s = sub.add_parser("selftest")
    s.add_argument("--parts", required=True)
    a = ap.parse_args()
    res = check(a) if a.mode == "check" else selftest(a.parts)
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
