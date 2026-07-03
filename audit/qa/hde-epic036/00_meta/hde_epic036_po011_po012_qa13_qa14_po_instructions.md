# PO Instructions - HDE-EPIC036 - po-011 / po-012 / qa-13-governed-evidence-gates / qa-14-close-out-deliverables

## Manifest Header

### Artifact Map

- HDE-EPIC: HDE-EPIC036 / Fermentation Pass 7
- Steps: po-011 / po-012 / qa-13-governed-evidence-gates / qa-14-close-out-deliverables
- Approved QA Plan File: QA Plan HDE-EPIC036.md
- Approval Doc File: approval QA Plan HDE-EPIC036.md
- Previous Step Report File: PF10; addendum 2.8
- Repo root validated: amthorn78/glow-hdengine-v2, default branch main, current HEAD 4cc6b50ffc28f282501657f055d6a566d3e7eece, compare main...main status identical.
- PF-Canon consulted: PF10 (current) + PF05 + PF02
- Output: PO Instructions - HDE-EPIC036 - po-011 / po-012 / qa-13-governed-evidence-gates / qa-14-close-out-deliverables

## Step po-011 - PO-011

### Step intent excerpt (verbatim from Approved Plan)

> Verify that the bounded live production-like proof demonstrates the relevant route-policy behavior without overclaiming broader runtime compatibility.

### Step proof excerpt (verbatim from Approved Plan and/or Approval Doc)

> - PASS if PO-010 live proof exists and records route-policy refusal.
> - PASS if the live proof does not claim broader runtime compatibility.
> - PASS if runtime nonclaims and BodyGraph-detail insufficiency remain recorded.

## Short recap - HDE-EPIC036 / Fermentation Pass 7 - po-011

This step is an interpretive closed-rails check over the PO-010 live proof and the existing runtime-nonclaim / BodyGraph-detail proof artifacts. It is meant to confirm the bounded live proof demonstrates route-policy refusal without expanding the claim into broader runtime compatibility. It matters because HDE-EPIC036 must keep the live proof bounded to route-policy behavior and preserve the unsupported-runtime nonclaim boundary.

## Canon Revalidation Notes

- PF10 current addendum 2.8 was consulted as prior-step context only; it records po-010 as PASS after Moon Loop remediation, but it is not used as current executable proof for po-011.
- PF05 command-safety posture applies: do not issue executable instructions when the repo-resident helper command is not currently validated for the selected check.
- PF02 architecture posture applies: do not invent a replacement route, runtime surface, public transport behavior, vendor endpoint, or evidence shortcut to compensate for an unresolved QA helper locus.

## Live Repo Validation Notes

- Repo validation confirmed the repository root as amthorn78/glow-hdengine-v2 on default branch main, with current HEAD 4cc6b50ffc28f282501657f055d6a566d3e7eece.
- Repo validation confirmed audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py exists on main.
- Repo validation found that current audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py registers checks only through po-010 in its CHECKS map and does not register po-011.
- Repo validation found no check_po011 implementation in the current HDE-EPIC036 helper view.
- The Approved Plan's po-011 command depends on audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-011; current repo validation contradicts that executable helper locus for this selected step.

## Drift Inputs

- Captured from Approved Plan: check ID po-011.
- Captured from Approved Plan: audit/qa/hde-epic036/checks/po-011/primary.log.
- Captured from Approved Plan: audit/qa/hde-epic036/checks/po-011/primary.log.path_proof.txt.
- Captured from Approved Plan: audit/qa/hde-epic036/checks/po-010/live_route_policy.log.
- Captured from Approved Plan: audit/qa/hde-epic036/checks/po-010/live_route_policy.log.path_proof.txt.
- Captured from Approved Plan: artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json.
- Captured from Approved Plan: artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json.
- Captured from Approved Plan: SAFE_MODE=1, ALLOW_NETWORK=0, APP_ENV=dev, LC_ALL=C, LANG=C, TZ=UTC.
- Captured from Previous Step Report: PF10 addendum 2.8 records po-010 PASS after Moon Loop remediation; this is dependency context only and not current repo proof for po-011 execution.
- Captured from live repo validation: current HDE-EPIC036 QA helper is not currently executable for po-011.

## PO Inputs Needed

- Needed input: A current, source-grounded po-011 executable helper path or an approved rerun/update of the QA helper that restores po-011 support in audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py.
- Why it is needed: The Approved Plan command for this step depends on python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-011, but current repo validation shows the helper's CHECKS map does not include po-011; issuing the command as-is would rely on an unvalidated and currently contradicted repo-resident executable locus.
- Allowed source: Approved Plan, Approval Doc, live repo validation, or a PO-provided updated QA helper evidence state under audit/qa/hde-epic036/00_meta/.

