"""Write HDE-CRD-0002's T1 causal inputs (reference draft) into a repository root.

Usage: build_close_inputs.py <repo-root>

Writes audit/HDE-CRD-0002_close_candidate_source.json and the two ledgers, and applies the
RF-12 nonclaim edits to README.md, AGENTS.md and CHANGELOG.md. Scratch tool for the Isis
rehearsal; the close session re-verifies every value against the records.
"""
import json
import sys
from pathlib import Path

root = Path(sys.argv[1])
CRD = "HDE-CRD-0002"
E = "docs/ephemeral/"
Q = "audit/qa/hde-crd-0002/"

checks = [
    "qa-01-preflight", "qa-02-ci-coverage", "qa-03-attestation-debian", "qa-04-showcompat-help",
    "qa-05-aux-preview-band", "qa-06-dev-harness-retired", "qa-07-dev-reader-gate",
    "qa-08-release-evidence-tooling", "qa-09-override-matrix", "qa-10-endpoint-catalog",
    "qa-11-template-and-documents", "qa-12-security-review", "qa-13-prepush-check",
    "qa-14-close-pack-writer", "qa-15-s01-removal", "qa-16-deployed-identity",
    "qa-17-deployed-not-found", "qa-18-deployed-dev-surfaces", "qa-19-deployed-reader-input",
    "qa-20-live-vendor-override", "qa-21-evidence-admission",
]
evidence = [
    {"binding": "specification", "path": E + "HDE-CRD-0002-specification-v1.1-approved.md"},
    {"binding": "specification_delta_01", "path": E + "HDE-CRD-0002-specification-delta-v1.0.md"},
    {"binding": "plan_delta_01", "path": E + "HDE-CRD-0002-implementation-plan-delta-01-v1.1.md"},
    {"binding": "qa_plan", "path": E + "HDE-CRD-0002-QA50-qa-plan-v1.3.md"},
    {"binding": "qa_verdict", "path": E + "HDE-CRD-0002-QA120-qa-report-v1.0.md"},
    {"binding": "qa_rca_record", "path": E + "HDE-CRD-0002-QA120-qa-rca-v1.0.md"},
    {"binding": "closure_decision", "path": E + "HDE-CRD-0002-CL-C-10-closure-decision-v1.0.md"},
    {"binding": "corrective_decisions", "path": E + "HDE-CRD-0002-WU-PR-03-corrective-architecture-decisions-v1.0.md"},
    {"binding": "adr", "path": "docs/adr/hde/close_pack_writer_adr.md"},
    {"binding": "doc_deltas", "path": "audit/docdeltas/hde-crd-0002_doc_deltas.md"},
    {"binding": "drain_targets", "path": "audit/docdeltas/hde-crd-0002_drain_targets.md"},
    {"binding": "qa_manifest", "path": Q + "qa_step_logs_manifest.json"},
] + [
    {"binding": "qa_" + c[3:5], "path": Q + "checks/" + c + "/primary.log"} for c in checks
]

NONE = "None beyond the QA Report."


def row(criterion, numbers, limitation=NONE):
    return {
        "criterion_id": criterion,
        "evidence_bindings": ["qa_manifest"] + ["qa_%02d" % n for n in numbers],
        "result": "MET",
        "limitation": limitation,
    }


acceptance = [
    row("S01", [15], "Removed by Specification delta 01 (Product Owner OPTION 1, 2026-10-21). Check 15 proves the removal and its stated limit, not delivery: a regular wheel install outside a source checkout still does not admit the release."),
    row("S02", [17]),
    row("S03", [2]),
    row("S04", [2]),
    row("S05", [2]),
    row("S06", [3], "Proven under Ubuntu 26.04's patched setuptools 78.1.1, wired by a Moon Loop, not under the Plan's literal E-D construction (QA RCA v1.0, R-1)."),
    row("S07", [4]),
    row("S08", [5]),
    row("S09", [6], "Delivered by retiring the harness."),
    row("S10", [7, 18], "Delivered as an exact dev gate: test and local also refuse, as approved Plan v1.1 section 15 and corrective decision AD-2 (CR-8) read canon."),
    row("S11", [8]),
    row("S12", [8]),
    row("S13", [8]),
    row("S14", [9, 20], "Includes one bounded live vendor call, initiated by the Product Owner (check 20)."),
    row("S15", [10], "Canon-retired routes are excluded with a basis rather than removed, under corrective decision AD-1 (CR-7)."),
    row("S16", [11], "Delivered by WU-PR-08 as Implementation Plan delta 01 reduced it."),
    row("S17", [11], "Delivered by WU-PR-08 as Implementation Plan delta 01 reduced it."),
    row("S18", [11]),
    row("S19", [12, 18, 19, 20], "Findings F01 to F09 are fixed; R01 to R07 are routed to the Product Owner with reasons (FND-029, pending, non-gating)."),
    row("S20", [13], "QA110-F01, found in check 13 attempt 1, was remedied by WU-REM-02 and verified by RV-1; S20 stays in scope by Product Owner option A."),
    row("S21", [14], "Delivered as capability; this close pack is its first use on a real close."),
    row("S22", [21]),
]

