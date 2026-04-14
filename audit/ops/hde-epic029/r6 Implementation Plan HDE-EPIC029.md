# Artifact Map

**Inputs**

* IG: `Epic Plan HDE-EPIC029.md`  
* Caveats: none provided  
* PF docs used selectively: `PF10`, `PF09.4`, `PF14`, `PF12`, `PF02`, `PF04`, `PF19`

**Output**

* One self-contained Implementation Plan covering PRs, OPS tasks, PF09 completion scope, IG crosswalk, evidence outputs, and paste-ready Codex prompts

# **Brief recap of scope**

This epic is a narrow Conjunction closeout slice. PF10 speaks here only on PF09 routing: the retired single-document PF09 is no longer active, so this plan uses `PF09.4 - Conjunction` as the only phased completion backbone. No Caveats doc was provided.

This epic closes only the three IG-scoped PF09.4 subtasks `HDE-CONJ009.1`, `HDE-CONJ008.1`, and `HDE-CONJ001.4`. The plan uses the existing conjunction loci already embedded in this document and does not treat any planning audit as authoritative or required for execution.

# PF09 Completion Scope

| PF09 task ID | PF09 subtask ID | Disposition for this plan | Implementing task ID(s) | IG source item(s): exact IG labels | Caveat ID(s) | Proof pointer | ADR ID | Notes |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| `HDE-CONJ009` | `HDE-CONJ009.1` | Complete in this epic | `PR-01`, `PR-04` | `Deliverable D1 — Global discipline`; `ISSUE-HDE-EPIC029-001 — Conjunction JSON surface inventory boundary`; `Tokens and Evidence (Acceptance)` | None | N/A | N/A | PR-01 closes the code/evidence slice; PR-04 binds the explicit inventory artifact into the final acceptance surfaces. |
| `HDE-CONJ008` | `HDE-CONJ008.1` | Complete in this epic | `PR-02`, `PR-04` | `Deliverable D2 — Writer Surfaces (API)`; `Tokens and Evidence (Acceptance)` | None | N/A | N/A | PR-02 closes writer posture on the existing dev writer surface; PR-04 binds final acceptance artifacts. |
| `HDE-CONJ001` | `HDE-CONJ001.4` | Complete in this epic | `PR-03`, `OPS-01`, `PR-04` | `Deliverable D3 — Dev HTTP Harness`; `ISSUE-HDE-EPIC029-002 — Non-Codespaces harness binding coverage`; `QA Rails — Open/Close (Final PR)` | None | N/A | N/A | PR-03 closes repo-side wiring; OPS-01 captures explicit environment evidence; PR-04 binds final disposition and close-pack surfaces. |

# Crosswalk: IG items \-\> Plan tasks

| IG work item (exact label from IG) | Caveats applied | PF09 task ID(s) | PF09 subtask ID(s) | Implementation tasks (PR-0N / OPS-0N IDs, or Already implemented) | Evidence pointer (Already implemented only) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| `Deliverable D1 — Global discipline` | None | `HDE-CONJ009` | `HDE-CONJ009.1` | `PR-01`, `PR-04` | N/A |
| `Deliverable D2 — Writer Surfaces (API)` | None | `HDE-CONJ008` | `HDE-CONJ008.1` | `PR-02`, `PR-04` | N/A |
| `Deliverable D3 — Dev HTTP Harness` | None | `HDE-CONJ001` | `HDE-CONJ001.4` | `PR-03`, `OPS-01`, `PR-04` | N/A |
| `ISSUE-HDE-EPIC029-001 — Conjunction JSON surface inventory boundary` | None | `HDE-CONJ009` | `HDE-CONJ009.1` | `PR-01`, `PR-04` | N/A |
| `ISSUE-HDE-EPIC029-002 — Non-Codespaces harness binding coverage` | None | `HDE-CONJ001` | `HDE-CONJ001.4` | `PR-03`, `OPS-01`, `PR-04` | N/A |
| `Tokens and Evidence (Acceptance)` | None | `HDE-CONJ009`, `HDE-CONJ008`, `HDE-CONJ001` | `HDE-CONJ009.1`, `HDE-CONJ008.1`, `HDE-CONJ001.4` | `PR-04` | N/A |
| `QA Rails — Open/Close (Final PR)` | None | `HDE-CONJ001` | `HDE-CONJ001.4` | `OPS-01`, `PR-04` | N/A |

# Execution plan

1. **PR-01** **One-line intent:** Make the in-scope conjunction JSON surface inventory explicit and close single-emitter canonical JSON discipline for the bounded conjunction surfaces. **Depends on, if any:** none **IG item(s) covered, exact IG labels:** `Deliverable D1 — Global discipline`; `ISSUE-HDE-EPIC029-001 — Conjunction JSON surface inventory boundary` **PF09 task ID(s):** `HDE-CONJ009` **PF09 subtask ID(s):** `HDE-CONJ009.1` **PF09 completion role:** `Contributes evidence only`  
     
2. **PR-02** **One-line intent:** Finish writer success/error envelope posture for `/dev/writer/conjunction` and refresh the governed conjunction writer evidence family without widening into A7. **Depends on, if any:** `PR-01` **IG item(s) covered, exact IG labels:** `Deliverable D2 — Writer Surfaces (API)` **PF09 task ID(s):** `HDE-CONJ008` **PF09 subtask ID(s):** `HDE-CONJ008.1` **PF09 completion role:** `Contributes evidence only`  
     
3. **PR-03** **One-line intent:** Close the repo-side start-helper and healthcheck wiring for the dev sampler harness so QA consumes `DEV_SAMPLER_URL` instead of guessing. **Depends on, if any:** `PR-01` **IG item(s) covered, exact IG labels:** `Deliverable D3 — Dev HTTP Harness`; `ISSUE-HDE-EPIC029-002 — Non-Codespaces harness binding coverage` **PF09 task ID(s):** `HDE-CONJ001` **PF09 subtask ID(s):** `HDE-CONJ001.4` **PF09 completion role:** `Contributes evidence only`  
     
4. **OPS-01** **One-line intent:** Validate Codespaces and local-dev sampler harness bindings and capture the explicit environment-coverage evidence required to close `HDE-CONJ001.4` without guesswork. **Depends on, if any:** `PR-03` merged **IG item(s) covered, exact IG labels:** `Deliverable D3 — Dev HTTP Harness`; `ISSUE-HDE-EPIC029-002 — Non-Codespaces harness binding coverage`; `QA Rails — Open/Close (Final PR)` **PF09 task ID(s):** `HDE-CONJ001` **PF09 subtask ID(s):** `HDE-CONJ001.4` **PF09 completion role:** `Contributes evidence only`  
     
5. **PR-04** **One-line intent:** Generate the epic029 acceptance map, token/evidence matrix, viability log, doc-delta ledgers, QA step manifest, close-pack pair, and explicit closure artifacts, then refresh the Human Index and Machine Mirror in the same PR. **Depends on, if any:** `PR-01`, `PR-02`, `PR-03`, `OPS-01`, and epic-close Live QA outputs being available **IG item(s) covered, exact IG labels:** `Tokens and Evidence (Acceptance)`; `QA Rails — Open/Close (Final PR)`; `Deliverable D1 — Global discipline`; `Deliverable D2 — Writer Surfaces (API)`; `Deliverable D3 — Dev HTTP Harness` **PF09 task ID(s):** `HDE-CONJ009`, `HDE-CONJ008`, `HDE-CONJ001` **PF09 subtask ID(s):** `HDE-CONJ009.1`, `HDE-CONJ008.1`, `HDE-CONJ001.4` **PF09 completion role:** `Complete in this epic`

# PR series

## PR-01 — Conjunction JSON surface inventory and single-emitter canonical JSON closure

### Intent (what must be true after PR)

After this PR, the conjunction JSON-emitting surface inventory is explicit, bounded, and checkable in-repo, and the in-scope conjunction JSON surfaces are all confirmed to use the single shared emitter with canonical JSON invariants enforced. No alternate serializer path, no alternate canonical JSON gate family, and no new public surface are introduced.

### IG source items (exact IG labels)