## Step po-012 - PO-012

### Step intent excerpt (verbatim from Approved Plan)

> Verify that future work does not use this epic's evidence to claim full BodyGraph-detail compatibility unless a later proof establishes required internal data coverage.

### Step proof excerpt (verbatim from Approved Plan and/or Approval Doc)

> - PASS if future compatibility remains blocked on later internal data coverage proof.
> - PASS if this epic's evidence does not claim full BodyGraph-detail compatibility.
> - PASS if the primary log and sibling path proof exist.

## Short recap - HDE-EPIC036 / Fermentation Pass 7 - po-012

This step is a closed-rails compatibility-boundary check over the acceptance map, BodyGraph-detail proof, and runtime nonclaim artifacts. It is meant to confirm future work cannot use HDE-EPIC036 evidence to claim full BodyGraph-detail compatibility without later internal coverage proof. It matters because HDE-EPIC036 must remain a route-policy proof slice, not a full compatibility proof.

## Canon Revalidation Notes

- PF10 current addendum 2.8 was consulted as prior-step context only; it records po-010 as PASS after Moon Loop remediation, but it does not authorize skipping po-012's approved check.
- PF05 command-safety posture applies: do not issue executable instructions when the repo-resident helper command is not currently validated for the selected check.
- PF02 architecture posture applies: do not invent a replacement compatibility proof, data-coverage proof, vendor endpoint, or runtime surface to compensate for an unresolved QA helper locus.

## Live Repo Validation Notes

- Repo validation confirmed the repository root as amthorn78/glow-hdengine-v2 on default branch main, with current HEAD 4cc6b50ffc28f282501657f055d6a566d3e7eece.
- Repo validation confirmed audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py exists on main.
- Repo validation found that current audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py registers checks only through po-010 in its CHECKS map and does not register po-012.
- Repo validation found no check_po012 implementation in the current HDE-EPIC036 helper view.
- The Approved Plan's po-012 command depends on audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-012; current repo validation contradicts that executable helper locus for this selected step.

## Drift Inputs

- Captured from Approved Plan: check ID po-012.
- Captured from Approved Plan: audit/qa/hde-epic036/checks/po-012/primary.log.
- Captured from Approved Plan: audit/qa/hde-epic036/checks/po-012/primary.log.path_proof.txt.
- Captured from Approved Plan: docs/acceptance_map_epic036.json.
- Captured from Approved Plan: artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json.
- Captured from Approved Plan: artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json.
- Captured from Approved Plan: SAFE_MODE=1, ALLOW_NETWORK=0, APP_ENV=dev, LC_ALL=C, LANG=C, TZ=UTC.
- Captured from Previous Step Report: PF10 addendum 2.8 records po-010 PASS after Moon Loop remediation; this is dependency context only and not current repo proof for po-012 execution.
- Captured from live repo validation: current HDE-EPIC036 QA helper is not currently executable for po-012.

## PO Inputs Needed

- Needed input: A current, source-grounded po-012 executable helper path or an approved rerun/update of the QA helper that restores po-012 support in audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py.
- Why it is needed: The Approved Plan command for this step depends on python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-012, but current repo validation shows the helper's CHECKS map does not include po-012; issuing the command as-is would rely on an unvalidated and currently contradicted repo-resident executable locus.
- Allowed source: Approved Plan, Approval Doc, live repo validation, or a PO-provided updated QA helper evidence state under audit/qa/hde-epic036/00_meta/.

## Step qa-13-governed-evidence-gates - Governed evidence gates

### Step intent excerpt (verbatim from Approved Plan)

> Verify targeted tests, generated evidence check mode, evidence paths, canonical JSON posture, Evidence Index, Machine Mirror, hash sentinels, mirror schema, and LF gates for HDE-EPIC036.

### Step proof excerpt (verbatim from Approved Plan and/or Approval Doc)

> - PASS if targeted tests exit 0.
> - PASS if route-policy generator check mode exits 0.
> - PASS if evidence path validation exits 0.

## Short recap - HDE-EPIC036 / Fermentation Pass 7 - qa-13-governed-evidence-gates

This step is the governed evidence gate for the epic's route-policy evidence, tests, evidence paths, canonical JSON posture, Human Evidence Index, Machine Mirror, hash sentinel, schema, and LF posture. It is meant to prove the generated evidence and supporting ledgers are internally consistent without regenerating artifacts. It matters because later closeout deliverables depend on a governed evidence gate over the approved proof family.

