# EPIC-006 — Assessment (Part 1)

```json
{
  "run_ts": "Sat, 25 Oct 2025 11:13:53 GMT",
  "run_id": "",
  "release_id": "6d8efb271281916e7c775f6b45efafba8c78d55604c40eaa0d89cc40a7eea925"
}
```

## Acceptance tokens
PASS: INTVER_NO_STORE_NO_ETAG_OK DB_DISCOVERY_SHARED_OK DB_SCHEMA_HDE_OK DB_RW_OK
FAIL: DB_SEARCH_PATH_OK ENV_SNAPSHOT_RECORDED_OK SERVICE_CMD_CAPTURED_OK

## /internal/version headers (captured)
### GET
```txt
HTTP/2 200 
cache-control: no-store
content-type: application/json; charset=utf-8
date: Sat, 25 Oct 2025 11:13:53 GMT
server: railway-edge
x-railway-edge: railway/europe-west4-drams3a
x-railway-request-id: MVs3R2aJT9G2BN9YjUJq2g
content-length: 261

{"engine_tag":"hdengine@prod","release_id":"6d8efb271281916e7c775f6b45efafba8c78d55604c40eaa0d89cc40a7eea925","invocation_tag":"INV-f2ac55d77ce9aacc","emitter_sha256":"c828effe645deae150593adbc90589f67141ab20fab1e719171cd8effad9bc19","build_commit":"local-dev"}
```
### HEAD
```txt
HTTP/2 200 
cache-control: no-store
content-type: application/json; charset=utf-8
date: Sat, 25 Oct 2025 11:14:28 GMT
server: railway-edge
x-railway-edge: railway/europe-west4-drams3a
x-railway-request-id: 96T00YwWQqWdivSow9P4nw
content-length: 261


```
### Conditional GET
```txt
HTTP/2 200 
cache-control: no-store
content-type: application/json; charset=utf-8
date: Sat, 25 Oct 2025 11:15:09 GMT
server: railway-edge
x-railway-edge: railway/europe-west4-drams3a
x-railway-request-id: bV6tUcAiS7G-u5HtjUJq2g
content-length: 261

{"engine_tag":"hdengine@prod","release_id":"6d8efb271281916e7c775f6b45efafba8c78d55604c40eaa0d89cc40a7eea925","invocation_tag":"INV-f2ac55d77ce9aacc","emitter_sha256":"c828effe645deae150593adbc90589f67141ab20fab1e719171cd8effad9bc19","build_commit":"local-dev"}
```

## Env snapshot (redacted)
(Env snapshot not present in artifacts)

## DB snapshots (via pg-bridge)
### Version
```txt
version
PostgreSQL 17.6 (Debian 17.6-2.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
(1 row)

```
### Schemas
```txt
schema
information_schema
pg_catalog
pg_toast
public
(4 rows)

```
### Discovery report excerpt
```txt
 ?column? |                                                      version                                                       
----------+--------------------------------------------------------------------------------------------------------------------
 version  | PostgreSQL 17.6 (Debian 17.6-2.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
(1 row)

   ?column?   | current_user 
--------------+--------------
 current_user | postgres
(1 row)

  ?column?   | current_setting 
-------------+-----------------
 search_path | "$user", public
(1 row)

 ?column? | string_agg 
----------+------------
 schemas  | public
(1 row)

   ?column?   |         string_agg          
--------------+-----------------------------
 roles_sample | hde_owner, hde_rw, postgres
(1 row)


```
### Search path
```txt
search_path
"$user", public
(1 row)

```
### Read/Write smoke
```txt
Output format is unaligned.
PASS: schema hde exists
PASS: all 4 base tables exist
PASS: current-month partitions exist
PASS: public_results PK(id, created_at)
PASS: pair_evaluation PK(id, evaluated_at)
PASS: pair_evaluation UNIQUE(min_user,max_user,release_id,evaluated_at)
PASS: public_results indexes present
PASS: pair_evaluation indexes present

```

# Artifacts Index

| path | bytes | sha256 |
|---|---:|---|
| artifacts/headers/internal_version_200.txt | 520 | `a73d3d2ed8d39a070cecd71914b6739db2e939905e294fe5b006253165772b07` |
| artifacts/headers/internal_version_head.txt | 259 | `96e5aecdfb3ce781a17201cd0b21605fac6b7839d95d4e395b695569b1853964` |
| artifacts/headers/internal_version_if_none_match.txt | 520 | `576b0fee5b02401a8aa2284cf0b74e3035e5e78c5ad2b99f095aa3ff49b39bdc` |
| artifacts/env/ENV_SNAPSHOT.txt | - | - |
| artifacts/validation/service_cmd.txt | - | - |
| artifacts/db/version.txt | 131 | `36b57d321a9390b45a2aefdf1a79c09e045d91c7351d7ddc4f5f0c03884c2623` |
| artifacts/db/schemas.tsv | 62 | `f7332fb2aaafdaaa377514ceef6e13858ecafc9a29cb9d67f24f08daf0ec7577` |
| artifacts/db/search_path.txt | 36 | `b2cc89178ff4b3c3afc36fb8dd5fbf2bdbfc20fa00854e9933a6c3992ecea0f0` |
| artifacts/db/discovery_report.md | 809 | `a247c970780a54d5029045e4b862d93029de27422f16b54454b195c10b8f5970` |
| artifacts/db/verify_epic005.txt | 349 | `7db86293e5488a7080ac37397fd47146c558890bf4f51e553605b7e573170433` |