* `Deliverable D1 — Global discipline`  
* `ISSUE-HDE-EPIC029-001 — Conjunction JSON surface inventory boundary`

### Caveats applied (CAV-001 style IDs; None if not applicable)

None

### PF09 task IDs (exact \+ proof excerpts from PF09)

* `HDE-CONJ009`

`## Task HDE-CONJ009 — Global discipline (canonical JSON & Index updates)` `**Task ID:** HDE-CONJ009`

### PF09 subtask IDs (exact \+ proof excerpts from PF09)

* `HDE-CONJ009.1`

`### Subtask HDE-CONJ009.1 — Canonical JSON invariants (all surfaces)` `Enforce canonical JSON invariants (encoding, key order, compactness, LF, set ordering) for all surfaces that emit JSON, using the single shared emitter.`

### PF09 completion role (Complete in this epic | Contributes evidence only | Already implemented and reused | Blocked on ADR)

Contributes evidence only

### PF14 pointers (anchors \+ proof excerpts from PF14)

* `PF14 — HDE Mechanics Guide, §8.2 Policy — Emitter & serializer`

`## **8.2 Policy — Emitter & serializer**` `Single emitter (byte-authoritative). Reader and CLI public bytes MUST be emitted via the same presenter–emitter entrypoint symbol.`

* `PF14 — HDE Mechanics Guide, §5.8 Dev sampler HTTP harness (internal/dev-only)`

`## **5.8 Dev sampler HTTP harness (internal/dev-only)**` `Purpose. Provide a dev/admin-only HTTP harness for the sampler core that mirrors the dev sampler CLI semantics while remaining a strictly internal surface.`

* `PF14 — HDE Mechanics Guide, # 10) Writer Surfaces (API)`

`# 10\) Writer Surfaces (API)` `Purpose. Provide minimal, idempotent writer endpoints (e.g., preferences) with strict schema validation and deterministic effects.`

* `PF14 — HDE Mechanics Guide, §24.2 Production posture (Reader / Compat)`

`## **24.2 Production posture (Reader / Compat)**` `POST non-conditional. Requests do not carry validators; responses never return 304 (ignore If-* conditionals).`

### Discovery (Codex read-only check first): what to inspect and what must be confirmed found versus missing

Inspect first:

* `adapter/http_reader.py`  
* `engine/cli/main.py`  
* `engine/presenter/emitter.py`  
* `docs/ENDPOINTS_CATALOG.json`  
* `tools/evidence/run_canonical_json_gate.py`  
* `audit/gates/json_gate/canonical/`  
* `audit/gates/canonical_json/`  
* `docs/evidence/INDEX.json`  
* `artifacts/evidence_index.jsonl`

Confirm found:

* `/reader`  
* `/dev/writer/conjunction`  
* `/internal/dev/sampler`  
* the current shared-emitter call path for all in-scope conjunction JSON surfaces  
* the current authoritative canonical JSON gate family under `audit/gates/json_gate/canonical/`  
* any still-produced legacy canonical JSON gate outputs under `audit/gates/canonical_json/`

Confirm missing:

* any compiled, explicit conjunction JSON surface-inventory artifact for epic029  
* any in-scope conjunction JSON emitter path that bypasses the shared emitter  
* any alternate canonical JSON gate family or alternate evidence home introduced outside the canonical families already present

### Implementation requirements (what, not how; include PF doc citations when you use PF canon to add specificity)

* Create one explicit conjunction JSON surface inventory artifact at `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md`. This artifact must enumerate the bounded conjunction JSON-emitting surfaces for this epic and state, for each surface, whether it is in-scope, out-of-scope, or carry-forward.  
* Treat only the three repo-proven conjunction loci as in-scope unless the repo proves another conjunction JSON-emitting surface in the same bounded slice: `/reader`, `/dev/writer/conjunction`, and `/internal/dev/sampler`.  
* Ensure each in-scope conjunction JSON surface emits via the shared emitter required by `PF14 — HDE Mechanics Guide, §8.2 Policy — Emitter & serializer`.  
* Refresh the authoritative canonical JSON gate family under `audit/gates/json_gate/canonical/`.  
* If the current gate writer still produces the legacy family under `audit/gates/canonical_json/`, refresh that family coherently in the same PR rather than leaving it stale.  
* Refresh `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`, `audit/gates/topology/orientation_demo.txt`, and all affected sibling `*.path_proof.txt` files in the same PR if any governed bytes change.  
* Do not add a new public route, do not introduce a second canonical JSON gate family, and do not introduce a second Index/Mirror home.

### Concrete anchors (small snippets: pseudocode, schema fragments, CLI examples, or exact repo anchors only when needed)

* `@bp.get("/reader")`  
* `@bp.get("/dev/writer/conjunction")`  
* `@bp.route("/internal/dev/sampler", methods=["POST"])`  
* `emit_public(...)`  
* `engine/presenter/emitter.py`  
* `tools/evidence/run_canonical_json_gate.py`

### Evidence outputs (paths \+ artifact names \+ filenames; governed where applicable)

* `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md` — will be created in this PR.  
* `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md.path_proof.txt` — will be created in this PR if the inventory artifact is indexed.  
* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson` — already exists and will be refreshed if bytes change.  
* `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson` — already exists and will be refreshed if bytes change.  
* `audit/gates/json_gate/canonical/json_gate_structured_record.json` — already exists and will be refreshed if bytes change.  
* `audit/gates/canonical_json/json_canonical_check.log` — refresh only if the current gate writer still produces the legacy family.  
* `audit/gates/canonical_json/json_canon_compare.log` — refresh only if the current gate writer still produces the legacy family.  
* `docs/evidence/INDEX.json` — already exists and will be refreshed if governed bytes change.  
* `docs/evidence/INDEX.sha256` — already exists and will be refreshed if governed bytes change.  
* `artifacts/evidence_index.jsonl` — already exists and will be refreshed if governed bytes change.  
* `artifacts/evidence_index.jsonl.sha256` — already exists and will be refreshed if governed bytes change.  
* `audit/gates/topology/orientation_demo.txt` — already exists as a governed evidence-skeleton artifact and will be refreshed if the evidence skeleton changes.  
* `audit/gates/topology/orientation_demo.txt.path_proof.txt` — already exists where indexed or will be refreshed in this PR if bytes change.  
* All affected sibling `*.path_proof.txt` files for the files above — already exist where applicable or will be created/refreshed in this PR.

### Acceptance tokens (minimal list; explicit; do not invent)

* `EVIDENCE_INDEX_UPDATED_OK`  
* `MACHINE_MIRROR_UPDATED_OK`  
* `EVIDENCE_INDEX_HASH_OK`  
* `JSON_CANONICAL_CHECK_OK`

### Rails posture (closed by default; if opened, specify condition \+ evidence \+ close-back rule)

Closed by default. This PR must not open rails.

### Basic QA task (exactly one) \+ pass condition

`python tools/evidence/run_canonical_json_gate.py`

Pass condition: the canonical JSON gate exits `0`, the refreshed gate outputs remain coherent, and the new epic029 inventory artifact does not widen the in-scope surface set beyond repo-proven conjunction loci.

### PO inputs (only if required; names-only; no secret values)

None

### Codex Prompt (paste-ready; required)

Task: close `HDE-CONJ009.1` for the bounded conjunction JSON-emitting surfaces only.

Inspect first:

* `adapter/http_reader.py`  
* `engine/cli/main.py`  
* `engine/presenter/emitter.py`  
* `docs/ENDPOINTS_CATALOG.json`  
* `tools/evidence/run_canonical_json_gate.py`  
* `audit/gates/json_gate/canonical/`  
* `audit/gates/canonical_json/`  
* `docs/evidence/INDEX.json`  
* `artifacts/evidence_index.jsonl`

PF09 scope:

* `HDE-CONJ009`  
* `HDE-CONJ009.1`

PF14 anchors:

* `§8.2 Policy — Emitter & serializer`  
* `§5.8 Dev sampler HTTP harness (internal/dev-only)`  
* `# 10) Writer Surfaces (API)`  
* `§24.2 Production posture (Reader / Compat)`

