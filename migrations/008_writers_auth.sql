-- HDE-EPIC008 • Diagnostic writer idempotence & auth posture
BEGIN;

CREATE SCHEMA IF NOT EXISTS hde;

CREATE TABLE IF NOT EXISTS hde.idempotent_writes (
  idempotence_hash CHAR(64) PRIMARY KEY CHECK (idempotence_hash ~ '^[0-9a-f]{64}$'),
  canonical_bytes  TEXT    NOT NULL,
  canonical_json   JSONB   NOT NULL,
  created_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_idempotent_writes_created_at
  ON hde.idempotent_writes (created_at);

COMMIT;