## Canon Revalidation Notes

- PF10 current addendum 2.8 was consulted as prior-step context only; it records po-010 as PASS after Moon Loop remediation, but it does not authorize skipping qa-13.
- PF05 command-safety posture applies: do not issue executable instructions when the repo-resident helper command is not currently validated for the selected check.
- PF02 architecture posture applies: do not invent replacement evidence-index, mirror, hash, generator, or test-runner commands to compensate for an unresolved QA helper locus.

## Live Repo Validation Notes

- Repo validation confirmed the repository root as amthorn78/glow-hdengine-v2 on default branch main, with current HEAD 4cc6b50ffc28f282501657f055d6a566d3e7eece.
- Repo validation confirmed audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py exists on main.
- Repo validation found that current audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py registers checks only through po-010 in its CHECKS map and does not register qa-13-governed-evidence-gates.
- Repo validation found no check_qa13 implementation in the current HDE-EPIC036 helper view.
- The Approved Plan's qa-13-governed-evidence-gates command depends on audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py qa-13-governed-evidence-gates; current repo validation contradicts that executable helper locus for this selected step.

## Drift Inputs

- Captured from Approved Plan: check ID qa-13-governed-evidence-gates.
- Captured from Approved Plan: audit/qa/hde-epic036/checks/qa-13-governed-evidence-gates/primary.log.
- Captured from Approved Plan: audit/qa/hde-epic036/checks/qa-13-governed-evidence-gates/primary.log.path_proof.txt.
- Captured from Approved Plan: tests/bodygraph/test_bg_resolve_route_policy.py.
- Captured from Approved Plan: tests/bodygraph/test_resolver_vendor.py.
- Captured from Approved Plan: tests/cli/test_bg_resolve.py.
- Captured from Approved Plan: tests/evidence/test_hde_epic036_pr02_evidence_loop.py.
- Captured from Approved Plan: tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py.
- Captured from Approved Plan: tools/evidence/validate_evidence_paths.py.
- Captured from Approved Plan: tools/evidence/check_lf_endings.py.
- Captured from Approved Plan: tools/evidence/update_evidence_index.py.
- Captured from Approved Plan: ci/checks/check_mirror_schema.sh.
- Captured from Approved Plan: ci/checks/check_evidence_index_hash.sh.
- Captured from Approved Plan: ci/checks/check_final_lf.sh.
- Captured from Approved Plan: docs/evidence/INDEX.json.
- Captured from Approved Plan: docs/evidence/INDEX.sha256.
- Captured from Approved Plan: artifacts/evidence_index.jsonl.
- Captured from Approved Plan: artifacts/evidence_index.jsonl.sha256.
- Captured from Approved Plan: docs/acceptance_map_epic036.json.
- Captured from Approved Plan: artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json.
- Captured from Approved Plan: artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json.
- Captured from Approved Plan: artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json.
- Captured from Approved Plan: artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json.
- Captured from Approved Plan: artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json.
- Captured from Approved Plan: SAFE_MODE=1, ALLOW_NETWORK=0, APP_ENV=dev, LC_ALL=C, LANG=C, TZ=UTC.
- Captured from Previous Step Report: PF10 addendum 2.8 records po-010 PASS after Moon Loop remediation; this is dependency context only and not current repo proof for qa-13 execution.
- Captured from live repo validation: current HDE-EPIC036 QA helper is not currently executable for qa-13-governed-evidence-gates.

## PO Inputs Needed

- Needed input: A current, source-grounded qa-13-governed-evidence-gates executable helper path or an approved rerun/update of the QA helper that restores qa-13-governed-evidence-gates support in audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py.
- Why it is needed: The Approved Plan command for this step depends on python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py qa-13-governed-evidence-gates, but current repo validation shows the helper's CHECKS map does not include qa-13-governed-evidence-gates; issuing the command as-is would rely on an unvalidated and currently contradicted repo-resident executable locus.
- Allowed source: Approved Plan, Approval Doc, live repo validation, or a PO-provided updated QA helper evidence state under audit/qa/hde-epic036/00_meta/.

## Step qa-14-close-out-deliverables - Close-out deliverables

### Step intent excerpt (verbatim from Approved Plan)

> Produce the PF27-required closeout execution deliverables: QA step-log manifest, discovery artifact, and QA RCA / Doc Delta summary. This check does not perform PO closeout and does not claim epic closure.

### Step proof excerpt (verbatim from Approved Plan and/or Approval Doc)

> - PASS if the QA step-log manifest exists and lists every expected check with status, log_path, and path_proof_path.
> - PASS if the manifest path proof exists and matches the manifest path.
> - PASS if the discovery artifact exists.