Observed repo facts to preserve:

* `/reader`, `/dev/writer/conjunction`, and `/internal/dev/sampler` already exist.  
* The shared-emitter path already exists in repo reality.  
* The authoritative canonical JSON gate family already exists under `audit/gates/json_gate/canonical/`.  
* The Human Evidence Index and Machine Evidence Mirror already exist.

What to change:

* create one explicit inventory artifact at `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md`  
* bound the in-scope conjunction JSON surface inventory to repo-proven conjunction loci only  
* ensure all in-scope conjunction JSON emission uses the shared emitter  
* refresh the authoritative canonical JSON gate family  
* if the current gate writer still emits the legacy `audit/gates/canonical_json/` family, refresh it coherently in the same PR  
* refresh Index/Mirror, companion proofs, and the topology orientation demo in the same PR if the evidence skeleton changes  
* do not add any new public route, any alternate serializer path, any alternate canonical JSON gate family, or any second Index/Mirror home

Where to change it:

* only the smallest necessary code, evidence-tooling, and audit/meta files under the existing adapter, emitter, gate, and governed evidence roots

What tests or checks to run:

* `python tools/evidence/run_canonical_json_gate.py`  
* `python -m pytest -q tests/http/test_dev_conjunction_http.py`  
* `python -m pytest -q tests/adapter/test_dev_sampler_http.py`  
* `python tools/evidence/update_evidence_index.py`  
* `python tools/evidence/update_evidence_index.py --check`  
* `python tools/evidence/orientation_demo.py`  
* `python tools/evidence/orientation_demo.py --check`  
* `python tools/evidence/validate_evidence_paths.py`  
* `python tools/evidence/check_lf_endings.py`  
* `python ci/checks/check_mirror_schema.sh artifacts/evidence_index.jsonl`

What evidence outputs to produce:

* `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md`  
* `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md.path_proof.txt`  
* refreshed authoritative canonical JSON gate outputs under `audit/gates/json_gate/canonical/`  
* refreshed legacy canonical JSON gate outputs under `audit/gates/canonical_json/` only if they are still-produced governed outputs  
* refreshed `docs/evidence/INDEX.json`  
* refreshed `docs/evidence/INDEX.sha256`  
* refreshed `artifacts/evidence_index.jsonl`  
* refreshed `artifacts/evidence_index.jsonl.sha256`  
* refreshed `audit/gates/topology/orientation_demo.txt`  
* refreshed affected sibling `*.path_proof.txt` files

What pass or fail result means success:

* Success means the in-scope conjunction JSON surface inventory is explicit, bounded, emitter-bound, and supported by refreshed canonical JSON gate evidence with no new public surface and no alternate evidence home.  
* Failure means any in-scope conjunction JSON emitter still bypasses the shared emitter, the inventory silently widens scope, or any still-produced canonical JSON family is left stale.

## PR-02 — Conjunction writer envelope posture closure

### Intent (what must be true after PR)

After this PR, `/dev/writer/conjunction` remains a dev-only surface behind the shared dev-admin gate, returns typed numeric-free writer success and error envelopes, stays no-store and non-conditional, preserves idempotent write/readback behavior, and remains explicitly outside the A7 proof family.

### IG source items (exact IG labels)

* `Deliverable D2 — Writer Surfaces (API)`

### Caveats applied (CAV-001 style IDs; None if not applicable)

None

### PF09 task IDs (exact \+ proof excerpts from PF09)

* `HDE-CONJ008`

`## Task HDE-CONJ008 — Writer Surfaces (API)` `**Task ID:** HDE-CONJ008`

### PF09 subtask IDs (exact \+ proof excerpts from PF09)

* `HDE-CONJ008.1`

`### Subtask HDE-CONJ008.1 — Writer envelope & posture` `Writers: \`Cache-Control: no-store`, never 304.`

### PF09 completion role (Complete in this epic | Contributes evidence only | Already implemented and reused | Blocked on ADR)

Contributes evidence only

### PF14 pointers (anchors \+ proof excerpts from PF14)

* `PF14 — HDE Mechanics Guide, # 10) Writer Surfaces (API)`

`# 10\) Writer Surfaces (API)` `Purpose. Provide minimal, idempotent writer endpoints (e.g., preferences) with strict schema validation and deterministic effects.`

* `PF14 — HDE Mechanics Guide, §10.2 Transport posture (titles-only; owned by Governance)`

`## **10.2 Transport posture (titles-only; owned by Governance)**` `Writers and errors:` `* Cache-Control: no-store; no ETag.`

* `PF14 — HDE Mechanics Guide, §10.6.1 Conjunction writer evidence family (dev harness only)`

`### **10.6.1 Conjunction writer evidence family (dev harness only)**` `Required governed artifacts. The writer evidence family MUST include:`

### Discovery (Codex read-only check first): what to inspect and what must be confirmed found versus missing

Inspect first:

* `adapter/http_reader.py`  
* `tests/http/test_dev_conjunction_http.py`  
* `tests/http/test_endpoint_catalog.py`  
* `tools/evidence/generate_conjunction_writer_evidence.py`  
* `artifacts/writer/`  
* `docs/ENDPOINTS_CATALOG.json`  
* `docs/evidence/INDEX.json`  
* `artifacts/evidence_index.jsonl`

Confirm found:

* `/dev/writer/conjunction`  
* the shared dev-admin gate on that route  
* the current conjunction writer evidence family  
* current idempotent write/readback behavior  
* current endpoint-catalog presence for `dev.writer.conjunction.v1`

Confirm missing:

* any remaining success/error envelope shape that is not typed and numeric-free  
* any no-store / non-conditional posture gap on the conjunction writer surface  
* any lingering use of the conjunction writer route as an A7 proof surface  
* any stale writer evidence or index/mirror companions after writer artifact refresh

### Implementation requirements (what, not how; include PF doc citations when you use PF canon to add specificity)

* Keep `/dev/writer/conjunction` as the existing dev-only conjunction writer surface.  
* Finish `HDE-CONJ008.1` by making both success and error envelopes typed and numeric-free.  
* Preserve `Cache-Control: no-store`, no `ETag`, and no HEAD/304 semantics on the writer route, consistent with `PF14 — HDE Mechanics Guide, §10.2 Transport posture`.  
* Preserve idempotent behavior already required by `HDE-CONJ008.2`; this PR is posture completion, not a new writer redesign.  
* Keep the route outside the A7 proof family.  
* Refresh the governed conjunction writer evidence family exactly at the canonized PF14 paths.  
* Refresh the Human Index, hash sentinel, Machine Mirror, topology orientation demo, and affected path proofs in the same PR if any governed writer artifact bytes change.  
* Do not create a new writer route, do not widen the writer contract into a public surface, and do not introduce a new writer evidence family home.

### Concrete anchors (small snippets: pseudocode, schema fragments, CLI examples, or exact repo anchors only when needed)

* `/dev/writer/conjunction`  
* `dev.writer.conjunction.v1`  
* `artifacts/writer/conjunction_write_readback.log`  
* `artifacts/writer/conjunction_writer_summary.json`

  ### **Evidence outputs (paths \+ artifact names \+ filenames; governed where applicable)**

* `artifacts/writer/conjunction_write_readback.log` — already exists and will be refreshed if bytes change.  
* `artifacts/writer/conjunction_write_readback.log.path_proof.txt` — already exists and will be refreshed if bytes change.  
* `artifacts/writer/conjunction_writer_summary.json` — already exists and will be refreshed if bytes change.  
* `artifacts/writer/conjunction_writer_summary.json.path_proof.txt` — already exists and will be refreshed if bytes change.  
* `docs/evidence/INDEX.json` — already exists and will be refreshed if governed bytes change.  
* `docs/evidence/INDEX.sha256` — already exists and will be refreshed if governed bytes change.  
* `artifacts/evidence_index.jsonl` — already exists and will be refreshed if governed bytes change.  
* `artifacts/evidence_index.jsonl.sha256` — already exists and will be refreshed if governed bytes change.  
* `audit/gates/topology/orientation_demo.txt` — already exists and will be refreshed if the evidence skeleton changes.  
* `audit/gates/topology/orientation_demo.txt.path_proof.txt` — already exists where indexed or will be refreshed in this PR if bytes change.  
* All affected sibling `*.path_proof.txt` files for the files above — already exist where applicable or will be refreshed in this PR.

