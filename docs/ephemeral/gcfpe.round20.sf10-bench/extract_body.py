#!/usr/bin/env python3
"""Extract one prompt body from a persisted Notion fetch result, strip-both convention.

    extract_body.py <persisted-notion-fetch-result.json> <out.md>

This is the extractor actually used to build the 55-body corpus that `bench.py` and the
repair report's regression runs consume.  It is committed because the registry's
`corroboration_not_reproducible_here` key requires the extraction command alongside the
per-body digests and byte counts before a body-corpus claim is evidence rather than
corroboration -- and an earlier version of the run record gave the digests and counts while
naming the corpus only as `<55-body corpus>`, which is a placeholder, not a command.

The convention is **strip-both**, which is not a formatting preference but the thing the
recorded digests depend on: the body is the text between the first `<content>` and the last
`</content>`, with exactly one leading and one trailing newline removed if present.  The
registry records that the three untouched control prompts reproduce their digests only under
strip-both, so any other variant produces different bytes and a different SHA-256.

What this does NOT make reproducible: the persisted fetch results are per-session artifacts
of a Notion read, and prompt bodies are authored in Notion in place and never mirrored into
this repository.  So this script plus the recorded digests let a holder of the bodies confirm
they have the same bytes; they do not let a clean checkout obtain them.
"""
import hashlib
import json
import pathlib
import sys


def extract(raw_text: str) -> bytes:
    obj = json.loads(raw_text)
    # Persisted tool-result form is [{"type": "text", "text": "<json string>"}].
    if isinstance(obj, list):
        obj = json.loads(obj[0]["text"])
    text = obj["text"]
    open_at = text.find("<content>")
    close_at = text.rfind("</content>")
    if open_at == -1 or close_at == -1 or close_at < open_at:
        raise SystemExit("NO_CONTENT_MARKERS")
    start = open_at + len("<content>")
    if text[start:start + 1] == "\n":
        start += 1
    end = close_at
    if text[end - 1:end] == "\n":
        end -= 1
    return text[start:end].encode("utf-8")


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit(__doc__.splitlines()[2].strip())
    body = extract(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    pathlib.Path(sys.argv[2]).write_bytes(body)
    print(f"OK bytes={len(body)} sha256={hashlib.sha256(body).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
