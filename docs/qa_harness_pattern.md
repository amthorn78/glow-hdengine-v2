# QA harness pattern (non-canonical summary)

This is a repository-facing summary of the current generic harness in [tools/qa/qa_harness.py](../tools/qa/qa_harness.py), the composed evidence writer in [tools/evidence/update_evidence_index.py](../tools/evidence/update_evidence_index.py), and the reduced compatibility helper in [tools/qa/step_log_header.py](../tools/qa/step_log_header.py). PF27 — Plan Templates owns the header/outcome contract; PF12 — Schemas & Artifacts owns artifact integrity; PF04 — HDE Governance owns the optional historical-token policy. Apply PF10 — HDE Build Notes within its explicit scope. This guide does not itself create QA results, Live QA, acceptance, deployment, or closeout.

## Stable identity

Import `HarnessConfig` from `tools.qa.qa_harness` with the repository source root importable. Its first three positional fields remain `epic_id=None`, `repo_root=None`, and `step_names=()`; `crd_id` is keyword-only. Supply exactly one Epic or CRD identity. `repository_root` in the example below means the actual checkout root as a `pathlib.Path`, not a new configuration variable or another output directory.

| Mode | Supported configuration and derived paths |
| --- | --- |
| Explicit Epic | `HarnessConfig("HDE-EPIC<NNN>", repository_root)` retains `audit/qa/hde-epic<NNN>/`, `docs/acceptance_map_epic<NNN>.json`, the token matrix and viability ledger. Existing positional clients remain supported. |
| Ordinary CRD | `HarnessConfig(crd_id="HDE-CRD-0001", repo_root=repository_root)` selects `audit/qa/hde-crd-0001/`. The Epic-only `epic_number`, `acceptance_map_path`, `token_matrix_path` and `viability_ledger_path` are `None`. Ordinary records require no Epic map, token roster, matrix or viability operation. |

CRD identity uses a full-string ASCII match of `HDE-CRD-[0-9]{4,}`: at least four decimal digits, expanding after 9999. Local recording also accepts canonical IDs such as `HDE-CRD-10000`; syntax support neither allocates that change nor grants governed-publication admission. The composed writer currently admits only `HDE-CRD-0001`.

Optional `step_names` and each current `check_id` use lowercase ASCII-safe full-string identity `[a-z0-9][a-z0-9._-]*`. Unsafe paths, symlinked CRD roots/ancestors and ambiguous class selection reject. Run IDs are not current-state correctness identity. Older run-ID-era wrappers and captures remain historical; current records bind to their stable change and check IDs. Configuration construction is not check execution or evidence publication.

## Governed statuses

The status set is exactly:

- `PASS` — the actual command or approved proof action reached its decisive point, every in-scope predicate passed, and required evidence/current-state validation is trustworthy.
- `FAIL_BEHAVIOR` — trustworthy tooling exercised the behavior and contradicted an explicit in-scope predicate.
- `FAIL_TOOLING` — an attempted evaluation mechanism, parsing, collection, harness or evidence writer malfunctioned or produced untrustworthy evidence.
- `TOOLING_BLOCKED` — a mandatory prerequisite, input, authorization, script, test or selector is unavailable or unresolved, preventing behavior-decisive evaluation.
- `PARKED` — an actual authorized exclusion, supersession or deferral means the check is intentionally not attempted. Record its reason, authority, affected claim and reactivation condition; do not hide a failed attempt by parking it afterward.

Absent, empty, placeholder, stale, or unevaluated inputs never become `PASS`. Preserve causal precedence: a valid prior non-execution decision permits `PARKED`; attempted untrustworthy tooling means `FAIL_TOOLING`; otherwise an unavailable mandatory prerequisite means `TOOLING_BLOCKED`; trustworthy behavior failure means `FAIL_BEHAVIOR`; only affirmative satisfaction supports `PASS`. A native skipped test is not blindly translated into success or a governed status.

`CheckResult`, imported with `Status` from `tools.qa.qa_harness`, must describe the actual observation. Its command/provenance, exit code, reason and output must agree; no command means no invented exit code or claim of execution. A harness result is not a Live QA result unless separately authorized Live QA was actually performed, and implementation validation does not supply an independent QA verdict.

## Local recording and current records

Use the existing Python APIs in `tools.qa.qa_harness` according to their actual responsibility:

