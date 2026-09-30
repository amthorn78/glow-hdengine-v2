"""PART-02 of MODIFICATION-20260930-gtwpe-tw-model-advice: build the edited skill trees.

Usage: python3 skill_edits.py <skills-root> <out-dir>
Copies tw-flowmaster and flowmaster-validate from <skills-root> into <out-dir> (which must not
exist), applies EDITS in order, each of whose old strings must occur exactly once, recomputes
flowmaster-validate's SKILL_TREE_SHA256 with its own skill_tree_digest, and prints each changed
file's sha256 and both trees' digests. It writes nothing else.
"""
import hashlib, importlib.util, pathlib, re, shutil, sys

EDITS = [
    ('tw-flowmaster/SKILL.md', '`TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.2.0`',
     '`TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.3.0`',
     'revision 1.2.0 -> 1.3.0'),
    ('tw-flowmaster/SKILL.md', '- `APPLICATION_REASONING_POLICY = ULTRA_IF_RENDERED_PAGES_GT_100_OR_UNKNOWN` for legacy non-GCFPE stages only. Selected-catalog TW uses the task-bound assessment policy below; GCFPE retains its own actual-work policy.\n',
     '',
     '258: the fixed APPLICATION_REASONING_POLICY'),
    ('tw-flowmaster/SKILL.md', '- `PF_RENDERED_PAGE_COUNTS = none`, containing only directly established rendered page counts\n',
     '',
     '266: PF_RENDERED_PAGE_COUNTS'),
    ('tw-flowmaster/SKILL.md', '- `STRENGTH_ANALYZER_PROMPT_ID = none`: for selected-catalog TW resolve TW-ASSESS-10 from the verified current TW catalog when not explicitly supplied. Pin its actual identity/version; no additional operator manifest is needed.\n',
     '',
     '268: STRENGTH_ANALYZER_PROMPT_ID'),
    ('tw-flowmaster/SKILL.md', 'and carry the mandatory pre-creation/pre-Apply assessment and exact no-redlines contracts.',
     'and carry the exact no-redlines contract.',
     "331: the profile's condition"),
    ('tw-flowmaster/SKILL.md', 'the legacy repository-source, fixed-model/page-count, direct creation-to-application and all-targets-must-apply clauses below.',
     'the legacy repository-source and all-targets-must-apply clauses below.',
     '333: the superseded legacy clauses'),
    ('tw-flowmaster/SKILL.md', '- Resolve and read complete TW-ASSESS-10. Before redline creation dispatch, run its assessment-only turn for the actual selected drain, full target and whole or selected incoming source. After a complete READY package is verified, run a separate assessment-only turn for the actual Apply prompt, original, redlines and report. Both assessments normally use the same authoritative TW session. Do not skip the second because research or source reading can be reused. An unchanged completed stage assessment may be reused on resume after exact input/contract checks.\n',
     '',
     "337: TW-ASSESS-10's two turns"),
    ('tw-flowmaster/SKILL.md', '- The analyzer may use the installed OpenAI documentation skill for needed current capability/effort research; follow its official-documentation procedure. Missing/stale/materially changed evidence, a non-obvious choice or inadequately supported Max/Ultra consideration requires a current official check. Reuse dated research across stages. If research/skill availability is limited, retain honestly qualified supported advice; missing decisive input makes assessment incomplete. No automatic skill installation, stronger-model escalation or delegation follows.\n',
     '',
     "338: the analyzer's research"),
    ('tw-flowmaster/SKILL.md', "- Recommendations are task-bound human advice: exact surface/model/reasoning, reasons, cheaper eligible conditions, dated evidence, uncertainty and reassessment triggers. Do not use rendered-page cutoffs or inherit the controller/creation setting for Apply. Record actual configuration only when directly verified; advice is not configuration evidence. For an analyzer's starting configuration, use its current supported operator advice under the same authority.",
     '- Record actual configuration only when directly verified.',
     '339: recommendations, all but the actual-configuration rule'),
    ('tw-flowmaster/SKILL.md', '- Add per-target `PRE_CREATION_ASSESSMENT` and `PRE_APPLY_ASSESSMENT` stages with independent action keys and the existing PENDING/SEND_ATTEMPTED/RUNNING_OR_UNKNOWN/terminal states. Complete and validate the first before creation, and the second before application. A missing or decisively incomplete required assessment stops only its dependent substantive stage. Do not dispatch from an advisory paragraph without complete task-bound assessment evidence.\n',
     '',
     '340: the two assessment stages'),
    ('tw-flowmaster/SKILL.md', "- Validate each analyzer/creator's final response for source prompt/files, exact scope, model/reasoning recommendation or qualified limit, package status,",
     "- Validate each creator's final response for source prompt/files, exact scope, package status,",
     '341: analyzer and recommendation'),
    ('tw-flowmaster/SKILL.md', 'READY creator output points to pre-Apply TW-ASSESS-10; completed pre-Apply assessment points to TW-APPLY-10.',
     'READY creator output points to TW-APPLY-10.',
     "341: READY's route"),
    ('tw-flowmaster/SKILL.md', 'do not dispatch pre-Apply assessment/application.',
     'do not dispatch application.',
     '342'),
    ('tw-flowmaster/SKILL.md', 'revalidated and assessed before Apply is rerun',
     'revalidated before Apply is rerun',
     '343'),
    ('tw-flowmaster/SKILL.md', 'recommendation versus observed configuration',
     'observed configuration',
     '345'),
    ('tw-flowmaster/SKILL.md', 'Report assessments, no-change count,',
     'Report no-change count,',
     '347'),
    ('tw-flowmaster/SKILL.md', '- For legacy non-GCFPE runs outside the selected-catalog TW profile, use GPT-5.6 Sol with Max reasoning for the Flowmaster context, target-identification session, TW-session initialization, and redline creation. For GCFPE stages, apply the actual-work recommendation policy above; for selected-catalog TW, apply its two-checkpoint policy.',
     '- For GCFPE stages, apply the actual-work recommendation policy above.',
     "351: the legacy fixed model and TW's two-checkpoint policy"),
    ('tw-flowmaster/SKILL.md', '- For legacy non-GCFPE application outside that TW profile, use Ultra when the exact rendered PF page count is over 100 or unknown. Use Max only when an exact rendered count of 100 or fewer is directly recorded. GCFPE application uses its actual-work recommendation or provisional fallback; selected-catalog TW uses its completed pre-Apply assessment, never the page-count rule.',
     '- GCFPE application uses its actual-work recommendation or provisional fallback.',
     "352: the legacy Ultra/Max rule and TW's pre-Apply assessment"),
    ('tw-flowmaster/SKILL.md', '- Never infer rendered pages from line count, words, characters, bytes, or filename.\n',
     '',
     '353: rendered-page inference'),
    ('tw-flowmaster/SKILL.md', ', or Sol Max for a non-GCFPE target,',
     ',',
     '393'),
    ('tw-flowmaster/SKILL.md', ' For a non-GCFPE application, select Sol Ultra unless an exact rendered count of 100 or fewer is recorded; otherwise select Sol Max.',
     '',
     "451: step 3's non-GCFPE model"),
    ('flowmaster-validate/scripts/validate_flowmaster.py', '        "TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.2.0",\n',
     '        "TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.3.0",\n',
     'REQUIRED: the TW revision'),
    ('flowmaster-validate/scripts/validate_flowmaster.py', '        "PRE_CREATION_ASSESSMENT",\n',
     '',
     'REQUIRED: PRE_CREATION_ASSESSMENT removed'),
    ('flowmaster-validate/scripts/validate_flowmaster.py', '        "PRE_APPLY_ASSESSMENT",\n',
     '',
     'REQUIRED: PRE_APPLY_ASSESSMENT removed'),
    ('flowmaster-validate/scripts/validate_flowmaster.py', '        "ULTRA_IF_RENDERED_PAGES_GT_100_OR_UNKNOWN",\n',
     '',
     'REQUIRED: ULTRA_IF_RENDERED_PAGES_GT_100_OR_UNKNOWN removed'),
    ('flowmaster-validate/scripts/validate_flowmaster.py', 'CONTRACT_FORBIDDEN = {\n    "tw-flowmaster": (\n',
     'CONTRACT_FORBIDDEN = {\n    "tw-flowmaster": (\n        # MODIFICATION-20260930-gtwpe-tw-model-advice: TW-ASSESS-10 is retired and the fixed\n        # model policy is removed; neither returns.\n        "TW-ASSESS-10",\n        "PRE_CREATION_ASSESSMENT",\n        "PRE_APPLY_ASSESSMENT",\n        "STRENGTH_ANALYZER_PROMPT_ID",\n        "APPLICATION_REASONING_POLICY",\n        "PF_RENDERED_PAGE_COUNTS",\n',
     'FORBIDDEN: the guard'),
    ('flowmaster-validate/scripts/validate_flowmaster.py', '"validator_revision": "3.3.1",',
     '"validator_revision": "3.3.2",',
     'validator_revision 3.3.1 -> 3.3.2'),
    ('flowmaster-validate/scripts/validate_gcfpe_20260914.py', '"validator_revision": "3.3.1",',
     '"validator_revision": "3.3.2",',
     'validator_revision 3.3.1 -> 3.3.2'),
    ('flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py', '"validator_revision": "3.3.1",',
     '"validator_revision": "3.3.2",',
     'validator_revision 3.3.1 -> 3.3.2'),
    ('flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json', '"validator_revision": "3.3.1"',
     '"validator_revision": "3.3.2"',
     "validator_revision 3.3.1 -> 3.3.2 (the fourth site: change-flow's PROFILE_IDENTITY compares it)"),
    ('flowmaster-validate/SKILL.md', 'FLOWMASTER_VALIDATE_REVISION: 3.3.1\n',
     'FLOWMASTER_VALIDATE_REVISION: 3.3.2\n',
     'FLOWMASTER_VALIDATE_REVISION 3.3.1 -> 3.3.2'),
    ('flowmaster-validate/SKILL.md', "the TW specialization revision is 1.2.0 (including Nathan's PF04 incident-name correction). Its selected-catalog profile requires pre-creation and pre-Apply assessments, no-redlines terminal handling and source-file header provenance.",
     "the TW specialization revision is 1.3.0 (including Nathan's PF04 incident-name correction; MODIFICATION-20260930-gtwpe-tw-model-advice removed TW-ASSESS-10's assessment stages and the fixed model policy, and the validator forbids their identifiers). Its selected-catalog profile requires no-redlines terminal handling and source-file header provenance.",
     '184: the TW paragraph'),
]