allocation = [
    ("WU-PR-01", "CI coverage of every test file, fail-closed classification of unregistered tools/qa sources and the aligned documentation skip list (S03 to S05; #627, #630)."),
    ("WU-PR-02", "Evidence tooling: the release bundle builder under Debian-patched setuptools, the closure probe, engine-core currency, Mirror labels and the HDE-CRD-0002 QA-root admission (S06, S11 to S13, S22; #634, #637)."),
    ("WU-REM-01", "Evidence-lane tests and the QA harness accept the change's own QA root and close pack (FND-001 remedy; #716)."),
    ("WU-PR-03", "Public, dev and CLI surfaces: the governed not-found envelope, the showcompat help summary, the retired dev harness, the exact dev gate, the Endpoint Catalog and the document corrections (S02, S07, S09, S10, S15, S18; #643, #646)."),
    ("WU-PR-04", "The production vendor override and the Aux preview band flag for pair-file input (S08, S14; #651)."),
    ("WU-PR-05", "The code security review of the HDE-EPIC040 PR04 to PR06a code, with fixes F01 to F09 and routed items R01 to R07 (S19; #656)."),
    ("WU-PR-06", "The read-only pre-push and pre-plan check with its own test (S20; #660)."),
    ("WU-REM-02", "Pre-push check copies own their objects, remedying QA110-F01 (S20; #734)."),
    ("WU-PR-07", "The close-pack writer for Epic and CRD identities: the v2 source schema, the post-verdict close-run family and the ADR (S21; #668, #670)."),
    ("WU-PR-08", "The GEO_API_KEY template entry and the readiness and port corrections, as Implementation Plan delta 01 reduced the unit (S16, S17; #687)."),
    ("WU-DOC-01", "Final repository documentation (#692, #695, #700)."),
    ("WU-OPS-01", "The QA candidate placed on the production service and its deployment facts recorded; the Ops task is accepted."),
]

deferrals = [
    ("CLC10-01", "Pending drainage", "PO-2 (do not pin tool versions) and PO-5 (evidence persistence, Glow QA Guide 3.4.3) await Product Owner drainage."),
    ("CLC10-02", "Proposed", "QA RCA v1.0 D-1: a Plan Templates guard that excludes storage paths takes the classifier's whole prefix list; the Product Owner owns the canon decision."),
    ("CLC10-03", "Pending drainage", "This change's HDE Build Notes addenda, including CR-7, CR-10, CR-11 and the S21 ADR's affected canon homes, drain through canon maintenance; not a closure prerequisite (HDE Build Notes 2.15)."),
    ("CLC10-04", "Later change", "FND-028 of the change audit triage v1.1: removing the replay report is a later change; S20 stays in scope by Product Owner option A."),
    ("CLC10-05", "Pending, non-gating", "FND-029 (S19-R01 to R07), FND-012, X-02 and the legacy chart-loader defect (HDE-SEPA006) stay with the Product Owner."),
    ("CLC10-06", "Open documentation defect", "LR7-O1 and FND-020: the S21 ADR's line 65 clause is superseded by HDE Build Notes 2.17 resolution A; the ADR is revised on Product Owner instruction."),
    ("CLC10-07", "Candidate", "Documentation and canon delta candidates FND-017 to FND-021 and FND-040, and the HDE CLI API Vendor Ref 7.1.11 DD-04 paragraph, stay with the Product Owner."),
    ("CLC10-08", "Later-change candidate", "FND-022, FND-023, FND-024, FND-037, FND-038, X-01 to X-04 and LR6-O4, as the change audit triage v1.1 records them."),
    ("CLC10-09", "Later-change candidate", "O-1 (OPS03 EXDEV), O-A (owner-test fixtures re-time the checkout), OBS-1, OBS-2 and OBS-12."),
    ("CLC10-10", "Open", "The Ops task's FND-004 (residual Railway login on the workstation) and the residual workstation and service-host state of QA Report section 12 stay with the Product Owner."),
    ("CLC10-11", "Risk accepted", "I-1 transcript handling: the Product Owner holds the risk (PO-QA100-4)."),
    ("CLC10-12", "Reported", "MB-021, the QA-100 evidence-commit default and MB-030, the close-mutation-set route, are reported to the GCFPE-MGMT-10 maintenance owner."),
]

