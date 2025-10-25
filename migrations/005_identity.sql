-- HDE-EPIC005 • Identity & Evidence Persistence (UTC anchored)
BEGIN;

CREATE SCHEMA IF NOT EXISTS hde;

CREATE TABLE IF NOT EXISTS hde.meta (
  id             TEXT PRIMARY KEY CHECK (id='singleton'),
  engine_tag     TEXT NOT NULL,
  build_commit   TEXT NOT NULL,
  invocation_tag TEXT NOT NULL CHECK (invocation_tag ~ '^INV-[0-9A-Fa-f]+$'),
  emitter_sha256 TEXT NOT NULL CHECK (emitter_sha256 ~ '^[0-9a-f]{64}$'),
  created_at     TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Partitioned by created_at (month); PK must include partition key
CREATE TABLE IF NOT EXISTS hde.public_results (
  id         UUID NOT NULL,
  release_id TEXT  NOT NULL CHECK (release_id ~ '^[0-9a-f]{64}$'),
  payload    JSONB NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (id, created_at)
) PARTITION BY RANGE (created_at);

DO $$
DECLARE
  start_utc TIMESTAMPTZ := date_trunc('month', timezone('UTC', now()));
  end_utc   TIMESTAMPTZ := start_utc + interval '1 month';
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM pg_class c
    JOIN pg_namespace n ON n.oid = c.relnamespace
    WHERE n.nspname='hde' AND c.relname='public_results_pcur'
  ) THEN
    EXECUTE format(
      'CREATE TABLE hde.public_results_pcur PARTITION OF hde.public_results
       FOR VALUES FROM (%L) TO (%L);', start_utc, end_utc);
  END IF;
END$$;

-- Helpful indexes
CREATE INDEX IF NOT EXISTS idx_public_results_id         ON hde.public_results (id);
CREATE INDEX IF NOT EXISTS idx_public_results_release_id ON hde.public_results (release_id);
CREATE INDEX IF NOT EXISTS idx_public_results_created_at ON hde.public_results (created_at);

-- Optional additive tables (no app coupling in 005)
CREATE TABLE IF NOT EXISTS hde.chart_snapshot (
  id           UUID PRIMARY KEY,
  user_id      TEXT NOT NULL,
  release_id   TEXT NOT NULL CHECK (release_id ~ '^[0-9a-f]{64}$'),
  chart_json   JSONB NOT NULL,
  provider     TEXT NOT NULL,
  fingerprint  TEXT NOT NULL CHECK (fingerprint ~ '^[0-9a-f]{64}$'),
  computed_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (user_id, release_id)
);

-- Partitioned by evaluated_at; PK must include partition key
CREATE TABLE IF NOT EXISTS hde.pair_evaluation (
  id                UUID NOT NULL,
  min_user          TEXT NOT NULL,
  max_user          TEXT NOT NULL,
  release_id        TEXT NOT NULL CHECK (release_id ~ '^[0-9a-f]{64}$'),
  bands_json        JSONB NOT NULL,
  internal_json     JSONB,
  idempotence_hash  TEXT NOT NULL CHECK (idempotence_hash ~ '^[0-9a-f]{64}$'),
  evaluated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (id, evaluated_at),
  UNIQUE (min_user, max_user, release_id, evaluated_at)
) PARTITION BY RANGE (evaluated_at);

DO $$
DECLARE
  start_utc TIMESTAMPTZ := date_trunc('month', timezone('UTC', now()));
  end_utc   TIMESTAMPTZ := start_utc + interval '1 month';
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM pg_class c
    JOIN pg_namespace n ON n.oid = c.relnamespace
    WHERE n.nspname='hde' AND c.relname='pair_evaluation_pcur'
  ) THEN
    EXECUTE format(
      'CREATE TABLE hde.pair_evaluation_pcur PARTITION OF hde.pair_evaluation
       FOR VALUES FROM (%L) TO (%L);', start_utc, end_utc);
  END IF;
END$$;

-- Helpful indexes
CREATE INDEX IF NOT EXISTS idx_pair_eval_id            ON hde.pair_evaluation (id);
CREATE INDEX IF NOT EXISTS idx_pair_eval_release       ON hde.pair_evaluation (release_id);
CREATE INDEX IF NOT EXISTS idx_pair_eval_evaluated_at  ON hde.pair_evaluation (evaluated_at);

-- Seed singleton identity if absent
INSERT INTO hde.meta (id, engine_tag, build_commit, invocation_tag, emitter_sha256)
SELECT 'singleton', 'engine-local', '0000000', 'INV-0000', repeat('0',64)
WHERE NOT EXISTS (SELECT 1 FROM hde.meta WHERE id='singleton');

COMMIT;
