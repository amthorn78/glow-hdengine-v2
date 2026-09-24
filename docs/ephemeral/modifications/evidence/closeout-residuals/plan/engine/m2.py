#!/usr/bin/env python3
"""PART-06, method M2 (spec §7.4), made mechanical (P-105): the page content built from the Drive file, and the
readback F1-F10 computed from the page as fetched. The Drive file is the Candidate CRD list, not a prompt body; it is
read from the newest download_file_content result of this session (engine/drive_check.newest_download, the same
checks), decoded in memory. Only `build` writes, and only to the --out directory it is given (EXECUTE's $SCRATCH).

  m2.py build --run EX/run.json --out DIR [--harness-root H] [--session S]
      Refuses unless the download passes drive_check's size, sha256, fence and M2-old checks. Writes
      DIR/page.create.md, the whole create-time content (§7.4.2 steps 3-4: M2-R1..R9 with the three self-link spots
      as plain text, the callout, the revision bullet, both tables as <table header-row="true">, the fence as one
      ```markdown block), and DIR/page.small.md, the same without the H3 *Preserved pre-repair source*, its paragraph
      and the code block (the fallback of step 5). Prints sizes and sha256s only. {{MIGRATION_DATE}} comes from
      EX/run.json; a create sends page.create.md with preserve_internal_links true, so the list's Notion links keep
      their text.
  m2.py check --page PAGE --hub HUB --run EX/run.json --stage create|final|auto [--harness-root H] [--session S]
      F1-F10 (§7.4.3) on the newest fetch of PAGE against the content `build` makes from the same download, `create`
      at step 6 (the self-link spots as plain text, 8 links) or `final` after step 7 (the links in place, 11 links),
      and on the newest fetch of HUB for F1's parent (exactly one Hub child carries the title, and it is PAGE). `auto` (a resumed X5.1, P-112) reads the stage from the page:
      `create` while all three step-7 old_strs stand on it, `final` once none does; with some and not others it
      refuses PARTIAL_STEP7 (send `step7-ops`, then check again). Prints booleans and counts, the stage used, and
      on a failure the first differing item's position; exits 0 only when all ten pass.
  m2.py step7-ops --page PAGE --run EX/run.json [--harness-root H] [--session S]
      Step 7's operations (M2.json self_links.step7_ops, the URL filled from EX/run.json) whose old_str still stands
      on the page as fetched, for one update_content call; each is a replacement whose old_str is gone once it lands,
      so sent again it matches nothing (P-103). Prints an empty list once all three have landed.
  m2.py insert-op --page PAGE --run EX/run.json [--harness-root H] [--session S]
      The fallback's second write: the update_content operation that puts the H3, its paragraph and the code block
      back before `## Maintenance rule` on the page as fetched, widened to the line before so that sent again it
      matches nothing (P-103). Refuses unless the page has no code block yet.

Normalizations the readback applies to both sides, and nothing else: blank lines are ignored (Notion drops them);
a backslash before any of \\ * ~ ` $ [ ] < > { } | ^ is removed; a block's {color=...} attribute list is removed; a
<mention-page url="U">T</mention-page> is read as the link [T](U), and a text-less <mention-page url="U"/> as [T](U) with
the one text the build gives links to U; a Notion link target is compared by its 32-hex page
id; list numbers are not compared (Notion may renumber); whitespace runs are one space; in the code block only
trailing spaces on a line are tolerated, and they are counted (F7).
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import dryrun as D  # noqa: E402
import drive_check as DC  # noqa: E402
import ctrl as K  # noqa: E402

M2 = DC.M2
TITLE = "Candidate CRD Items List"
H3 = "### Preserved pre-repair source"
MAINT = "## Maintenance rule"
NOTION = re.compile(r"https?://(?:[a-z]+\.)?notion\.(?:so|com)/(?:[^\s)\"]*?)([0-9a-f]{32}|[0-9a-f-]{36})")
FENCE_SHA = re.search(r"sha256 ([0-9a-f]{64})", M2["file"]["fence"]).group(1)


def refuse(why, **kw):
    print(json.dumps({"refused": why, **kw}))
    raise SystemExit(1)


def drive_text():
    got = DC.newest_download()
    if got is None:
        refuse("NO_DOWNLOAD_FOUND")
    _, src, data = got
    if len(data) != M2["file"]["bytes"] or hashlib.sha256(data).hexdigest() != M2["file"]["sha256"]:
        refuse("DRIVE_BYTES_DIFFER", source_file=src)
    return data.decode("utf-8"), src


def fence_bounds(lines):
    o = [i for i, ln in enumerate(lines) if ln.startswith("```markdown")]
    if len(o) != 1:
        refuse("FENCE_NOT_ONE")
    c = min(i for i, ln in enumerate(lines) if ln == "```" and i > o[0])
    return o[0], c


def table_md(rows):
    out = ['<table header-row="true">']
    for r in rows:
        out.append("\t<tr>")
        out += [f"\t\t<td>{c}</td>" for c in r]
        out.append("\t</tr>")
    out.append("</table>")
    return out


def build(text, run, stage):
    """The page content for `stage` ('create' or 'final'), as a list of lines, and the fence's inner text."""
    lines = text.split("\n")
    fo, fc = fence_bounds(lines)
    inner = "".join(ln + "\n" for ln in lines[fo + 1:fc])
    before, after = "\n".join(lines[:fo]), "\n".join(lines[fc + 1:])
    date = run.get("migration_date")
    url = run.get("url")
    if not date or (stage == "final" and not url):
        refuse("TOKEN_NOT_RECORDED", need=["migration_date"] + (["url"] if stage == "final" else []))
    for r in M2["rewrites"]:
        old = r["old"].rstrip("\n")
        new = r["new"]
        if stage == "create" and r["id"] in M2["self_links"]["create_time_text"]:
            new = M2["self_links"]["create_time_text"][r["id"]]
        new = new.replace("{{MIGRATION_DATE}}", date)
        if url:
            new = new.replace("{{CANDIDATE_CRD_LIST_URL}}", url)
        n = D.occ(before, old) + D.occ(after, old)
        if n != 1:
            refuse("M2_OLD_NOT_ONCE", id=r["id"], count=n)
        if old in before:
            before = before.replace(old, new, 1)
        else:
            after = after.replace(old, new, 1)
    out = []
    callout = M2["callout"].strip().replace("{{MIGRATION_DATE}}", date)
    if M2["file"]["sha256"] not in callout:
        callout = callout.replace("31,923 B,", f"31,923 B, sha256 `{M2['file']['sha256']}`,", 1)
    out += ["<callout>", "\t" + callout, "</callout>"]

    def convert(seg, drop_h1):
        res, tbl = [], []
        for ln in seg.split("\n"):
            if drop_h1 and ln == "# " + TITLE:
                drop_h1 = False
                continue
            if ln.startswith("|"):
                cells = [c.strip() for c in ln.strip().strip("|").split("|")]
                if not all(re.fullmatch(r"-{3,}", c) for c in cells):
                    tbl.append(cells)
                continue
            if tbl:
                res += table_md(tbl)
                tbl = []
            if ln.strip():
                res.append(ln.rstrip())
        if tbl:
            res += table_md(tbl)
        return res
    out += convert(before, True)
    out += ["```markdown"] + inner.rstrip("\n").split("\n") + ["```"]
    tail = convert(after, False)
    last = max(i for i, ln in enumerate(tail) if ln.startswith("- "))
    bullet = M2["revision_bullet"].replace("{{MIGRATION_DATE}}", date)
    tail.insert(last + 1, bullet)
    out += tail
    if any("{{" in ln for ln in out if not ln.startswith("\t")) or ("{{" in callout):
        refuse("UNFILLED_TOKEN")
    return out, inner


