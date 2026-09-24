#!/usr/bin/env python3
"""X4.4 (P-100): fill the PLAN-time D24 brief draft into this round's brief, mechanically.

  fill_brief.py <EX/packages.json> [--prior-file EV/skills/REVIEWER-PROMPT-prior.md] [--write]

Run from the repository root, on the branch, after X4.3's commit (which carries EX/packages.json). Prints the brief;
with --write (X4.4) it writes it to docs/ephemeral/modifications/evidence/closeout-residuals/REVIEWER-PROMPT-cr<K>.md
instead, refusing to overwrite, and prints {"k", "brief", "reviewers": [{"id", "record"}]}. X4.4 commits and pushes
the brief before either reviewer starts. Fills the draft's six tokens (EV/skills/REVIEWER-PROMPT-cr.draft.md):
  {{K}}         1 + the number of REVIEWER-PROMPT-cr*.md files under the closeout-residuals evidence directory and
                its attempt-*/ directories;
  {{ARCHIVES}}  one line per package from EX/packages.json;
  {{OUT_DIR}}   EX/packages.json's out_dir;
  {{HEAD}}      git rev-parse HEAD (X4.3's commit; the brief's own commit comes after);
  {{PRIOR}} and {{REREVIEW}}  the variant the repository selects: first (no earlier brief), re-cut (the newest
                earlier brief is in the closeout-residuals directory itself, so it belongs to this attempt), or
                plan change (the newest earlier brief is under attempt-*/: the text comes from --prior-file, which
                the PLAN session writes, with a '## PRIOR' and a '## REREVIEW' section).
Refuses (exit 1, nothing printed) when EX/packages.json does not hold the seven packages with the freeze lines of
EV/skills/expected_after_patch.txt, when a plan-change round has no --prior-file, when a re-cut round follows a round
whose verdict file reads SKILL_REPAIR_REQUIRED first (REPAIR_VERDICT_PENDING: that is a stop, P-84 revised), or when
any {{ remains.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

EV = Path("docs/ephemeral/modifications/evidence/closeout-residuals/plan")
DIR = Path("docs/ephemeral/modifications/evidence/closeout-residuals")


def refuse(why, **kw):
    print(json.dumps({"refused": why, **kw}), file=sys.stderr)
    raise SystemExit(1)


def quoted(draft, label):
    """The '> ' lines after the paragraph that starts with `label`."""
    m = re.search(re.escape(label) + r"[^\n]*(?:\n(?!> )[^\n]*)*\n((?:> [^\n]*\n)+)", draft)
    if not m:
        refuse("DRAFT_VARIANT_NOT_FOUND", label=label)
    return "\n".join(line[2:] for line in m.group(1).splitlines())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("packages")
    ap.add_argument("--prior-file")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    draft = (EV / "skills/REVIEWER-PROMPT-cr.draft.md").read_text(encoding="utf-8")
    pk = json.loads(Path(a.packages).read_text(encoding="utf-8"))
    expected = (EV / "skills/expected_after_patch.txt").read_text(encoding="utf-8").split("\n")
    got = [f"{r['skill']} {r['freeze']}" for r in pk["archives"]]
    if got != [x for x in expected if x]:
        refuse("FREEZE_LINES_DIFFER", got=got)
    briefs = sorted(list(DIR.glob("REVIEWER-PROMPT-cr*.md")) + list(DIR.glob("attempt-*/REVIEWER-PROMPT-cr*.md")),
                    key=lambda p: int(re.search(r"-cr(\d+)\.md$", p.name).group(1)))
    k = len(briefs) + 1
    if not briefs:
        prior = quoted(draft, "`{{PRIOR}}`, first variant")
        rereview = "NONE, first review."
    elif briefs[-1].parent == DIR:
        # a re-cut round never re-rolls a rejection (D24 condition 5): a SKILL_REPAIR_REQUIRED verdict of the earlier
        # round is a stop before X5.0 (P-84 revised), not a reason for another round on the same bytes
        for v in sorted(DIR.glob(f"SECTION-10-REVIEW-cr{k - 1}-*.md")):
            t = v.read_text(encoding="utf-8")
            first = min(((t.find(w), w) for w in ("SKILL_REPAIR_REQUIRED", "SKILL_FIT_CONFIRMED") if w in t),
                        default=(-1, None))[1]
            if first == "SKILL_REPAIR_REQUIRED":
                refuse("REPAIR_VERDICT_PENDING", verdict=str(v))
        prior = quoted(draft, "`{{PRIOR}}`, second variant").replace("<k-1>", str(k - 1))
        rereview = f"Give the disposition of every finding in round cr{k - 1}'s verdict files, if any."
    else:
        if not a.prior_file:
            refuse("PLAN_CHANGE_ROUND_NEEDS_PRIOR_FILE", newest=str(briefs[-1]))
        t = Path(a.prior_file).read_text(encoding="utf-8")
        prior = t.split("## PRIOR", 1)[1].split("## REREVIEW", 1)[0].strip()
        rereview = t.split("## REREVIEW", 1)[1].strip()
    head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    lines = [f"- {r['file']}, {r['files']} files, {r['bytes']} bytes, sha256 {r['sha256']}; extracted freeze {r['freeze']}"
             for r in pk["archives"]]
    block = re.search(r"```plain text\n.*?```\n", draft, re.S).group(0)
    fill = {"{{K}}": str(k), "{{ARCHIVES}}": "\n".join(lines), "{{OUT_DIR}}": pk["out_dir"], "{{HEAD}}": head,
            "{{PRIOR}}": prior, "{{REREVIEW}}": rereview}
    for tok, val in fill.items():
        block = block.replace(tok, val)
    header = (f"---\nartifact_type: SKILL_REVIEWER_PROMPT\n"
              f"template: docs/prompt_ecosystem_management/reviewer-prompt-template.md v1.1\n"
              f"round: cr{k} (MODIFICATION-20260923-closeout-residuals)\n"
              f"filled_from: {EV}/skills/REVIEWER-PROMPT-cr.draft.md by fill_brief.py (P-100)\n"
              f"committed_before_review: true (D24)\n---\n\n"
              f"# Reviewer prompt, round cr{k}\n\n"
              f"The same brief goes to both reviewers. Only the reviewer id and the record path differ. Both are fresh.\n"
              f"- **SFR-CR{k}-1** writes `{DIR}/SECTION-10-REVIEW-cr{k}-SFR-CR{k}-1.md`\n"
              f"- **SFR-CR{k}-2** writes `{DIR}/SECTION-10-REVIEW-cr{k}-SFR-CR{k}-2.md`\n\n")
    out = header + block
    if "{{" in out:
        refuse("UNFILLED_TOKEN", at=out[out.index("{{"):out.index("{{") + 40])
    if not a.write:
        sys.stdout.write(out)
        return
    dest = DIR / f"REVIEWER-PROMPT-cr{k}.md"
    if dest.exists():
        refuse("BRIEF_EXISTS", path=str(dest))
    dest.write_text(out, encoding="utf-8")
    print(json.dumps({"k": k, "brief": str(dest),
                      "reviewers": [{"id": f"SFR-CR{k}-{i}", "record": str(DIR / f"SECTION-10-REVIEW-cr{k}-SFR-CR{k}-{i}.md")}
                                    for i in (1, 2)]}))


if __name__ == "__main__":
    main()
