# HDE-EPIC032 Doc Deltas

## Scope

HDE-FERM003.2 PR-02 adds repo evidence and tooling for narrative registry diffing, Doc-Delta binding, pack identity, and evidence indexing.

## PF-Canon change posture

No PF-Canon file is edited by this PR. The PF09.5, PF12, PF14, PF17, PF04, PF03, and PF06 anchors remain references for later owner review only.

## Repo evidence posture

- `tools/evidence/generate_narrative_registry_diff.py` generates `audit/gates/narratives/registry.diff.json` and refreshes `audit/gates/narratives/pack_identity.txt` under closed rails.
- `registry.diff.json` records manifest identity, keys-only registry counts, and a truthful current-manifest no-prior-baseline diff state without template text.
- `pack_identity.txt` records `pack_sha = sha256(canonical manifest bytes)` and same-bytes two-run identity.
- `tools/evidence/update_evidence_index.py` binds the PR-02 artifacts into the Human Evidence Index, Machine Mirror, hash sentinels, and co-located path proofs.
