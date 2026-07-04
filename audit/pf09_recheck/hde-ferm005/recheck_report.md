# PF09 HDE-FERM005 Recheck Report

Target: PF09.5 HDE-FERM005 / HDE-FERM005.1

Repo: glow-hdengine-v2

Branch: main

HEAD: 3fc61d3bf7b3563c7f27054975738de8ffb0519b

Reviewed by local smoke: yes

PF09 status change: none

## Scope

This is a local functionality and evidence-shape recheck for the CLI Aux preview story. It does not edit PF09, regenerate governed evidence, update the Human Evidence Index, update the Machine Mirror, create path proofs, or claim QA PASS.

The recheck ran under closed deterministic rails:

`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`

No network or credentialed vendor call was performed.

## Runtime Smoke

Command captured in `command_trace.txt`:

`python -m engine.cli aux-preview --pair-file artifacts/cli/showcompat/stdout.json --show-narrative --admin-out audit/pf09\ recheck/aux_preview_pair_sidecar.json`

Result:

- Exit code: 0
- Stderr: empty
- Stdout: LF-terminated narrative text, no CRLF, no ANSI escapes
- Admin sidecar: canonical sorted compact JSON with one trailing LF
- Admin sidecar fields: `composition_id`, `key`, `pack_sha`, `pair`, `release_id`
- Pair IDs: present for `a_person_uid` and `b_person_uid`
- Sidecar prose check: no obvious narrative prose fields or narrative words

Smoke stdout excerpt:

`Together you feel bright without rush. There is room to breathe.`

## Historical Artifact Checks

Historical preview artifacts remain present:

- `artifacts/cli/narrative/stdout.txt`
- `artifacts/cli/narrative/sidecar.json`

Both sibling path proofs exist and match artifact path, size, and sha256:

- `artifacts/cli/narrative/stdout.txt.path_proof.txt`
- `artifacts/cli/narrative/sidecar.json.path_proof.txt`

The current preview sidecar is canonical sorted compact JSON with one trailing LF and contains selector fields only.

## EPIC-017 Evidence Checks

The cited EPIC-017 QA evidence files remain present and readable:

- `audit/qa/hde-epic017/logs/step_aux_preview1.txt`
- `audit/qa/hde-epic017/logs/step_aux_preview1_admin.json`

The admin JSON contains the expected selector shape: `composition_id`, `key`, `pack_sha`, `pair`, and `release_id`.

## Index And Mirror

The Human Evidence Index contains one minimal key/path record for each preview artifact.

The Machine Mirror contains one record for each preview artifact with matching `sha256`, `size_bytes`, and `proof_anchor`.

The Machine Mirror proof anchors match the sibling path proofs:

- `artifacts/cli/narrative/stdout.txt.path_proof.txt`
- `artifacts/cli/narrative/sidecar.json.path_proof.txt`

Note: the Human Index target records are minimal key/path rows and do not carry hash/size fields for these older artifacts. Hash/size/proof linkage is present and matching in the Machine Mirror and path proofs.

## Classification

`STILL_SUPPORTABLE_WITH_NOTE`

The `hdctl aux-preview` functionality mentioned by PF09 works on the current local checkout, including narrative stdout and IDs-only admin sidecar output from compat pair input. The historical evidence files, EPIC-017 evidence files, path proofs, and Machine Mirror linkage remain present and coherent. The only note is the older minimal Human Index row shape for the two preview artifacts.

