# Per-member analysis coverage

One row records all three requested dimensions for each of 55 members. `C` means the assigned native source/graph check completed without an additional confirmed finding in that dimension; it is not runtime PASS. IDs point to findings.md. F01 is a shared supplied-controller compatibility limit across runtime role/artifact handoffs; F06 applies to absent current validation, not to every body as a separate defect. Listed remarks remain listed. Coordinator addendum rechecks supersede worker initial no-finding entries for that specific dimension.

| ID | Internal contract | Graph interface | Skill interface | Rationale / additional limits |
|---|---|---|---|---|
| CF-C-10 | C | C | C + shared F01 | Initial selection and sanitized source; no future artifact requirement. |
| CF-C-20 | C | C | C + shared F01 | Canonical Specification format from complete kickoff; no self-approval. |
| CF-C-30 | F05 | F03/F05 | F03/F05 + shared F01 | Distinct initial, assessment and delta modes; F03 continuation and F05 format. |
| CF-C-40 | C | C | C + shared F01 | Exact redlines; first delta needs assessment, not a nonexistent prior delta. |
| CF-E-10 | C | C | C + shared F01 | Epic identity/mapping retained; historical CRD registration is not a gate. |
| CF-E-20 | C | C | C + shared F01 | Initial Specification; future implementation and QA are not intake. |
| CF-E-30 | F05 | F03/F05 | F03/F05 + shared F01 | Distinct review modes; F03 continuation and F05 format. |
| CF-E-40 | C | C | C + shared F01 | Separate pending delta preserves approved base and reviewer. |
| CF-PO-10 | C | C | C + shared F01 | Actual PO selection only; missing or conflicting choice remains unresolved. |
| CL-20 | C | C | C + shared F01 | Carries closure basis and own reads; not re-closing; L06 heading. |
| CL-30 | C | C | C + shared F01 | Optional ADR candidate, no canon approval; actual receiver or terminal owner; L06. |
| CL-40 | C | C | C + shared F01 | Bounded final scan and candidate-list writer; no new-change launch; L06. |
| CL-C-10 | C | C | C + shared F01 | Isis closes with actual Canon/evidence; no Epic-only PF09 demand; L06. |
| CL-E-10 | C | C | C + shared F01 | Isis closes with actual evidence and Strategy Card; L06. |
| CL-E-20 | C | C | C + shared F01 | Optional post-closure revalidation; complete to CL-E-30; partial preserves task. |
| CL-E-30 | C | C | C + shared F01 | Independent maintenance review; ACCEPT to CL-E-40; denial to author. |
| CL-E-40 | C | C | C + shared F01 | Maintenance candidate only; manual application separate from closure; final scan next. |
| DOC-10 | C | C | C + shared F01 | Instructions only; accepted dependencies and lawful rescope author. |
| DOC-20 | C | C | C + shared F01 | Verifies merged/accepted documentation without another PR-lineage verdict. |
| ESC-10 | C | C | C + shared F01 | Actual evidence escalation to ESC-30; no invented task or direct reviewer jump. |
| ESC-25 | C | C | F08 + shared F01 | One authorized discovery task; actual pending proposal lineage; F08 package gap. |
| ESC-30 | C | C | F08 + shared F01 | Stage-existing inputs; bounded discovery/proposal; F08 package gap. |
| ESC-40 | F05 | F05 | F05/F08 + shared F01 | APPROVE_AS_CHANGED plus existing bases; F08 package gap; F05 format. |
| GCFPE-MGMT-10 | C | C | C | Reused selected member matches its old batch contract; L01 known D20/D26 redesign debt. Testing body used separately. |
| IA-10 | C | C | C + shared F01 | Audit precedes Plan; unresolved decisive questions do not become ready. |
| IA-20 | C | C | C + shared F01 | Reuses complete audit; only materially changed facts rechecked. |
| IA-30 | F05 | F03/F05 | F04/F05 + shared F01 | F03/F05; native IA-40 delta loop agrees with graph; F04 support conflict. |
| IA-40 | C | C | F04 + shared F01 | Standalone delta preserves approved Plan; F04 is support drift. |
| IA-50 | C | C | C + shared F01 | Real answer authority; partial answers retain unknowns and correct return. |
| IA-60 | C | C | C + shared F01 | Research supplies evidence, never approval; usable results seed IA-50. |
| MGR-10 | C | C | C + shared F01 | One actual ready native stage; F01 is support continuity drift. |
| OPS-10 | C | C | C + shared F01 | PF27 task authority, executable procedure and evidence; L04 transport timing. |
| OPS-20 | C | C | C + shared F01 | Six truthful execution results to OPS-30; real delegated authority; no DevOps skill. |
| OPS-30 | C | C | C + shared F01 | Stored evidence before ACCEPT; real Plan dependencies; missing proof retains owner. |
| PR-10 | C | C | C + shared F01 | Ready instruction to PR-20; lawful PR author for rescope; L03 legacy fields. |
| PR-20 | C | C | C + shared F01 | Plan awaits actual Proceed; no future PR vehicle; L03. |
| PR-30 | C | C | F05 + shared F01 | Four states; publish then separate PR-35; L02/L03; current skill format F05. |
| PR-35 | C | C | F05 + shared F01 | Six states; corrections and observed merge; one PR-40 entry; L02/L03. |
| PR-40 | C | C | C + shared F01 | Five plan-driven ACCEPT receivers; preserve pending ACCEPT; REJECT replans; attribution supplemental. |
| PR-50 | C | C | C + shared F01 | PO-only manual entry; terminal evidence; no destructive cleanup or automatic inbound. |
| QA-10 | C | C | C + shared F01 | Audit/triage/readiness; READY to Guide; objective failure to native remediation. |
| QA-100 | C | C | F02 + shared F01 | All five outcomes return QA-110; PO-chosen executor; no self-acceptance. |
| QA-110 | C | C | C + shared F01 | Canon and indexing proof; missing index uses evidence owner, not needless rerun. |
| QA-120 | C | C | C + shared F01 | Report/RCA covers complete required Plan; partial collection remains interim. |
| QA-20 | C | C | C + shared F01 | Guide with indexing instructions; no invented approval; QA-50 next. |
| QA-50 | F02 | C | F02 + shared F01 | F02 conflicting named different executor; audit/Plan sequencing otherwise preserved. |
| QA-60 | C | C | C + shared F01 | Recovery Plan authoring retains actual audit/approval; no new executor gate. |
| QA-70 | F05 | F05 | F05 + shared F01 | Initial versus delta review; F05 format; native conditional return preserved. |
| QA-80 | C | C | C + shared F01 | Pending Plan revision only; not the standalone IA-40 delta loop. |
| QA-90 | C | C | F02 + shared F01 | Finite selected set and dependencies; indexing instructions; authoring is not execution. |
| RS-10 | C | C | C + shared F01 | Optional PR-author support; independent IA decision; no invented Proceed/PR. |
| RS-20 | F05 | F05/F09 | F05 + shared F01 | Native pre-Proceed return is present, but graph lacks the PR-20 branch (F09); F05 addendum numbering conflict. |
| RS-30 | C | C | C + shared F01 | Existing proposal and actual correction produce revised artifact/report; L04 upstream timing. |
| RS-40 | C | C | F05 + shared F01 | Open-PR only, original Proceed, phase result; PR-35-only Canon block; L02. |
| UTIL-10 | C | C | C + shared F01 | Exact reviewed base and once-only redlines; no approved-base rewrite. |

