# STEP-0D Full Report — token_roster_validate (run_20260102_211957_utc)

## Summary
- Epic / Step: HDE-EPIC022 / STEP-0D (token_roster_validate)
- Status: TOOLING_BLOCKED (exit_code=0)
- Blocked reason: missing validator at tools/qa/token_roster_validate.py
- Rails: SAFE_MODE=1, ALLOW_NETWORK=0, APP_ENV=local, LC_ALL=C, LANG=C, TZ=UTC
- PF matches: PF04-Canon-HDE-Governance-v1.7.7.md; PF20-Canon-HDE-Phased-Epics-v1.7.1.md
- Run stamp (UTC): 20260102_211957_utc
- Working directory: /workspaces/glow-hdengine-v2
- Python: Python 3.11.14

## Evidence Paths
- Step log: [audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/logs/step_0d_token_roster_validate.log](audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/logs/step_0d_token_roster_validate.log)
- Outcome JSON: [audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/results/outcome.json](audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/results/outcome.json)
- Stdout: [audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/stdout/token_roster_validate.stdout.txt](audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/stdout/token_roster_validate.stdout.txt)
- Stderr: [audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/stderr/token_roster_validate.stderr.txt](audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/stderr/token_roster_validate.stderr.txt)
- PF match lists: [audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/inputs/pf04_matches.txt](audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/inputs/pf04_matches.txt), [audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/inputs/pf20_matches.txt](audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/inputs/pf20_matches.txt)
- Context inputs: [audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/inputs/run_stamp_utc.txt](audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/inputs/run_stamp_utc.txt), [audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/inputs/python_version.txt](audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/inputs/python_version.txt), [audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/inputs/pwd.txt](audit/qa/hde-epic022/hde_epic022_step_0d_qapass5/run_20260102_211957_utc/inputs/pwd.txt)

## Outcome JSON
```json
{
  "status": "TOOLING_BLOCKED",
  "exit_code": 0,
  "pf04_matches_count": 1,
  "pf20_matches_count": 1,
  "tooling_blocked_reason": "missing_validator:tools/qa/token_roster_validate.py"
}
```

## Step Log (header + body)
```
{"check_id": "STEP-0D", "step_name": "token_roster_validate", "epic_id": "HDE-EPIC022", "run_id": "run_20260102_211957_utc", "command": "python tools/qa/token_roster_validate.py --epic \"HDE-EPIC022\" --pf04 <resolved> --pf20 <resolved>", "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "local", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "rails": "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=local LC_ALL=C LANG=C TZ=UTC", "pf_refs": ["PF04 - HDE-Governance, 72.0", "PF20 - HDE-Phased Epics, 72.7", "PF19 - Glow QA Guide, 4.4", "PF19 - Glow QA Guide, 3.5.11"], "intended_tokens": [], "claimed_tokens": [], "tokens": [], "status": "TOOLING_BLOCKED", "exit_code": 0, "started_at_utc": "2026-01-02T21:19:57Z", "ended_at_utc": "2026-01-02T21:19:58Z", "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"}

---- STDOUT ----


---- STDERR ----

```

## Stdout (empty)
```

```

## Stderr (empty)
```

```

## PF Canon Matches
```
docs/pfcanon/PF04-Canon-HDE-Governance-v1.7.7.md
docs/pfcanon/PF20-Canon-HDE-Phased-Epics-v1.7.1.md
```

## Context Inputs
```
run_stamp_utc.txt: 20260102_211957_utc
python_version.txt: Python 3.11.14
pwd.txt: /workspaces/glow-hdengine-v2
```