### Acceptance tokens (minimal list; explicit; do not invent)

* `EVIDENCE_INDEX_UPDATED_OK`  
* `MACHINE_MIRROR_UPDATED_OK`  
* `EVIDENCE_INDEX_HASH_OK`  
* `ENV_RAILS_POLICY_OK`

### Rails posture (closed by default; if opened, specify condition \+ evidence \+ close-back rule)

Closed by default.

One bounded exception is allowed only if the current conjunction writer evidence generator still requires open rails:

* open condition: `SAFE_MODE=0 ALLOW_NETWORK=1` for the generator run only  
* evidence: refreshed conjunction writer evidence family plus index/mirror refresh  
* close-back rule: all subsequent checks and index validation return immediately to closed rails

### Basic QA task (exactly one) \+ pass condition

`python -m pytest -q tests/http/test_dev_conjunction_http.py`

Pass condition: the test exits `0` and proves the conjunction writer surface preserves idempotent semantics while returning typed numeric-free success/error envelopes on the existing dev-only route.

### PO inputs (only if required; names-only; no secret values)

None

### Codex Prompt (paste-ready; required)

Task: close `HDE-CONJ008.1` for the existing conjunction writer surface only.

Inspect first:

* `adapter/http_reader.py`  
* `tests/http/test_dev_conjunction_http.py`  
* `tests/http/test_endpoint_catalog.py`  
* `tools/evidence/generate_conjunction_writer_evidence.py`  
* `artifacts/writer/`  
* `docs/ENDPOINTS_CATALOG.json`  
* `docs/evidence/INDEX.json`  
* `artifacts/evidence_index.jsonl`

PF09 scope:

* `HDE-CONJ008`  
* `HDE-CONJ008.1`

PF14 anchors:

* `# 10) Writer Surfaces (API)`  
* `§10.2 Transport posture (titles-only; owned by Governance)`  
* `§10.6.1 Conjunction writer evidence family (dev harness only)`

Observed repo facts to preserve:

* `/dev/writer/conjunction` already exists.  
* The conjunction writer readback artifacts already exist.  
* The writer route is already intentionally outside the A7 proof family.

What to change:

* make the conjunction writer success and error envelopes typed and numeric-free  
* preserve `Cache-Control: no-store`, no `ETag`, and non-conditional writer posture  
* preserve idempotent write/readback behavior  
* keep the route outside the A7 proof family  
* refresh the canonized conjunction writer evidence family  
* refresh Index/Mirror, orientation demo, and companion proofs in the same PR if governed bytes change  
* do not create a new writer route, new public surface, or new writer evidence family home

Where to change it:

* only the smallest necessary writer route, envelope, test, and evidence-generator files under the existing adapter, tests, tools, and artifacts roots

What tests or checks to run:

* `python -m pytest -q tests/http/test_dev_conjunction_http.py`  
* `python -m pytest -q tests/http/test_endpoint_catalog.py`  
* `SAFE_MODE=0 ALLOW_NETWORK=1 python tools/evidence/generate_conjunction_writer_evidence.py` only if the generator still requires open rails  
* `python tools/evidence/update_evidence_index.py`  
* `python tools/evidence/update_evidence_index.py --check`  
* `python tools/evidence/orientation_demo.py`  
* `python tools/evidence/orientation_demo.py --check`  
* `python tools/evidence/validate_evidence_paths.py`  
* `python tools/evidence/check_lf_endings.py`  
* `python ci/checks/check_mirror_schema.sh artifacts/evidence_index.jsonl`

What evidence outputs to produce:

* refreshed `artifacts/writer/conjunction_write_readback.log`  
* refreshed `artifacts/writer/conjunction_write_readback.log.path_proof.txt`  
* refreshed `artifacts/writer/conjunction_writer_summary.json`  
* refreshed `artifacts/writer/conjunction_writer_summary.json.path_proof.txt`  
* refreshed `docs/evidence/INDEX.json`  
* refreshed `docs/evidence/INDEX.sha256`  
* refreshed `artifacts/evidence_index.jsonl`  
* refreshed `artifacts/evidence_index.jsonl.sha256`  
* refreshed `audit/gates/topology/orientation_demo.txt`  
* refreshed affected sibling `*.path_proof.txt` files

What pass or fail result means success:

* Success means `/dev/writer/conjunction` remains dev-only, stays outside A7, emits typed numeric-free success/error envelopes, preserves idempotent readback behavior, and leaves the writer evidence family, orientation demo, and Index/Mirror coherent.  
* Failure means the route still emits non-typed or numeric-bearing envelopes, gains public/A7 posture, or leaves stale governed evidence companions.

## PR-03 — Repo-side dev harness binding and healthcheck closure

### Intent (what must be true after PR)

After this PR, the repo-side sampler harness wiring no longer relies on guessed hostnames or ports: the dev Reader start helper propagates `APP_ENV` exactly as supplied, repo-side healthcheck tooling reads `DEV_SAMPLER_URL` directly from the environment, and test coverage proves that missing or empty `DEV_SAMPLER_URL` is a tooling failure rather than silent fallback behavior.

### IG source items (exact IG labels)

* `Deliverable D3 — Dev HTTP Harness`  
* `ISSUE-HDE-EPIC029-002 — Non-Codespaces harness binding coverage`

### Caveats applied (CAV-001 style IDs; None if not applicable)

None

### PF09 task IDs (exact \+ proof excerpts from PF09)

* `HDE-CONJ001`

`## Task HDE-CONJ001 — Dev HTTP Harness (single home)` `**Task ID:** HDE-CONJ001`

### PF09 subtask IDs (exact \+ proof excerpts from PF09)

* `HDE-CONJ001.4`

`### **Subtask HDE-CONJ001.4 — Dev/internal HTTP harness infra wiring**` `Ensure that any **internal/dev HTTP harness** intended for QA or evidence flows (including, but not limited to, \`POST /internal/dev/sampler`) has infra-owned start commands and URLs, so QA and PO are never guessing hosts, ports, or paths:`

### PF09 completion role (Complete in this epic | Contributes evidence only | Already implemented and reused | Blocked on ADR)

Contributes evidence only

### PF14 pointers (anchors \+ proof excerpts from PF14)

* `PF14 — HDE Mechanics Guide, §5.8 Dev sampler HTTP harness (internal/dev-only)`

`## **5.8 Dev sampler HTTP harness (internal/dev-only)**` `Purpose. Provide a dev/admin-only HTTP harness for the sampler core that mirrors the dev sampler CLI semantics while remaining a strictly internal surface.`

### Discovery (Codex read-only check first): what to inspect and what must be confirmed found versus missing

Inspect first:

* `.devcontainer/devcontainer.json`  
* `scripts/dev_start_reader.sh`  
* `scripts/qa/dev_sampler_healthcheck.py`  
* `tests/scripts/test_dev_sampler_healthcheck.py`  
* `adapter/http_reader.py`  
* `tests/adapter/test_dev_sampler_http.py`  
* `docs/hde_epic019_remediation.md`

Confirm found:

* `/internal/dev/sampler`  
* current `APP_ENV` gate behavior on the sampler route  
* current repo-side start helper and healthcheck surfaces  
* current `DEV_SAMPLER_URL` usage in repo scripts

Confirm missing:

* any repo-side step that still hardcodes or reconstructs the sampler URL instead of consuming `DEV_SAMPLER_URL`  
* any repo-side helper that silently defaults `APP_ENV` to an allowed value  
* any repo-side healthcheck failure path that does not fail loudly on missing/empty `DEV_SAMPLER_URL`  
* any explicit non-Codespaces disposition artifact; that remains for `OPS-01` plus `PR-04`

### Implementation requirements (what, not how; include PF doc citations when you use PF canon to add specificity)

