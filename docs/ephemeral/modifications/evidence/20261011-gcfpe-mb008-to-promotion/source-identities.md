# Source identities — MB-008 ANALYZE — 2026-10-11

Measured in this session. A digest identifies bytes; it is not an approval or an install receipt.

## Repository

| Fact | Value |
|---|---|
| `main` and this branch's base | `9312add259ddcf42f98516680c3c003414949f26` (PF10 v13.5.2) |
| Parent record on `main` | `docs/ephemeral/modifications/MODIFICATION-20261010-gcfpe-candidate-skill-analysis.md`, `COMPLETE`, landed by PR #600 (squash `effb68c5`) |
| Candidate graph execution copy (parent's, carries F05 and F09) | `docs/ephemeral/modifications/evidence/20261010-gcfpe-candidate-skill-analysis/execute/candidate-graph-parts/`, 56 files, `freeze.py` `8985120e1b1751f5886edbfef67dd47e11d5f4b7249d7571223a8a51e2400a8b` |
| Candidate build (installed glow-graph-contract) | 55 nodes · 237 edges · 55 state_routes · 596,008 B · sha256 `ff296b1e740a77ee207c1223cc9bdff1f56c6c167bd4714a41ae92ef8708f18b`, validation PASS — equals the parent's X3 value |
| Selected build, `docs/graph/parts` | 55 nodes · 229 edges · 575,074 B · sha256 `ae2bd159f0ba947c2e470f96579fadfbf060f74423aa974ae1194ac16bb2484d` — the recorded proof token |
| PF10 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.2.md`, 13,583 B, sha256 `c53dac75b7a6e7b7…`; one addendum, 2.1 |

## Installed skills (`freeze.py`, per skill directory)

| Skill | Files and digest | Bound by | Role here |
|---|---|---|---|
| change-flow | `22 9a551af36e042e56a48045297ac316b4102a4eb21f31622853c8be700e223f47` | parent's supplied archive (equal); closeout-residuals install | repair baseline |
| flowmaster-validate | `31 90c15e985a0c4b78d24298fe8187e8a50576689ddfc509d09fa11187ab97fcc2` | parent's supplied archive (equal); tw1 verdicts | repair baseline |
| glow-hde-pr-development | `4 265f9170d8459fc477287c320f0bbdd8eaaf0e6ba1dd4ee513275a76a22f8f7a` | parent's supplied archive (equal) | repair baseline |
| session-relay-flowmaster | `5 c8a5b22432a44f57fb12bc508169f85aa3d0ca3298b793590c364eb9a2afc8e4` | closeout-residuals install (D22 status entry) | repair baseline (PF10 2.1) |
| amthor-workspace-governance-audit | `15 c214e8741e9c54d395cfbd1379cbc7947e6c07beee5bd03aca433dc5dda937ab` | closeout-residuals install | repair baseline (PF10 2.1, MB-003) |
| glow-graph-contract | `9 e241bb9a67c4470895fc666a25d0f97d8df7e8e2df06539de5deaf12bc46467c` | closeout-residuals install; cr1 verdicts | build, derivation, contract recipe; probable repair (F06) |
| typesafe-scoring | `3 088c77f36ae96bcb9a1bcbdd9b1b8ee58272175094b0f3208b5337a3ce4881f5` | parent's supplied archive (equal) | the installed TypeSafe scoring skill PF10 2.1 names; no change established |
| flowmaster-primary | `2 2d41da26a39de98af02ad65e0f2818732fc0930e87223cb90ef75a2dc9e977e6` | parent's supplied archive (equal) | unchanged |
| tw-flowmaster | `2 0581205ba29f195ce784ff585ca9019de5644750c9e357b06e377e91827a722c` | tw1 verdicts | suite sibling; GTWPE, outside PF10 2.1 |
| session-branch-flowmaster | `2 17b5800b35d352216eb6ea7708fa4058400f66dd7d908debbea16fa9154b3008` | no repository verdict (parent's SB-1) | suite sibling |
| glow-merged-change-attribution-lock | `10 c518ccb0076b042859de4d2e136ef682bb127b6524133d2a575d433490eaf48f` | none; the parent analysed `11 ee253cfa…` under the same advertised 1.2.0 (MB-005) | required sibling of the GCFPE validation profile (DN-E) |
| skill-creator | `18 e4fee9c98c4f3941916fd9005ea9e8bec6bc1adc1aae85380f0150febbdf6ebe` | governed packaging route | packaging |
| glow-po-reporting | `1 7e04368a63e40c99e31ede3eda9ba88cfbbb9915a48b46cdc39027da7cef68e1` | closeout-residuals install | unaffected |

Every value above that the parent also recorded reproduces unchanged.

## Notion

| Surface | ID | Read |
|---|---|---|
| GCFPE-MGMT-10 three-mode testing body (this run's contract) | `3e34590a05eb811b93d2da9b4ef8106d` | last edited 2026-09-24T11:00:24.691Z |
| GCFPE Modification Backlog | `3e54590a05eb81eb818fd0f42045167a` | last edited 2026-10-11T13:33:28.036Z, MB-008 `OPEN` |
| Candidate catalog GCFPE-20261009.1 | `3f44590a05eb8110aa69fe4189ad9abc` | last edited 2026-10-11T19:47:45.856Z |
| Membership and Release Register | `3d24590a05eb81ce942ad994cfca9fa1` | selects GCFPE-20260914.1 / 091426.1 / 55 |
| TypeSafe uses row for this run (PE40, v6) | `3f64590a05eb813b8af4c3adec853d67` | cell "Opus 5.5 at extra high", Nathan's pick "pending" |
| 56 prompt pages | `body-scan.json` | each page's `page_last_edited_at` at its read |
