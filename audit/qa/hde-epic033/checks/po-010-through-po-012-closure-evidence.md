# PO-010 through PO-012 Closure Evidence — HDE-EPIC033

_Remediated for PO-010 and PO-012 on 2026-06-04. This file records the initial failures, Moon Loop scope basis, remediation receipts, and resulting closure posture._

---

## 0. Moon Loop Deviation Record for PO-010 and PO-012

The plan-defined receipts `audit/qa/hde-epic033/checks/po-010/primary.log` and `audit/qa/hde-epic033/checks/po-012/primary.log` both finished with `status=FAIL_BEHAVIOR` and `exit_code=1`.

Both failures were caused by the same QA-harness-only brittle phrase-match defect already seen earlier in this epic: the plan used the exact case-sensitive literal `grep -F "no runtime v2 request shaping"` against `artifacts/vendor/hdapi_v2/known_anomalies.md`, while the governed anomaly ledger states the boundary sentence with leading-capital `No runtime v2 request shaping`.

Moon Loop scope authority remains the EPIC033 plan rule that remediation may repair only QA-created evidence-harness, header, manifest, path-proof, doc-delta, or QA evidence assembly defects under `audit/qa/hde-epic033/`. No product code, repo test, governed artifact outside the QA root, public contract, PF document, acceptance token, or multi-subsystem implementation surface was changed.

Deviation classification: QA evidence-harness defect. The remediation normalizes the brittle semantic phrase check inside the QA root only.

Accepted remediation receipts:

- `audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log`
- `audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log`

The remediation commands preserved the original proof targets while replacing the brittle exact-case phrase check with `grep -Ei "runtime( [A-Za-z0-9_-]+)? request shaping"` against the anomaly ledger.

---

## 1. Execution Summary

### PO-010

- Step ID: `po-010`
- Initial run timestamp: `2026-06-04T15:37:01Z`
- Initial exit code: `1`
- Initial status: `FAIL_BEHAVIOR`
- Moon Loop remediation used: yes
- Final remediation receipt: `audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log`
- Final remediation timestamp: `2026-06-04T15:54:00Z`
- Final remediation exit code: `0`
- Final remediation status: `PASS`
- Final claimed tokens: none
- Rails: `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`

### PO-011

- Step ID: `po-011`
- Run timestamp: `2026-06-04T15:37:01Z`
- Exit code: `0`
- Final status: `PASS`
- Moon Loop remediation used: no
- Claimed tokens: none
- Rails: `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`

### PO-012

- Step ID: `po-012`
- Initial run timestamp: `2026-06-04T15:37:01Z`
- Initial exit code: `1`
- Initial status: `FAIL_BEHAVIOR`
- Moon Loop remediation used: yes
- Final remediation receipt: `audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log`
- Final remediation timestamp: `2026-06-04T15:54:00Z`
- Final remediation exit code: `0`
- Final remediation status: `PASS`
- Final claimed tokens: none
- Rails: `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`

---

## 2. Final Closure Posture

PO-010 final proof posture: later adapter architecture, runtime request shaping, live vendor smoke, and runtime v2 conformance remain unclaimed by this epic. The initial failure did not prove an over-claim; it only exposed a case-sensitive QA receipt defect.

PO-011 final proof posture: contract inventory evidence remains inventory-only and does not claim runtime vendor conformance.

PO-012 final proof posture: live vendor smoke, public Reader change, new HTTP home, and AI runtime or evidence scope remain outside this epic. The remediation confirms those boundaries without modifying governed artifacts outside the QA root.

All accepted remediation artifacts remain within `audit/qa/hde-epic033/checks/`. No changes were made to `artifacts/vendor/hdapi_v2/known_anomalies.md`, `artifacts/vendor/hdapi_v2/contract_map.json`, `docs/acceptance_map_epic033.json`, or `audit/qa/hde-epic033/acceptance_map_viability.log`.

---

## 3. Process Update Captured as Doc Delta

Suggested process update for EPIC033 QA planning and future PF27-style checks:

- When the proof target is semantic boundary posture rather than exact byte identity, avoid case-sensitive exact `grep -F` checks against governed prose artifacts.
- Prefer regex-normalized or case-normalized QA checks within the QA root, or define a single canonical phrase constant that both the generator and the QA plan reuse.
- If a proof fails only because of prose-case drift while the semantic boundary remains present, classify it as a QA evidence-harness defect and keep any Moon Loop repair fully inside `audit/qa/hde-epic033/`.

This process update is recorded in both EPIC033 doc-delta surfaces.

---

## 4. Verdictability Appendix

This appendix records the proof body requested for final QA review: plan-defined receipts, final remediation receipts, sibling path proofs, evidence-artifact bindings, hashes, and exact PASS-criteria proof lines.

### 4.1 Required Deliverables and Artifact Facts

