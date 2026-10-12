#!/usr/bin/env python3
"""X19: structure of the 57 archive-set pages, read from this session's fetch records (D22: metadata only).

  x19_pages.py inspect  --fetched-after T            each page's parent, title, revision and child pages/databases
  x19_pages.py archived --fetched-after T            the archive's child pages include all 57; any of the 57 re-read
                                                     after T sits under the archive with the same child count

Only ids, titles, revisions and child-block urls are printed; no body text is read beyond those tags.
"""
import argparse, glob, json, os, re, sys
from datetime import datetime, timezone
from pathlib import Path
sys.dont_write_bytecode = True
E = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(E / "plan"))
import body_check as B
import control_check as C

ARCHIVE = "3c94590a05eb811cb145cd010e3b3fcf"
HEX = re.compile(r"[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}")
HEAD = re.compile(r'Here is the result of "fetch" for the Page with URL \S*?([0-9a-f]{32}|[0-9a-f-]{36})\S* as of (\d{4}-\d\d-\d\dT[0-9:.]+Z)')


def norm(s):
    return s.replace("-", "")


def fetches(fetched_after):
    """Every captured page fetch after the cutoff: {page_id: (captured, as_of, full_text)}, latest kept."""
    root, session = os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"]
    cutoff_iso = fetched_after
    cutoff = datetime.strptime(fetched_after, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc).timestamp()
    base = os.path.join(root, "*", session)
    files = glob.glob(base + ".jsonl") + glob.glob(base + "/tool-results/*") \
        + glob.glob(base + "/subagents/**/*.jsonl", recursive=True) + glob.glob(base + "/subagents/**/tool-results/*", recursive=True)
    out = {}
    for f in files:
        if os.path.getmtime(f) < cutoff:
            continue
        if f.endswith(".jsonl"):
            entries = B._recent_lines(f, cutoff_iso)
        else:
            try:
                entries = [json.loads(open(f, encoding="utf-8").read())]
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
                m = HEAD.match(inner)
                if not m:
                    continue
                captured = ts if f.endswith(".jsonl") else datetime.fromtimestamp(os.path.getmtime(f), timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
                if not captured or captured < cutoff_iso:
                    continue
                pid = norm(m.group(1))
                if pid not in out or captured > out[pid][0]:
                    out[pid] = (captured, m.group(2), inner)
    return out


def structure(text):
    anc = re.search(r"<ancestor-path>\n<parent-(page|database|data-source)[^>]*url=\"([^\"]+)\"[^>]*title=\"([^\"]*)\"", text)
    title = re.search(r"<properties>\n(\{.*?\})\n</properties>", text, re.S)
    content = re.search(r"<content>\n?(.*)</content>", text, re.S)
    body = content.group(1) if content else ""
    children = [{"kind": k, "id": norm(HEX.search(u).group(0)), "title": t.strip()[:120]}
                for k, u, t in re.findall(r"<(page|database)\s+url=\"([^\"]+)\"[^>]*>(.*?)</\1>", body)]
    try:
        t = json.loads(title.group(1)).get("title") if title else None
    except ValueError:
        t = None
    return {"parent_kind": anc.group(1) if anc else None, "parent": norm(HEX.search(anc.group(2)).group(0)) if anc else None,
            "parent_title": anc.group(3) if anc else None, "title": t, "children": children}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["inspect", "archived"])
    ap.add_argument("--fetched-after", required=True)
    a = ap.parse_args()
    archive_set = C.archive_set(str(E / "execute/candidate-graph-parts"))
    # control_check.py labels the 091426.1 catalog in short form; its page title carries the release too
    archive_set["3db4590a05eb81738ef1d846e3c0df8c"] = "Glow HDE Complete Prompt Set — GCFPE-20260914.1 — 091426.1"
    got = fetches(a.fetched_after)
    if a.mode == "inspect":
        rows, missing = [], []
        for pid, expected_title in archive_set.items():
            if pid not in got:
                missing.append(pid)
                continue
            s = structure(got[pid][2])
            rows.append({"id": pid, "as_of": got[pid][1], "title_matches": s["title"] == expected_title, **s,
                         "children_outside_archive_set": [c for c in s["children"] if c["id"] not in archive_set]})
        parents = {}
        for r in rows:
            parents.setdefault(f"{r['parent']} {r['parent_title']}", []).append(r["id"])
        res = {"mode": "inspect", "fetched_after": a.fetched_after, "archive_set": len(archive_set), "read": len(rows), "missing": missing,
               "titles_match": sum(r["title_matches"] for r in rows), "pages_with_children": [{"id": r["id"], "title": r["title"], "children": r["children"]} for r in rows if r["children"]],
               "children_outside_archive_set": [{"id": r["id"], "title": r["title"], "children": r["children_outside_archive_set"]} for r in rows if r["children_outside_archive_set"]],
               "already_under_archive": [r["id"] for r in rows if r["parent"] == ARCHIVE],
               "parents": {k: len(v) for k, v in parents.items()}, "rows": rows}
        res["ok"] = not missing and res["titles_match"] == len(archive_set) and not res["children_outside_archive_set"]
        print(json.dumps(res, indent=1))
        return 0 if res["ok"] else 1
    if ARCHIVE not in got:
        print(json.dumps({"mode": "archived", "ok": False, "error": "ARCHIVE_NOT_READ"}))
        return 1
    arch = structure(got[ARCHIVE][2])
    under = {c["id"] for c in arch["children"]}
    absent = sorted(pid for pid in archive_set if pid not in under)
    reread = {pid: structure(got[pid][2])["parent"] for pid in archive_set if pid in got}
    wrong_parent = sorted(pid for pid, p in reread.items() if p != ARCHIVE)
    res = {"mode": "archived", "fetched_after": a.fetched_after, "archive": ARCHIVE, "archive_as_of": got[ARCHIVE][1],
           "archive_children": len(under), "archive_set": len(archive_set), "present_under_archive": len(archive_set) - len(absent),
           "absent": absent, "pages_reread": len(reread), "reread_parent_not_archive": wrong_parent}
    res["ok"] = not absent and not wrong_parent
    print(json.dumps(res, indent=1))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
