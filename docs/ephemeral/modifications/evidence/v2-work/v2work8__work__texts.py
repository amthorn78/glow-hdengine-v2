import re
V1 = open('/tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/v2/v1.md', encoding='utf-8').read()
S3 = V1[V1.index('## §3 Canonical wording, final'):V1.index('## §4 Graph transforms')]
def block_after(marker, nth=0):
    i = S3.index(marker)
    for _ in range(nth + 1):
        j = S3.index('```text\n', i); k = S3.index('\n```', j + 8)
        val = S3[j + 8:k]; i = k + 4
    return val
T = {
 'C-ART': block_after('**C-ART** (PART-03)'),
 'C-HANDOFF': block_after('**C-HANDOFF** (PART-04'),
 'C-PLACE': block_after('**C-PLACE** (PART-05)'),
 'C-DEC': block_after('**C-DEC** (PART-06'),
 'C-LAT': block_after('**C-LAT** (PART-07'),
 'C-D22': block_after('**C-D22** (PART-13)'),
 'C-SESSION': block_after('**C-SESSION** (PART-09), amended'),
 'C-SUB': block_after('**C-SUB** (PART-10), A1-5'),
 'C-DISPATCH': block_after('**C-DISPATCH** (PART-11), A1-5'),
 'C-TOP': block_after('**C-TOP** (A1-8), new'),
 'OVERRIDE': block_after('**GCFPE override** (A1-6), new'),
 'C-PROCEED': block_after('**C-PROCEED** (the single-Proceed rule'),
 'C-PR20-ENTRY': block_after('**C-PR20-ENTRY**'),
 'C-PR30-ENTRY': block_after('**C-PR30-ENTRY**'),
 'C-REPLAN': block_after('**C-REPLAN**'),
 'STEP2': block_after('**Step 2** — C-NOTION in the relay'),
 'INVARIANT': block_after('**Governance-audit invariant**'),
}
T['NINE'] = "The exact ordered nine-field GCF-17 continuity list is: `WORK_UNIT_ID`; original Product Owner Proceed; workspace/worktree; branch; pull request; PR instruction; detailed PR plan; primary skill authority; continuous recovery/artifact lineage"
T['TEN'] = "The exact ordered ten-field GCF-17 continuity list is: `WORK_UNIT_ID`; original Product Owner Proceed; dedicated PR-development session; workspace/worktree; branch; pull request; PR instruction; detailed PR plan; primary skill authority; continuous recovery/artifact lineage"
T['V6'] = "The PR-35 result vocabulary is exactly `MERGE_PENDING`, `MERGE_OBSERVED`, `RESCOPE_PENDING`, `RECOVERY_PENDING`, `REMOTE_EVIDENCE_PENDING`, or `PRODUCT_OWNER_DECISION_REQUIRED`"
T['V5'] = "The PR-35 result vocabulary is exactly `MERGE_PENDING`, `RESCOPE_PENDING`, `RECOVERY_PENDING`, `REMOTE_EVIDENCE_PENDING`, or `PRODUCT_OWNER_DECISION_REQUIRED`"
T['FALLBACK'] = "only where no `MERGE_OBSERVED` result was returned for this merge"
T['LANDED'] = "A pull request merged under an earlier plan cycle is landed history: never resume, reuse or push to it."
T['A18'] = "PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session."
T['W9'] = "For a GCFPE main-ecosystem stage, return the paste-ready `NEXT_PROMPT_HANDOFF` and stop for Nathan; provisioning does not apply."
T['S6'] = "A runtime handoff still names its destination by full name, version and direct Notion URL (C-HANDOFF); `NOTION_REFERENCE` stays versionless for reusable prompt text."
T['S7'] = "`NOTION` means a maintenance surface that a destination rule names; live task, handoff and decision state lives in the repository."
assert T['C-SESSION'].endswith(T['A18'])
if __name__ == '__main__':
    import hashlib
    for k, v in T.items():
        print(k, len(v), hashlib.sha256(v.encode()).hexdigest()[:12], repr(v[:70]))