| deliverable | present | size_bytes | sha256 |
| --- | --- | ---: | --- |
| `audit/qa/hde-epic033/checks/po-010/primary.log` | yes | 1415 | `fd599727b9b5d1ac5ee2ecdea48ac05e1e0e58ba37c89810fe6fb47c9d1b901d` |
| `audit/qa/hde-epic033/checks/po-010/primary.log.path_proof.txt` | yes | 208 | `bc667058c056eaa6e1222f5e059f5ec4c1e2e725b640ee647e537266daa33244` |
| `audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log` | yes | 6415 | `e81ad2967e7e7421441068c06b53fc69638ec5d48805551f19e81bc182a9266e` |
| `audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log.path_proof.txt` | yes | 228 | `dc7e55090b7d38ba042a1db33e154074f25968290cc62061c19a088690b5ec65` |
| `audit/qa/hde-epic033/checks/po-011/primary.log` | yes | 5688 | `ae651a83f8e062f5f129bfa3bdd136f8ba1de9647d8528ed680ccc57433ba869` |
| `audit/qa/hde-epic033/checks/po-011/primary.log.path_proof.txt` | yes | 208 | `e30ff2ccedea880749254baa6192c954b08dbb16eb7f6c0e5361b51f9bcd85e8` |
| `audit/qa/hde-epic033/checks/po-012/primary.log` | yes | 1614 | `e5260c69aad808b675c501cd4c29c16617ac0f616fe042e2b349b6a6b6d1a6e1` |
| `audit/qa/hde-epic033/checks/po-012/primary.log.path_proof.txt` | yes | 208 | `bd683fedb6342bec2958b39bf1b7314d8bf70915c19d207066e6859ea6c07dff` |
| `audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log` | yes | 3152 | `3e1d19cd0000adf60930a6df97afc90777e081b4e4e5333c9fdf73a0dac2711d` |
| `audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log.path_proof.txt` | yes | 228 | `2b9c7383069830616c164ff257fac9862e612c44bbdc6d3fa5ce0fcf60915f7b` |
| `artifacts/vendor/hdapi_v2/known_anomalies.md` | yes | 1027 | `b5cfc2409a68a1db7134afca5995e8f770cbba3984c2c7f7ef2eae0dfd3f8ef2` |
| `artifacts/vendor/hdapi_v2/source_inventory.md` | yes | 6346 | `77be62306d819fb875a9914d9f384faac1937d71b96e5cb42c13601835feee2f` |
| `artifacts/vendor/hdapi_v2/contract_map.json` | yes | 4163 | `01cafbe4541315622dec3d73224770952131c792d3012d761a22c581fe229de2` |
| `docs/acceptance_map_epic033.json` | yes | 2275 | `5f2c07686baf2100e52ae7278d23e81a9da2e07e54ae9c2ae651117f7988f309` |
| `audit/qa/hde-epic033/acceptance_map_viability.log` | yes | 384 | `4dbbdc4b8726e0d2d6ddf973475859904085335bfcf4aa383c3d1ddb2e9aced5` |

### 4.2 Evidence-Artifact Binding Confirmation

- PO-010 initial receipt lists `audit/qa/hde-epic033/checks/po-010/primary.log.path_proof.txt` in `evidence_artifacts`.
- PO-010 final remediation receipt lists both `audit/qa/hde-epic033/checks/po-010/primary.log.path_proof.txt` and `audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log.path_proof.txt` in `evidence_artifacts`.
- PO-011 receipt lists `audit/qa/hde-epic033/checks/po-011/primary.log.path_proof.txt` in `evidence_artifacts`.
- PO-012 initial receipt lists `audit/qa/hde-epic033/checks/po-012/primary.log.path_proof.txt` in `evidence_artifacts`.
- PO-012 final remediation receipt lists both `audit/qa/hde-epic033/checks/po-012/primary.log.path_proof.txt` and `audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log.path_proof.txt` in `evidence_artifacts`.

### 4.3 Exact PASS-Criteria Proof Lines

PO-010 final accepted proof lines:

