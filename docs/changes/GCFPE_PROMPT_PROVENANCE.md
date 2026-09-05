# GCFPE prompt-use provenance

Version: 1.0.0. Procedural repository documentation for the GCFPE alpha establishment checklist, tasks 10–12. This file defines metadata capture, not a replacement Specification, Implementation Plan, approval, evidence index, or runtime acceptance rule.

## Prompt locators and observed records

Reusable prompt bodies identify source documents/prompts by **versionless file or page names plus verified directory paths**. They must not embed static file links, provider IDs as locator substitutes, or source-version pins. Resolve the applicable source through that directory/name at execution time, then record its actual resolved version and provider identity in the usage ledger or permitted runtime handoff metadata outside the prompt body.

The IDs, versions and source references in this schema, the synthetic fixture and observed ledgers are provenance records. They are not authoring templates for hard-coded prompt source locators. Keep recorded historical identities intact and do not copy them back into reusable prompt instructions. Likewise, links in this procedural document are navigation/reference links outside a prompt body. This distinction preserves both current-source discovery and an accurate account of what each invocation actually used.

## What is recorded

Keep one metadata ledger at `docs/changes/gcfpe/prompt-usage/<change-id>.json`, using `schemas/gcfpe_prompt_usage.v1.json`. The ledger's `usages` array contains one entry for each actual prompt invocation relevant to the change. A component may have multiple entries across planning, implementation, Ops, QA, review and closure. Each entry binds its own Specification version so an approved revision does not erase which baseline earlier work used.

| Field | Capture meaning |
|---|---|
| `schema_version`, `record_kind`, `change_id` | Metadata format, observed record versus synthetic example, and existing change identity. |
| `usage_id` | Stable identity for one actual invocation; assign a new identity for a new invocation. |
| `spec.id`, `spec.version`, `spec.source_ref` | Exact governing Specification identity/version and its observed source. This does not duplicate Specification content. |
| `component_ids`, `work_unit_id` | Actual affected component/requirement identifiers and existing planned work-unit identity, where already established. |
| `ecosystem_release` | Release whose selected prompt was used, distinct from the engine's catalog/release identity. |
| `prompt.id`, `prompt.version` | Stable prompt ID and the human version label actually read. |
| `prompt.notion_page_id`, `prompt.notion_url` | Exact selected Notion source. Prompt bodies stay in Notion. |
| `prompt.source_revision` | Provider revision, observed last-edited timestamp, or preserved Notion version reference. A mutable page URL or the word “latest” is insufficient. |
| `prompt.content_sha256` | Optional content fingerprint from the ecosystem release record or observed source. Record the hash's source/projection in the handoff when supplied. A hash is identity evidence, not an approval token. |
| `role`, `stage`, `capture_point`, `captured_at_utc` | Role and stage that used the prompt, when capture occurred, and the actual UTC capture time. |
| `actual_model` | Observed running model/effort if exposed reliably. Human header recommendation does not establish the model actually used. |
| `state` | `started`, `recorded`, or `unknown_historical`; these describe provenance only, not QA or change acceptance. |
| `result_refs` | Observed resulting artifact references, PR references and full commit SHAs as they become available. |
| `supersedes_usage_id` | Earlier invocation explicitly replaced or retried after a prompt/baseline transition; retain the earlier record. Use null otherwise. |
| `unknown_fields` | Dotted field names mapped to concrete reasons for missing facts. Never fill missing historical versions from current recommendations. |
| `binding` (optional) | Later binding of previously unestablished spec/component/work-unit fields: `bound_at_utc`, actual `source_ref`, and `resolved_fields`. Keep the original prompt capture time. |

## Capture in the actual flow