def unescape(s):
    return re.sub(r"\\([\\*~`$\[\]<>{}|^])", r"\1", s)


def target(u):
    m = NOTION.search(u)
    return m.group(1).replace("-", "") if m else u


def links(s):
    s = re.sub(r'<mention-page url="([^"]*)"\s*(?:/>|>(.*?)</mention-page>)', lambda m: f"[{m.group(2) or ''}]({m.group(1)})", s)
    return [(unescape(t).strip(), target(u)) for t, u in re.findall(r"\[([^\]]*)\]\(([^)\s]*)\)", s)]


def norm(s):
    s = re.sub(r'<mention-page url="([^"]*)"\s*(?:/>|>(.*?)</mention-page>)', lambda m: m.group(2) or "", s)
    s = re.sub(r"\[([^\]]*)\]\(([^)\s]*)\)", r"\1", s)
    s = re.sub(r"\s*\{color=\"[^\"]*\"\}\s*$", "", s)
    s = unescape(s).replace("<br>", " ")
    s = re.sub(r"^\s*(?:#{1,4} |> |- \[[ x]\] |- |\d+\. )", "", s)
    s = s.replace("**", "").replace("~~", "").replace("`", "")
    s = re.sub(r"(?<!\w)\*(?!\s)|(?<!\s)\*(?!\w)", "", s)
    return re.sub(r"\s+", " ", s).strip()