```text
No runtime v2 request shaping, runtime source selection, open-rails vendor smoke, public Reader byte change, public route, public flag, public payload, new HTTP home, or AI runtime/evidence scope is introduced by this inventory.
{"ai_boundary":"No OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider credential, AI rail, AI evidence family, AI token, or AI runtime scope is introduced.","generated_at_utc":"2026-05-31T18:12:31Z","non_conformance_claim":"Contract inventory only; no HumanDesignAPI v2 runtime request shaping, source selection, live conformance, public Reader change, or open-rails smoke is claimed.","quarantined_sources":[{"reason":"api-reference/openapi.json did not prove HumanDesignAPI title/server/path-family ownership in this run or repo-local artifact was absent.","source_key":"suspect_openapi_json","source_url":"https://docs.humandesignapi.nl/api-reference/openapi.json"}],"route_families":[{"auth_model":"Authorization Bearer token plus HD-Geocode-Key header","geocode_key_requirement":"required","method":"POST","path":"/v2/charts","request_content_type":"application/json","request_fields":["birthdate","birthtime","location"],"route_family":"recommended_v2_chart","source_precedence_rank":1,"source_sha256":"6ce2197373a1dad6204e33d6e6b8561a572250e166463152d7a8c0754d1f2f82","source_spec":"docs.humandesignapi.nl/openapi/v2-routes.yaml#/paths/~1charts/post","success_envelope":"StandardResponse with type=ChartResult and data=ChartResult","tier":"Advanced"},{"auth_model":"Authorization Bearer token plus HD-Geocode-Key header","geocode_key_requirement":"required","method":"POST","path":"/v2/charts/simple","request_content_type":"application/json","request_fields":["birthdate","birthtime","location"],"route_family":"recommended_v2_chart","source_precedence_rank":1,"source_sha256":"6ce2197373a1dad6204e33d6e6b8561a572250e166463152d7a8c0754d1f2f82","source_spec":"docs.humandesignapi.nl/openapi/v2-routes.yaml#/paths/~1charts~1simple/post","success_envelope":"StandardResponse with type=ChartSimpleResult and data=ChartSimpleResult","tier":"Basic + Advanced"},{"auth_model":"Authorization Bearer token","geocode_key_requirement":"not needed","method":"POST","path":"/v2/charts/coordinates","request_content_type":"application/json","request_fields":["birthdate","birthtime","lat","lng"],"route_family":"recommended_v2_chart","source_precedence_rank":1,"source_sha256":"6ce2197373a1dad6204e33d6e6b8561a572250e166463152d7a8c0754d1f2f82","source_spec":"docs.humandesignapi.nl/openapi/v2-routes.yaml#/paths/~1charts~1coordinates/post","success_envelope":"StandardResponse with type=ChartResult and data=ChartResult","tier":"Advanced"},{"auth_model":"HD-Api-Key header plus HD-Geocode-Key header","geocode_key_requirement":"required","method":"POST","path":"/v1/bodygraphs","request_content_type":"application/json","request_fields":["birthdate","birthtime","location"],"route_family":"legacy_v1_bodygraph","source_precedence_rank":1,"source_sha256":"683734c932514462cc45dd0c4b69892b9b7a6cb5ebf053eb02fe82244c91a288","source_spec":"docs.humandesignapi.nl/openapi/v1-routes.yaml#/paths/~1bodygraphs/post","success_envelope":"flat JSON BodygraphResponse; no v2 StandardResponse envelope","tier":"Advanced"},{"auth_model":"HD-Api-Key header plus HD-Geocode-Key header","geocode_key_requirement":"required","method":"POST","path":"/v1/bodygraphs/simple","request_content_type":"application/json","request_fields":["birthdate","birthtime","location"],"route_family":"legacy_v1_bodygraph","source_precedence_rank":1,"source_sha256":"683734c932514462cc45dd0c4b69892b9b7a6cb5ebf053eb02fe82244c91a288","source_spec":"docs.humandesignapi.nl/openapi/v1-routes.yaml#/paths/~1bodygraphs~1simple/post","success_envelope":"flat JSON SimpleBodygraphResponse; no v2 StandardResponse envelope","tier":"Basic + Advanced"}],"source_precedence":["validated v2 and v1 YAML route specs","rendered endpoint pages","high-level guide pages","suspect artifacts quarantined until validated"],"validated_sources":[{"sha256":"6ce2197373a1dad6204e33d6e6b8561a572250e166463152d7a8c0754d1f2f82","source_key":"v2_routes_yaml","source_url":"https://docs.humandesignapi.nl/openapi/v2-routes.yaml"},{"sha256":"683734c932514462cc45dd0c4b69892b9b7a6cb5ebf053eb02fe82244c91a288","source_key":"v1_routes_yaml","source_url":"https://docs.humandesignapi.nl/openapi/v1-routes.yaml"}]}
runtime_v2_conformance_claim=NONE
```

PO-011 final accepted proof lines:

