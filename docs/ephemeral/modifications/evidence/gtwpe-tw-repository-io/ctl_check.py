"""Pre-read and readback of a control page that the harness saves to a file (X4.4, X4.6).

  python3 ctl_check.py pre  <save> <state.json> <anchor-heading>
  python3 ctl_check.py post <save> <state.json> <new-heading> <renamed-heading> [--has TEXT]... [--row CODE=ID@VERSION]...

The save is the harness's file for one notion-fetch of a control page (Alpha 1 or the Glow
Operations Hub), never a prompt body. `pre` prints the edit time and flags, requires the anchor
heading exactly once, and writes the page's heading list to state.json. `post` requires: the new
heading once, the renamed heading once and directly after it; the anchor heading gone; the heading
list equal to the pre-read's with the anchor replaced by those two; and, in the text from the new
heading to the renamed one, each --has text and, for each --row, one line starting "- `CODE` —"
that links app.notion.com/p/ID and ends "; VERSION.". It prints one line per check and exits 0 only if all pass.
"""
import json, re, sys


def load(path):
    raw = open(path, encoding="utf-8").read()
    d = json.loads(raw)
    if isinstance(d, list):
        d = json.loads(d[0]["text"])
    body = d["text"].split("<content>\n", 1)[1].rsplit("\n</content>", 1)[0]
    return d, body


def headings(body):
    return [l for l in body.split("\n") if re.match(r"^#{1,4} ", l)]


def main(argv):
    mode, save, state = argv[0], argv[1], argv[2]
    d, body = load(save)
    heads = headings(body)
    print("edited", d.get("page_last_edited_at"), "truncated", d.get("truncated"), "unknown", d.get("unknown_block_count"))
    ok = not d.get("truncated") and not d.get("unknown_block_count")
    if mode == "pre":
        anchor = argv[3]
        n = heads.count(anchor)
        print("anchor", n, "headings", len(heads))
        ok &= n == 1
        json.dump({"anchor": anchor, "headings": heads, "edited": d.get("page_last_edited_at")}, open(state, "w", encoding="utf-8"), ensure_ascii=False)
    else:
        new, renamed = argv[3], argv[4]
        has, rows, i = [], [], 5
        while i < len(argv):
            (has if argv[i] == "--has" else rows).append(argv[i + 1]); i += 2
        pre = json.load(open(state, encoding="utf-8"))
        k = pre["headings"].index(pre["anchor"])
        want = pre["headings"][:k] + [new, renamed] + pre["headings"][k + 1:]
        checks = [("new heading once", heads.count(new) == 1),
                  ("renamed heading once", heads.count(renamed) == 1),
                  ("renamed directly after new", heads.count(new) == 1 and heads.index(new) + 1 < len(heads) and heads[heads.index(new) + 1] == renamed),
                  ("anchor gone", pre["anchor"] not in heads),
                  ("heading list = pre-read's, anchor replaced (%d)" % len(want), heads == want)]
        sec = ""
        if new in body and ("\n" + renamed) in body:
            a = body.index(new); sec = body[a: body.index("\n" + renamed, a)]
        for t in has:
            checks.append(("has %r" % t, t in sec))
        for r in rows:
            code, rest = r.split("=", 1)
            pid, ver = rest.split("@", 1)
            lines = [l for l in sec.split("\n") if l.startswith("- `%s` —" % code)]
            checks.append(("row %s links %s at %s" % (code, pid, ver),
                           len(lines) == 1 and ("app.notion.com/p/" + pid) in lines[0] and lines[0].endswith("; %s." % ver)))
        for name, res in checks:
            print("PASS" if res else "FAIL", name)
            ok &= res
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main(sys.argv[1:])