source = {
    "schema_version": "close_candidate_source.v2",
    "change_id": CRD,
    "plan_path": E + "HDE-CRD-0002-implementation-plan-v1.1.md",
    "evidence_inputs": evidence,
    "requirements_binding": "specification",
    "qa_plan_binding": "qa_plan",
    "qa_report_binding": "qa_verdict",
    "acceptance": acceptance,
    "deliverables": [d for _, d in allocation],
    "allocation": [{"slice": s, "deliverable": d} for s, d in allocation],
    "reuse_boundary": [
        "The HDE-EPIC039 generic writer is reused at its registered path; its v1 model, refusals and output bytes are unchanged, and this close uses the v2 schema.",
        "The release stays 1.3.0, refreshed in place with no version cut, as Implementation Plan delta 01 decided.",
    ],
    "deferrals": [{"id": i, "adr_status": s, "rationale": r} for i, s, r in deferrals],
    "later_drain_statements": [
        {
            "canon_homes": ["Change Process Guide", "HDE Schemas and Artifacts", "Glow QA Guide", "HDE Mechanics Guide", "HDE Governance"],
            "locators": ["3.5.2 Close PR contents", "3.5.2.1 Close-pack files", "3.5.4 ADR block in the close-pack", "Close-pack artifacts", "8.17 New standardized evidence families", "3.4.3 Evidence layout", "37.2 Governance and homes", "2.0.19 Close-pack baseline artifacts"],
            "current_posture": "The S21 ADR's affected canon homes are undrained; HDE Build Notes 2.15 and 2.17 govern until drainage.",
            "action": "No status change recommended",
            "readiness": "Supportable from repo evidence",
            "evidence_bindings": ["adr"],
            "close_expectation": "after a separate canon-only drain step",
        },
        {
            "canon_homes": ["Glow QA Guide"],
            "locators": ["3.4.3 Evidence layout: current-state first"],
            "current_posture": "PO-5, evidence persistence, is pending Product Owner drainage.",
            "action": "No status change recommended",
            "readiness": "Supportable from repo evidence",
            "evidence_bindings": ["qa_rca_record"],
            "close_expectation": "after a separate canon-only drain step",
        },
        {
            "canon_homes": ["Plan Templates"],
            "locators": ["Code-identity guards that exclude storage paths"],
            "current_posture": "QA RCA v1.0 D-1 is proposed and undecided.",
            "action": "No status change recommended",
            "readiness": "Not yet supportable from repo evidence",
            "evidence_bindings": ["qa_rca_record"],
            "close_expectation": "after a separate canon-only drain step",
        },
    ],
    "tracked_issues": [],
    "adr_block": {"decisions": [
        {
            "label": "ADR, close-pack writer for Epic and CRD identities",
            "statement": "One writer serves Epic and CRD identities through a second source schema, and admitted CRDs gain a post-verdict close-run family.",
            "decision_point": "How a CRD close report and manifest are written from tracked inputs, and where same-run close evidence lives without reopening an approved QA manifest.",
            "options_considered": [
                "Extend the generic writer and admit a post-verdict family.",
                "A separate governed close-report writer beside the neutral one.",
                "Let the close PR add a manifest check after the verdict.",
            ],
            "bounding_canon": ["Change Process Guide", "HDE Schemas and Artifacts", "Glow QA Guide", "HDE Governance", "HDE Mechanics Guide"],
            "final_decision": "Extend the generic writer and admit the close-run family; approved with changes by the Product Owner (AQ-1, HDE Build Notes 2.15), and the ADR defers to HDE Build Notes (2.17).",
            "scope": "canonical",
            "doc_delta_targets": ["Change Process Guide", "HDE Schemas and Artifacts", "Glow QA Guide", "HDE Mechanics Guide", "HDE Governance"],
        },
        {
            "label": "ADR, Endpoint Catalog under canon route postures (AD-1)",
            "statement": "Every served pair is catalogued once or excluded once with a basis; a new exclusion class covers canon-retired routes.",
            "decision_point": "Whether S15 requires catalog rows, or removal, for routes that canon retires and excludes from the Endpoint Catalog.",
            "options_considered": [],
            "bounding_canon": ["HDE Architecture", "HDE Users Guide", "HDE Schemas and Artifacts"],
            "final_decision": "Exclusion under canon, CR-7 alternative (a), by Product Owner direction of 2026-10-14 (HDE Build Notes 2.7); removal stays with the canon owner.",
            "scope": "change_specific",
            "doc_delta_targets": [],
        },
        {
            "label": "ADR, exact dev Reader gate (AD-2)",
            "statement": "Dev GET and HEAD /reader are served only when APP_ENV is exactly dev.",
            "decision_point": "S10 names dev, test or local, while canon gates the dev Reader on dev.",
            "options_considered": [],
            "bounding_canon": ["HDE CLI API Vendor Ref", "HDE Schemas and Artifacts", "HDE Mechanics Guide"],
            "final_decision": "Exact comparison, CR-8 alternative (a), by Product Owner direction of 2026-10-14 (HDE Build Notes 2.7).",
            "scope": "change_specific",
            "doc_delta_targets": [],
        },
        {
            "label": "ADR, S01 removed and no version cut (Specification delta 01)",
            "statement": "S01 is removed from scope, and the release stays 1.3.0 refreshed in place.",
            "decision_point": "Whether to deliver wheel packaging of every release member in this change.",
            "options_considered": [],
            "bounding_canon": ["Change Process Guide"],
            "final_decision": "DELTA_APPROVE, Product Owner OPTION 1, 2026-10-21 (HDE Build Notes 2.19 and 2.20).",
            "scope": "change_specific",
            "doc_delta_targets": [],
        },
        {
            "label": "ADR, path proofs for consumed Ops evidence (CR-9)",
            "statement": "The Ops evidence carries a SHA-256 ledger, and its path-proof coverage comes from the QA check that consumes it.",
            "decision_point": "The Plan asks for path proofs under the WU-OPS-01 root, which no canonical writer covers.",
            "options_considered": [
                "Canon route: a SHA-256 ledger, with coverage from the consuming QA check.",
                "A registration unit that admits the Ops root in the updater.",
                "No promotion, with a nonclaim.",
            ],
            "bounding_canon": ["Glow QA Guide", "HDE Schemas and Artifacts", "Plan Templates"],
            "final_decision": "The canon route, APPROVED by Isis in the CL-C-10 closure decision v1.0, section 6.1.",
            "scope": "change_specific",
            "doc_delta_targets": [],
        },
    ]},
    "closure_decision": {"decision": "SATISFIED", "posture": "review_trace_only"},
    "follow_ups": [],
    "superseded": [
        {"binding": "specification_delta_01", "evidence_change": "S01 is removed from scope by Specification delta 01; check 15 proves the removal and its stated limit."},
        {"binding": "plan_delta_01", "evidence_change": "Implementation Plan delta 01 drops the 1.4.0 cut and reduces WU-PR-08 to S16 and S17."},
    ],
    "pointers": [
        "audit/docdeltas/hde-crd-0002_doc_deltas.md",
        "audit/docdeltas/hde-crd-0002_drain_targets.md",
        Q + "qa_step_logs_manifest.json",
        Q + "close/",
        Q + "checks/",
        "docs/adr/hde/close_pack_writer_adr.md",
    ],
    "qa_rca": {"summary_lines": [
        "QA RCA and Doc Delta summary of record: docs/ephemeral/HDE-CRD-0002-QA120-qa-rca-v1.0.md (Glow QA Guide 3.1.2).",
        "Outcome: all 21 checks of approved QA Plan v1.3 are PASS in the QA step-logs manifest and their step-log headers; the QA Report v1.0 verdict is PASS.",
        "Product defect QA110-F01 (S20): in check 13 attempt 1 the pre-push check's read-only guard tripped on a full-history checkout, because its throwaway copies shared the source object store.",
        "QA110-F01 was remedied by WU-REM-02, whose copies own their objects, and verified by check 13's remediation verification RV-1.",
        "Deviation note, check 3: the E-D venue was wired from uv CPython with the system dist-packages by a bounded Moon Loop; S06's target is unchanged, with the venue caveat R-1.",
        "Deviation note, checks 3, 13 and 21: in-session reruns consume the ordinary rerun (R-2); RV-1 is remediation verification, not attempt 2; no proof target changed.",
        "Deviation note, check 21: one Markdown file was restored in the throwaway copy by a Moon Loop, with an independent run on unmodified main (R-4); no proof target changed.",
        "Superseded attempts are preserved byte for byte in their primaries, with each Moon Loop's failure signature and rerun basis.",
        "Doc deltas: PO-2 and PO-5 pending drainage; D-1 proposed for Plan Templates; LR5-O1 recorded; check 1 found no Step-0B doc-delta surface.",
        "Causal limits: the RCA does not establish which object-store file changed in check 13 attempt 1; the mechanism is established by reproduction.",
    ]},
    "key_outputs": {
        "close_report": "audit/HDE-CRD-0002_close_report.md",
        "close_manifest": "audit/HDE-CRD-0002_MANIFEST.json",
        "doc_deltas": "audit/docdeltas/hde-crd-0002_doc_deltas.md",
        "drain_targets": "audit/docdeltas/hde-crd-0002_drain_targets.md",
        "qa_step_logs_manifest": Q + "qa_step_logs_manifest.json",
    },
    "nonclaims": ["no_canon_drainage_or_register_movement", "no_execution_by_writer", "no_hosted_feedback_inputs", "no_unbound_claim"],
}