* Preserve `/internal/dev/sampler` as the existing internal/dev-only harness route.  
* Keep the sampler route contract itself stable; this PR is wiring closure, not contract redesign.  
* Ensure the canonical dev Reader start helper propagates `APP_ENV` exactly as supplied, including missing, empty, allowed, and disallowed values.  
* Ensure repo-side sampler healthcheck tooling consumes `DEV_SAMPLER_URL` directly from the environment and fails loudly if it is missing or empty.  
* Ensure repo-side healthcheck tooling records the effective `DEV_SAMPLER_URL` and rails inputs needed for later OPS evidence.  
* Add or update repo-side test coverage proving the no-guess posture.  
* Do not hard-code local-dev or Codespaces host/port guesses in QA scripts or repo docs. Live environment binding proof lands in `OPS-01`, and final explicit disposition lands in `PR-04`.

### Concrete anchors (small snippets: pseudocode, schema fragments, CLI examples, or exact repo anchors only when needed)

* `.devcontainer/devcontainer.json`  
* `scripts/dev_start_reader.sh`  
* `scripts/qa/dev_sampler_healthcheck.py`  
* `tests/scripts/test_dev_sampler_healthcheck.py`  
* `POST /internal/dev/sampler`

### Evidence outputs (paths \+ artifact names \+ filenames; governed where applicable)

* This PR does not itself mint a new governed evidence family.  
    
* Repo-side readiness for this PR is proven by changes in:  
    
  * `.devcontainer/devcontainer.json`  
  * `scripts/dev_start_reader.sh`  
  * `scripts/qa/dev_sampler_healthcheck.py`  
  * `tests/scripts/test_dev_sampler_healthcheck.py`


* The live binding evidence this PR prepares will be produced by `OPS-01` at:  
    
  * `audit/ops/hde-epic029/ops-01/commands.txt`  
  * `audit/ops/hde-epic029/ops-01/stdout.log`  
  * `audit/ops/hde-epic029/ops-01/stderr.log`  
  * `audit/ops/hde-epic029/ops-01/exit_codes.txt`  
  * `audit/ops/hde-epic029/ops-01/codespaces_dev_sampler_url.md`  
  * `audit/ops/hde-epic029/ops-01/local_dev_sampler_url.md`  
  * `audit/ops/hde-epic029/ops-01/binding_disposition.md`  
  * `audit/ops/hde-epic029/ops-01/created_files_sha256.txt`

### Acceptance tokens (minimal list; explicit; do not invent)

* `ENV_RAILS_POLICY_OK`

### Rails posture (closed by default; if opened, specify condition \+ evidence \+ close-back rule)

Closed by default. This PR should not open rails.

### Basic QA task (exactly one) \+ pass condition

`python -m pytest -q tests/scripts/test_dev_sampler_healthcheck.py`

Pass condition: the test exits `0` and proves the healthcheck tooling consumes `DEV_SAMPLER_URL`, refuses missing or empty bindings, and preserves explicit `APP_ENV` handling.

### PO inputs (only if required; names-only; no secret values)

None

### Codex Prompt (paste-ready; required)

Task: close the repo-side wiring portion of `HDE-CONJ001.4` only.

Inspect first:

* `.devcontainer/devcontainer.json`  
* `scripts/dev_start_reader.sh`  
* `scripts/qa/dev_sampler_healthcheck.py`  
* `tests/scripts/test_dev_sampler_healthcheck.py`  
* `adapter/http_reader.py`  
* `tests/adapter/test_dev_sampler_http.py`  
* `docs/hde_epic019_remediation.md`

PF09 scope:

* `HDE-CONJ001`  
* `HDE-CONJ001.4`

PF14 anchor:

* `§5.8 Dev sampler HTTP harness (internal/dev-only)`

Observed repo facts to preserve:

* `/internal/dev/sampler` already exists.  
* `APP_ENV` gating already exists on the sampler route.  
* `DEV_SAMPLER_URL` is already an infra-owned config key for the sampler harness pattern.

What to change:

* make the canonical dev Reader start helper propagate `APP_ENV` exactly as supplied  
* make the repo-side healthcheck harness consume `DEV_SAMPLER_URL` directly  
* fail loudly when `DEV_SAMPLER_URL` is missing or empty  
* add or update repo-side tests proving the no-guess posture  
* do not hard-code or reconstruct host/port for the sampler harness in repo-side tooling  
* do not change the sampler route contract itself beyond what is strictly necessary for the repo-side wiring slice

Where to change it:

* only the smallest necessary repo-side helper, script, config, and test files under the existing dev harness surfaces

What tests or checks to run:

* `python -m pytest -q tests/scripts/test_dev_sampler_healthcheck.py`  
* `python -m pytest -q tests/adapter/test_dev_sampler_http.py`

What evidence outputs to produce:

* updated `.devcontainer/devcontainer.json`  
* updated `scripts/dev_start_reader.sh`  
* updated `scripts/qa/dev_sampler_healthcheck.py`  
* updated `tests/scripts/test_dev_sampler_healthcheck.py`  
* no new governed evidence family in this PR; the explicit live-binding evidence is produced in `OPS-01` and indexed in `PR-04`

What pass or fail result means success:

* Success means repo-side tooling no longer guesses the sampler URL, no longer silently defaults `APP_ENV`, and has test-covered direct consumption of `DEV_SAMPLER_URL`.  
* Failure means any repo-side step still reconstructs host/port, silently defaults `APP_ENV`, or lacks test-covered no-guess behavior.

## PR-04 — Epic029 acceptance, close-pack, and closure-artifact binding

### Intent (what must be true after PR)

After this PR, the epic029 offline acceptance and close-pack surfaces exist at their canonical paths, bind the outputs from PR-01 through PR-03 plus OPS-01 and epic-close Live QA, and explicitly close the two planning-audit blockers by recording one explicit conjunction JSON surface inventory artifact and one explicit harness-binding coverage disposition artifact. Human Index, hash sentinel, Machine Mirror, topology orientation demo, and path-proof companions are refreshed coherently in the same PR.

### IG source items (exact IG labels)

* `Tokens and Evidence (Acceptance)`  
* `QA Rails — Open/Close (Final PR)`  
* `Deliverable D1 — Global discipline`  
* `Deliverable D2 — Writer Surfaces (API)`  
* `Deliverable D3 — Dev HTTP Harness`

### Caveats applied (CAV-001 style IDs; None if not applicable)

None

### PF09 task IDs (exact \+ proof excerpts from PF09)

* `HDE-CONJ009`

`## Task HDE-CONJ009 — Global discipline (canonical JSON & Index updates)` `**Task ID:** HDE-CONJ009`

* `HDE-CONJ008`

`## Task HDE-CONJ008 — Writer Surfaces (API)` `**Task ID:** HDE-CONJ008`

* `HDE-CONJ001`

`## Task HDE-CONJ001 — Dev HTTP Harness (single home)` `**Task ID:** HDE-CONJ001`

### PF09 subtask IDs (exact \+ proof excerpts from PF09)

* `HDE-CONJ009.1`

`### Subtask HDE-CONJ009.1 — Canonical JSON invariants (all surfaces)` `Enforce canonical JSON invariants (encoding, key order, compactness, LF, set ordering) for all surfaces that emit JSON, using the single shared emitter.`

* `HDE-CONJ008.1`

`### Subtask HDE-CONJ008.1 — Writer envelope & posture` `Writers: \`Cache-Control: no-store`, never 304.`

* `HDE-CONJ001.4`

`### **Subtask HDE-CONJ001.4 — Dev/internal HTTP harness infra wiring**` `If infra has not yet provided a validated \`DEV\_SAMPLER\_URL `for a given environment, this subtask remains **Not done** for that environment and the sampler HTTP harness is not considered ready for Live QA in that environment.`

### PF09 completion role (Complete in this epic | Contributes evidence only | Already implemented and reused | Blocked on ADR)

Complete in this epic

### PF14 pointers (anchors \+ proof excerpts from PF14)

* `PF14 — HDE Mechanics Guide, §8.2 Policy — Emitter & serializer`

