"""Cross-check: every `old:`/`new:` block of spec §8a and §8b is reflected in the edited tree (the `new:` text,
token-expanded, occurs in some file of the six packages, and the `old:` text no longer occurs where it was a
replacement). Also checks that the §5.9 historical files are byte-identical to the synced tree.
usage: PYTHONDONTWRITEBYTECODE=1 python3 check_spec_blocks.py <edited-skills-root> <synced-root>"""
import hashlib, re, sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from texts import SPEC, x  # noqa: E402
K, SYN = Path(sys.argv[1]), Path(sys.argv[2])
PKGS = ("glow-hde-pr-development", "amthor-workspace-governance-audit", "change-flow", "session-relay-flowmaster", "tw-flowmaster", "flowmaster-validate")
corpus = {p: p.read_text(encoding="utf-8") for pk in PKGS for p in (K / pk).rglob("*") if p.is_file() and p.suffix in (".md", ".py", ".json")}
succ_map = hashlib.sha256((K / "change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json").read_bytes()).hexdigest()
sec = SPEC[SPEC.index("## §8a Skill edits"):SPEC.index("## §9 The gate")]
blocks = re.findall(r"(?ms)^```\n(old: .*?)\n```$", sec)
missing, stale = [], []
for b in blocks:
    old, new = b.split("\nnew: ", 1) if "\nnew: " in b else (b, None)
    if new is None:
        new = b.split("\nnew:", 1)[1] if "\nnew:" in b else None
    old = old[len("old: "):]
    in8b = sec.index(b) > sec.index("## §8b Skill edits")
    fix = lambda s: x(s.replace("\\n", "\n") if in8b else s).replace("<successor runtime map sha256, §5>", succ_map)
    new_t, old_t = fix(new or ""), fix(old)
    if new_t.strip() and not any(new_t in t for t in corpus.values()):
        missing.append(new_t[:120])
    if old_t.strip() and old_t not in new_t and any(old_t in t for t in corpus.values()) and new_t.strip():
        stale.append(old_t[:120])
print(f"spec old/new blocks: {len(blocks)}; new text absent: {len(missing)}; old text still present: {len(stale)}")
for m in missing: print("  MISSING:", repr(m))
for s in stale: print("  STALE:  ", repr(s))
HIST = ["flowmaster-validate/references/glow-hde-canonical-change-flow-r1.json",
        "change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map.json",
        "change-flow/references/strength-analyzer-middleware-correction.json", "change-flow/references/epic-alpha-repair-correction.json",
        "change-flow/references/epic-reengineering-correction.json", "change-flow/references/integrated-qa-readiness-correction.json",
        "change-flow/references/pre-guide-audit-correction.json", "change-flow/references/final-cycle-scan-extension.json",
        "change-flow/references/alpha-feedback-correction.json", "change-flow/references/gcfpe-20260912.2-direct-handoff-contract.json",
        "change-flow/references/gcfpe-20260913.1-direct-handoff-contract.json", "change-flow/references/gcfpe-20260913.1-091326.2-direct-handoff-contract.json",
        "change-flow/references/gcfpe-current-direct-handoff-contract.json"]
HS = ["validate_strength_middleware.py", "validate_epic_alpha.py", "validate_epic_reengineering.py", "run_strength_middleware_fixtures.py",
      "run_epic_alpha_fixtures.py", "validate_integrated_readiness.py", "validate_pre_guide_correction.py", "validate_final_scan.py",
      "validate_alpha_feedback.py", "run_integrated_readiness_fixtures.py", "run_final_scan_fixtures.py", "run_alpha_feedback_fixtures.py"]
HIST += ["flowmaster-validate/scripts/" + s for s in HS] + ["flowmaster-primary/SKILL.md"]
diff = [h for h in HIST if (K / h).read_bytes() != (SYN / h).read_bytes()]
print(f"historical files byte-identical: {len(HIST) - len(diff)} of {len(HIST)}", diff)