1. At role/work-unit start, locate the selected Notion prompt and required sources using their versionless names and verified directory paths, then read the actual resolved prompt version/revision. Capture these observed facts and the already-established source/change/component/work-unit identifiers in the existing permitted artifact metadata or handoff outside the prompt body. Start with `state: started` and an empty result-reference list. Do not add new Specification sections, rewrite frozen source sections, or create a parallel substantive authority.
2. Before formation establishes an exact Specification, component or work unit, use null (or an empty component list) plus its reason in `unknown_fields`. Never allocate a speculative Specification/work-unit identity to satisfy provenance. Carry this source metadata through the permitted handoff. When the real downstream source establishes those facts, the authorized repository writer may fill the previously unestablished fields, remove only their resolved unknown reasons, and add `binding` with the actual binding time, source and resolved field names. This makes earlier formation/planning uses discoverable by the later component query without pretending their spec/component IDs existed at capture time. Preserve the observed prompt identity and original capture time; a later change to an already-known approved spec/prompt baseline is a new invocation, not this binding operation.
3. After saving an output, put its actual provider reference in the subsequent existing handoff/proof. Do not require the output to contain its own not-yet-known URL or hash. Append observed artifact/PR/commit references to the usage record as they become available; keep the original captured source facts intact. Use `recorded` when the actual result reference is known. A recorded result may itself be a failure; the field does not certify success.
4. The already-authorized PR implementation or documentation writer includes the metadata ledger in the appropriate existing repository change. Read-only actors, including Implementation Audit and documentation-impact reviewers, supply the metadata in their permitted output and hand it to that writer. This procedure grants no new repository, Ops, approval, merge or publication authority.
5. Carry the ledger path and relevant usage IDs in the existing PR review and closure evidence. The reviewer checks the component mapping against the actual spec/work-unit scope, rather than relying only on a set-wide release number. Where a governing evidence generator owns an output, supply metadata through its existing supported input/handoff; do not hand-edit generated acceptance maps, manifests, close reports, indexes or path proofs. If late QA/review/closure metadata arrives after the current writer's authorized transaction has ended, retain it in that actor's permitted handoff and identify the exact pending ledger update for the next already-authorized repository/documentation writer. Do not invent a new PR, grant a read-only actor write permission, or turn this transfer into an additional closure gate; report the pending provenance gap truthfully until recorded.
6. On a new invocation or explicit version transition, append a new usage entry. Preserve prior prompt versions and source baselines; fill `supersedes_usage_id` only for a real replacement/retry relationship. Resolve a recorded metadata error visibly in the same reviewable Git history, retaining the reason and previous evidence in the existing handoff or error record. Do not silently relabel historical use.

The ordinary JSON ledger is source metadata maintained by the authorized writer. It is not a generated evidence-index or acceptance artifact. Store references and identifiers only: no executable prompt-body copy, pasted private conversation, credentials, birth payloads or unrelated personal data. Existing governance determines what may be committed to this public repository.

## Read-only validation and component lookup

The helper uses only Python's standard library. It reads the ledger and schema, makes no network calls and does not change any file:

```bash
env LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 \
  python tools/qa/gcfpe_prompt_provenance.py \
  docs/changes/gcfpe/prompt-usage/<change-id>.json
```

Use all three selectors to answer the exact component question:

```bash
python tools/qa/gcfpe_prompt_provenance.py \
  docs/changes/gcfpe/prompt-usage/<change-id>.json \
  --spec-id <exact-spec-id> --spec-version <exact-version> \
  --component-id <exact-component-id>
```

The response preserves every matching invocation, including older versions and retries. `trace_found: false` means no matching trace was found; a metadata-format PASS is not component coverage, execution proof, QA acceptance or alpha graduation. Null facts remain visible with reasons. A validated record still requires source-grounded human/agent review of its factual claims; this helper cannot prove that a model executed a prompt, that a Notion revision still exists, or that linked artifacts contain the claimed result.

## Bounded setup example

`tests/qa/fixtures/gcfpe/component_trace.example.json` is an explicitly synthetic metadata example. It maps one fictional spec component to two versions of a fictional implementation prompt and a fictional review prompt. Its Notion identities and artifact references are deliberately fixture values. No real Epic or CRD is executed, no real prompt-use evidence is invented and no model run is claimed.

```bash
python tools/qa/gcfpe_prompt_provenance.py \
  tests/qa/fixtures/gcfpe/component_trace.example.json \
  --spec-id EXAMPLE-SPEC-ONLY --spec-version example.1 \
  --component-id EXAMPLE-COMPONENT-A
python -m unittest discover -s tests/qa -p test_gcfpe_prompt_provenance.py -v
```

The setup demonstration validates metadata semantics and lookup behavior only. The system remains alpha; the Product Owner selects the real CRD test after establishment closes.

## Source routing

- [GCFPE alpha establishment checklist](https://app.notion.com/p/3d24590a05eb81059255fa60ed15ee7b).
- [Glow HDE Prompt Flow Index](https://app.notion.com/p/3cc4590a05eb8101b5ded32c12616eb6), including the selected complete ecosystem release.
- PF10 — HDE Build Notes, applicable current numbered addenda, controls Specification/IP and role/approval ownership. Repo PF-Canon is read-only except for the exact Product Owner-directed mirror operation in `AGENTS.md`.

This procedure supplements the current flow's capture contract. It neither expands workflow membership nor reactivates PF20/PF30 as runtime authorities.