## Short recap - HDE-EPIC036 / Fermentation Pass 7 - qa-14-close-out-deliverables

This step is the PF27 closeout-deliverable assembly step for the QA run. It is meant to produce the QA step-log manifest, discovery artifact, and QA RCA / Doc Delta summary while avoiding PO closeout, PF edits, branch/PR/merge actions, OPS completion, PF09 status movement, or epic closure claims. It matters because the final evidence package must be inspectable without converting QA evidence into acceptance or closeout authority.

## Canon Revalidation Notes

- PF10 current addendum 2.8 was consulted as prior-step context only; it records po-010 as PASS after Moon Loop remediation, but it does not authorize skipping qa-14.
- PF05 command-safety posture applies: do not issue executable instructions when the repo-resident helper command is not currently validated for the selected check.
- PF02 architecture posture applies: do not invent replacement manifest assembly, closeout, PF-edit, branch/PR/merge, OPS, or public/runtime commands to compensate for an unresolved QA helper locus.

## Live Repo Validation Notes

- Repo validation confirmed the repository root as amthorn78/glow-hdengine-v2 on default branch main, with current HEAD 4cc6b50ffc28f282501657f055d6a566d3e7eece.
- Repo validation confirmed audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py exists on main.
- Repo validation found that current audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py registers checks only through po-010 in its CHECKS map and does not register qa-14-close-out-deliverables.
- Repo validation found no closeout helper implementation for qa-14-close-out-deliverables in the current HDE-EPIC036 helper view.
- The Approved Plan's qa-14-close-out-deliverables command depends on audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py qa-14-close-out-deliverables; current repo validation contradicts that executable helper locus for this selected step.

## Drift Inputs

- Captured from Approved Plan: check ID qa-14-close-out-deliverables.
- Captured from Approved Plan: audit/qa/hde-epic036/checks/qa-14-close-out-deliverables/primary.log.
- Captured from Approved Plan: audit/qa/hde-epic036/checks/qa-14-close-out-deliverables/primary.log.path_proof.txt.
- Captured from Approved Plan: audit/qa/hde-epic036/qa_step_logs_manifest.json.
- Captured from Approved Plan: audit/qa/hde-epic036/qa_step_logs_manifest.json.path_proof.txt.
- Captured from Approved Plan: audit/qa/hde-epic036/00_meta/discovery_artifact.md.
- Captured from Approved Plan: audit/qa/hde-epic036/00_meta/discovery_artifact.md.path_proof.txt.
- Captured from Approved Plan: audit/qa/hde-epic036/00_meta/qa_rca_doc_delta_summary.md.
- Captured from Approved Plan: audit/qa/hde-epic036/00_meta/qa_rca_doc_delta_summary.md.path_proof.txt.
- Captured from Approved Plan: prior expected check IDs step-0b-doc-delta-capture, po-001, po-002, po-003, po-004, po-005, po-006, po-007, po-008, po-009, po-010, po-011, po-012, and qa-13-governed-evidence-gates.
- Captured from Approved Plan: SAFE_MODE=1, ALLOW_NETWORK=0, APP_ENV=dev, LC_ALL=C, LANG=C, TZ=UTC.
- Captured from Previous Step Report: PF10 addendum 2.8 records po-010 PASS after Moon Loop remediation; this is dependency context only and not current repo proof for qa-14 execution.
- Captured from live repo validation: current HDE-EPIC036 QA helper is not currently executable for qa-14-close-out-deliverables.

## PO Inputs Needed

- Needed input: A current, source-grounded qa-14-close-out-deliverables executable helper path or an approved rerun/update of the QA helper that restores qa-14-close-out-deliverables support in audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py.
- Why it is needed: The Approved Plan command for this step depends on python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py qa-14-close-out-deliverables, but current repo validation shows the helper's CHECKS map does not include qa-14-close-out-deliverables; issuing the command as-is would rely on an unvalidated and currently contradicted repo-resident executable locus.
- Allowed source: Approved Plan, Approval Doc, live repo validation, or a PO-provided updated QA helper evidence state under audit/qa/hde-epic036/00_meta/.

- Needed input: Current prior-check evidence for po-011, po-012, and qa-13-governed-evidence-gates, after those checks become executable and run.
- Why it is needed: The Approved Plan states qa-14 must run after Step-0B, PO-001 through PO-012, and qa-13-governed-evidence-gates; qa-14 must check every prior primary log and sibling path proof.
- Allowed source: Approved Plan, Deliverables Report from prior steps, or live repo validation under audit/qa/hde-epic036/checks/.