def main(root, out):
    root, out = pathlib.Path(root), pathlib.Path(out)
    if out.exists():
        sys.exit(f"refused: {out} exists")
    out.mkdir(parents=True)
    for skill in ("tw-flowmaster", "flowmaster-validate"):
        shutil.copytree(root / skill, out / skill)
    changed = []
    for rel, old, new, label in EDITS:
        path = out / rel
        text = path.read_text(encoding="utf-8")
        n = text.count(old)
        if n != 1:
            sys.exit(f"refused: {label}: {n} matches in {rel}")
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
        if rel not in changed:
            changed.append(rel)
    fv = out / "flowmaster-validate"
    spec = importlib.util.spec_from_file_location("vg", fv / "scripts" / "validate_gcfpe_20260914.py")
    vg = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(fv / "scripts"))
    spec.loader.exec_module(vg)
    digest = vg.skill_tree_digest(fv)
    md = fv / "SKILL.md"
    text, k = re.subn(r"(?m)^SKILL_TREE_SHA256: [0-9a-f]{64}$", f"SKILL_TREE_SHA256: {digest}", md.read_text(encoding="utf-8"))
    if k != 1:
        sys.exit(f"refused: {k} SKILL_TREE_SHA256 lines")
    md.write_text(text, encoding="utf-8")
    if vg.skill_tree_digest(fv) != digest:
        sys.exit("refused: the declaration line changed the digest")
    for rel in changed:
        print(hashlib.sha256((out / rel).read_bytes()).hexdigest(), rel)
    print("SKILL_TREE_SHA256", digest)
    print("edits", len(EDITS))


if __name__ == "__main__":
    main(*sys.argv[1:3])