def parse(content):
    """(code blocks [(lang, text)], tables [[cells]], blocks [(kind, raw line)]) of Notion-flavored Markdown."""
    codes, tables, blocks = [], [], []
    lines = content.split("\n")
    i = 0
    while i < len(lines):
        ln = lines[i]
        st = ln.strip()
        if st.startswith("```"):
            lang = st[3:].strip()
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            codes.append((lang, "".join(x + "\n" for x in lines[i + 1:j])))
            i = j + 1
            continue
        if st.startswith("<callout"):
            while i < len(lines) and "</callout>" not in lines[i]:
                i += 1
            i += 1
            continue
        if st.startswith("<table"):
            rows, cur = [], None
            while i < len(lines) and "</table>" not in lines[i]:
                t = lines[i].strip()
                if t.startswith("<tr"):
                    cur = []
                elif t.startswith("</tr>"):
                    rows.append(cur)
                    cur = None
                else:
                    for c in re.findall(r"<td[^>]*>(.*?)</td>", t):
                        if cur is not None:
                            cur.append(c)
                i += 1
            tables.append(rows)
            i += 1
            continue
        if st and st != "<empty-block/>":
            kind = "h" if re.match(r"#{1,4} ", st) else "li" if re.match(r"(?:- |\d+\. )", st) else "p"
            blocks.append((kind, st))
        i += 1
    return codes, tables, blocks


def sections(blocks):
    sec, cur = {}, None
    for kind, raw in blocks:
        if kind == "h" and raw.startswith("## "):
            cur = norm(raw)
            sec[cur] = []
        elif cur is not None:
            sec[cur].append((kind, raw))
    return sec


def fill_mentions(content, pairs):
    """A text-less <mention-page url="U"/> (Notion shows the page's title there) read as [T](U), where T is the text the
    build gives every link to U; a target the build links under more than one text, or not at all, is left as is and
    fails F6 (P-112)."""
    by = {}
    for t, u in pairs:
        by.setdefault(u, set()).add(t)

    def sub(m):
        ts = by.get(target(m.group(1)))
        return f"[{next(iter(ts))}]({m.group(1)})" if ts and len(ts) == 1 else m.group(0)
    return re.sub(r'<mention-page url="([^"]*)"\s*/>', sub, content)


