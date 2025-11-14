-- HDE-EPIC011 • BodyGraph durability (Option A home)
BEGIN;

CREATE SCHEMA IF NOT EXISTS hde;

CREATE TABLE IF NOT EXISTS hde.body_graphs (
  user_id UUID NOT NULL,
  vendor TEXT NOT NULL,
  vendor_version INTEGER NOT NULL,
  input_fingerprint CHAR(64) NOT NULL CHECK (input_fingerprint ~ '^[0-9a-f]{64}$'),
  payload JSONB NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  refreshed_at TIMESTAMPTZ,
  ttl_at TIMESTAMPTZ,
  UNIQUE (user_id, vendor, vendor_version, input_fingerprint)
);

CREATE INDEX IF NOT EXISTS idx_body_graphs_user_vendor ON hde.body_graphs (user_id, vendor);

CREATE OR REPLACE VIEW hde.body_graphs_current AS
SELECT DISTINCT ON (user_id, vendor)
       user_id,
       vendor,
       vendor_version,
       input_fingerprint,
       payload,
       created_at,
       refreshed_at,
       ttl_at
FROM hde.body_graphs
ORDER BY user_id, vendor, COALESCE(refreshed_at, created_at) DESC;

CREATE OR REPLACE VIEW public.hde_body_graphs_current AS
SELECT user_id,
       vendor,
       vendor_version,
       input_fingerprint,
       payload,
       created_at,
       refreshed_at,
       ttl_at
FROM hde.body_graphs_current;

COMMIT;