DOC_DELTAS = """# HDE-CRD-0002 doc deltas

Sources: QA RCA v1.0 section 9 (docs/ephemeral/HDE-CRD-0002-QA120-qa-rca-v1.0.md), the CL-C-10 closure decision v1.0 sections 7 and 8, and this close pull request. Check 1 (qa-01-preflight) found no Step-0B doc-delta surface (CR-11).

- PO-5, evidence persistence. Target: Glow QA Guide section 3.4.3. Owner: Product Owner. State: PENDING_DRAINAGE (HDE Build Notes 2.28).
- PO-2, do not pin tool versions. Target: the owner's choice of home. Owner: Product Owner. State: PENDING_DRAINAGE.
- D-1 of the QA RCA. Target: Plan Templates; a code-identity guard that excludes storage paths uses the classifier's whole set of CI-exempt storage prefixes. Owner: Product Owner. State: proposed.
- LR5-O1, the IR-3 observation (GET //reader?v=1 answered 403 directly). Target: as the Product Owner decides. Owner: Product Owner. State: recorded, no predicate.
- The S21 ADR's affected canon homes (docs/adr/hde/close_pack_writer_adr.md, "Affected canon and drainage consequences"). Owner: Product Owner, through canon maintenance. State: undrained; HDE Build Notes 2.15 and 2.17 govern.
- QA110-F01 remedy limits. Recorded in HDE Build Notes 2.27 and README.md "Pre-push check (HDE-CRD-0002)". State: recorded; no further delta.
- RF-12. README.md, AGENTS.md and CHANGELOG.md nonclaim lines now state that HDE-CRD-0002's close pack, candidate source and close-run family are the only ones produced with the v2 writer. Owner: this close work. State: applied in this close pull request.
"""