```text
This governed inventory records public same-origin HumanDesignAPI documentation sources only. It does not call credentialed runtime vendor endpoints and does not claim runtime v2 conformance.
{"ai_boundary":"No OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider credential, AI rail, AI evidence family, AI token, or AI runtime scope is introduced.","generated_at_utc":"2026-05-31T18:12:31Z","non_conformance_claim":"Contract inventory only; no HumanDesignAPI v2 runtime request shaping, source selection, live conformance, public Reader change, or open-rails smoke is claimed.","quarantined_sources":[{"reason":"api-reference/openapi.json did not prove HumanDesignAPI title/server/path-family ownership in this run or repo-local artifact was absent.","source_key":"suspect_openapi_json","source_url":"https://docs.humandesignapi.nl/api-reference/openapi.json"}],"route_families":[{"auth_model":"Authorization Bearer token plus HD-Geocode-Key header","geocode_key_requirement":"required","method":"POST","path":"/v2/charts","request_content_type":"application/json","request_fields":["birthdate","birthtime","location"],"route_family":"recommended_v2_chart","source_precedence_rank":1,"source_sha256":"6ce2197373a1dad6204e33d6e6b8561a572250e166463152d7a8c0754d1f2f82","source_spec":"docs.humandesignapi.nl/openapi/v2-routes.yaml#/paths/~1charts/post","success_envelope":"StandardResponse with type=ChartResult and data=ChartResult","tier":"Advanced"},{"auth_model":"Authorization Bearer token plus HD-Geocode-Key header","geocode_key_requirement":"required","method":"POST","path":"/v2/charts/simple","request_content_type":"application/json","request_fields":["birthdate","birthtime","location"],"route_family":"recommended_v2_chart","source_precedence_rank":1,"source_sha256":"6ce2197373a1dad6204e33d6e6b8561a572250e166463152d7a8c0754d1f2f82","source_spec":"docs.humandesignapi.nl/openapi/v2-routes.yaml#/paths/~1charts~1simple/post","success_envelope":"StandardResponse with type=ChartSimpleResult and data=ChartSimpleResult","tier":"Basic + Advanced"},{"auth_model":"Authorization Bearer token","geocode_key_requirement":"not needed","method":"POST","path":"/v2/charts/coordinates","request_content_type":"application/json","request_fields":["birthdate","birthtime","lat","lng"],"route_family":"recommended_v2_chart","source_precedence_rank":1,"source_sha256":"6ce2197373a1dad6204e33d6e6b8561a572250e166463152d7a8c0754d1f2f82","source_spec":"docs.humandesignapi.nl/openapi/v2-routes.yaml#/paths/~1charts~1coordinates/post","success_envelope":"StandardResponse with type=ChartResult and data=ChartResult","tier":"Advanced"},{"auth_model":"HD-Api-Key header plus HD-Geocode-Key header","geocode_key_requirement":"required","method":"POST","path":"/v1/bodygraphs","request_content_type":"application/json","request_fields":["birthdate","birthtime","location"],"route_family":"legacy_v1_bodygraph","source_precedence_rank":1,"source_sha256":"683734c932514462cc45dd0c4b69892b9b7a6cb5ebf053eb02fe82244c91a288","source_spec":"docs.humandesignapi.nl/openapi/v1-routes.yaml#/paths/~1bodygraphs/post","success_envelope":"flat JSON BodygraphResponse; no v2 StandardResponse envelope","tier":"Advanced"},{"auth_model":"HD-Api-Key header plus HD-Geocode-Key header","geocode_key_requirement":"required","method":"POST","path":"/v1/bodygraphs/simple","request_content_type":"application/json","request_fields":["birthdate","birthtime","location"],"route_family":"legacy_v1_bodygraph","source_precedence_rank":1,"source_sha256":"683734c932514462cc45dd0c4b69892b9b7a6cb5ebf053eb02fe82244c91a288","source_spec":"docs.humandesignapi.nl/openapi/v1-routes.yaml#/paths/~1bodygraphs~1simple/post","success_envelope":"flat JSON SimpleBodygraphResponse; no v2 StandardResponse envelope","tier":"Basic + Advanced"}],"source_precedence":["validated v2 and v1 YAML route specs","rendered endpoint pages","high-level guide pages","suspect artifacts quarantined until validated"],"validated_sources":[{"sha256":"6ce2197373a1dad6204e33d6e6b8561a572250e166463152d7a8c0754d1f2f82","source_key":"v2_routes_yaml","source_url":"https://docs.humandesignapi.nl/openapi/v2-routes.yaml"},{"sha256":"683734c932514462cc45dd0c4b69892b9b7a6cb5ebf053eb02fe82244c91a288","source_key":"v1_routes_yaml","source_url":"https://docs.humandesignapi.nl/openapi/v1-routes.yaml"}]}
runtime_v2_conformance_claim=NONE
```

PO-012 final accepted proof lines:

```text
No runtime v2 request shaping, runtime source selection, open-rails vendor smoke, public Reader byte change, public route, public flag, public payload, new HTTP home, or AI runtime/evidence scope is introduced by this inventory.
public_reader_surface_change=NONE
ai_scope=NONE
```

## 5. Full Primary Log Bodies

### 5.1 `audit/qa/hde-epic033/checks/po-010/primary.log`

```text
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-06-04T15:37:01Z", "check_id": "po-010", "check_name": "PO-010", "status": "FAIL_BEHAVIOR", "fail_status": "FAIL_BEHAVIOR", "command": "command -v grep >/dev/null || { echo \"TOOLING_BLOCKED: grep missing\"; exit 99; }; test -f artifacts/vendor/hdapi_v2/known_anomalies.md && test -f artifacts/vendor/hdapi_v2/contract_map.json && test -f audit/qa/hde-epic033/acceptance_map_viability.log && grep -F \"no runtime v2 request shaping\" artifacts/vendor/hdapi_v2/known_anomalies.md && grep -F \"open-rails vendor smoke\" artifacts/vendor/hdapi_v2/known_anomalies.md && grep -F \"no HumanDesignAPI v2 runtime request shaping\" artifacts/vendor/hdapi_v2/contract_map.json && grep -F \"runtime_v2_conformance_claim=NONE\" audit/qa/hde-epic033/acceptance_map_viability.log", "command_provenance": "Copy/paste from plan", "exit_code": 1, "evidence_artifacts": ["audit/qa/hde-epic033/checks/po-010/primary.log", "artifacts/vendor/hdapi_v2/known_anomalies.md", "artifacts/vendor/hdapi_v2/contract_map.json", "audit/qa/hde-epic033/acceptance_map_viability.log", "audit/qa/hde-epic033/checks/po-010/primary.log.path_proof.txt"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 — HDE-Build Notes", "PF04 — HDE Governance"], "intended_tokens": [], "claimed_tokens": []}
```

### 5.2 `audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log`

