#!/usr/bin/env python3
"""Read-only Drive check for MODIFICATION-20260923-closeout-residuals PART-06 (P-95, P-102; spec §7.4.2 steps 1-3,
X4.6 and X5.1). The Drive file `Candidate-CRD-Items-List.md` is the Candidate CRD list, not a prompt body. It is read
from the newest `download_file_content` result for its file id in this session's harness files (the same rule and
window as dryrun.latest_body: the running session only, the last --since-minutes), decoded in memory and never
written, printed or copied. So nothing is transcribed by hand.

  drive_check.py [--hub HUB_PAGE_ID] [--since-minutes N] [--harness-root H] [--session S]

Checks, against notion/M2.json:
  size          the decoded bytes are M2.file.bytes (31 923 B) and hash to M2.file.sha256 (2d7ff093...);
  fence         the one fenced block (its opening line starts ```markdown, its closing line is ```): the lines
                between them, each with its LF, hash to the sha256 in M2.file.fence (7108e84a...);
  old_outside   each M2 rewrite's `old` occurs exactly once outside the fence (M2-R3 also once inside, not rewritten);
  hub           with --hub: the Hub's newest fetch lists no child page titled exactly "Candidate CRD Items List"
                (the collision check; a child of that title is reported by id, for X5.1's resume rule).
Prints counts, booleans and the harness file read (D22 condition 5); exits 0 when every check passes, else 1.
"""
import argparse
import base64
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import dryrun as D  # noqa: E402
import ctrl as K  # noqa: E402

M2 = json.loads((HERE.parent / "notion/M2.json").read_text(encoding="utf-8"))
FILE_ID = M2["file"]["id"]
TITLE = "Candidate CRD Items List"


def strings(obj):
    """Every string in a transcript entry: a tool result's content may be a plain string, not a {"text": ...} part."""
    if isinstance(obj, dict):
        for v in obj.values():
            yield from strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from strings(v)
    elif isinstance(obj, str):
        yield obj


def newest_download():
    """(captured, source_file, bytes) of the newest download_file_content result for FILE_ID, or None."""
    import time
    cutoff_iso = datetime.fromtimestamp(time.time() - D.SINCE, timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    best = None
    for f in D.candidates():
        try:
            raw = open(f, encoding="utf-8").read()
        except Exception:
            continue
        if FILE_ID not in raw:
            continue
        for line in (raw.splitlines() if f.endswith(".jsonl") else [raw]):
            try:
                obj = json.loads(line)
            except Exception:
                continue
            entry_ts = obj.get("timestamp") if isinstance(obj, dict) else None
            if f.endswith(".jsonl") and not (isinstance(entry_ts, str) and entry_ts >= cutoff_iso):
                continue
            for t in [obj] if isinstance(obj, dict) and "content" in obj and "id" in obj else strings(obj):
                if not isinstance(t, dict) and FILE_ID not in t:
                    continue
                try:
                    j = t if isinstance(t, dict) else json.loads(t)
                except Exception:
                    continue
                if not isinstance(j, dict) or j.get("id") != FILE_ID or not isinstance(j.get("content"), str):
                    continue
                try:
                    data = base64.b64decode(j["content"], validate=True)
                except Exception:
                    continue
                captured = entry_ts if f.endswith(".jsonl") else datetime.fromtimestamp(
                    os.path.getmtime(f), timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
                if best is None or (captured or "") >= best[0]:
                    best = (captured or "", f, data)
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hub")
    ap.add_argument("--since-minutes", type=int, default=30)
    ap.add_argument("--harness-root", default=D.ROOT)
    ap.add_argument("--session", default=D.SESSION or "any",
                    help="the session whose harness files are read (default: the running session, P-101); any: all")
    a = ap.parse_args()
    D.SINCE = a.since_minutes * 60
    D.ROOT = a.harness_root
    D.SESSION = None if a.session == "any" else a.session
    got = newest_download()
    if got is None:
        print(json.dumps({"file_id": FILE_ID, "error": "NO_DOWNLOAD_FOUND", "pass": False}))
        raise SystemExit(1)
    captured, src, data = got
    out = {"file_id": FILE_ID, "captured": captured, "source_file": src, "bytes": len(data),
           "size_ok": len(data) == M2["file"]["bytes"],
           "sha256_ok": hashlib.sha256(data).hexdigest() == M2["file"]["sha256"]}
    text = data.decode("utf-8")
    lines = text.split("\n")
    opens = [i for i, ln in enumerate(lines) if ln.startswith("```markdown")]
    closes = [i for i, ln in enumerate(lines) if ln == "```"]
    fence_ok, outside, inside = False, text, ""
    if len(opens) == 1 and len([c for c in closes if c > opens[0]]) >= 1:
        o = opens[0]
        c = min(x for x in closes if x > o)
        inside = "".join(ln + "\n" for ln in lines[o + 1:c])
        outside = "\n".join(lines[:o + 1]) + "\n" + "\n".join(lines[c:])
        want = re.search(r"sha256 ([0-9a-f]{64})", M2["file"]["fence"]).group(1)
        fence_ok = hashlib.sha256(inside.encode("utf-8")).hexdigest() == want
        out["fence_lines"] = [o + 1, c + 1]
        out["fence_bytes"] = len(inside.encode("utf-8"))
    out["fence_sha256_ok"] = fence_ok
    out["old_outside"] = {r["id"]: outside.count(r["old"]) for r in M2["rewrites"]}
    out["old_inside"] = {r["id"]: inside.count(r["old"]) for r in M2["rewrites"] if inside.count(r["old"])}
    ok = out["size_ok"] and out["sha256_ok"] and fence_ok and all(v == 1 for v in out["old_outside"].values())
    if a.hub:
        ts, content = D.latest_body(a.hub)
        same = [{"id": i, "title": t.strip()} for i, t in K.CHILD.findall(content) if t.strip() == TITLE]
        out["hub"] = {"page": a.hub, "fetched": ts, "source_file": D.SOURCE, "children_titled": same}
        ok = ok and not same
    out["pass"] = bool(ok)
    print(json.dumps(out, indent=1))
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
