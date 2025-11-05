# Idempotent Writes (EPIC-008)

Preimage: `{method:"POST", writer_route_id:"ops.writer.diagnostic.v1", canonical_request_body}`  
Digest: lowercase sha256 hex (64)  
Storage: `hde.idempotent_writes (idempotence_hash, canonical_bytes, canonical_json, created_at)`  
Duplicate-policy: same status as first success.
