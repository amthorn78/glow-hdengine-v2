#!/usr/bin/env python3
"""PLAN proof of engine/m2.py (P-105; repair round 7). No Notion write and no page exists yet, so the readback is run
on page texts made from the build itself: the Drive file is read from this session's newest download (the same
checks as drive_check.py), m2.py builds the create and final content, and m2.check runs on
  - each content as Notion would return it verbatim (must pass);
  - a Notion-style rendering of the final content: blank lines between blocks, every numbered list renumbered 1.,
    the internal links as <mention-page> with the same text and a notion.so URL, a {color="default"} on a heading,
    table cells re-indented, and trailing spaces on code lines 3 and 10, both non-empty (must pass; the
    trailing-space lines are counted);
  - the final content with every Notion page link stored as a text-less <mention-page url=.../> (must pass, P-112);
  - seven single faults (each must fail, on the criterion named);
  - the fallback: the small create content, then m2.py's insert-op on it (the result must pass as `create`, and the
    same operation sent again must match nothing);
  - a resumed X5.1 (P-112): `stage_of` reads `create` on the create content and its Notion-style rendering, `final` on
    the final content, its Notion-style rendering and its text-less-mention form, and PARTIAL_STEP7 with one self-link landed; `step7_ops` then gives exactly the two
    operations left, which bring the page to the final content, and none on the final content; the small create
    content reads `create` but fails the check until insert-op has run.
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
                out.append(ln + "  " if n in (3, 10) and ln.strip() else ln)
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

    def bare(c):
        """every Notion page link outside the code block as a text-less mention, as a native mention is stored"""
        out, in_code = [], False
        for ln in c.split("\n"):
            if ln.startswith("```"):
                in_code = not in_code
            elif not in_code:
                ln = re.sub(r"\[([^\]]*)\]\(https://app\.notion\.com/p/([0-9a-f]{32})[^)]*\)",
                            lambda m: f'<mention-page url="https://www.notion.so/{m.group(2)}"/>', ln)
            out.append(ln)
        return "\n".join(out)

    cases = {"create verbatim": (create, "create", True, None), "final verbatim": (final, "final", True, None),
             "final, Notion-style rendering": (notionish(final), "final", True, None),
             "final, every page link a text-less mention": (bare(final), "final", True, None)}
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
    res = M.insert_op(small, text, run)                   # m2.py's own insert-op code path
    op = res["op"]
    assert D.occ(small, op["old_str"]) == 1
    after = small.replace(op["old_str"], op["new_str"], 1)
    r = chk(after, "create")
    again = M.insert_op(after, text, run)
    rows["fallback: small create then insert-op"] = {**r, "op_matches_again": D.occ(after, op["old_str"]),
                                                     "insert_op_on_the_result": again.get("refused"),
                                                     "ok": r["pass"] and D.occ(after, op["old_str"]) == 0
                                                     and again.get("refused") == "CODE_BLOCK_ALREADY_PRESENT"}
    # a second page of the same title under the Hub (a lost create response, then a stale Hub fetch): F1 fails
    two = M.check(final, M.TITLE, kids + [{"id": "0" * 31 + "2", "title": M.TITLE}], PAGE, text, run, "final")
    rows["a second child of the same title"] = {"pass": two["pass"], "F1": two["F1_title_and_parent"],
                                                "children_titled": two["F1_children_titled"],
                                                "ok": (not two["pass"]) and not two["F1_title_and_parent"]}
    # a resumed X5.1: the stage read from the page, and the step-7 operations still to send (P-112)
    s7 = M.step7_ops(create, run)["ops"]
    one = create.replace(s7[0]["old_str"], s7[0]["new_str"], 1)
    left = M.step7_ops(one, run)["ops"]
    two = one
    for op in left:
        two = two.replace(op["old_str"], op["new_str"], 1)
    rows["resume: stage read from the page"] = {
        "create": M.stage_of(create), "create_notion_style": M.stage_of(notionish(create)), "final": M.stage_of(final),
        "final_notion_style": M.stage_of(notionish(final)), "final_mentions": M.stage_of(bare(final)),
        "one_self_link_landed": M.stage_of(one), "ops_left_after_one": len(left), "ops_left_on_final": len(M.step7_ops(final, run)["ops"]),
        "ops_left_then_final_equal": two == final, "small_stage": M.stage_of(small), "small_check_passes": chk(small, "create")["pass"],
        "ok": (M.stage_of(create), M.stage_of(notionish(create)), M.stage_of(final), M.stage_of(notionish(final)),
               M.stage_of(bare(final)), M.stage_of(one)) == ("create", "create", "final", "final", "final", "PARTIAL_STEP7:2")
              and len(left) == 2 and two == final and not M.step7_ops(final, run)["ops"] and chk(two, "final")["pass"]
              and M.stage_of(small) == "create" and not chk(small, "create")["pass"]}
    print(json.dumps({"drive_source_file": src, "create_bytes": len(create.encode()), "final_bytes": len(final.encode()),
                      "small_bytes": len(small.encode()), "all_ok": all(v["ok"] for v in rows.values()), "cases": rows},
                     indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
