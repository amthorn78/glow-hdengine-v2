# Post-deploy smoke provenance

- Base URL: https://glow-hdengine-v2-production.up.railway.app
- Started (UTC): 2026-11-26T06:15:15Z
- Ops task reference: HDE-EPIC043-WU-OPS-01-OPS-TASK-v1.0
- Harness: scripts/ops/post_deploy_smoke.py (sha256 b1e1b44943b8c995ea1d1b0eaa7de2769cbcbd20adbacb69e000066c21087cca)
- Checkout HEAD: ce27daf34877bb6df4e13d8675ddbae503c3e794
- Run result: PASS

## Deployed identity (served by GET /internal/version)

- engine_tag: hdengine@prod
- build_commit: 9479d28
- invocation_tag: INV-f2ac55d77ce9aacc
- invocation_sha256: 3f119e727a2a1f8a5332fe8f159321ea5274988e6a05633103fe0a5ae42c6e69
- emitter_sha256: c828effe645deae150593adbc90589f67141ab20fab1e719171cd8effad9bc19
- release_id: 2d5a4ec485fde5dd51004e0286fff1cb1211e4ee79fa71bc62b2a5ecd0b6c129

## Reference inputs

- artifacts/db/check_constraints.txt sha256 9add416795022732b73947e70c3ba6cd240f43415d7604302ef8690ba2b465aa
- artifacts/db/check_schema.txt sha256 239944b558d2dcf93e254a3ab36884c17408f31ee738c2fa540c26ec5cc9aa34
- artifacts/db/ddl_fingerprint.json sha256 42ab602694f691e49fc98563e9d51e955a3de0ab377b318ce1f0d60fee90647f
- artifacts/db/grants.txt sha256 02c6075a80f7f4d35ee97cb986f5564a3155d090edc56ee9568b62895be1f096
- docs/ENDPOINTS_CATALOG.json sha256 96838d412873b1a2dffa82c800562ead00b3b313d485c36bbb09cc8b8ed68a6e
- migrations/011_body_graphs_durability.sql sha256 de7a55e8beae49ce4e96810203e7a51b3502220c30490619326bb68608893f85

## C-16

The three A7 success-route proofs (success_get.txt, success_head.txt, success_304.txt) are not captured, under the Product Owner's waiver C-16. The production refusal of GET /reader is captured in their place in reader_refusal_get.txt.

## Nonclaims

- no QA verdict
- no acceptance
- no PF09 status movement
- no production A7 success-route behaviour
- no comparison of the deployed release_id with an expected value
- no path proof, Evidence Index row or Machine Mirror row
- server rails not observed