def check(content, title, hub_children, page_id, text, run, stage):
    exp_lines, inner = build(text, run, stage)
    e_codes, e_tables, e_blocks = parse("\n".join(exp_lines))
    content = fill_mentions(content, [x for _, b in e_blocks for x in links(b)]
                            + [x for t in e_tables for row in t for c in row for x in links(c)])
    codes, tables, blocks = parse(content)
    r = {}
    # exactly one Hub child carries the title, and it is this page: a second create (a lost response, then a stale
    # Hub fetch) fails F1 (P-112)
    same = [c for c in hub_children if c["title"] == TITLE]
    r["F1_title_and_parent"] = title == TITLE and len(same) == 1 and same[0]["id"] == page_id
    r["F1_children_titled"] = len(same)
    eh = [norm(b) for k, b in e_blocks if k == "h"]
    gh = [norm(b) for k, b in blocks if k == "h"]
    r["F2_headings"] = eh == gh
    r["F2_counts"] = {"expected": len(eh), "got": len(gh)}
    esec, gsec = sections(e_blocks), sections(blocks)
    act = "Active CRD candidate list"
    r["F3_active_empty_and_moved_rows"] = (not [b for k, b in gsec.get(act, []) if k == "li"]
                                           and any("Empty — 0 active" in norm(b) for _, b in gsec.get(act, []))
                                           and len(tables) == 2 and len(tables[1]) - 1 == 4)

    def cells(t):
        return [[(norm(c), sorted(links(c))) for c in row] for row in t]
    r["F4_moved_table"] = len(tables) == 2 and len(e_tables) == 2 and cells(tables[1]) == cells(e_tables[1]) \
        and all(len(row) == 6 for row in tables[1][1:])
    r["F5_review_table"] = len(tables) >= 1 and cells(tables[0]) == cells(e_tables[0]) and len(tables[0]) - 1 == 6 \
        and all(len(row) == 2 for row in tables[0])
    el = sorted(x for _, b in e_blocks for x in links(b)) + sorted(x for t in e_tables for row in t for c in row for x in links(c))
    gl = sorted(x for _, b in blocks for x in links(b)) + sorted(x for t in tables for row in t for c in row for x in links(c))
    r["F6_links"] = sorted(el) == sorted(gl) and len(gl) == (8 if stage == "create" else 11)
    r["F6_counts"] = {"expected": len(el), "got": len(gl)}
    ok7, trailing = False, 0
    if len(codes) == 1 and codes[0][0] == "markdown":
        got = codes[0][1].replace("\r\n", "\n")
        exp = inner
        g_lines, e_lines = got.split("\n"), exp.split("\n")
        trailing = sum(1 for a, b in zip(g_lines, e_lines) if a != b and a.rstrip(" ") == b.rstrip(" "))
        ok7 = len(g_lines) == len(e_lines) and all(a.rstrip(" ") == b.rstrip(" ") for a, b in zip(g_lines, e_lines))
        r["F7_code_sha256_exact"] = hashlib.sha256(got.encode()).hexdigest() == FENCE_SHA
    r["F7_code_block"] = ok7
    r["F7_code_blocks_found"] = len(codes)
    r["F7_trailing_space_lines"] = trailing

    def lcount(sec, kind="li"):
        return len([b for k, b in gsec.get(sec, []) if k == kind])
    want = {"Inclusion criteria": 5, "Routing instructions": 7, "Classification test": 5, "Candidate item format": 13,
            "Scope-repair revision record": 3}
    got8 = {k: lcount(k) for k in want}
    labels = lambda sec: [re.sub(r":.*$", "", norm(b)) for k, b in sec.get("Candidate item format", []) if k == "li"]
    r["F8_list_counts"] = got8 == want and labels(gsec) == labels(esec)
    r["F8_counts"] = got8
    ep = [norm(b) for k, b in e_blocks if k != "h"]
    gp = [norm(b) for k, b in blocks if k != "h"]
    r["F9_text"] = ep == gp
    if ep != gp:
        first = next((i for i, (a, b) in enumerate(zip(ep, gp)) if a != b), min(len(ep), len(gp)))
        r["F9_first_difference"] = {"block": first, "expected_blocks": len(ep), "got_blocks": len(gp)}
    titles = ["Repository prompt-use provenance helper", "QA-10 substantive, paste-ready PF10 findings summary",
              "QA-90 explicit Product Owner task selection", "Combined audit-and-plan invocations for IA and QA preparation"]
    code_h2 = [ln for ln in (codes[0][1].split("\n") if codes else []) if ln.startswith("## ")]
    r["F10_ids_and_titles"] = (len(tables) == 2
                               and [norm(row[0]) for row in tables[1][1:]] == ["1", "2", "3", "4"]
                               and [norm(row[1]) for row in tables[1][1:]] == titles
                               and all(any(t in h for h in code_h2) for t in titles))
    r["pass"] = all(r[k] for k in r if k.startswith("F") and isinstance(r[k], bool) and k != "F7_code_sha256_exact")
    return r


def insert_op(content, text, run):
    """The step-5 fallback's second write: the preserved-source block put back before `## Maintenance rule`, widened
    to the line before so that sent again it matches nothing (P-103). Refuses once a code block is on the page."""
    codes, _, _ = parse(content)
    if codes:
        return {"refused": "CODE_BLOCK_ALREADY_PRESENT"}
    lines, _ = build(text, run, "create")
    block = lines[lines.index(H3):lines.index(MAINT)]
    if D.occ(content, MAINT) != 1:
        return {"refused": "ANCHOR_NOT_ONCE"}
    p = content.index(MAINT)
    ls = content.rfind("\n", 0, p)
    start = content.rfind("\n", 0, ls) + 1 if ls > 0 else 0
    op = {"old_str": content[start:p] + MAINT, "new_str": content[start:p] + "\n".join(block) + "\n" + MAINT}
    after = content.replace(op["old_str"], op["new_str"], 1)
    return {"op": op, "reapply_refused": D.occ(after, op["old_str"]) == 0}


