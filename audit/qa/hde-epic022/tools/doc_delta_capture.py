#!/usr/bin/env python3
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from pathlib import Path

def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

BASE_DELTAS = [
    {
        "kind": "CANON GAP",
        "title": "EPIC022 acceptance tokens not present in PF04 token registry",
        "detail": "PF20 roster includes many EPIC022-specific tokens that are not present in PF04 v1.7. Per PF10 §2.7, classify these as UNREGISTERED_ACCEPTANCE_TOKEN; do not claim them; route registry update to PF04 or update PF20 to reference registered tokens.",
        "intended_fix_location": "PF04 token registry and/or PF20 EPIC022 acceptance roster",
        "resolution_status": "OPEN",
    },
    {
        "kind": "CANON CONFLICT",
        "title": "internal_version conditional header artifact filenames differ across canon homes",
        "detail": "PF12 Evidence Catalog uses headers_cond_if_* naming while PF14/PF20 use cond_if_*_headers naming. This run produces both variants and records a reconciliation need.",
        "intended_fix_location": "PF12 vs PF14/PF20 reconciliation",
        "resolution_status": "OPEN",
    },
    {
        "kind": "CANON DRAIN",
        "title": "release_id canonical path is artifacts/math/release_id.txt",
        "detail": "PF10 §2.8 establishes artifacts/math/release_id.txt as canonical. Any references to legacy paths must be drained.",
        "intended_fix_location": "PF12/PF20/PF14 references (if any legacy remains)",
        "resolution_status": "ACKNOWLEDGED",
    },
]

def render(deltas: list[dict]) -> str:
    lines = []
    lines.append(f"# Doc Delta Capture — hde-epic022")
    lines.append(f"generated_at_utc: {utc_now()}")
    lines.append("")
    if not deltas:
        lines.append("no deltas")
        lines.append("")
        return "\n".join(lines)

    lines.append("## Deltas")
    for i, d in enumerate(deltas, 1):
        lines.append(f"{i}. **{d['kind']}** — {d['title']}")
        lines.append(f"   - Detail: {d['detail']}")
        lines.append(f"   - Intended PF fix location: {d['intended_fix_location']}")
        lines.append(f"   - Resolution status: {d['resolution_status']}")
        lines.append("")
    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    txt = render(BASE_DELTAS)
    out.write_text(txt, encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