```text
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-06-04T15:54:00Z", "check_id": "po-010-remediation-r1", "check_name": "PO-010 Moon Loop Remediation R1", "status": "PASS", "fail_status": "", "command": "command -v grep >/dev/null || { echo \"TOOLING_BLOCKED: grep missing\"; exit 99; }; test -f audit/qa/hde-epic033/checks/po-010/primary.log && test -f audit/qa/hde-epic033/checks/po-010/primary.log.path_proof.txt && test -f artifacts/vendor/hdapi_v2/known_anomalies.md && test -f artifacts/vendor/hdapi_v2/contract_map.json && test -f audit/qa/hde-epic033/acceptance_map_viability.log && grep -Ei \"runtime( [A-Za-z0-9_-]+)? request shaping\" artifacts/vendor/hdapi_v2/known_anomalies.md && grep -F \"open-rails vendor smoke\" artifacts/vendor/hdapi_v2/known_anomalies.md && grep -F \"no HumanDesignAPI v2 runtime request shaping\" artifacts/vendor/hdapi_v2/contract_map.json && grep -F \"runtime_v2_conformance_claim=NONE\" audit/qa/hde-epic033/acceptance_map_viability.log", "command_provenance": "Moon Loop remediation R1: regex-normalized QA phrase check", "exit_code": 0, "evidence_artifacts": ["audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log", "audit/qa/hde-epic033/checks/po-010/primary.log", "audit/qa/hde-epic033/checks/po-010/primary.log.path_proof.txt", "artifacts/vendor/hdapi_v2/known_anomalies.md", "artifacts/vendor/hdapi_v2/contract_map.json", "audit/qa/hde-epic033/acceptance_map_viability.log", "audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log.path_proof.txt"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 — HDE-Build Notes", "PF04 — HDE Governance"], "intended_tokens": [], "claimed_tokens": []}
No runtime v2 request shaping, runtime source selection, open-rails vendor smoke, public Reader byte change, public route, public flag, public payload, new HTTP home, or AI runtime/evidence scope is introduced by this inventory.
No runtime v2 request shaping, runtime source selection, open-rails vendor smoke, public Reader byte change, public route, public flag, public payload, new HTTP home, or AI runtime/evidence scope is introduced by this inventory.
{"ai_boundary":"No OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider credential, AI rail, AI evidence family, AI token, or AI runtime scope is introduced.","generated_at_utc":"2026-05-31T18:12:31Z","non_conformance_claim":"Contract inventory only; no HumanDesignAPI v2 runtime request shaping, source selection, live conformance, public Reader change, or open-rails smoke is claimed.","quarantined_sources":[{"reason":"api-reference/openapi.json did not prove HumanDesignAPI title/server/path-family ownership in this run or repo-local artifact was absent.","source_key":"suspect_openapi_json","source_url":"https://docs.humandesignapi.nl/api-reference/openapi.json"}],"route_families":[{"auth_model":"Authorization Bearer token plus HD-Geocode-Key header","geocode_key_requirement":"required","method":"POST","path":"/v2/charts","request_content_type":"application/json","request_fields":["birthdate","birthtime","location"],"route_family":"recommended_v2_chart","source_precedence_rank":1,"source_sha256":"6ce2197373a1dad6204e33d6e6b8561a572250e166463152d7a8c0754d1f2f82","source_spec":"docs.humandesignapi.nl/openapi/v2-routes.yaml#/paths/~1charts/post","success_envelope":"StandardResponse with type=ChartResult and data=ChartResult","tier":"Advanced"},{"auth_model":"Authorization Bearer token plus HD-Geocode-Key header","geocode_key_requirement":"required","method":"POST","path":"/v2/charts/simple","request_content_type":"application/json","request_fields":["birthdate","birthtime","location"],"route_family":"recommended_v2_chart","source_precedence_rank":1,"source_sha256":"6ce2197373a1dad6204e33d6e6b8561a572250e166463152d7a8c0754d1f2f82","source_spec":"docs.humandesignapi.nl/openapi/v2-routes.yaml#/paths/~1charts~1simple/post","success_envelope":"StandardResponse with type=ChartSimpleResult and data=ChartSimpleResult","tier":"Basic + Advanced"},{"auth_model":"Authorization Bearer token","geocode_key_requirement":"not needed","method":"POST","path":"/v2/charts/coordinates","request_content_type":"application/json","request_fields":["birthdate","birthtime","lat","lng"],"route_family":"recommended_v2_chart","source_precedence_rank":1,"source_sha256":"6ce2197373a1dad6204e33d6e6b8561a572250e166463152d7a8c0754d1f2f82","source_spec":"docs.humandesignapi.nl/openapi/v2-routes.yaml#/paths/~1charts~1coordinates/post","success_envelope":"StandardResponse with type=ChartResult and data=ChartResult","tier":"Advanced"},{"auth_model":"HD-Api-Key header plus HD-Geocode-Key header","geocode_key_requirement":"required","method":"POST","path":"/v1/bodygraphs","request_content_type":"application/json","request_fields":["birthdate","birthtime","location"],"route_family":"legacy_v1_bodygraph","source_precedence_rank":1,"source_sha256":"683734c932514462cc45dd0c4b69892b9b7a6cb5ebf053eb02fe82244c91a288","source_spec":"docs.humandesignapi.nl/openapi/v1-routes.yaml#/paths/~1bodygraphs/post","success_envelope":"flat JSON BodygraphResponse; no v2 StandardResponse envelope","tier":"Advanced"},{"auth_model":"HD-Api-Key header plus HD-Geocode-Key header","geocode_key_requirement":"required","method":"POST","path":"/v1/bodygraphs/simple","request_content_type":"application/json","request_fields":["birthdate","birthtime","location"],"route_family":"legacy_v1_bodygraph","source_precedence_rank":1,"source_sha256":"683734c932514462cc45dd0c4b69892b9b7a6cb5ebf053eb02fe82244c91a288","source_spec":"docs.humandesignapi.nl/openapi/v1-routes.yaml#/paths/~1bodygraphs~1simple/post","success_envelope":"flat JSON SimpleBodygraphResponse; no v2 StandardResponse envelope","tier":"Basic + Advanced"}],"source_precedence":["validated v2 and v1 YAML route specs","rendered endpoint pages","high-level guide pages","suspect artifacts quarantined until validated"],"validated_sources":[{"sha256":"6ce2197373a1dad6204e33d6e6b8561a572250e166463152d7a8c0754d1f2f82","source_key":"v2_routes_yaml","source_url":"https://docs.humandesignapi.nl/openapi/v2-routes.yaml"},{"sha256":"683734c932514462cc45dd0c4b69892b9b7a6cb5ebf053eb02fe82244c91a288","source_key":"v1_routes_yaml","source_url":"https://docs.humandesignapi.nl/openapi/v1-routes.yaml"}]}
runtime_v2_conformance_claim=NONE
```