def plain_spots(content):
    """The step-7 old_strs still standing on the page (whitespace collapsed; a landed self-link keeps its markup)."""
    ws = lambda s: re.sub(r"\s+", " ", s)
    return [op["old_str"] for op in M2["self_links"]["step7_ops"] if D.occ(ws(content), ws(op["old_str"]))]


def stage_of(content):
    """`create` while all three step-7 old_strs stand, `final` once none does, else PARTIAL_STEP7:<n> (P-112)."""
    n = len(plain_spots(content))
    return "create" if n == len(M2["self_links"]["step7_ops"]) else "final" if n == 0 else f"PARTIAL_STEP7:{n}"


def step7_ops(content, run):
    """Step 7's operations still to send on the page as fetched, the URL filled from run.json (P-103, P-112)."""
    if not run.get("url"):
        return {"refused": "TOKEN_NOT_RECORDED", "need": ["url"]}
    left = set(plain_spots(content))
    ops = [{"old_str": op["old_str"], "new_str": op["new_str"].replace("{{CANDIDATE_CRD_LIST_URL}}", run["url"])}
           for op in M2["self_links"]["step7_ops"] if op["old_str"] in left]
    if any(D.occ(content, op["old_str"]) != 1 for op in ops):
        return {"refused": "OLD_STR_NOT_LITERALLY_ONCE"}
    return {"ops": ops}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["build", "check", "insert-op", "step7-ops"])
    ap.add_argument("--run", required=True)
    ap.add_argument("--out")
    ap.add_argument("--page")
    ap.add_argument("--hub", default="3ce4590a05eb814f8892f88ff8539308")
    ap.add_argument("--stage", choices=["create", "final", "auto"], default="create")
    ap.add_argument("--since-minutes", type=int, default=30)
    ap.add_argument("--harness-root", default=D.ROOT)
    ap.add_argument("--session", default=D.SESSION or "any")
    a = ap.parse_args()
    D.SINCE = a.since_minutes * 60
    D.ROOT = a.harness_root
    D.SESSION = None if a.session == "any" else a.session
    run = json.loads(Path(a.run).read_text(encoding="utf-8"))
    text, src = drive_text()
    if a.mode == "build":
        if not a.out:
            refuse("NEED_OUT")
        lines, _ = build(text, run, "create")
        full = "\n".join(lines) + "\n"
        i = lines.index(H3)
        j = lines.index(MAINT)
        small = "\n".join(lines[:i] + lines[j:]) + "\n"
        out = Path(a.out)
        out.mkdir(parents=True, exist_ok=True)
        (out / "page.create.md").write_text(full, encoding="utf-8")
        (out / "page.small.md").write_text(small, encoding="utf-8")
        print(json.dumps({"drive_source_file": src, "create": {"bytes": len(full.encode()), "sha256": hashlib.sha256(full.encode()).hexdigest()},
                          "small": {"bytes": len(small.encode()), "sha256": hashlib.sha256(small.encode()).hexdigest()},
                          "files": [str(out / "page.create.md"), str(out / "page.small.md")]}, indent=1))
        return
    if not a.page:
        refuse("NEED_PAGE")
    ts, content = D.latest_body(a.page)
    title, page_src = D.TITLE, D.SOURCE
    if a.mode == "insert-op":
        res = insert_op(content, text, run)
        if res.get("refused"):
            refuse(res["refused"])
        print(json.dumps({"page": a.page, "fetched": ts, "source_file": page_src, **res}, ensure_ascii=False))
        return
    if a.mode == "step7-ops":
        res = step7_ops(content, run)
        if res.get("refused"):
            refuse(res["refused"], **{k: v for k, v in res.items() if k != "refused"})
        print(json.dumps({"page": a.page, "fetched": ts, "source_file": page_src, **res}, ensure_ascii=False))
        return
    stage = a.stage
    if stage == "auto":
        stage = stage_of(content)
        if stage.startswith("PARTIAL_STEP7"):
            refuse("PARTIAL_STEP7", plain_spots=int(stage.split(":")[1]))
    _, hub = D.latest_body(a.hub)
    children = [{"id": i, "title": t.strip()} for i, t in K.CHILD.findall(hub)]
    res = check(content, title, children, a.page.replace("-", ""), text, run, stage)
    print(json.dumps({"page": a.page, "fetched": ts, "source_file": page_src, "drive_source_file": src,
                      "stage": stage, **res}, indent=1))
    raise SystemExit(0 if res["pass"] else 1)


if __name__ == "__main__":
    main()