| API | Scope |
| --- | --- |
| `write_primary_log` | Writes a check's primary log; this alone does not publish the current manifest or the complete integrity graph. |
| `update_manifest` | Updates current manifest selection from a primary; this alone does not publish the complete integrity graph. |
| `record_check` | Records a local primary and manifest, returning `(log_path, manifest_path)`. |
| `record_check_family` | Records a local family and manifest, returning `(tuple_of_log_paths, manifest_path)`. Its optional final verifier participates in local exception recovery. |
| `validate_crd_check_family(config)` | Validates the current CRD primary/manifest family and returns the checked manifest relationships; it makes no domain-acceptance decision. |

For `HDE-CRD-0001`, current primaries are `audit/qa/hde-crd-0001/checks/<check_id>/primary.log` and the manifest is `audit/qa/hde-crd-0001/qa_step_logs_manifest.json`. The manifest is a flat mapping keyed by check ID. Each entry has exactly `check_id`, `status` and `log_path`; a wrapper object, v1 record or extra identity/status field is not the current format.

Each generic primary starts with the complete `pf27.step_log_header.v2` header, containing exactly these 14 fields:

| Field | Current producer meaning |
| --- | --- |
| `schema_version` | `pf27.step_log_header.v2` |
| `timestamp_utc` | Actual finalization time in the supported UTC form |
| `check_id` | Stable check identity |
| `check_name` | Check name |
| `status` | One of the five governed outcomes |
| `status_reason` | Empty for `PASS`; causal explanation for another outcome |
| `command` | Actual executed command sequence; empty only when none ran |
| `command_provenance` | Truthful source of the command, or `Not executed` with an empty command |
| `exit_code` | Actual integer after command execution; `null` if none ran; `PASS` requires `0` |
| `evidence_artifacts` | Required evidence references, including this check's own primary log |
| `captured_env` | Actual secret-safe values for the applicable canon-defined environment names |
| `pf_refs` | Owning in-document PF titles |
| `intended_tokens` | Required explicit array; ordinary tokenless use is `[]` |
| `claimed_tokens` | Required explicit array; the generic producer keeps it `[]` and never issues claims |

The generic producer does not infer claims from `PASS`, intentions or prose. If a `PASS` has intentions but no claims, its log body retains the explicit nonclaim explanation. Required empty header arrays do not authorize extra optional fields in an Index row. Do not substitute the reduced compatibility helper for this full header or add `fail_status`, `epic_id` or `crd_id` to it.

Current-family validation uses the full v2 parser and stable raw-byte reads. It checks canonical compact/sorted JSON, UTF-8 without BOM, final-LF discipline, safe lexical paths, matching manifest/primary check and status, and own-log evidence binding. Malformed/wrapped/v1/duplicate/aliased/inconsistent records, or bytes that change during capture, reject. These are structural/evidence-integrity facts, not proof that a domain predicate passed.

CRD `additional_files` in `record_check`/`record_check_family` must stay within the active QA root; foreign or unsafe targets reject before publication. Local family exception recovery includes its authorized additional files. `supersede_check_ids` changes the current manifest selection while preserving prior primary log bytes. It does not delete historical evidence or publish the Index/Mirror/proof graph. Keep optional family absence distinct from selected, present or indexed incompleteness.

## Governed CRD publication

The composed Python API is `publish_crd_check_family` from `tools.evidence.update_evidence_index`. Its signature is:

```text
publish_crd_check_family(config, results, *, captured_at_utc=None, coherence_verifier=None)
```

It returns the primary-path tuple and manifest path. The updater module must belong to `config.repo_root`; the supported governed identity is **only `HDE-CRD-0001`**. A broader syntactically valid local CRD ID is not broader writer admission. A nonempty valid `CheckResult` family and an already coherent existing evidence graph are required before this composed writer touches QA bytes. It does not silently repair another evidence family's prior incoherence.

One outer `_WriteTransaction` captures planned QA preimages, performs local recording, runs the existing canonical convergence and validates the resulting family. The optional `coherence_verifier` is read-only and runs after actual writes inside the recovery boundary. Recovery covers exceptions in the existing single-writer operation; it does not promise process-crash recovery, interprocess locking or simultaneous atomic visibility to concurrent readers. A rollback failure leaves an untrustworthy state that must be reported with the original cause, not described as successful restoration.