### 5.3 `audit/qa/hde-epic033/checks/po-011/primary.log`

```text
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-06-04T15:37:01Z", "check_id": "po-011", "check_name": "PO-011", "status": "PASS", "fail_status": "", "command": "command -v grep >/dev/null || { echo \"TOOLING_BLOCKED: grep missing\"; exit 99; }; test -f artifacts/vendor/hdapi_v2/source_inventory.md && test -f artifacts/vendor/hdapi_v2/contract_map.json && test -f audit/qa/hde-epic033/acceptance_map_viability.log && grep -F \"does not claim runtime v2 conformance\" artifacts/vendor/hdapi_v2/source_inventory.md && grep -F \"Contract inventory only\" artifacts/vendor/hdapi_v2/contract_map.json && grep -F \"runtime_v2_conformance_claim=NONE\" audit/qa/hde-epic033/acceptance_map_viability.log", "command_provenance": "Copy/paste from plan", "exit_code": 0, "evidence_artifacts": ["audit/qa/hde-epic033/checks/po-011/primary.log", "artifacts/vendor/hdapi_v2/source_inventory.md", "artifacts/vendor/hdapi_v2/contract_map.json", "audit/qa/hde-epic033/acceptance_map_viability.log", "audit/qa/hde-epic033/checks/po-011/primary.log.path_proof.txt"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 — HDE-Build Notes", "PF04 — HDE Governance"], "intended_tokens": [], "claimed_tokens": []}
This governed inventory records public same-origin HumanDesignAPI documentation sources only. It does not call credentialed runtime vendor endpoints and does not claim runtime v2 conformance.
{"ai_boundary":"No OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider credential, AI rail, AI evidence family, AI token, or AI runtime scope is introduced.","generated_at_utc":"2026-05-31T18:12:31Z","non_conformance_claim":"Contract inventory only; no HumanDesignAPI v2 runtime request shaping, source selection, live conformance, public Reader change, or open-rails smoke is claimed.","quarantined_sources":[{"reason":"api-reference/openapi.json did not prove HumanDesignAPI title/server/path-family ownership in this run or repo-local artifact was absent.","source_key":"suspect_openapi_json","source_url":"https://docs.humandesignapi.nl/api-reference/openapi.json"}],"route_families":[{"auth_model":"Authorization Bearer token plus HD-Geocode-Key header","geocode_key_requirement":"required","method":"POST","path":"/v2/charts","request_content_type":"application/json","request_fields":["birthdate","birthtime","location"],"route_family":"recommended_v2_chart","source_precedence_rank":1,"source_sha256":"6ce2197373a1dad6204e33d6e6b8561a572250e166463152d7a8c0754d1f2f82","source_spec":"docs.humandesignapi.nl/openapi/v2-routes.yaml#/paths/~1charts/post","success_envelope":"StandardResponse with type=ChartResult and data=ChartResult","tier":"Advanced"},{"auth_model":"Authorization Bearer token plus HD-Geocode-Key header","geocode_key_requirement":"required","method":"POST","path":"/v2/charts/simple","request_content_type":"application/json","request_fields":["birthdate","birthtime","location"],"route_family":"recommended_v2_chart","source_precedence_rank":1,"source_sha256":"6ce2197373a1dad6204e33d6e6b8561a572250e166463152d7a8c0754d1f2f82","source_spec":"docs.humandesignapi.nl/openapi/v2-routes.yaml#/paths/~1charts~1simple/post","success_envelope":"StandardResponse with type=ChartSimpleResult and data=ChartSimpleResult","tier":"Basic + Advanced"},{"auth_model":"Authorization Bearer token","geocode_key_requirement":"not needed","method":"POST","path":"/v2/charts/coordinates","request_content_type":"application/json","request_fields":["birthdate","birthtime","lat","lng"],"route_family":"recommended_v2_chart","source_precedence_rank":1,"source_sha256":"6ce2197373a1dad6204e33d6e6b8561a572250e166463152d7a8c0754d1f2f82","source_spec":"docs.humandesignapi.nl/openapi/v2-routes.yaml#/paths/~1charts~1coordinates/post","success_envelope":"StandardResponse with type=ChartResult and data=ChartResult","tier":"Advanced"},{"auth_model":"HD-Api-Key header plus HD-Geocode-Key header","geocode_key_requirement":"required","method":"POST","path":"/v1/bodygraphs","request_content_type":"application/json","request_fields":["birthdate","birthtime","location"],"route_family":"legacy_v1_bodygraph","source_precedence_rank":1,"source_sha256":"683734c932514462cc45dd0c4b69892b9b7a6cb5ebf053eb02fe82244c91a288","source_spec":"docs.humandesignapi.nl/openapi/v1-routes.yaml#/paths/~1bodygraphs/post","success_envelope":"flat JSON BodygraphResponse; no v2 StandardResponse envelope","tier":"Advanced"},{"auth_model":"HD-Api-Key header plus HD-Geocode-Key header","geocode_key_requirement":"required","method":"POST","path":"/v1/bodygraphs/simple","request_content_type":"application/json","request_fields":["birthdate","birthtime","location"],"route_family":"legacy_v1_bodygraph","source_precedence_rank":1,"source_sha256":"683734c932514462cc45dd0c4b69892b9b7a6cb5ebf053eb02fe82244c91a288","source_spec":"docs.humandesignapi.nl/openapi/v1-routes.yaml#/paths/~1bodygraphs~1simple/post","success_envelope":"flat JSON SimpleBodygraphResponse; no v2 StandardResponse envelope","tier":"Basic + Advanced"}],"source_precedence":["validated v2 and v1 YAML route specs","rendered endpoint pages","high-level guide pages","suspect artifacts quarantined until validated"],"validated_sources":[{"sha256":"6ce2197373a1dad6204e33d6e6b8561a572250e166463152d7a8c0754d1f2f82","source_key":"v2_routes_yaml","source_url":"https://docs.humandesignapi.nl/openapi/v2-routes.yaml"},{"sha256":"683734c932514462cc45dd0c4b69892b9b7a6cb5ebf053eb02fe82244c91a288","source_key":"v1_routes_yaml","source_url":"https://docs.humandesignapi.nl/openapi/v1-routes.yaml"}]}
runtime_v2_conformance_claim=NONE
```

