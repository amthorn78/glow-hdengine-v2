#!/usr/bin/env python3
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Dict, List

OK_TOKEN_RE = re.compile(r"\b([A-Z][A-Z0-9_]*_OK)\b")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_ok_tokens(text: str) -> List[str]:
    return sorted(set(OK_TOKEN_RE.findall(text)))


def slice_epic_block(pf20_text: str, epic_id: str) -> str:
    needle = f"**Epic ID:** {epic_id}"
    start = pf20_text.find(needle)
    if start == -1:
        raise ValueError(f"EPIC_ID_NOT_FOUND: {epic_id}")
    nxt = pf20_text.find("**Epic ID:** HDE-EPIC", start + len(needle))
    end = nxt if nxt != -1 else len(pf20_text)
    return pf20_text[start:end]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--epic", required=True)
    ap.add_argument("--pf04", required=True)
    ap.add_argument("--pf20", required=True)
    args = ap.parse_args()

    epic_id = args.epic.strip()
    pf04 = Path(args.pf04)
    pf20 = Path(args.pf20)

    if not pf04.exists():
        print(json.dumps({"error": "PF04_MISSING", "path": str(pf04)}, sort_keys=True))
        return 2
    if not pf20.exists():
        print(json.dumps({"error": "PF20_MISSING", "path": str(pf20)}, sort_keys=True))
        return 2

    pf04_text = read_text(pf04)
    pf20_text = read_text(pf20)

    try:
        epic_block = slice_epic_block(pf20_text, epic_id)
    except ValueError as e:
        print(json.dumps({"error": str(e)}, sort_keys=True))
        return 3

    tokens_epic = extract_ok_tokens(epic_block)
    tokens_pf04 = set(extract_ok_tokens(pf04_text))

    out: Dict[str, object] = {
        "epic_id": epic_id,
        "pf04_sha256": sha256_file(pf04),
        "pf20_sha256": sha256_file(pf20),
        "epic_tokens_ok_count": len(tokens_epic),
        "epic_tokens_ok": tokens_epic,
        "pf04_tokens_ok_count": len(tokens_pf04),
    }

    if len(tokens_epic) == 0:
        out["error"] = "NO_OK_TOKENS_FOUND_IN_EPIC_BLOCK"
        print(json.dumps(out, sort_keys=True))
        return 10

    missing = sorted([t for t in tokens_epic if t not in tokens_pf04])
    out["missing_in_pf04"] = missing
    out["missing_in_pf04_count"] = len(missing)

    print(json.dumps(out, sort_keys=True))
    return 0 if len(missing) == 0 else 10


if __name__ == "__main__":
    raise SystemExit(main())
