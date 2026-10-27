#!/usr/bin/env python3
"""The shared fetch normalizer for MODIFICATION-20261027-gcfpe-backlog-open-items (C-15, repair R1).

Notion's fetch renders inline code as `<code>x</code>`, bold as `<b>x</b>`, italics as `<i>x</i>` and a plain-text
underscore as `\\_`. Every guard, registry assertion and profile body check is written for the Markdown form, so it
runs on normalize(read), which maps exactly these four forms and nothing else (C-15):

  <code>x</code>  ->  `x`
  <b>x</b>        ->  **x**
  <i>x</i>        ->  *x*
  \\_              ->  _        (an underscore escaped by one backslash; an escaped backslash `\\\\` is left alone)

Mention elements (`<mention ...>...</mention>`, `<mention ... />`) are copied unchanged, tags and inner text alike.
Nothing else is rewritten: no other tag, entity or escape. normalize is idempotent (normalize(normalize(t)) ==
normalize(t)), and it runs in memory on the read in hand (D22): it is never given a file to write, and no operation's
anchor is normalized, because update_content matches the fetch's own form.

  PYTHONDONTWRITEBYTECODE=1 python3 normalize_fetch.py selftest   synthetic text only; every mapping, idempotence,
                                                                 mentions unchanged, and injected misses that the
                                                                 self-test must catch
"""
from __future__ import annotations

import json
import re
import sys

sys.dont_write_bytecode = True

MENTION = re.compile(r"<mention\b[^>]*/>|<mention\b[^>]*>.*?</mention>", re.S)
CODE = re.compile(r"<code>(.*?)</code>")
BOLD = re.compile(r"<b>(.*?)</b>")
ITAL = re.compile(r"<i>(.*?)</i>")
# an underscore escaped by one backslash: the backslash run before it is odd (`\_`, `\\\_`), so `\\_` (an escaped
# backslash, then a plain underscore) is not touched and a second pass changes nothing
ESC_US = re.compile(r"(?<!\\)((?:\\\\)*)\\_")
MAPPINGS = ("code", "bold", "italic", "underscore")


def _plain(seg: str, skip: frozenset = frozenset()) -> str:
    if "code" not in skip:
        seg = CODE.sub(lambda m: "`" + m.group(1) + "`", seg)
    if "bold" not in skip:
        seg = BOLD.sub(lambda m: "**" + m.group(1) + "**", seg)
    if "italic" not in skip:
        seg = ITAL.sub(lambda m: "*" + m.group(1) + "*", seg)
    if "underscore" not in skip:
        seg = ESC_US.sub(lambda m: m.group(1) + "_", seg)
    return seg


def normalize(text: str, _skip: frozenset = frozenset()) -> str:
    """The Markdown form of a fetch read (C-15). `_skip` exists only for the self-test's injected misses."""
    out, pos = [], 0
    for m in MENTION.finditer(text):
        out.append(_plain(text[pos:m.start()], _skip))
        out.append(m.group(0))
        pos = m.end()
    out.append(_plain(text[pos:], _skip))
    return "".join(out)


def selftest() -> dict:
    A = "a" * 32
    mention_self = f'<mention url="https://app.notion.com/p/{A}" />'
    mention_titled = f'<mention url="https://app.notion.com/p/{A}">QA\\_10 <b>x</b></mention>'
    cases = {
        "code": ("Write <code>QA_REPORT</code> now.", "Write `QA_REPORT` now."),
        "bold": ("A <b>Handoff:</b> line.", "A **Handoff:** line."),
        "italic": ("An <i>exact</i> word.", "An *exact* word."),
        "underscore": ("session\\_disposition and role\\_session\\_ref", "session_disposition and role_session_ref"),
        "nested_bold_code": ("<b><code>PASS</code></b> |", "**`PASS`** |"),
        "two_spans_one_line": ("<code>A</code> and <code>B</code>", "`A` and `B`"),
        "escaped_backslash_kept": ("a\\\\_b", "a\\\\_b"),
        "escaped_backslash_then_escaped_underscore": ("a\\\\\\_b", "a\\\\_b"),
        "mention_self_closing_unchanged": (f"See {mention_self} now.", f"See {mention_self} now."),
        "mention_inner_text_unchanged": (f"Go to {mention_titled}.", f"Go to {mention_titled}."),
        "around_mention_still_mapped": (f"<b>Go</b> {mention_self} <code>x\\_y</code>", f"**Go** {mention_self} `x_y`"),
        "other_tags_unchanged": ("<page url=\"u\">T</page> <br> <em>e</em> \\* \\[", "<page url=\"u\">T</page> <br> <em>e</em> \\* \\["),
        "unpaired_tag_unchanged": ("an open <code> with no close", "an open <code> with no close"),
        "code_does_not_cross_lines": ("<code>a\nb</code>", "<code>a\nb</code>"),
        "plain_text_unchanged": ("Plain line. Second sentence!", "Plain line. Second sentence!"),
    }
    rows = {}
    for name, (src, want) in cases.items():
        got = normalize(src)
        rows[name] = {"maps": got == want, "idempotent": normalize(got) == got}
    # injected misses: a normalizer that drops one mapping must fail that mapping's case, so the cases above are what
    # prove each mapping is applied
    injected = {}
    for skip, case in (("code", "code"), ("bold", "bold"), ("italic", "italic"), ("underscore", "underscore")):
        src, want = cases[case]
        injected[f"drop_{skip}_caught"] = normalize(src, frozenset({skip})) != want
    # a normalizer that also rewrote mentions would change the mention case
    injected["mention_rewrite_caught"] = _plain(cases["mention_inner_text_unchanged"][0]) != cases["mention_inner_text_unchanged"][1]
    # a one-pass `\_` -> `_` replace is not idempotent on an escaped backslash before an underscore
    naive = lambda s: s.replace("\\_", "_")
    injected["naive_underscore_not_idempotent_caught"] = naive(naive("a\\\\\\_b")) != naive("a\\\\\\_b")
    ok = all(all(r.values()) for r in rows.values()) and all(injected.values())
    return {"mode": "selftest", "mappings": list(MAPPINGS), "cases": len(rows),
            "cases_failing": [k for k, r in rows.items() if not all(r.values())],
            "injected": injected, "ok": ok}


def main() -> int:
    if sys.argv[1:] != ["selftest"]:
        print(json.dumps({"error": "usage: normalize_fetch.py selftest (import normalize() to use it)"}))
        return 2
    res = selftest()
    print(json.dumps(res, indent=1))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
