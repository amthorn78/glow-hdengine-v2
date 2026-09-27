---
artifact_type: OPS_TASK
artifact_id: HDE-EPIC040-OPS01-OPS-TASK
artifact_version: "1.2"
predecessor: docs/ephemeral/HDE-EPIC040-OPS01-ops-task-v1.1.md
task_state: READY
execution_state: NOT_EXECUTED
change_class: EPIC
change_id: HDE-EPIC040
ops_unit_id: HDE-EPIC040-OPS01
authoring_context: APPROVED_BASE_WITH_OVERLAYS
creator: HDE-EPIC040-2, successor retained whole-change HDE-EPIC040 Implementation Architect (OPS-10); acceptance owner (OPS-30)
execution_posture: MANUAL_PROMPT_EXECUTION
capture_time_utc: 2026-09-27T03:10:00Z
---

# HDE-EPIC040-OPS01 — Ops Task v1.2 (corrective): supplemental adverse checks, with environment setup

This task **has not been executed**. It replaces v1.1 as required by `docs/ephemeral/HDE-EPIC040-OPS01-ops-task-receipt-v1.1.md`.

v1.1 is unchanged in every respect but one. Its environment step installed the two requirements files and not the repository package, so the isolated closure stage could not import `engine` (receipt v1.1 §1). v1.2 adds the repository's standard install and an import probe. The script is the same file with the same hash.

## 1. Authority

- **Executor:** the session Nathan delegates in writing for Task ID `HDE-EPIC040-OPS01`.
- **P-0:** the delegation message Nathan pastes into that session. It names this task, v1.2. The executor saves it to `/tmp/ops01_p0.txt` exactly as pasted. Nathan composes nothing.
- **Prerequisites:** PR #524 (result v1.3) and the PR carrying this task are both merged into `main`.

## 2. Exact commands

Nothing is written inside the repository until step 3. Run these from the repository root:

```bash
git checkout main && git pull --ff-only && git status --porcelain      # must print nothing
python -m pip install -r requirements.txt -r requirements-dev.txt -e .
( cd /tmp && python -c "import engine, jsonschema; print('env_ready')" ) # must print env_ready
git status --porcelain                                                 # must still print nothing
sha256sum docs/ephemeral/HDE-EPIC040-OPS01-supplemental-run-v1.1.sh     # must be 8a6e0af8fee7d6f3d34916fef6efd7458cdb11020151a2ff4a875813fe7d361c
cp docs/ephemeral/HDE-EPIC040-OPS01-supplemental-run-v1.1.sh /tmp/ops01-run.sh
cat > /tmp/ops01_p0.txt <<'EOF'
<Nathan's delegation message, exactly as pasted into this session>
EOF
P0_FILE=/tmp/ops01_p0.txt bash /tmp/ops01-run.sh; echo "script_exit=$?"
```

- **The probe runs from `/tmp` on purpose.** From the repository root, `import engine` would succeed without the install and prove nothing.
- **Stop points.** If any "must" line fails, stop and report it; do not run the script. Do not edit the script.
- **Retries.** One retry is allowed, and only for an infrastructure failure before the tool body runs (install or checkout). A failure inside the tool is final: report it and return to the IA.

## 3. Evidence storage (only after the script exits, whatever its result)

`W` is the `WORKDIR=` path the script printed last. The script always names its log `…attempt4.md`. This run is stored as **attempt 5**, and the stored filename is authoritative:

```bash
W=<the printed WORKDIR>
git checkout -b ops/hde-epic040-ops01-supplemental-v1.2
cp "$W/ops01_execution_log.attempt4.md" audit/ops/hde-epic040/ops01/ops01_execution_log.attempt5.md
( cd audit/ops/hde-epic040/ops01 && sha256sum attestation.json attestation.json.sha256 build.log ops01_execution_log.attempt1.md ops01_execution_log.attempt2.md ops01_execution_log.attempt4.md ops01_execution_log.attempt5.md > SHA256SUMS )
```

Then write `docs/ephemeral/HDE-EPIC040-OPS01-ops-execution-result-v1.4.md`. It records:
- the script exit code and its `RESULT:` line;
- the A-5, A-6 and A-7 exit codes and refusal codes;
- the `env_ready` probe output;
- the P-0 message;
- the candidate HEAD;
- the evidence paths.

Commit, push, and open **one** PR. Do not merge it. Do not copy the fixture bundle into the repository.

## 4. Outcome

- **PASS** (script exit 0): A-5, A-6 and A-7 refused as required. OPS-30 can then accept OPS01 on the stored attestation plus this run.
- **FAIL_BEHAVIOR** (exit 2): a real finding against the release tooling. Return it to the IA.
- **STOP** (exit 3): nothing is concluded. Record it and return to the IA.

## 5. Unchanged

The following carry over unchanged:
- the v1.0 §7 prohibitions and §11 non-claims;
- the v1.1 §1 carry-over (the accepted attestation, A-1 to A-4);
- attempt 3's `NOT_PRODUCED` status.

In particular, this task makes no network, vendor or database call, performs no merge, and claims no QA, acceptance, deployment or closure.

## 6. Provenance

- **Prompt use:** `GCFPE-USE-HDE-EPIC040-OPS-10-20260927-OPS01-03`. That is OPS-10 — Create Bounded Ops Task — 091426.1. Repository persistence: `PENDING / NON_GATING`.
- **Pre-check:** the IA ran the unedited script in a scratch environment built with these exact install steps. It exited 0 (receipt v1.1 §2). That run is not evidence.
- **Next prompt:** OPS-20 — Execute Bounded Ops Task, on this task. Its result returns to OPS-30.