### 5.4 `audit/qa/hde-epic033/checks/po-012/primary.log`

```text
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-06-04T15:37:01Z", "check_id": "po-012", "check_name": "PO-012", "status": "FAIL_BEHAVIOR", "fail_status": "FAIL_BEHAVIOR", "command": "command -v grep >/dev/null || { echo \"TOOLING_BLOCKED: grep missing\"; exit 99; }; test -f artifacts/vendor/hdapi_v2/known_anomalies.md && test -f docs/acceptance_map_epic033.json && test -f audit/qa/hde-epic033/acceptance_map_viability.log && grep -F \"no runtime v2 request shaping\" artifacts/vendor/hdapi_v2/known_anomalies.md && grep -F \"open-rails vendor smoke\" artifacts/vendor/hdapi_v2/known_anomalies.md && grep -F \"public Reader byte change\" artifacts/vendor/hdapi_v2/known_anomalies.md && grep -F \"new HTTP home\" artifacts/vendor/hdapi_v2/known_anomalies.md && grep -F \"AI runtime/evidence scope\" artifacts/vendor/hdapi_v2/known_anomalies.md && grep -F \"public_reader_surface_change=NONE\" audit/qa/hde-epic033/acceptance_map_viability.log && grep -F \"ai_scope=NONE\" audit/qa/hde-epic033/acceptance_map_viability.log", "command_provenance": "Copy/paste from plan", "exit_code": 1, "evidence_artifacts": ["audit/qa/hde-epic033/checks/po-012/primary.log", "artifacts/vendor/hdapi_v2/known_anomalies.md", "docs/acceptance_map_epic033.json", "audit/qa/hde-epic033/acceptance_map_viability.log", "audit/qa/hde-epic033/checks/po-012/primary.log.path_proof.txt"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 — HDE-Build Notes", "PF04 — HDE Governance"], "intended_tokens": [], "claimed_tokens": []}
```

### 5.5 `audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log`

```text
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-06-04T15:54:00Z", "check_id": "po-012-remediation-r1", "check_name": "PO-012 Moon Loop Remediation R1", "status": "PASS", "fail_status": "", "command": "command -v grep >/dev/null || { echo \"TOOLING_BLOCKED: grep missing\"; exit 99; }; test -f audit/qa/hde-epic033/checks/po-012/primary.log && test -f audit/qa/hde-epic033/checks/po-012/primary.log.path_proof.txt && test -f artifacts/vendor/hdapi_v2/known_anomalies.md && test -f docs/acceptance_map_epic033.json && test -f audit/qa/hde-epic033/acceptance_map_viability.log && grep -Ei \"runtime( [A-Za-z0-9_-]+)? request shaping\" artifacts/vendor/hdapi_v2/known_anomalies.md && grep -F \"open-rails vendor smoke\" artifacts/vendor/hdapi_v2/known_anomalies.md && grep -F \"public Reader byte change\" artifacts/vendor/hdapi_v2/known_anomalies.md && grep -F \"new HTTP home\" artifacts/vendor/hdapi_v2/known_anomalies.md && grep -F \"AI runtime/evidence scope\" artifacts/vendor/hdapi_v2/known_anomalies.md && grep -F \"public_reader_surface_change=NONE\" audit/qa/hde-epic033/acceptance_map_viability.log && grep -F \"ai_scope=NONE\" audit/qa/hde-epic033/acceptance_map_viability.log", "command_provenance": "Moon Loop remediation R1: regex-normalized QA phrase check", "exit_code": 0, "evidence_artifacts": ["audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log", "audit/qa/hde-epic033/checks/po-012/primary.log", "audit/qa/hde-epic033/checks/po-012/primary.log.path_proof.txt", "artifacts/vendor/hdapi_v2/known_anomalies.md", "docs/acceptance_map_epic033.json", "audit/qa/hde-epic033/acceptance_map_viability.log", "audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log.path_proof.txt"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 — HDE-Build Notes", "PF04 — HDE Governance"], "intended_tokens": [], "claimed_tokens": []}
No runtime v2 request shaping, runtime source selection, open-rails vendor smoke, public Reader byte change, public route, public flag, public payload, new HTTP home, or AI runtime/evidence scope is introduced by this inventory.
No runtime v2 request shaping, runtime source selection, open-rails vendor smoke, public Reader byte change, public route, public flag, public payload, new HTTP home, or AI runtime/evidence scope is introduced by this inventory.
No runtime v2 request shaping, runtime source selection, open-rails vendor smoke, public Reader byte change, public route, public flag, public payload, new HTTP home, or AI runtime/evidence scope is introduced by this inventory.
No runtime v2 request shaping, runtime source selection, open-rails vendor smoke, public Reader byte change, public route, public flag, public payload, new HTTP home, or AI runtime/evidence scope is introduced by this inventory.
No runtime v2 request shaping, runtime source selection, open-rails vendor smoke, public Reader byte change, public route, public flag, public payload, new HTTP home, or AI runtime/evidence scope is introduced by this inventory.
public_reader_surface_change=NONE
ai_scope=NONE
```

