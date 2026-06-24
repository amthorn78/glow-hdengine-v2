# HDE-EPIC034 PR-04 Doc Deltas

## Scope

This current-epic doc-delta surface binds HDE-EPIC034 PR-04 to PF09.5 HDE-FERM007.4 adapter and presenter boundary evidence only.

## PF-Canon document deltas

No PF-Canon document edits are required by PR-04. The PR proves structural adapter and presenter boundary preservation using repo-governed evidence without changing PF-Canon text.

## Boundaries

- Source-selection, request-shaping, and response-envelope mapping baselines are reused rather than reimplemented.
- Adapter remains the HTTP home; no second HTTP home is introduced.
- Adapter guards are not bypassed.
- Presenter/emitter remains byte-authoritative for governed and public output paths.
- No ad-hoc serializer is introduced on governed or public output paths.
- Pure compute modules remain free of external I/O except for the sanctioned BodyGraph/vendor seam.
- No HDE-FERM007.5 deterministic shaping proof is implemented or claimed.
- No HDE-FERM008 completion or subtask completion is implemented or claimed.
- No live vendor call, HumanDesignAPI v2 runtime conformance, open-rails smoke, or vendor account/tier claim is implemented or claimed.
- No public Reader route, public flag, public payload, public response shape, public transport behavior, CLI public-output change, or new HTTP home is introduced.
- No OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider credential, AI rail, AI evidence family, or AI acceptance-token scope is introduced.

## Evidence binding

- `artifacts/vendor/hdapi_v2/source_selection.snapshot.json`
- `artifacts/vendor/hdapi_v2/request_shaping.snapshot.json`
- `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`
- `artifacts/vendor/hdapi_v2/adapter_boundary_proof.log`
- `audit/qa/hde-epic034/pr-04/boundary_check.log`
- `audit/qa/hde-epic034/00_meta/doc_deltas.md`

## Status posture

HDE-FERM007.4 is proven at the repo evidence level by this PR slice, pending final PO review. PF09.5 text remains unchanged by this PR.

## PR-06 OPS-02 smoke evidence binding

- OPS-02 repo-confirmed evidence supports PF09.5 HDE-FERM008.2 only.
- Later PF09.5 drainage may update HDE-FERM008.2 from Not done to Done, subject to PO/canon status action.
- No PF-Canon text edit is performed in PR-06.
- No HDE-FERM008 parent completion or HDE-FERM008.3/.4/.5 completion is claimed.
- Version ownership remains `HD_API_BASE_URL`; runtime route resources remain version-neutral, including `charts/coordinates`.
- V2 chart auth remains `Authorization: Bearer <redacted>`; `HD-Api-Key` is not used as v2 chart-route auth.
- No full HumanDesignAPI v2 runtime conformance, public Reader change, public route, public flag, public payload change, new HTTP home, public transport change, or AI scope is claimed.
- Primary PR-06 binding evidence: `audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log`.
- Bound OPS-02 evidence root: `audit/ops/hde-epic034/ops-02/`.
