#!/usr/bin/env python3
"""Control-page check for MODIFICATION-20261027-gcfpe-backlog-open-items (PLAN assembly A4; W8
transaction.control_checks; adapted from docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/
plan/control_check.py). It runs on fresh reads of the control pages and fails while any of them states the wrong
release for the phase it is in.

  control_check_102726.py check --successor-map F --phase candidate|activation|archived|sweep
                                [--register-pending] [--pages ID ...] [--catalog ID] [--entry ID]
                                [--fetched-after T] [--since-minutes N] [--report-lines]
  control_check_102726.py selftest --successor-map F

Retired values (activation, archived and sweep phases):
  - the 57 page ids of this release's archive set, all from the successor map: the predecessor_page_id of every
    SUCCESSOR row (54 under C-1), PE Metaprompt 100926.1, the 100926.1 catalog 3f74590a05eb812db385c2544d7570f7 and
    the CL-05 candidate 4054590a05eb8155b301e2cb6dec31d5; and the precedent's 57 091426.1 archive-set ids (its
    candidate parts' predecessors plus its two extras), in either id form;
  - the literals 100926.1, GCFPE-20261009.1, GCFPE-PCR-20261009.1; member-count statements of 55 ("55 members"
    except "other 55 members", "55-member", "exactly 55", "all 55", "member_count: 55"); a v5.0.0 procedure
    reference not marked superseded or historical within 150 characters after it or 100 before it; and every
    091426.1 value the precedent retired (091426.1, GCFPE-20260914.1, its MGMT-10 vocabulary, gcfpe.round27, "sole
    new/added member").
  GCFPE-MGMT-10's 100926.1 page and title are NOT retired (C-1): its page id is not in the archive set, and a
  100926.1 that follows a KEPT member id within 60 characters, or sits on that member's table row, is excused.
Excuses, judged per occurrence on a line whose Notion escapes (\\_) are removed first (C-5 Q-6): a historical
section (the innermost heading naming history, a predecessor, a supersession or an archive; one beginning
"Current" is current; the frontmatter block is never historical); a predecessor marker within 100 characters before
("predecessor", "supersede", "historical", "archive", "unchanged" (W8), and "corrected", a disclosed addition for
the Overview's dated "Corrected … from" lines), or earlier in the same sentence (a disclosed A4 addition: W8's
"Archival: the 57 superseded pages — …, the <code>100926.1</code> catalog" carries its marker 100+ characters back);
struck text (~~…~~ or <s>…</s>). Child-page blocks (<page url=…> … </page>, one or several lines) are not counted in
the candidate and activation phases, because the 100926.1 pages stay children until P5; the archived and sweep
phases count them, except the two dated records W8 keeps in place (the 20261009.1 register entry and the previous
candidate inventory). The sweep pages (Glow Operations Hub, HDE Change Flow Overview) are judged on this release's
57 archive ids, 100926.1, GCFPE-(PCR-)20261009.1 and v5.0.0 only (W8's P6 test), not on member-count wording or the
091426.1 family, which their dated canonical sections use for other purposes.
Phase rules:
  candidate   (C3, C4) controls still select 100926.1: no current non-candidate line of a control names
              GCFPE-20261027.1 or 102726.1 (CANDIDATE_ASSERTED); the Flow Index and each hub carry one
              "## Candidate — GCFPE-20261027.1 / 102726.1" section and the register one "Unselected candidate record
              — GCFPE-20261027.1"; the register's Current selection names GCFPE-20261009.1, 100926.1 and 55 and not
              GCFPE-20261027.1; the catalog (--catalog) links all 56 members at the map's ids and keeps its staging
              frontmatter (status UNSELECTED_CANDIDATE, promotion_authorized false, candidate_release), never
              REGISTER_CONTROLLED; titles are the 100926.1 ones.
  activation  (P1, P2) retired values are findings; frontmatter staging values are findings (an UNSELECTED status or
              posture, promotion_authorized false, candidate_release, validation_status QUALIFICATION_PENDING);
              titles are the 102726.1 ones (register unchanged); each hub links every member whose registry parent
              it is at the map's id (CL-05 on the Change Flow hub, PE on the TW hub); the Flow Index links all 56;
              the catalog links all 56 and is REGISTER_CONTROLLED; the register's Current selection names
              GCFPE-20261027.1, 102726.1 and 56 and links the catalog, PE and the register entry, and v5.1.0 is bound
              in its three current sections and on the Flow Index. --register-pending (P1, before P2) judges the
              register by the candidate rules instead.
  archived    (P5) as activation, child-page blocks counted; the Flow Index's disposition is
              SUPERSEDED_ARCHIVED_INTACT.
  sweep       (P6) the Glow Operations Hub and the HDE Change Flow Overview by the archived rules, plus a current
              selection section naming GCFPE-20261027.1 and linking the catalog.
PE Metaprompt 102726.1 is judged on its frontmatter only (the coordinator writes its head; its body is a reviewed
member body).

Stand-in: with a stand-in map (stand_in: true) the successor ids are binding_pass.probe() synthetic ids, so a
successor never equals a retired predecessor; the report says stand_in: true.

Bodies are D22 transient reads of this session's harness records (the precedent's reader, through this plan's
body_check.py helpers; subagents included). The report carries counts, ids and section headings; --report-lines adds
an 80-character excerpt for the terminal only, never to be redirected into the repository. Run with
PYTHONDONTWRITEBYTECODE=1 and CLAUDE_CODE_SESSION_ID set.
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[5]
PRECEDENT = HERE.parent.parent / "20261011-gcfpe-mb008-to-promotion"
REGISTRY = REPO / "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"
TSV = HERE / "members-100926.1.tsv"

REGISTER = "3d24590a05eb81ce942ad994cfca9fa1"
FLOW_INDEX = "3db4590a05eb81de9736ea69bac61016"
CF_HUB, IA_HUB, QA_HUB = "3db4590a05eb81d59059eb6b95ed5fcf", "3db4590a05eb8195a2ccf7c0959a8b6e", "3db4590a05eb814d96d3dcfa8835f96d"
ESC_HUB, TW_HUB = "3db4590a05eb81cd938de84cfffead9c", "3db4590a05eb811b9c14f2ae89c28df7"
HUB_NAMES = {CF_HUB: "HDE Change Flow", IA_HUB: "HDE IA", QA_HUB: "HDE QA", ESC_HUB: "Escalation", TW_HUB: "HDE TW"}
CHECKLIST = "3db4590a05eb812f87caed515836687f"
OPS_HUB = "3ce4590a05eb814f8892f88ff8539308"
OVERVIEW = "3c74590a05eb811d8433e7022629e213"
OLD_CATALOG = "3f74590a05eb812db385c2544d7570f7"
PE_PRED = "3f44590a05eb81f98b76c83465dc1960"
CL05_CANDIDATE = "4054590a05eb8155b301e2cb6dec31d5"
OLD_REL, OLD_VER, NEW_REL, NEW_VER = "GCFPE-20261009.1", "100926.1", "GCFPE-20261027.1", "102726.1"
KEPT_IDS_DEFAULT = ("GCFPE-MGMT-10",)
CONTROLS = [REGISTER, FLOW_INDEX, CF_HUB, IA_HUB, QA_HUB, ESC_HUB, TW_HUB, CHECKLIST]
SWEEP_PAGES = [OPS_HUB, OVERVIEW]
EXTRA_091426 = {"3db4590a05eb81738ef1d846e3c0df8c": "Glow HDE Complete Prompt Set — 091426.1",
                "3db4590a05eb8174be35d9e35acb3f77": "PE Metaprompt 091426.1"}

TITLES_OLD = {FLOW_INDEX: f"Glow HDE Prompt Flow Index — {OLD_REL} — {OLD_VER}",
              **{h: f"{n} — {OLD_REL} — {OLD_VER}" for h, n in HUB_NAMES.items()},
              CHECKLIST: f"GCFPE Alpha Establishment and Change Management Checklist — {OLD_VER}",
              REGISTER: "GCFPE Membership and Release Register"}
TITLES_NEW = {FLOW_INDEX: f"Glow HDE Prompt Flow Index — {NEW_REL} — {NEW_VER}",
              **{h: f"{n} — {NEW_REL} — {NEW_VER}" for h, n in HUB_NAMES.items()},
              CHECKLIST: f"GCFPE Alpha Establishment and Change Management Checklist — {NEW_VER}",
              REGISTER: "GCFPE Membership and Release Register",
              OPS_HUB: "Glow Operations Hub", OVERVIEW: "HDE Change Flow Overview"}
CATALOG_TITLE = f"Glow HDE Complete Prompt Set — {NEW_REL} — {NEW_VER}"
PE_TITLE = f"PE Metaprompt {NEW_VER}"

STRUCK = re.compile(r"~~.*?~~|<s>.*?</s>")
STAGING = re.compile(r"^(?:status: \S*UNSELECTED\S*|mutation_posture: \S*UNSELECTED\S*|promotion_authorized: false|"
                     r"candidate_release:.*|validation_status: QUALIFICATION_PENDING)$")
LIT_102726 = re.compile(r"100926\.1|GCFPE-(?:PCR-)?20261009\.1|(?<!other )\b55 members\b|\b55-member\b|"
                        r"\bexactly 55\b|\ball 55\b|member_count: 55\b")
LIT_091426 = re.compile(r"091426\.1|GCFPE-20260914\.1|GCFPE_ECOSYSTEM_CHANGE_REPORT|GCFPE_SUCCESSOR_RELEASE|"
                        r"READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION|gcfpe\.round27|(?i:sole (?:new|added) member)")
V500 = re.compile(r"v5\.0\.0")
V500_EXCUSE = re.compile(r"(?i)supersed|historical")
CANDIDATE_LIT = re.compile(r"GCFPE-20261027\.1|102726\.1")
MARKER = re.compile(r"(?i)predecessor|supersed|historical|archive|unchanged|corrected")
WINDOW, KEPT_WINDOW, AFTER_WINDOW = 100, 60, 150
CHILD_OPEN = re.compile(r'^\s*<page url="https://app\.notion\.com/p/([0-9a-f]{32})"[^>]*>')
HEX = re.compile(r"[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}")
FETCH_HEAD = re.compile(r'Here is the result of "fetch" for the Page with URL https://[^/\s]+/p/([0-9a-f-]{32,36}) '
                        r'as of (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z):')
TITLE = re.compile(r'<properties>\s*(\{.*?\})\s*</properties>', re.S)


def _body_check():
    sys.path.insert(0, str(HERE))
    import body_check  # noqa: E402
    return body_check


def _binding_pass():
    sys.path.insert(0, str(HERE))
    import binding_pass  # noqa: E402
    return binding_pass


def unescape(s: str) -> str:
    return s.replace("\\_", "_")


# --- transient read (the precedent's reader, keeping the title) --------------------------------------------------
def latest(page_id: str, root: str, session: str, since: int, fetched_after: str):
    """(captured, as_of, title, content) of the newest fetch at or after the cutoff, or None."""
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


# --- context from the successor map -------------------------------------------------------------------------
def tsv_rows() -> list:
    rows = []
    for line in TSV.read_text(encoding="utf-8").splitlines():
        if line.strip():
            pid, page, title, lane = line.split("\t")
            rows.append((pid, page, title, lane))
    assert len(rows) == 55
    return rows


def registry_parents() -> dict:
    t = REGISTRY.read_text(encoding="utf-8")
    rows = re.findall(r"^- prompt_key: (\S+)(.*?)(?=^- prompt_key: |\Z)", t, re.S | re.M)
    return {k: re.search(r"expected_parent_id: (\S+)", b).group(1) for k, b in rows}


def effective_map(path: str) -> tuple[dict, bool]:
    smap = json.loads(Path(path).read_text(encoding="utf-8"))
    stand_in = bool(smap.get("stand_in"))
    if stand_in:
        smap = _binding_pass().probe(smap)
    return smap, stand_in


def probe_id(name: str) -> str:
    return hashlib.sha256(f"probe:{name}".encode()).hexdigest()[:32]


def context(map_path: str, catalog: str = "", entry: str = "") -> dict:
    smap, stand_in = effective_map(map_path)
    raw = json.loads(Path(map_path).read_text(encoding="utf-8"))
    members = smap["members"]
    arch = {}
    for pid, row in raw["members"].items():
        if row["disposition"] == "SUCCESSOR":
            arch[row["predecessor_page_id"]] = pid
    arch[raw["pe"]["predecessor_page_id"]] = "PE 100926.1"
    arch[OLD_CATALOG] = "catalog 100926.1"
    arch[CL05_CANDIDATE] = "CL-05 candidate 102626.2"
    old = dict(EXTRA_091426)
    for f in sorted((PRECEDENT / "execute/candidate-graph-parts/prompts").glob("*.json")):
        node = json.loads(f.read_text(encoding="utf-8"))["node"]
        old[node["predecessor"]["notion_page_id"].replace("-", "")] = node["predecessor"]["title"]
    parents = registry_parents()
    expect = {}
    for pid, row in members.items():
        parent = parents.get(pid, CF_HUB if pid == "CL-05" else None)
        expect.setdefault(parent, set()).add(row["page_id"])
    expect.setdefault(TW_HUB, set()).add(smap["pe"]["page_id"])
    kept = tuple(pid for pid, r in members.items() if r["disposition"] == "KEPT") or KEPT_IDS_DEFAULT
    return {"map": smap, "stand_in": stand_in, "archive": {**old, **arch}, "archive_102726": arch,
            "archive_091426": old, "expect": expect, "all_members": {r["page_id"] for r in members.values()},
            "kept": kept, "pe": smap["pe"]["page_id"], "catalog": catalog, "entry": entry}


# --- sections and child-page blocks -----------------------------------------------------------------------------
def sections(text: str):
    """(heading path, logical line, is_child_block) for every line; the leading frontmatter block is its own
    section, and a child-page block (one or several lines) is one logical line."""
    lines = text.split("\n")
    stack, out, i = [], [], 0
    if lines and lines[0].strip() == "---":
        j = next((k for k in range(1, len(lines)) if lines[k].strip() == "---"), 0)
        for k in range(0, j + 1):
            out.append((("<frontmatter>",), lines[k], False))
        i = j + 1
    while i < len(lines):
        line = lines[i]
        if CHILD_OPEN.match(line):
            j = i
            while j < len(lines) and "</page>" not in lines[j]:
                j += 1
            out.append((tuple(h for _, h in stack), " ".join(lines[i:j + 1]), True))
            i = j + 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            stack = [s for s in stack if s[0] < level] + [(level, m.group(2).strip())]
        out.append((tuple(h for _, h in stack), line, False))
        i += 1
    return out


HIST = re.compile(r"(?i)histor|predecessor|supersed|archiv")


def historical(path: tuple) -> bool:
    if path == ("<frontmatter>",):
        return False
    for h in reversed(path):
        if HIST.search(h):
            return True
        if h.lower().startswith("current"):
            return False
    return False


def candidate_section(path: tuple) -> bool:
    return bool(path) and (path[-1].startswith("Candidate —") or path[-1].startswith("Unselected candidate record"))


SENTENCE_END = re.compile(r"[.;](?:</[a-z]+>)*\s")


def excused(line: str, start: int, kept: tuple, value: str) -> bool:
    if MARKER.search(line[max(0, start - WINDOW):start]):
        return True
    ends = [m.end() for m in SENTENCE_END.finditer(line, 0, start)]
    if MARKER.search(line[(ends[-1] if ends else 0):start]):
        return True  # a marker earlier in the same sentence (A4 addition; the 100-character window is kept)
    if any(k.start() <= start < k.end() for k in STRUCK.finditer(line)):
        return True
    if value == "100926.1":
        before = line[max(0, start - KEPT_WINDOW):start]
        if any(k in before for k in kept):
            return True
        if any(line.lstrip().startswith(f"| <code>{k}</code> |") for k in kept):
            return True
    return False


# dated records W8 keeps in place at P5 (transaction.steps P5: the 20261009.1 register entry and the previous
# candidate inventory); their child-page blocks name the release they record
RETAINED_RECORDS = {"3f74590a05eb81b8b7bbcbfe0dcacea9": "GCFPE Membership and Release Register Entry — GCFPE-20261009.1",
                    "3f44590a05eb8110aa69fe4189ad9abc": "GCFPE-20261009.1 — Alpha Feedback Candidate — 100926.1"}


def findings(text: str, ctx: dict, phase: str, sweep_page: bool = False) -> list:
    ids = set(ctx["archive_102726"]) if sweep_page else set(ctx["archive"])
    lits = LITERALS_SWEEP if sweep_page else LITERALS_ALL
    out = []
    count_children = phase in ("archived", "sweep")
    for path, raw, is_child in sections(text):
        line = unescape(raw)
        if path == ("<frontmatter>",) and STAGING.match(line.strip()):
            out.append({"section": "<frontmatter>", "archive_ids": [], "literals": ["STAGING_VALUE"],
                        "excerpt": line.strip()[:80]})
            continue
        if historical(path):
            continue
        if is_child and not count_children:
            continue
        if is_child and CHILD_OPEN.match(line) and CHILD_OPEN.match(line).group(1) in RETAINED_RECORDS:
            continue
        hits, lit = set(), set()
        for m in list(HEX.finditer(line)) + list(lits.finditer(line)):
            value = m.group(0)
            is_id = HEX.fullmatch(value) is not None
            if is_id and value.replace("-", "") not in ids:
                continue
            if excused(line, m.start(), ctx["kept"], value):
                continue
            (hits if is_id else lit).add(value.replace("-", "") if is_id else value)
        for m in V500.finditer(line):
            if V500_EXCUSE.search(line[max(0, m.start() - WINDOW):m.end() + AFTER_WINDOW]):
                continue
            if any(k.start() <= m.start() < k.end() for k in STRUCK.finditer(line)):
                continue
            lit.add("v5.0.0")
        if hits or lit:
            out.append({"section": path[-1] if path else "<top>", "archive_ids": sorted(hits),
                        "literals": sorted(lit), "excerpt": line.strip()[:80]})
    return out


LITERALS_ALL = re.compile(LIT_102726.pattern + "|" + LIT_091426.pattern)
# sweep pages (the Glow Operations Hub, the HDE Change Flow Overview) are workspace navigation, not release controls:
# W8's P6 test is "no page asserting GCFPE-20261009.1 / 100926.1 / 55 as current", so they are judged on this
# release's archive ids, its release literals and the v5.0.0 binding; member-count wording and the 091426.1 family,
# which their dated canonical sections use for other purposes, are not judged there (A4 limit, disclosed)
LITERALS_SWEEP = re.compile(r"100926\.1|GCFPE-(?:PCR-)?20261009\.1")


def candidate_findings(text: str) -> list:
    out = []
    for path, raw, is_child in sections(text):
        line = unescape(raw)
        if is_child or historical(path) or candidate_section(path) or path == ("<frontmatter>",):
            continue
        if CANDIDATE_LIT.search(line):
            out.append({"section": path[-1] if path else "<top>", "archive_ids": [],
                        "literals": ["CANDIDATE_ASSERTED"], "excerpt": line.strip()[:80]})
    return out


def frontmatter_lines(text: str) -> list:
    return [unescape(l).strip() for p, l, _ in sections(text) if p == ("<frontmatter>",)]


def section_text(text: str, pred) -> str:
    return "\n".join(unescape(l) for p, l, _ in sections(text) if p and pred(p[-1]))


def linked(text: str) -> set:
    return {h.replace("-", "") for h in HEX.findall(text)}


def check_text(page: str, title: str, text: str, ctx: dict, phase: str, register_pending: bool = False) -> dict:
    """page: a real page id, or 'CATALOG', 'PE', 'ENTRY' for the pages this Modification creates."""
    is_catalog = page in ("CATALOG", ctx.get("catalog") or "<none>")
    is_pe = page in ("PE", ctx["pe"])
    is_entry = page in ("ENTRY", ctx.get("entry") or "<none>")
    judge = "candidate" if (phase == "candidate" or (page == REGISTER and register_pending)) else phase
    row = {"page": page, "phase": phase, "judged_as": judge}
    links = linked(text)
    if judge == "candidate":
        f = [] if (is_catalog or is_pe or is_entry) else candidate_findings(text)
        if page in (FLOW_INDEX, *HUB_NAMES):
            n = sum(1 for p, l, _ in sections(text) if l.strip() == f"## Candidate — {NEW_REL} / {NEW_VER}")
            row["candidate_section_once"] = n == 1
        if page == REGISTER:
            n = sum(1 for p, l, _ in sections(text) if l.startswith(f"## Unselected candidate record — {NEW_REL}"))
            row["candidate_record_once"] = n == 1
            cur = section_text(text, lambda h: h.lower().startswith("current selection"))
            row["current_selection_ok"] = (all(t in cur for t in (OLD_REL, OLD_VER, "55"))
                                           and NEW_REL not in cur and NEW_VER not in cur)
        if is_catalog:
            fm = frontmatter_lines(text)
            row["catalog_staging_ok"] = ("status: UNSELECTED_CANDIDATE" in fm and "promotion_authorized: false" in fm
                                         and any(l.startswith("candidate_release:") for l in fm)
                                         and "status: REGISTER_CONTROLLED" not in fm)
            row["catalog_members_missing"] = len(ctx["all_members"] - links)
            want_title = CATALOG_TITLE
        else:
            want_title = TITLES_OLD.get(page)
    else:
        f = findings(text, ctx, phase, sweep_page=page in SWEEP_PAGES)
        if is_pe:
            f = [r for r in f if r["section"] == "<frontmatter>"]
            want_title = PE_TITLE
        elif is_catalog:
            want_title = CATALOG_TITLE
            fm = frontmatter_lines(text)
            row["catalog_selected_ok"] = "status: REGISTER_CONTROLLED" in fm
            row["catalog_members_missing"] = len(ctx["all_members"] - links)
        elif is_entry:
            want_title = None
        else:
            want_title = TITLES_NEW.get(page)
        if page in ctx["expect"] and page != FLOW_INDEX:
            row["successors_expected"] = len(ctx["expect"][page])
            row["successors_missing"] = len(ctx["expect"][page] - links)
        if page == FLOW_INDEX:
            row["topology_missing"] = len(ctx["all_members"] - links)
            row["procedure_v510_bound"] = "v5.1.0" in text
            if phase in ("archived", "sweep"):
                row["disposition_archived"] = ("predecessor_disposition: SUPERSEDED_ARCHIVED_INTACT"
                                               in frontmatter_lines(text))
        if page == REGISTER:
            cur = section_text(text, lambda h: h.lower().startswith("current selection"))
            want_links = {i for i in (ctx.get("catalog"), ctx["pe"], ctx.get("entry")) if i}
            row["current_selection_ok"] = (all(t in cur for t in (NEW_REL, NEW_VER, "56"))
                                           and want_links <= linked(cur) and len(want_links) == 3)
            bound = [section_text(text, lambda h, s=s: h.startswith(s)) for s in
                     ("Current selection", "Current source-reference policy", "Current GCFPE procedure")]
            row["procedure_v510_in_three_current_sections"] = all("v5.1.0" in b for b in bound)
        if page in SWEEP_PAGES:
            cur = section_text(text, lambda h: h.lower().startswith("current") and "selection" in h.lower())
            row["sweep_current_selection_ok"] = (NEW_REL in cur and bool(ctx.get("catalog"))
                                                 and ctx["catalog"] in linked(cur))
    if want_title is not None:
        row["title_ok"] = title == want_title
    row["findings"] = len(f)
    row["finding_rows"] = f
    bad_flags = [k for k in ("candidate_section_once", "candidate_record_once", "current_selection_ok",
                             "catalog_staging_ok", "catalog_selected_ok", "title_ok", "procedure_v510_bound",
                             "procedure_v510_in_three_current_sections", "disposition_archived",
                             "sweep_current_selection_ok") if row.get(k) is False]
    bad_counts = [k for k in ("successors_missing", "topology_missing", "catalog_members_missing") if row.get(k)]
    row["failed_checks"] = bad_flags + bad_counts
    row["ok"] = not f and not bad_flags and not bad_counts
    return row


def check(a) -> dict:
    ctx = context(a.successor_map, a.catalog, a.entry)
    root, session = os.path.expanduser("~/.claude/projects"), os.environ.get("CLAUDE_CODE_SESSION_ID")
    default = SWEEP_PAGES if a.phase == "sweep" else CONTROLS
    pages = (a.pages or list(default)) + ([a.catalog] if a.catalog else []) + ([a.entry] if a.entry else [])
    if a.with_pe:
        pages.append(ctx["pe"])
    rows, ok = [], True
    for page in pages:
        got = latest(page, root, session, a.since_minutes, a.fetched_after)
        if got is None:
            rows.append({"page": page, "error": "NO_FETCH_FOUND", "ok": False})
            ok = False
            continue
        row = check_text(page, got[2], got[3], ctx, a.phase, a.register_pending)
        row["as_of"] = got[1]
        if not a.report_lines:
            for r in row["finding_rows"]:
                r.pop("excerpt")
        ok &= row["ok"]
        rows.append(row)
    return {"mode": "check", "phase": a.phase, "register_pending": a.register_pending, "stand_in": ctx["stand_in"],
            "archive_set_102726": len(ctx["archive_102726"]), "archive_set_091426": len(ctx["archive_091426"]),
            "pages": rows, "findings_total": sum(r.get("findings", 0) for r in rows),
            "failed_checks_total": sum(len(r.get("failed_checks", [])) for r in rows) + sum("error" in r for r in rows),
            "ok": ok,
            "d22": "transient reads of this session's harness records; counts, ids and headings only"
                   + ("; excerpts for the terminal" if a.report_lines else "")}


# --- self-test: every check fails on an injected regression ---------------------------------------------------
def selftest(map_path: str) -> dict:
    ctx = context(map_path, catalog=probe_id("CATALOG"), entry=probe_id("ENTRY"))
    smap = ctx["map"]
    raw = json.loads(Path(map_path).read_text(encoding="utf-8"))
    pred_id = raw["members"]["PR-30"]["predecessor_page_id"]

    def links_for(page):
        return "".join(f'<mention url="https://app.notion.com/p/{s}">m</mention>\n' for s in sorted(ctx["expect"].get(page, ())))
    all_links = "".join(f'<mention url="https://app.notion.com/p/{s}">m</mention>\n' for s in sorted(ctx["all_members"]))
    cf = links_for(CF_HUB)
    cf_no_cl05 = cf.replace(f'<mention url="https://app.notion.com/p/{smap["members"]["CL-05"]["page_id"]}">m</mention>\n', "")
    reg_ok = (f"## Current selection — {NEW_REL} / {NEW_VER}\n{NEW_REL} / {NEW_VER} / 56 — "
              f"[c](https://app.notion.com/p/{ctx['catalog']}) [p](https://app.notion.com/p/{ctx['pe']}) "
              f"[e](https://app.notion.com/p/{ctx['entry']})\n| operating procedure | v5.1.0; v5.0.0 is superseded and historical |\n"
              f"## Current source-reference policy — {NEW_VER}\nv5.1.0\n## Current GCFPE procedure and operator access — {NEW_VER}\nv5.1.0\n")
    reg_old = (f"## Current selection — {OLD_REL} / {OLD_VER}\n{OLD_REL} / {OLD_VER} / 55\n"
               f"## Unselected candidate record — {NEW_REL} — 2026-10-27\nlisted\n")
    cat_cand = ("---\ncandidate_release: GCFPE-20261027.1\nstatus: UNSELECTED\\_CANDIDATE\npromotion_authorized: false\n---\n"
                + all_links)
    T = TITLES_NEW
    cases = {
        # (page, title, text, phase, register_pending, expect_ok)
        "count_statement_fails": (CF_HUB, T[CF_HUB], "## Native purpose\nexactly 55 members\n" + cf, "activation", False, False),
        "kept_member_title_passes": (CF_HUB, T[CF_HUB], "## Shared controls\n[GCFPE-MGMT-10 — Manage an Ecosystem Change — 100926.1]"
                                     "(https://app.notion.com/p/3f74590a05eb81b69bd8c27106f7a59d)\n" + cf, "activation", False, True),
        "kept_row_current_version_passes": (CF_HUB, T[CF_HUB], "## Membership\n| <code>GCFPE-MGMT-10</code> | x | <code>GCFPE-MGMT</code> | "
                                            "<code>https://app.notion.com/p/3f74590a05eb81b69bd8c27106f7a59d?pvs=204</code> | <code>100926.1</code> |\n" + cf,
                                            "activation", False, True),
        "successor_predecessor_id_fails": (CF_HUB, T[CF_HUB], f"## Native purpose\n<mention url=\"https://app.notion.com/p/{pred_id}\"/>\n" + cf,
                                           "activation", False, False),
        "same_id_under_historical_passes": (CF_HUB, T[CF_HUB], f"## Historical selection — {OLD_REL} / {OLD_VER}\n"
                                            f"<mention url=\"https://app.notion.com/p/{pred_id}\"/>\n" + cf, "activation", False, True),
        "cf_hub_without_cl05_fails": (CF_HUB, T[CF_HUB], "## Native purpose\nok\n" + cf_no_cl05, "activation", False, False),
        "register_binding_v500_fails": (REGISTER, T[REGISTER], reg_ok.replace("v5.1.0; v5.0.0 is superseded and historical",
                                                                               "docs/ephemeral/…-v5.0.0-20260923.md (on main)"),
                                        "activation", False, False),
        "register_v500_superseded_passes": (REGISTER, T[REGISTER], reg_ok, "activation", False, True),
        "candidate_catalog_register_controlled_fails": ("CATALOG", CATALOG_TITLE, cat_cand.replace("status: UNSELECTED\\_CANDIDATE",
                                                                                                    "status: REGISTER\\_CONTROLLED"),
                                                        "candidate", False, False),
        "candidate_catalog_passes": ("CATALOG", CATALOG_TITLE, cat_cand, "candidate", False, True),
        "candidate_catalog_missing_member_fails": ("CATALOG", CATALOG_TITLE, cat_cand.split("\n<mention")[0] + "\n", "candidate", False, False),
        "release_literal_fails": (IA_HUB, T[IA_HUB], f"## Activation contract\nThe register selects {OLD_REL}.\n" + links_for(IA_HUB),
                                  "activation", False, False),
        "precedent_literal_fails": (IA_HUB, T[IA_HUB], "## Activation contract\nThe register selected 091426.1.\n" + links_for(IA_HUB),
                                    "activation", False, False),
        "escaped_vocabulary_fails": (IA_HUB, T[IA_HUB], "## Native\nreturns GCFPE\\_SUCCESSOR\\_RELEASE\n" + links_for(IA_HUB),
                                     "activation", False, False),
        "struck_html_passes": (IA_HUB, T[IA_HUB], "## Checklist\n- [ ] <s>All 55 are 100926.1 siblings</s>\n" + links_for(IA_HUB),
                               "activation", False, True),
        "other_55_members_passes": (IA_HUB, T[IA_HUB], "## Release rule\nGCFPE-MGMT-10 is <code>100926.1</code>; the other 55 members are "
                                    "<code>102726.1</code>.\n" + links_for(IA_HUB), "activation", False, True),
        "all_55_fails": (IA_HUB, T[IA_HUB], "## Release rule\nall 55 are current\n" + links_for(IA_HUB), "activation", False, False),
        "child_block_activation_passes": (IA_HUB, T[IA_HUB], f'<page url="https://app.notion.com/p/{pred_id}">\nPR-30 — x — 100926.1\n</page>\n'
                                          + links_for(IA_HUB), "activation", False, True),
        "child_block_archived_fails": (IA_HUB, T[IA_HUB], f'<page url="https://app.notion.com/p/{pred_id}">\nPR-30 — x — 100926.1\n</page>\n'
                                       + links_for(IA_HUB), "archived", False, False),
        "staging_frontmatter_fails": (IA_HUB, T[IA_HUB], "---\nstatus: UNSELECTED\\_CANDIDATE\n---\n" + links_for(IA_HUB),
                                      "activation", False, False),
        "candidate_asserted_fails": (QA_HUB, TITLES_OLD[QA_HUB], f"## Candidate — {NEW_REL} / {NEW_VER}\nunselected\n"
                                     f"## Activation contract\nThe register selects {NEW_REL}.\n", "candidate", False, False),
        "candidate_section_passes": (QA_HUB, TITLES_OLD[QA_HUB], f"## Candidate — {NEW_REL} / {NEW_VER}\nThe {NEW_VER} pages are "
                                     f"an unselected candidate; the register still selects {OLD_REL}.\n", "candidate", False, True),
        "candidate_section_missing_fails": (QA_HUB, TITLES_OLD[QA_HUB], "## Activation contract\nok\n", "candidate", False, False),
        "register_pending_passes_old_selection": (REGISTER, T[REGISTER], reg_old, "activation", True, True),
        "register_not_pending_fails_old_selection": (REGISTER, T[REGISTER], reg_old, "activation", False, False),
        "candidate_register_selecting_new_fails": (REGISTER, T[REGISTER], reg_old.replace(f"{OLD_REL} / {OLD_VER} / 55\n",
                                                   f"{OLD_REL} / {OLD_VER} / 55 and {NEW_REL}\n"), "candidate", False, False),
        "wrong_title_fails": (IA_HUB, TITLES_OLD[IA_HUB], "## x\n" + links_for(IA_HUB), "activation", False, False),
        "flow_index_without_v510_fails": (FLOW_INDEX, T[FLOW_INDEX], "## Selected topology\n" + all_links, "activation", False, False),
        "flow_index_clean_passes": (FLOW_INDEX, T[FLOW_INDEX], "## Selected topology\nv5.1.0\n" + all_links, "activation", False, True),
        "flow_index_archived_disposition_missing_fails": (FLOW_INDEX, T[FLOW_INDEX], "---\npredecessor_disposition: SUPERSEDED\n---\n"
                                                          "## Selected topology\nv5.1.0\n" + all_links, "archived", False, False),
        "pe_body_not_judged_passes": (ctx["pe"], PE_TITLE, "---\nselected_release: GCFPE-20261027.1\n---\n## Body\nGCFPE-20261009.1\n",
                                      "activation", False, True),
        "pe_staging_fails": (ctx["pe"], PE_TITLE, "---\npromotion_authorized: false\n---\n", "activation", False, False),
        "sweep_hub_without_selection_fails": (OPS_HUB, T[OPS_HUB], "## Current selection — x\nnothing\n", "sweep", False, False),
        "sweep_hub_selected_passes": (OPS_HUB, T[OPS_HUB], f"## Current selection — {NEW_REL} / {NEW_VER}\n{NEW_REL} "
                                      f"[c](https://app.notion.com/p/{ctx['catalog']})\n", "sweep", False, True),
        "same_sentence_marker_passes": (IA_HUB, T[IA_HUB], "## Native\nThe 57 superseded pages — the changed members' <code>100926.1</code> "
                                        "pages, PE Metaprompt 100926.1, and, after a long enough clause to pass the window, the <code>100926.1</code> catalog.\n"
                                        + links_for(IA_HUB), "activation", False, True),
        "previous_sentence_distant_marker_fails": (IA_HUB, T[IA_HUB], "## Native\nThe superseded pages are gone, and this sentence is "
                                                   "made long enough to leave the window behind. The catalog is 100926.1 today.\n"
                                                   + links_for(IA_HUB), "activation", False, False),
        "sweep_count_wording_not_judged_passes": (OPS_HUB, T[OPS_HUB], f"## Current selection — {NEW_REL}\n{NEW_REL} "
                                                  f"[c](https://app.notion.com/p/{ctx['catalog']})\n## Method\nreturns all 55 values\n",
                                                  "sweep", False, True),
        "sweep_release_literal_fails": (OPS_HUB, T[OPS_HUB], f"## Current selection — {NEW_REL}\n{NEW_REL} "
                                        f"[c](https://app.notion.com/p/{ctx['catalog']})\n## Find\nUse the {OLD_REL} catalog\n",
                                        "sweep", False, False),
        "retained_record_child_archived_passes": (IA_HUB, T[IA_HUB], '<page url="https://app.notion.com/p/3f44590a05eb8110aa69fe4189ad9abc">\n'
                                                  "GCFPE-20261009.1 — Alpha Feedback Candidate — 100926.1\n</page>\n" + links_for(IA_HUB),
                                                  "archived", False, True),
        "corrected_line_passes": (OVERVIEW, T[OVERVIEW], f"## Current GCFPE selection — {NEW_REL}\n{NEW_REL} [c](https://app.notion.com/p/{ctx['catalog']})\n"
                                  "## Find\nCorrected 2026-10-28 from <code>100926.1</code>.\n", "sweep", False, True),
    }
    rows, ok = {}, True
    for name, (page, title, text, phase, pending, want) in cases.items():
        got = check_text(page, title, text, ctx, phase, pending)["ok"]
        rows[name] = got == want
        ok &= got == want
    sizes = {"archive_set_102726": len(ctx["archive_102726"]), "archive_set_091426": len(ctx["archive_091426"])}
    ok &= sizes["archive_set_102726"] == 57 and sizes["archive_set_091426"] == 57
    return {"mode": "selftest", "stand_in": ctx["stand_in"], **sizes, "cases": rows,
            "cases_passed": sum(rows.values()), "cases_total": len(rows), "ok": ok}


def main() -> int:
    ap = argparse.ArgumentParser(prog="control_check_102726.py")
    sub = ap.add_subparsers(dest="mode", required=True)
    c = sub.add_parser("check")
    c.add_argument("--successor-map", required=True)
    c.add_argument("--phase", choices=["candidate", "activation", "archived", "sweep"], required=True)
    c.add_argument("--register-pending", action="store_true")
    c.add_argument("--pages", nargs="*")
    c.add_argument("--catalog", default="")
    c.add_argument("--entry", default="")
    c.add_argument("--with-pe", action="store_true")
    c.add_argument("--fetched-after", default="")
    c.add_argument("--since-minutes", type=int, default=600)
    c.add_argument("--report-lines", action="store_true")
    s = sub.add_parser("selftest")
    s.add_argument("--successor-map", required=True)
    a = ap.parse_args()
    res = check(a) if a.mode == "check" else selftest(a.successor_map)
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