`## **8.2 Policy — Emitter & serializer**` `Single emitter (byte-authoritative). Reader and CLI public bytes MUST be emitted via the same presenter–emitter entrypoint symbol.`

* `PF14 — HDE Mechanics Guide, §10.6.1 Conjunction writer evidence family (dev harness only)`

`### **10.6.1 Conjunction writer evidence family (dev harness only)**` `Any byte change to this family MUST refresh the corresponding Human Index, Machine Mirror, checksum, and path-proof companions in the same PR.`

* `PF14 — HDE Mechanics Guide, §5.8 Dev sampler HTTP harness (internal/dev-only)`

`## **5.8 Dev sampler HTTP harness (internal/dev-only)**` `Environment gating (dev/admin only). The dev sampler HTTP harness is enabled only when APP_ENV is explicitly one of:`

* `PF14 — HDE Mechanics Guide, §24.2 Production posture (Reader / Compat)`

`## **24.2 Production posture (Reader / Compat)**` `Writers & errors. Cache-Control: no-store; no ETag. Errors must include Content-Type: application/json; charset=utf-8.`

### Discovery (Codex read-only check first): what to inspect and what must be confirmed found versus missing

Inspect first:

* `docs/acceptance_map_epic027.json`  
* `docs/acceptance_map_epic028.json`  
* `audit/qa/hde-epic027/token_evidence_matrix.md`  
* `audit/qa/hde-epic028/token_evidence_matrix.md`  
* `audit/qa/hde-epic027/acceptance_map_viability.log`  
* `audit/qa/hde-epic028/acceptance_map_viability.log`  
* `audit/EPIC-027_close_report.md`  
* `audit/EPIC-027_MANIFEST.json`  
* `audit/EPIC-028_close_report.md`  
* `audit/EPIC-028_MANIFEST.json`  
* `audit/docdeltas/`  
* `audit/qa/hde-epic029/` if present  
* `docs/evidence/INDEX.json`  
* `artifacts/evidence_index.jsonl`  
* `audit/ops/hde-epic029/ops-01/` if present  
* `tools/qa/`  
* `docs/pfcanon/PF04-Canon-HDE-Governance-v2.2.6.md`

Confirm found:

* the canonical acceptance-map pattern  
* the canonical token-matrix pattern  
* the canonical acceptance-map viability pattern  
* the canonical close-pack pair pattern  
* the canonical doc-delta and drain-target ledgers  
* the canonical QA step manifest pattern  
* the current Index/Mirror and companion proof surfaces  
* the actual outputs from PR-01 through PR-03 and OPS-01

Confirm missing:

* any epic029 acceptance map, token matrix, viability log, QA step manifest, doc-delta ledgers, or close-pack pair already present  
* any explicit epic029 surface-inventory artifact  
* any explicit epic029 non-Codespaces binding-coverage disposition artifact

### **Implementation requirements (what, not how; include PF doc citations when you use PF canon to add specificity)**

* Create the canonical epic029 acceptance map at `docs/acceptance_map_epic029.json` with sibling path proof.  
* Create the canonical epic029 token/evidence matrix at `audit/qa/hde-epic029/token_evidence_matrix.md` with sibling path proof.  
* Create the canonical epic029 acceptance-map viability log at `audit/qa/hde-epic029/acceptance_map_viability.log` with sibling path proof.  
* Create the canonical epic029 QA step manifest at `audit/qa/hde-epic029/qa_step_logs_manifest.json` with sibling path proof.  
* Create the canonical epic029 close-pack pair at `audit/EPIC-029_close_report.md` and `audit/EPIC-029_MANIFEST.json`, each with sibling path proof.  
* Create the required doc-delta ledgers at `audit/docdeltas/hde-epic029_doc_deltas.md` and `audit/docdeltas/hde-epic029_drain_targets.md`. Both must explicitly indicate when empty.  
* Create one explicit conjunction JSON surface-inventory artifact at `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md` if PR-01 did not already create it; otherwise bind and index the existing artifact here.  
* Create one explicit harness-binding coverage disposition artifact at `audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md`, using the actual `OPS-01` outputs to state environment-by-environment binding closure or remaining deferral.  
* Refresh `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`, `audit/gates/topology/orientation_demo.txt`, and all affected sibling path proofs in the same PR.  
* Bind tokens to primary governed artifacts and tests, not to the path-proof transcript itself.  
* Do not introduce a second acceptance-map home, a second close-pack home, a second mirror home, or a second canonical JSON gate family.  
* Treat `TESTS_PASS_OK`, `QA_PRECOMMIT_CHECKLIST_OK`, and `QA_POSTCOMMIT_CHECKLIST_OK` as temporarily canonical for `HDE-EPIC029`. Final close artifacts may claim these exact spellings when bound to truthful governed evidence. Record drainage as follow-up only; do not treat registry-home absence as a blocker.

### Concrete anchors (small snippets: pseudocode, schema fragments, CLI examples, or exact repo anchors only when needed)

* `docs/acceptance_map_epic029.json`  
* `audit/qa/hde-epic029/token_evidence_matrix.md`  
* `audit/qa/hde-epic029/acceptance_map_viability.log`  
* `audit/qa/hde-epic029/qa_step_logs_manifest.json`  
* `audit/docdeltas/hde-epic029_doc_deltas.md`  
* `audit/docdeltas/hde-epic029_drain_targets.md`  
* `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md`  
* `audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md`  
* `audit/EPIC-029_close_report.md`  
* `audit/EPIC-029_MANIFEST.json`

  ### **Evidence outputs (paths \+ artifact names \+ filenames; governed where applicable)**

* `docs/acceptance_map_epic029.json` — will be created in this PR.  
* `docs/acceptance_map_epic029.json.path_proof.txt` — will be created in this PR.  
* `audit/qa/hde-epic029/token_evidence_matrix.md` — will be created in this PR.  
* `audit/qa/hde-epic029/token_evidence_matrix.md.path_proof.txt` — will be created in this PR.  
* `audit/qa/hde-epic029/acceptance_map_viability.log` — will be created in this PR.  
* `audit/qa/hde-epic029/acceptance_map_viability.log.path_proof.txt` — will be created in this PR.  
* `audit/qa/hde-epic029/qa_step_logs_manifest.json` — will be created or refreshed in this PR using actual epic-close QA outputs.  
* `audit/qa/hde-epic029/qa_step_logs_manifest.json.path_proof.txt` — will be created or refreshed in this PR.  
* `audit/docdeltas/hde-epic029_doc_deltas.md` — will be created in this PR.  
* `audit/docdeltas/hde-epic029_drain_targets.md` — will be created in this PR.  
* `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md` — will be created or refreshed in this PR.  
* `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md.path_proof.txt` — will be created or refreshed if indexed.  
* `audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md` — will be created in this PR.  
* `audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md.path_proof.txt` — will be created if indexed.  
* `audit/EPIC-029_close_report.md` — will be created in this PR.  
* `audit/EPIC-029_close_report.md.path_proof.txt` — will be created in this PR.  
* `audit/EPIC-029_MANIFEST.json` — will be created in this PR.  
* `audit/EPIC-029_MANIFEST.json.path_proof.txt` — will be created in this PR.  
* `audit/ops/hde-epic029/ops-01/commands.txt` — will already exist from `OPS-01` and will be bound/indexed in this PR.  
* `audit/ops/hde-epic029/ops-01/stdout.log` — will already exist from `OPS-01` and will be bound/indexed in this PR.  
* `audit/ops/hde-epic029/ops-01/stderr.log` — will already exist from `OPS-01` and will be bound/indexed in this PR.  
* `audit/ops/hde-epic029/ops-01/exit_codes.txt` — will already exist from `OPS-01` and will be bound/indexed in this PR.  
* `audit/ops/hde-epic029/ops-01/codespaces_dev_sampler_url.md` — will already exist from `OPS-01` and will be bound/indexed in this PR.  
* `audit/ops/hde-epic029/ops-01/local_dev_sampler_url.md` — will already exist from `OPS-01` and will be bound/indexed in this PR.  
* `audit/ops/hde-epic029/ops-01/binding_disposition.md` — will already exist from `OPS-01` and will be bound/indexed in this PR.  
* `audit/ops/hde-epic029/ops-01/created_files_sha256.txt` — will already exist from `OPS-01` and will be bound/indexed in this PR.  
* `docs/evidence/INDEX.json` — already exists and will be refreshed if governed bytes change.  
* `docs/evidence/INDEX.sha256` — already exists and will be refreshed if governed bytes change.  
* `artifacts/evidence_index.jsonl` — already exists and will be refreshed if governed bytes change.  
* `artifacts/evidence_index.jsonl.sha256` — already exists and will be refreshed if governed bytes change.  
* `audit/gates/topology/orientation_demo.txt` — already exists and will be refreshed if the evidence skeleton changes.  
* `audit/gates/topology/orientation_demo.txt.path_proof.txt` — already exists where indexed or will be refreshed if bytes change.  
* All affected sibling `*.path_proof.txt` files for the files above — already exist where applicable or will be created/refreshed in this PR.

