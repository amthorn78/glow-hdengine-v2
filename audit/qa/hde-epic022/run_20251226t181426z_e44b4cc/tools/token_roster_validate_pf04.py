#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from datetime import datetime, timezone

def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# PF04-registered tokens confirmed present (names-only) for EPIC022 roster.
PF04_REGISTERED = set([
  "TESTS_PASS_OK",
  "DOC_DELTA_PRESENT_OK",
  "EVIDENCE_INDEX_UPDATED_OK",
  "EVIDENCE_INDEX_HASH_OK",
  "EVIDENCE_INDEX_MIRROR_OK",
  "EVIDENCE_PATHS_VALIDATED_OK",
  "MACHINE_MIRROR_UPDATED_OK",
  "ENV_RAILS_POLICY_OK",
  "DETERMINISM_ENV_PINS_OK",
  "SANITY_PIPELINE_OK",
  "CLI_READER_PARITY_OK",
  "TWO_RUN_IDENTITY_OK",
  "CLI_STDOUT_LF_OK",
  "INTERNAL_VERSION_200_CTYPE_JSON_UTF8_OK",
  "INTERNAL_VERSION_HEAD_PARITY_OK",
  "INTERNAL_VERSION_CONDITIONALS_IGNORED_OK",
  "INTERNAL_VERSION_NO_ETAG_OK",
  "INTERNAL_VERSION_NO_STORE_OK",
  "RELEASE_ID_RECOMPUTE_OK",
  "RELEASE_ID_FROM_MANIFEST_OK",
])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--roster", required=True)
    ap.add_argument("--out-json", required=True)
    ap.add_argument("--out-summary-md", required=True)
    args = ap.parse_args()

    roster = [ln.strip() for ln in Path(args.roster).read_text(encoding="utf-8").splitlines() if ln.strip() and not ln.strip().startswith("#")]

    rows = []
    unregistered = []
    for t in roster:
        ok = t in PF04_REGISTERED
        rows.append({"token": t, "pf04_registered": ok})
        if not ok:
            unregistered.append(t)

    out = {
        "captured_at_utc": utc_now(),
        "source_roster": str(Path(args.roster)),
        "pf04_validation_model": "EPIC022 plan-time PF04 presence check; absent tokens treated as UNREGISTERED_ACCEPTANCE_TOKEN per PF10 §2.7",
        "results": rows,
        "unregistered_tokens": unregistered,
    }
    Path(args.out_json).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    md = Path(args.out_summary_md)
    md.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Token roster validation (PF20 roster vs PF04 registry posture)",
        "",
        f"captured_at_utc: {out['captured_at_utc']}",
        "",
        "## UNREGISTERED_ACCEPTANCE_TOKEN (blocking canon gap; do not claim in step logs)",
        "",
    ]
    if unregistered:
        lines += [f"- {t}" for t in unregistered]
    else:
        lines += ["(none)"]
    lines += ["", "## Registered (claimable if evidence satisfied)", ""]
    lines += [f"- {t}" for t in roster if t in PF04_REGISTERED]
    md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Exit code: 0 if all registered; 2 if any unregistered (TOOLING_BLOCKED)
    raise SystemExit(0 if not unregistered else 2)

if __name__ == "__main__":
    main()