DRAIN_TARGETS = """# HDE-CRD-0002 drain targets

Sources: the CL-C-10 closure decision v1.0 section 7 (docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.0.md) and the QA RCA v1.0 section 9. No item is a closure prerequisite. HDE-CRD-0002 cites no tracked issue (TI) and has no PF30 record (CR-1), so every deferral maps through an ADR status.

- CLC10-01: PO-2 and PO-5. Drain target: PO-5 to Glow QA Guide section 3.4.3; PO-2 to the owner's choice of home. Owner: Product Owner. ADR status: Pending drainage.
- CLC10-02: D-1 of the QA RCA. Drain target: Plan Templates. Owner: Product Owner. ADR status: Proposed.
- CLC10-03: this change's HDE Build Notes addenda, including CR-7, CR-10 and CR-11 drainage and the S21 ADR's affected canon homes (Change Process Guide, HDE Schemas and Artifacts, Glow QA Guide, HDE Mechanics Guide, HDE Governance). Owner: Product Owner, through canon maintenance. ADR status: Pending drainage.
- CLC10-04: FND-028, remove the replay report. Drain target: a later change. Owner: Product Owner. ADR status: Later change.
- CLC10-05: FND-029 (S19-R01 to R07), FND-012, X-02 and the legacy chart-loader defect (HDE-SEPA006). Owner: Product Owner. ADR status: Pending, non-gating.
- CLC10-06: LR7-O1 and FND-020, the S21 ADR's line 65 clause. Drain target: docs/adr/hde/close_pack_writer_adr.md, on Product Owner instruction. ADR status: Open documentation defect.
- CLC10-07: FND-017 to FND-021, FND-040 and the HDE CLI API Vendor Ref section 7.1.11 DD-04 paragraph. Owner: Product Owner. ADR status: Candidate.
- CLC10-08: FND-022, FND-023 (LR8-F1), FND-024 (PR35-C1), FND-037, FND-038, X-01 to X-04 and LR6-O4. Owner: Product Owner. ADR status: Later-change candidate.
- CLC10-09: O-1 (OPS03 EXDEV; Thoth, or the Product Owner if independent), O-A, OBS-1, OBS-2 and OBS-12. ADR status: Later-change candidate.
- CLC10-10: FND-004 of the WU-OPS-01 Ops task (residual Railway login) and the residual workstation and service-host state (QA Report section 12). Owner: Product Owner. ADR status: Open.
- CLC10-11: I-1 transcript handling. Owner: Product Owner (PO-QA100-4). ADR status: Risk accepted.
- CLC10-12: MB-021, the QA-100 evidence-commit default and MB-030 (the close-mutation-set route; PF10 addendum record docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-close-pack-process-gap-v1.0.md). Owner: GCFPE-MGMT-10 maintenance owner. ADR status: Reported.
"""