No source row is omitted: 55 × 3 = 165 dimension dispositions. The three CL-E maintenance bodies were compared to native candidate parts and relevant runtime skill sections; detailed bundled row-map executable validation was not run. PE independently has F04 and F05; F05 reaches its applicable GCFPE addendum-authoring instructions without making it a seventh producer or 56th member; testing MGMT was read as the invocation source, not counted as a second member.

## Native read metadata

All dates below are the page metadata exposed by direct Notion reads on 2026-10-10. Each body was read through closing content/page wrappers in bounded slices; native unknown-block/truncated fields were not exposed. A rendered-character count is a coverage measurement, not a prompt-byte identity. Source URLs and predecessor mappings are in source-identities.md.

| ID | Last edited UTC | Rendered characters returned | Workload |
|---|---|---:|---|
| CF-C-10 | 2026-10-09T20:10:03.197Z | not separately recorded | formation |
| CF-C-20 | 2026-10-09T20:10:48.418Z | not separately recorded | formation |
| CF-C-30 | 2026-10-09T20:10:50.363Z | not separately recorded | formation |
| CF-C-40 | 2026-10-09T20:10:52.355Z | not separately recorded | formation |
| CF-E-10 | 2026-10-09T20:10:53.973Z | not separately recorded | formation |
| CF-E-20 | 2026-10-09T20:10:57.290Z | not separately recorded | formation |
| CF-E-30 | 2026-10-09T20:10:58.798Z | not separately recorded | formation |
| CF-E-40 | 2026-10-09T20:11:00.884Z | not separately recorded | formation |
| CF-PO-10 | 2026-10-09T20:11:02.449Z | not separately recorded | formation |
| CL-20 | 2026-10-09T20:11:05.162Z | 39922 | QA/closure/escalation |
| CL-30 | 2026-10-09T20:11:09.557Z | 34039 | QA/closure/escalation |
| CL-40 | 2026-10-09T20:11:12.358Z | 35508 | QA/closure/escalation |
| CL-C-10 | 2026-10-09T20:11:14.868Z | 45179 | QA/closure/escalation |
| CL-E-10 | 2026-10-09T20:11:17.445Z | 45962 | QA/closure/escalation |
| CL-E-20 | 2026-10-09T20:11:34.769Z | 19576 | QA/closure/escalation |
| CL-E-30 | 2026-10-09T20:11:36.747Z | 19392 | QA/closure/escalation |
| CL-E-40 | 2026-10-09T20:11:38.604Z | 20102 | QA/closure/escalation |
| DOC-10 | 2026-10-09T20:11:40.826Z | not separately recorded | formation |
| DOC-20 | 2026-10-09T20:11:42.869Z | not separately recorded | formation |
| ESC-10 | 2026-10-09T20:11:44.854Z | 20773 | QA/closure/escalation |
| ESC-25 | 2026-10-09T20:11:46.838Z | 22079 | QA/closure/escalation |
| ESC-30 | 2026-10-09T20:11:48.657Z | 21768 | QA/closure/escalation |
| ESC-40 | 2026-10-09T20:11:51.439Z | 23410 | QA/closure/escalation |
| GCFPE-MGMT-10 | 2026-09-24T15:38:34.295Z | not separately recorded | coordinator |
| IA-10 | 2026-10-09T20:11:54.630Z | not separately recorded | formation |
| IA-20 | 2026-10-09T20:11:57.808Z | not separately recorded | formation |
| IA-30 | 2026-10-09T20:11:59.445Z | not separately recorded | formation |
| IA-40 | 2026-10-09T20:12:01.074Z | not separately recorded | formation |
| IA-50 | 2026-10-09T20:12:02.847Z | not separately recorded | formation |
| IA-60 | 2026-10-09T20:12:04.842Z | not separately recorded | formation |
| MGR-10 | 2026-10-09T20:12:18.429Z | not separately recorded | formation |
| OPS-10 | 2026-10-09T20:12:20.059Z | 51425 | PR/rescope/Ops |
| OPS-20 | 2026-10-09T20:12:26.012Z | 44144 | PR/rescope/Ops |
| OPS-30 | 2026-10-09T20:12:28.694Z | 68456 | PR/rescope/Ops |
| PR-10 | 2026-10-09T20:12:31.713Z | 55967 | PR/rescope/Ops |
| PR-20 | 2026-10-09T20:12:34.254Z | 57947 | PR/rescope/Ops |
| PR-30 | 2026-10-09T20:12:37.057Z | 46613 | PR/rescope/Ops |
| PR-35 | 2026-10-09T20:12:39.512Z | 27365 | PR/rescope/Ops |
| PR-40 | 2026-10-09T20:12:41.788Z | 61282 | PR/rescope/Ops |
| PR-50 | 2026-10-09T20:12:44.991Z | 9796 | PR/rescope/Ops |
| QA-10 | 2026-10-09T20:12:46.643Z | 90295 | QA/closure/escalation |
| QA-100 | 2026-10-09T20:12:50.193Z | 19838 | QA/closure/escalation |
| QA-110 | 2026-10-09T20:13:14.927Z | 22091 | QA/closure/escalation |
| QA-120 | 2026-10-09T20:13:16.920Z | 21540 | QA/closure/escalation |
| QA-20 | 2026-10-09T20:13:19.327Z | 19819 | QA/closure/escalation |
| QA-50 | 2026-10-09T20:13:21.061Z | 25293 | QA/closure/escalation |
| QA-60 | 2026-10-09T20:13:23.178Z | 20847 | QA/closure/escalation |
| QA-70 | 2026-10-09T20:13:24.925Z | 22343 | QA/closure/escalation |
| QA-80 | 2026-10-09T20:13:27.062Z | 17504 | QA/closure/escalation |
| QA-90 | 2026-10-09T20:13:29.043Z | 20756 | QA/closure/escalation |
| RS-10 | 2026-10-09T20:13:30.743Z | 18436 | PR/rescope/Ops |
| RS-20 | 2026-10-09T20:13:33.913Z | 21907 | PR/rescope/Ops |
| RS-30 | 2026-10-09T20:13:35.779Z | 17263 | PR/rescope/Ops |
| RS-40 | 2026-10-09T20:13:37.596Z | 16851 | PR/rescope/Ops |
| UTIL-10 | 2026-10-09T20:13:56.908Z | not separately recorded | formation |

PE 100926.1: 2026-10-09T20:13:58.466Z, 78,253 rendered characters, complete returned text read. Testing MGMT: 2026-09-24T11:00:24.691Z, complete returned text read. The QA/closure/escalation batch measured 628,036 rendered characters for its 22 sources.

## Central refutation and scope decisions

- F05 was independently rechecked against current PF06/PF27 and native CF/IA/QA/RS/ESC producer clauses. All six form the shared correction cohort. PF10 file mutation/publication remains separate.
- Retained same-session words, predecessor identities and source_evidence historical paths were not automatically counted as operative persistent-ID requirements.
- QA-100 return is affirmed, not repaired on withdrawn AF-024 evidence. QA-80 pending-only behavior remains distinct from IA-40 standalone delta authoring.
- PE page-state front matter was not called executable governance contamination. Its IA-40 denial prohibition is a separate substantive finding.
- The absolute missing-source, current-substantive-proof and independent-acceptance boundaries remain. No new canonical writer or evidence index was created.
- F01/F06/F08 are listed compatibility limits; source workers suggested alternative severity, and coordinator applied D26 to the established consequence. No original independent verdict was edited.