The canonical updater owns the primary/manifest proofs and complete Human Index, Machine Mirror, hash sentinel, orientation and self-proof relationships. Existing CRD keys are `audit.qa.hde_crd_0001.qa_step_logs_manifest` and `audit.qa.hde_crd_0001.checks.<check_id>.primary.log`. Role and physical-path metadata stay writer-controlled; optional empty Index token metadata is omitted. Only admitted listed artifacts enter this graph. There is no arbitrary additional-files or Index-metadata injection argument on the composed publisher. Preserve collision, alias, path and malformed-family rejection; do not hand-edit generated companions.

A successful local record call is not complete governed publication, and complete governed publication does not itself authorize a QA verdict, acceptance, release or closure. There is no new CRD CLI wrapper and no updater `--crd-id` flag. The existing updater `--check` mode is read-only validation. Ordinary updater write mode and other evidence generators require their actual owning task's authority; documentation verification must not run this publisher as a demonstration or create a fictional QA family.

## Pytest and viability mechanics

`run_pytest_check` uses the same interpreter for readiness and execution through `sys.executable -m pytest`. When a selected check uses pytest, follow AGENTS.md readiness: install `requirements-dev.txt` with that interpreter and confirm `python -m pytest --version` before execution. No new dependency or migration is required for this interface. Keep the existing closed-rails defaults (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`, with the applicable `APP_ENV`) and redact sensitive values; no invented environment key or CLI switch is needed.

Explicit Epic reference viability resolves exact repository paths and test selectors, rejects placeholders and unsupported shell composition, performs same-interpreter collection, verifies current input stability, and fails closed when acceptance-map and token-matrix coverage or status disagree. These are selected compatibility operations, not prerequisites for ordinary tokenless CRD recording.

Both `evaluate_acceptance_map_viability` and `generate_acceptance_map_viability` refuse CRD mode before touching Epic-only paths. Explicit legacy-family options such as `replace_legacy_family_ids` and `admit_new_check_ids` are refused for CRD recording. An empty roster is not a vacuous viability `PASS`.

An explicit Epic viability `PASS` requires an exact command or approved proof action. Publication and manifest verification occur only after evaluation; writer failure is `FAIL_TOOLING`, and consumers of that viability contract must refuse any non-`PASS` or stale/mismatched ledger. Those safeguards and existing Epic clients remain intact.

## Reduced compatibility header helper

`tools.qa.step_log_header` preserves a separate reduced interface with four hard-required fields (`check_id`, `status`, `command`, `captured_env`) and three defaultable fields (`pf_refs`, `intended_tokens`, `claimed_tokens`). It does not produce the full generic v2 header or prove that a check ran.

- `create_header` and `update_header_status` never infer claims from intentions or `PASS`. Omitted, `None` or empty new claims produce an empty list, including a `PASS`-to-`PASS` update of previously claimed data. The preserved default status is caller data, not execution proof.
- Nonempty claims require `PASS` and membership in `intended_tokens`. Token inputs accept lists of strings or the supported `None` empty default. Invalid proposals reject before caller mutation; a non-`PASS` outcome carries no claims. Explain an intended-but-unclaimed `PASS` in the log body.
- `write_header` validates and fully serializes a candidate before creating directories, truncating an existing log or applying defaults to caller state. Validation/serialization rejection preserves the existing caller/header/log body. Valid publication preserves supported extra fields and deterministic serialization. I/O errors propagate; this is not a crash-safe or header/body transaction.
- `normalize_header` and `serialize_header` preserve supplied historical status/claims and extra fields for formatting. They do not validate a new outcome, establish registry authority, prove a token predicate or re-execute historical work.

Keep examples unmistakably illustrative and away from tracked evidence. Do not seed a fictional executed `PASS` into a governed family; configuration or signature examples establish no QA outcome.

## Current client pattern

`tools/qa/epic021_qa.py` remains a current explicit Epic client of the generic harness. Its wrapper supplies stable configuration and check definitions; it must not reintroduce run-ID correctness, collapse causal status classes, synthesize a phantom PASS, or treat repository evidence as proof that Live QA ran. Preserve its acceptance-map/matrix/viability scope and historical captures; it is not a CRD CLI or a requirement to disguise a CRD as an Epic.

For either class, record actual task/plan, governing sources, tested implementation/environment, criteria, command/configuration, outcome/evidence, actor, time and limitations. Apply PF10 — HDE Build Notes §2.8: distinguish tested state, later evidence-storage commit and review-time HEAD. Assess relevant substantive changes through the existing owner; a different or unavailable SHA alone does not reset approval or require a routine equivalence certificate or rerun. Missing substantive proof still limits its claim. Local checks, governed artifact publication, CI, authorized QA verdict, role acceptance and Isis closure remain distinct.