### Acceptance tokens (minimal list; explicit; do not invent)

* `DOC_DELTA_PRESENT_OK`  
* `EVIDENCE_INDEX_UPDATED_OK`  
* `MACHINE_MIRROR_UPDATED_OK`  
* `EVIDENCE_INDEX_HASH_OK`  
* `ENV_RAILS_POLICY_OK`  
* `JSON_CANONICAL_CHECK_OK`

`TESTS_PASS_OK`, `QA_PRECOMMIT_CHECKLIST_OK`, and `QA_POSTCOMMIT_CHECKLIST_OK` are temporarily canonical for `HDE-EPIC029`. Final close artifacts may claim these exact spellings when bound to truthful governed evidence. Record drainage as follow-up only; do not treat registry-home absence as a blocker.

### Rails posture (closed by default; if opened, specify condition \+ evidence \+ close-back rule)

Closed by default. This PR does not itself open rails. Any earlier bounded open-rails run for writer proof generation must already have closed back before this PR binds final acceptance artifacts.

### Basic QA task (exactly one) \+ pass condition

`python tools/evidence/update_evidence_index.py --check`

Pass condition: the command exits `0` after all epic029 acceptance, close-pack, doc-delta, ops-evidence, and companion proof surfaces are refreshed, with no stale ledger or path-proof companions.

### PO inputs (only if required; names-only; no secret values)

None

### Codex Prompt (paste-ready; required)

Task: finalize epic029 acceptance and close-pack binding for `HDE-CONJ009.1`, `HDE-CONJ008.1`, and `HDE-CONJ001.4` without widening scope.

Inspect first:

* `docs/acceptance_map_epic027.json`  
* `docs/acceptance_map_epic028.json`  
* `audit/qa/hde-epic027/token_evidence_matrix.md`  
* `audit/qa/hde-epic028/token_evidence_matrix.md`  
* `audit/qa/hde-epic027/acceptance_map_viability.log`  
* `audit/qa/hde-epic028/acceptance_map_viability.log`  
* `audit/EPIC-027_close_report.md`  
* `audit/EPIC-027_MANIFEST.json`  
* `audit/EPIC-028_close_report.md`  
* `audit/EPIC-028_MANIFEST.json`  
* `audit/docdeltas/`  
* `audit/qa/hde-epic029/` if present  
* `audit/ops/hde-epic029/ops-01/` if present  
* `docs/evidence/INDEX.json`  
* `artifacts/evidence_index.jsonl`  
* `tools/qa/`  
* `docs/pfcanon/PF04-Canon-HDE-Governance-v2.2.6.md`

PF09 scope:

* `HDE-CONJ009`  
* `HDE-CONJ009.1`  
* `HDE-CONJ008`  
* `HDE-CONJ008.1`  
* `HDE-CONJ001`  
* `HDE-CONJ001.4`

PF14 anchors:

* `§8.2 Policy — Emitter & serializer`  
* `§10.6.1 Conjunction writer evidence family (dev harness only)`  
* `§5.8 Dev sampler HTTP harness (internal/dev-only)`  
* `§24.2 Production posture (Reader / Compat)`

Observed repo facts to preserve:

* the acceptance-map, token-matrix, viability-log, doc-delta, and close-pack families already exist for prior epics  
* the Human Evidence Index, Machine Evidence Mirror, and topology orientation demo already exist  
* epic029 still lacks one explicit conjunction JSON surface-inventory artifact and one explicit harness-binding coverage disposition artifact  
* the final close artifacts must not widen scope or introduce alternate homes

What to change:

* create `docs/acceptance_map_epic029.json` and its path proof  
* create `audit/qa/hde-epic029/token_evidence_matrix.md` and its path proof  
* create `audit/qa/hde-epic029/acceptance_map_viability.log` and its path proof  
* create or refresh `audit/qa/hde-epic029/qa_step_logs_manifest.json` and its path proof using actual epic-close QA outputs  
* create `audit/docdeltas/hde-epic029_doc_deltas.md`  
* create `audit/docdeltas/hde-epic029_drain_targets.md`  
* create or refresh `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md`  
* create `audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md` using the actual `OPS-01` evidence  
* create `audit/EPIC-029_close_report.md` and `audit/EPIC-029_MANIFEST.json` with sibling path proofs  
* bind the `OPS-01` evidence files into the final epic029 ledger surfaces  
* refresh Index/Mirror, orientation demo, and companion proofs in the same PR  
* do not create a second acceptance-map home, second close-pack home, second mirror home, or second canonical JSON gate family  
* treat `TESTS_PASS_OK`, `QA_PRECOMMIT_CHECKLIST_OK`, and `QA_POSTCOMMIT_CHECKLIST_OK` as temporarily canonical for `HDE-EPIC029`; final close artifacts may claim these exact spellings when bound to truthful governed evidence, and remaining drainage is follow-up only rather than a blocker

Where to change it:

* only the governed offline evidence, audit, and closure surfaces under `docs/`, `audit/`, and `artifacts/`

What tests or checks to run:

* `python tools/evidence/update_evidence_index.py`  
* `python tools/evidence/update_evidence_index.py --check`  
* `python tools/evidence/orientation_demo.py`  
* `python tools/evidence/orientation_demo.py --check`  
* `python tools/evidence/validate_evidence_paths.py`  
* `python tools/evidence/check_lf_endings.py`  
* `python ci/checks/check_mirror_schema.sh artifacts/evidence_index.jsonl`  
* the smallest existing acceptance-map or close-pack validation check already present in the repo

What evidence outputs to produce:

* `docs/acceptance_map_epic029.json`  
* `docs/acceptance_map_epic029.json.path_proof.txt`  
* `audit/qa/hde-epic029/token_evidence_matrix.md`  
* `audit/qa/hde-epic029/token_evidence_matrix.md.path_proof.txt`  
* `audit/qa/hde-epic029/acceptance_map_viability.log`  
* `audit/qa/hde-epic029/acceptance_map_viability.log.path_proof.txt`  
* `audit/qa/hde-epic029/qa_step_logs_manifest.json`  
* `audit/qa/hde-epic029/qa_step_logs_manifest.json.path_proof.txt`  
* `audit/docdeltas/hde-epic029_doc_deltas.md`  
* `audit/docdeltas/hde-epic029_drain_targets.md`  
* `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md`  
* `audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md`  
* `audit/EPIC-029_close_report.md`  
* `audit/EPIC-029_close_report.md.path_proof.txt`  
* `audit/EPIC-029_MANIFEST.json`  
* `audit/EPIC-029_MANIFEST.json.path_proof.txt`  
* refreshed `docs/evidence/INDEX.json`  
* refreshed `docs/evidence/INDEX.sha256`  
* refreshed `artifacts/evidence_index.jsonl`  
* refreshed `artifacts/evidence_index.jsonl.sha256`  
* refreshed `audit/gates/topology/orientation_demo.txt`  
* refreshed affected sibling `*.path_proof.txt` files  
* bound/indexed `audit/ops/hde-epic029/ops-01/*` evidence files

What pass or fail result means success:

