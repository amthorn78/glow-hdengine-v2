---
artifact_type: OPS_TASK
artifact_id: HDE-EPIC040-OPS01-OPS-TASK
artifact_version: "1.1"
predecessor: docs/ephemeral/HDE-EPIC040-OPS01-ops-task-v1.0.md
task_state: READY
execution_state: NOT_EXECUTED
change_class: EPIC
change_id: HDE-EPIC040
ops_unit_id: HDE-EPIC040-OPS01
authoring_context: APPROVED_BASE_WITH_OVERLAYS
creator: retained whole-change HDE-EPIC040 Implementation Architect (OPS-10); acceptance owner (OPS-30)
execution_posture: MANUAL_PROMPT_EXECUTION
capture_time_utc: 2026-09-27T02:10:00Z
---

# HDE-EPIC040-OPS01 — Ops Task v1.1 (corrective): supplemental adverse checks

This task **has not been executed**. It is the bounded correction required by `docs/ephemeral/HDE-EPIC040-OPS01-ops-task-receipt-v1.0.md` §5, which rejected the earlier result.

## 1. What stays and what is corrected

**Stays accepted (not re-run).** The attestation stored at `audit/ops/hde-epic040/ops01/attestation.json` binds candidate `6f53d82`. Receipt §3 verified it independently. Adverse checks A-1 to A-4 are also met, per receipt §4. Every other v1.0 field is unchanged:
- the identity and lineage table, with its bases, PF10 v13.3.7 and the addenda;
- the target facts;
- the prohibitions;
- the non-claims;
- the register.

**Corrected.**
- A-5, A-6 and A-7 were not validly exercised.
- The attempt 3 log and `SHA256SUMS` are missing.

This task closes exactly those gaps. It uses one exact script, and the executor runs it without editing it.

## 2. Authority

| Field | Value |
| --- | --- |
| Executor | The PO, or the session the PO explicitly delegates for Task ID `HDE-EPIC040-OPS01` |
| P-0 | Nathan's explicit, secret-free delegation, supplied in the executing session. The earlier P-0, recorded in the attempt 2 log, names this Task ID and its adverse checks. A fresh confirmation for the supplemental run is required, and the script records it verbatim from `P0_FILE` |
| Target | A clean checkout of `main` in the executor's workspace. PF07-derived (§5.1, §2.8). Classification: `not applicable` (local, closed-rails, source read-only) |

## 3. The script (the only permitted execution)

- **File:** `docs/ephemeral/HDE-EPIC040-OPS01-supplemental-run-v1.1.sh`
- **SHA-256:** `8a6e0af8fee7d6f3d34916fef6efd7458cdb11020151a2ff4a875813fe7d361c`
- **Size:** 4,618 bytes

**What it does**
- Pins closed rails and unsets vendor and database keys.
- Writes **only** under one `mktemp -d /tmp/...` work directory.
- Refuses to run unless it is started from the repository root.
- Stops at the first failed precondition.

**Order of its steps**
1. P-0 quote, then preflight: candidate equivalence to `edbd414` outside `docs/ephemeral` and `audit/ops/hde-epic040`, a clean tree, and the manifest-only check.
2. A fixture bundle build and verify, used only as input for A-5 and A-6.
3. **A-5:** flip one byte of `attestation.json` in a copy. `--verify` must refuse with an `attestation_*` code.
4. **A-6:** append one byte to the first evidence file in a copy. `--verify` must refuse with an `attestation_*` code.
5. **A-7:** make a throwaway clone, **commit** a one-byte change to release member `schemas/reader.v2.schema.json`, and confirm the clone is clean. The build from that clone must refuse with a code **other than** `source_tree_not_clean`.
6. Post-check: the candidate's HEAD and tree are unchanged.

**Exit codes**
- `0` = PASS
- `2` = FAIL_BEHAVIOR (a check did not refuse as required)
- `3` = STOP (a precondition failed, so nothing is concluded)

Its full output is the log file `ops01_execution_log.attempt4.md` in the work directory.

## 4. Executor steps (exact)

From the repository root, on an up-to-date, clean `main`:

```bash
git checkout main && git pull --ff-only && git status --porcelain   # must print nothing
sha256sum docs/ephemeral/HDE-EPIC040-OPS01-supplemental-run-v1.1.sh  # must equal the §3 hash
cp docs/ephemeral/HDE-EPIC040-OPS01-supplemental-run-v1.1.sh /tmp/ops01-run.sh
cat > /tmp/ops01_p0.txt <<'EOF'
<paste Nathan's P-0 delegation message here, verbatim>
EOF
P0_FILE=/tmp/ops01_p0.txt bash /tmp/ops01-run.sh; echo "script_exit=$?"
```

Do not edit the script. If it stops or fails, report its output as it is. Do not retry with changes.

**Evidence storage** runs only after the script has exited, whatever its result. `W` is the `WORKDIR=` path the script printed last:

```bash
W=<the printed WORKDIR>
git checkout -b ops/hde-epic040-ops01-supplemental
cp "$W/ops01_execution_log.attempt4.md" audit/ops/hde-epic040/ops01/
( cd audit/ops/hde-epic040/ops01 && sha256sum attestation.json attestation.json.sha256 build.log ops01_execution_log.attempt1.md ops01_execution_log.attempt2.md ops01_execution_log.attempt4.md > SHA256SUMS )
```

Then write `docs/ephemeral/HDE-EPIC040-OPS01-ops-execution-result-v1.3.md`. It records:
- the script exit code and the result line;
- the A-5, A-6 and A-7 codes;
- the P-0 quote;
- the candidate HEAD;
- the evidence paths.

Commit, push, and open one PR. Do not merge it. Do not copy the fixture bundle into the repository.

**Attempt 3 log.** It was not stored. Record it as `NOT_PRODUCED`, with the reason "written to /tmp and not retained". Do not reconstruct it.

## 5. Outcome

- **PASS** means that A-5, A-6 and A-7 refused as required (script exit 0), together with the stored evidence. In that case, OPS-30 can accept OPS01 on the stored attestation plus this run.
- **FAIL_BEHAVIOR** (exit 2) is a real finding against the release tooling. It returns to the IA.
- **STOP** (exit 3) concludes nothing. Record the result and return it to the IA.

## 6. Prohibitions and non-claims

The v1.0 §7 prohibitions and §11 non-claims apply unchanged. In particular:
- no write inside the repository before the evidence-storage step;
- no merge;
- no network, vendor or database access;
- no QA, acceptance, deployment or closure claim.

## 7. Provenance

- **Prompt use:** `GCFPE-USE-HDE-EPIC040-OPS-10-20260927-OPS01-02`. That is OPS-10 — Create Bounded Ops Task — 091426.1, run by the whole-change IA. Repository persistence: `PENDING / NON_GATING`.
- **How the script was checked:** only statically (`bash -n` plus a code read of the tool's refusal paths). It was not executed by its author, because execution requires P-0.
