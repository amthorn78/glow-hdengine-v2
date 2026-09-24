#!/usr/bin/env python3
"""PLAN proof of engine/m2.py (P-105; repair round 7). No Notion write and no page exists yet, so the readback is run
on page texts made from the build itself: the Drive file is read from this session's newest download (the same
checks as drive_check.py), m2.py builds the create and final content, and m2.check runs on
  - each content as Notion would return it verbatim (must pass);
  - a Notion-style rendering of the final content: blank lines between blocks, every numbered list renumbered 1.,
    the internal links as <mention-page> with the same text and a notion.so URL, a {color="default"} on a heading,
    table cells re-indented, and trailing spaces on non-empty code lines 3 and 9 (must pass; the trailing-space lines
    are counted);
  - seven single faults (each must fail, on the criterion named);
  - the fallback: the small create content, then m2.py's insert-op on it (the result must pass as `create`, and the
    same operation sent again must match nothing).
Prints booleans and counts only.

  m2_proof.py <run.json> [--since-minutes N]
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
EV = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(EV / "engine"))
import dryrun as D  # noqa: E402
import m2 as M  # noqa: E402

PAGE = "0" * 31 + "1"


def flip(c, i):
    """c with the character at i replaced by another one."""
    return c[:i] + ("X" if c[i] != "X" else "Y") + c[i + 1:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run")
    ap.add_argument("--since-minutes", type=int, default=120)
    a = ap.parse_args()
    D.SINCE = a.since_minutes * 60
    run = json.loads(Path(a.run).read_text(encoding="utf-8"))
    text, src = M.drive_text()
    kids = [{"id": PAGE, "title": M.TITLE}]
    create = "\n".join(M.build(text, run, "create")[0]) + "\n"
    final = "\n".join(M.build(text, run, "final")[0]) + "\n"

    def chk(content, stage, title=M.TITLE):
        r = M.check(content, title, kids, PAGE, text, run, stage)
        return {"pass": r["pass"], "failed": sorted(k for k, v in r.items() if k.startswith("F") and v is False),
                "trailing": r["F7_trailing_space_lines"], "links": r["F6_counts"]["got"]}

    def notionish(c):
        out, in_code, n = [], False, 0
        for ln in c.split("\n"):
            if ln.startswith("```"):
                in_code = not in_code
                out.append(ln)
                continue
            if in_code:
                n += 1
                out.append(ln + "  " if n in (3, 9) and ln.strip() else ln)
                continue
            ln = re.sub(r"^\d+\. ", "1. ", ln)
            ln = re.sub(r"\[([^\]]*)\]\(https://app\.notion\.com/p/([0-9a-f]{32})[^)]*\)",
                        lambda m: f'<mention-page url="https://www.notion.so/{m.group(2)}">{m.group(1)}</mention-page>', ln)
            if ln == "## Document purpose":
                ln += ' {color="default"}'
            ln = ln.replace("\t\t<td>", "\t\t\t<td>")
            out.append(ln)
            if ln.strip() and not ln.startswith(("\t", "<")):
                out.append("")
        return "\n".join(out)

    cases = {"create verbatim": (create, "create", True, None), "final verbatim": (final, "final", True, None),
             "final, Notion-style rendering": (notionish(final), "final", True, None)}
    faults = {
        "a moved-items row dropped": (lambda c: re.sub(r"\t<tr>\n\t\t<td>3</td>(?:\n\t\t<td>.*</td>)+\n\t</tr>\n", "", c, 1),
                                      "F4_moved_table"),
        "one code byte changed": (lambda c: flip(c, c.index("```markdown\n") + len("```markdown\n") + 2), "F7_code_block"),
        "one link removed": (lambda c: c.replace("[Glow Operations Hub](https://app.notion.com/p/3ce4590a05eb814f8892f88ff8539308)",
                                                 "Glow Operations Hub", 1), "F6_links"),
        "a heading changed": (lambda c: c.replace("## Exclusion criteria", "## Exclusions", 1), "F2_headings"),
        "a paragraph word changed": (lambda c: c.replace("Future agents must not", "Future agents need not", 1), "F9_text"),
        "a routing item removed": (lambda c: re.sub(r"\n5\. Keep PF09-bound[^\n]*", "", c, 1), "F8_list_counts"),
        "the title wrong": (None, "F1_title_and_parent"),
    }
    rows = {}
    for name, (c, stage, want, _) in cases.items():
        r = chk(c, stage)
        rows[name] = {**r, "ok": r["pass"] == want}
    for name, (f, crit) in faults.items():
        if f is None:
            r = chk(final, "final", title="Candidate CRD Items")
        else:
            c = f(final)
            assert c != final, name
            r = chk(c, "final")
        rows[name] = {**r, "expected_failure": crit, "ok": (not r["pass"]) and crit in r["failed"]}
    # the fallback: the small create, then insert-op on the page as it would be fetched
    lines = M.build(text, run, "create")[0]
    small = "\n".join(lines[:lines.index(M.H3)] + lines[lines.index(M.MAINT):]) + "\n"
    p = small.index(M.MAINT)
    ls = small.rfind("\n", 0, p)
    start = small.rfind("\n", 0, ls) + 1
    block = lines[lines.index(M.H3):lines.index(M.MAINT)]
    op = {"old_str": small[start:p] + M.MAINT, "new_str": small[start:p] + "\n".join(block) + "\n" + M.MAINT}
    assert D.occ(small, op["old_str"]) == 1
    after = small.replace(op["old_str"], op["new_str"], 1)
    r = chk(after, "create")
    rows["fallback: small create then insert-op"] = {**r, "op_matches_again": D.occ(after, op["old_str"]),
                                                     "ok": r["pass"] and D.occ(after, op["old_str"]) == 0}
    print(json.dumps({"drive_source_file": src, "create_bytes": len(create.encode()), "final_bytes": len(final.encode()),
                      "small_bytes": len(small.encode()), "all_ok": all(v["ok"] for v in rows.values()), "cases": rows},
                     indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
