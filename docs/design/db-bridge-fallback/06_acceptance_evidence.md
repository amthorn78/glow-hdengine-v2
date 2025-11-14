# Acceptance Evidence — DB Bridge Fallback

| Evidence | Description | Storage |
| --- | --- | --- |
| `artifacts/db/check_schema.txt` | Captured after fallback connection succeeds; confirms schema scope (`hde`, `public`). | `artifacts/db/` |
| `artifacts/db/grants.txt` | ASCII-sorted grants showing bridge-connected posture results. | `artifacts/db/` |
| `artifacts/db/ddl_fingerprint.json` | Canonical JSON fingerprint demonstrating deterministic output via bridge. | `artifacts/db/` |
| `artifacts/evidence_index.jsonl` entry | Indexed pointer linking fallback run id to stored artifacts. | `artifacts/` |
| Audit diff (`audit/docs_snapshot_r7/`) | Snapshot confirming documentation update propagated. | `audit/` |

Acceptance is met when these artifacts are refreshed, LF-terminated, and reviewed alongside transport header proofs to ensure fallback introduces no regressions in refusal handling or presenter output.