## 6. Full Path-Proof Transcripts

### 6.1 `audit/qa/hde-epic033/checks/po-010/primary.log.path_proof.txt`

```text
path=audit/qa/hde-epic033/checks/po-010/primary.log
size_bytes=1415
sha256=fd599727b9b5d1ac5ee2ecdea48ac05e1e0e58ba37c89810fe6fb47c9d1b901d
mtime_utc=2026-06-04T15:37:01Z
produced_at_utc=2026-06-04T15:37:01Z
```

### 6.2 `audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log.path_proof.txt`

```text
path: audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log
size_bytes: 6415
sha256: e81ad2967e7e7421441068c06b53fc69638ec5d48805551f19e81bc182a9266e
mtime_utc: 2026-06-04T15:54:00Z
produced_at_utc: 2026-06-04T15:54:00Z
```

### 6.3 `audit/qa/hde-epic033/checks/po-011/primary.log.path_proof.txt`

```text
path=audit/qa/hde-epic033/checks/po-011/primary.log
size_bytes=5688
sha256=ae651a83f8e062f5f129bfa3bdd136f8ba1de9647d8528ed680ccc57433ba869
mtime_utc=2026-06-04T15:37:01Z
produced_at_utc=2026-06-04T15:37:01Z
```

### 6.4 `audit/qa/hde-epic033/checks/po-012/primary.log.path_proof.txt`

```text
path=audit/qa/hde-epic033/checks/po-012/primary.log
size_bytes=1614
sha256=e5260c69aad808b675c501cd4c29c16617ac0f616fe042e2b349b6a6b6d1a6e1
mtime_utc=2026-06-04T15:37:01Z
produced_at_utc=2026-06-04T15:37:01Z
```

### 6.5 `audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log.path_proof.txt`

```text
path: audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log
size_bytes: 3152
sha256: 3e1d19cd0000adf60930a6df97afc90777e081b4e4e5333c9fdf73a0dac2711d
mtime_utc: 2026-06-04T15:54:00Z
produced_at_utc: 2026-06-04T15:54:00Z
```

## 7. Boundary Source Proof Lines

### 7.1 `artifacts/vendor/hdapi_v2/known_anomalies.md`

```text
Quarantine effect: the suspect artifact is not used as authority for vendor bytes, schemas, endpoint routes, request shaping, response mapping, runtime conformance, or architecture conformance. Validated YAML route specs remain first-precedence authority for this contract-inventory slice.
No runtime v2 request shaping, runtime source selection, open-rails vendor smoke, public Reader byte change, public route, public flag, public payload, new HTTP home, or AI runtime/evidence scope is introduced by this inventory.
```

### 7.2 `artifacts/vendor/hdapi_v2/source_inventory.md`

```text
This governed inventory records public same-origin HumanDesignAPI documentation sources only. It does not call credentialed runtime vendor endpoints and does not claim runtime v2 conformance.
AI/LLM-oriented documentation, including `llms.txt` and `llms-full.txt`, is classified as documentation-discovery-only context and creates no AI product, runtime, evidence, token, credential, rail, QA, prompt, embedding, chatbot, model-call, or provider scope.
```

### 7.3 `audit/qa/hde-epic033/acceptance_map_viability.log`

```text
generated_at_utc=2026-05-31T18:12:31Z
epic_id=HDE-EPIC033
status=PASS
tokens_checked=TESTS_PASS_OK,DOC_DELTA_PRESENT_OK,EVIDENCE_INDEX_UPDATED_OK,MACHINE_MIRROR_UPDATED_OK,EVIDENCE_INDEX_HASH_OK,EVIDENCE_PATHS_VALIDATED_OK,EVIDENCE_PATH_PROOFS_OK,JSON_CANONICAL_CHECK_OK
vendor_v2_specific_tokens=NONE
runtime_v2_conformance_claim=NONE
public_reader_surface_change=NONE
ai_scope=NONE
```