* Success means all epic029 offline acceptance and close-pack surfaces exist at the canonical homes, both tracked blockers are explicitly closed by governed artifacts, Index/Mirror and orientation-demo refresh coherently, and no alternate home or scope widening has been introduced.  
* Failure means any required epic029 ledger surface is missing, either blocker remains implicit, the token roster is claimed untruthfully, or the evidence skeleton is left stale.

# Ops tasks

## OPS-01 — Validate Codespaces and local-dev sampler harness bindings and capture explicit environment evidence

### **Ops-task record (required fields)**

**Owner:** `PO`

**Facilitator:** `IA`

**Target system/service:** `Codespaces dev environment`; `local-dev environment`; `infra-owned dev Reader start helper`; `/internal/dev/sampler`

**Constraints / safety rails:** `No new public surface; internal/dev-only posture preserved; use published DEV_SAMPLER_URL only; no guessed host/port; secret-free evidence only; closed rails except for any canonized validation exception recorded in the run evidence.`

**Success criteria:** `For each intended environment, either a validated DEV_SAMPLER_URL run is evidenced, or binding_disposition.md records not-yet-closed status with reason; no environment is silently assumed closed.`

**Rollback intent:** `Revert the repo-side binding changes from PR-03 and discard invalid OPS evidence if validation shows the binding posture is incorrect.`

**Secret handling note:** `No plaintext secrets in docs or evidence; record presence-only or redacted values only.`

### Intent (what must be true after OPS task)

After this OPS task, the operator has validated the infra-owned sampler harness binding in both Codespaces and local dev, confirmed that the dev Reader start helper and sampler harness can be exercised without guessing, and captured the exact secret-free evidence needed for epic closure. If either environment remains unclosed, that fact is captured explicitly rather than silently assumed away.

### IG source items (exact IG labels)

* `Deliverable D3 — Dev HTTP Harness`  
* `ISSUE-HDE-EPIC029-002 — Non-Codespaces harness binding coverage`  
* `QA Rails — Open/Close (Final PR)`

### Caveats applied (CAV-001 style IDs; None if not applicable)

None

### PF09 task IDs (exact \+ proof excerpts from PF09)

* `HDE-CONJ001`

`## Task HDE-CONJ001 — Dev HTTP Harness (single home)` `**Task ID:** HDE-CONJ001`

### PF09 subtask IDs (exact \+ proof excerpts from PF09)

* `HDE-CONJ001.4`

`### **Subtask HDE-CONJ001.4 — Dev/internal HTTP harness infra wiring**` `If infra has not yet provided a validated \`DEV\_SAMPLER\_URL `for a given environment, this subtask remains **Not done** for that environment and the sampler HTTP harness is not considered ready for Live QA in that environment.`

### PF09 completion role (Complete in this epic | Contributes evidence only | Already implemented and reused | Blocked on ADR)

Contributes evidence only

### PF14 pointers (anchors \+ proof excerpts from PF14)

* `PF14 — HDE Mechanics Guide, §5.8 Dev sampler HTTP harness (internal/dev-only)`

`## **5.8 Dev sampler HTTP harness (internal/dev-only)**` `Environment gating (dev/admin only). The dev sampler HTTP harness is enabled only when APP_ENV is explicitly one of:`

### Preconditions (which PRs must already be merged; which env must exist)

* `PR-03` must already be merged  
* the Codespaces dev environment must exist  
* the local-dev environment must exist  
* the repo checkout used for the OPS task must include the merged repo-side wiring from `PR-03`

### Operator action (high-level; no secret values; include command shapes only if canonized)

* Run the infra-owned dev Reader start helper in Codespaces using an allowed `APP_ENV` and the determinism pins required by canon.  
* Issue at least one HTTP/1.1 `POST` to the effective `DEV_SAMPLER_URL` with `Content-Type: application/json; charset=utf-8` and a minimal schema-valid sampler payload.  
* Repeat the same validation in local dev using the local published binding.  
* Record the effective `DEV_SAMPLER_URL`, `APP_ENV`, `SAFE_MODE`, `ALLOW_NETWORK`, `LC_ALL`, `LANG`, and `TZ` for each run.  
* Capture one explicit environment-by-environment disposition statement that says either `closed` or `not yet closed`, with the reason.  
* Do not record secret values.

### Evidence outputs (exact governed paths \+ filenames; secret-free)

* `audit/ops/hde-epic029/ops-01/commands.txt`  
* `audit/ops/hde-epic029/ops-01/stdout.log`  
* `audit/ops/hde-epic029/ops-01/stderr.log`  
* `audit/ops/hde-epic029/ops-01/exit_codes.txt`  
* `audit/ops/hde-epic029/ops-01/codespaces_dev_sampler_url.md`  
* `audit/ops/hde-epic029/ops-01/local_dev_sampler_url.md`  
* `audit/ops/hde-epic029/ops-01/binding_disposition.md`  
* `audit/ops/hde-epic029/ops-01/created_files_sha256.txt`

### Tokens or gates impacted (minimal list; explicit)

* `ENV_RAILS_POLICY_OK`

### Evidence commit plan (which PR will add or index the evidence; enforce parity rules where canon requires them)

`PR-04` will add or refresh these OPS outputs in the repo, index them where required, refresh any affected sibling path proofs, and bind them into the epic029 acceptance surfaces and close-pack. If `binding_disposition.md` records any environment as still unclosed, `PR-04` must preserve that as an explicit deferral and must not claim `HDE-CONJ001.4` as complete without truthful disposition language.

### PO inputs (only if required; names-only; no secret values)

* Codespaces dev shell  
* local-dev shell  
* ability to run the infra-owned dev Reader start helper  
* ability to set non-secret environment variables needed for the validation run  
* ability to send a minimal HTTP/1.1 POST to the sampler harness

# PO Inputs Summary

* Codespaces dev shell  
* local-dev shell  
* ability to run the infra-owned dev Reader start helper  
* ability to set `APP_ENV`  
* ability to observe `DEV_SAMPLER_URL`  
* ability to send a minimal HTTP/1.1 `POST` to the sampler harness  
* availability of epic-close Live QA outputs so `audit/qa/hde-epic029/qa_step_logs_manifest.json` can be truthfully bound in `PR-04`

# ADRs (Canon reconciliation notes)

## ADR-001

**Type/Tag:** `TOKEN REGISTRY UPDATE NEEDED`

**Decision/Problem**

`TESTS_PASS_OK`, `QA_PRECOMMIT_CHECKLIST_OK`, and `QA_POSTCOMMIT_CHECKLIST_OK` are temporarily canonical for this epic. Final close artifacts may claim these exact spellings when they are bound to truthful governed evidence, so the remaining issue is drainage follow-up rather than claimability.

**Options**

1. Use the temporary bridge for final close artifacts and record drainage as follow-up.  
2. Delay final token claims until the registry home is drained.  
3. Invent substitutes or treat registry-home absence as a blocker.

**Recommendation**

Use option 1\. `TESTS_PASS_OK`, `QA_PRECOMMIT_CHECKLIST_OK`, and `QA_POSTCOMMIT_CHECKLIST_OK` are temporarily canonical for `HDE-EPIC029`. Final close artifacts may claim these exact spellings when bound to truthful governed evidence. Record drainage as follow-up only; do not treat registry-home absence as a blocker.

**Canon touchpoints (PF doc titles and sections)**

* `PF04 - HDE Governance`, `§2.0 Acceptance Tokens`  
* `PF19 - Glow QA Guide`, `0.3 Acceptance tokens (names-only; initial)`  
* `PF27 - Canon Plan Templates`, `A. Acceptance tokens`  
* `Epic Plan HDE-EPIC029.md`, `A. Acceptance tokens`

**Drain target (which PF doc must ultimately own the rule, for example PF04 for tokens)**

`PF04 - HDE Governance §2.0`

**Plan impact (which IG items and which PRs or OPS tasks are blocked or affected)**

Affects `Tokens and Evidence (Acceptance)` and `QA Rails — Open/Close (Final PR)` at final closeout, especially `PR-04`. It does not block PR-01, PR-02, PR-03, or OPS-01 implementation work, and remaining drainage is follow-up rather than a close blocker.

ASK OK?  