RF12 = [
    ("README.md",
     "the writer and the close-run family are capability only; no close pack or candidate source has been produced with this writer, under either schema, and no close-run family exists.",
     "the only close pack, candidate source and close-run family produced with this writer are HDE-CRD-0002's, under the v2 schema; no other has been produced, under either schema."),
    ("AGENTS.md",
     "The writer and the CRD close-run family are capability only: no close pack or candidate source has been produced with this writer, under either schema, and no close-run family exists; a close pack",
     "The only close pack, candidate source and close-run family produced with this writer are HDE-CRD-0002's, under the v2 schema; no other has been produced, under either schema. A close pack"),
    ("CHANGELOG.md",
     "Capability only: no close pack or candidate source has been produced with this writer, under either schema, and no close-run family exists.",
     "Its first use is HDE-CRD-0002's own close pack, candidate source and close-run family, under the v2 schema; no other has been produced with it, under either schema."),
]

(root / "audit/HDE-CRD-0002_close_candidate_source.json").write_text(json.dumps(source, indent=2, sort_keys=True) + "\n", encoding="utf-8")
(root / "audit/docdeltas/hde-crd-0002_doc_deltas.md").write_text(DOC_DELTAS, encoding="utf-8")
(root / "audit/docdeltas/hde-crd-0002_drain_targets.md").write_text(DRAIN_TARGETS, encoding="utf-8")
for rel, old, new in RF12:
    text = (root / rel).read_text(encoding="utf-8")
    assert text.count(old) == 1, (rel, text.count(old))
    (root / rel).write_text(text.replace(old, new), encoding="utf-8")
print("wrote T1 inputs")
