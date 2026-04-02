# HDE-EPIC028 - PO-003 Full Action Report and Evidence Output

## Scope
- Epic: HDE-EPIC028 (Conjunction Pass 4)
- Check ID: po-003
- Check Name: CLI compatibility surface presence and deterministic proof-surface verification
- Step intent: verify CLI compatibility surface presence and confirm deterministic closure proof surfaces remain present and passing
- Status: PASS

## Step Intent (Verbatim)
"Verify the CLI compatibility surface is present and that current repo-supported artifacts still support deterministic closure for the showcompat slice."

## Step Proof Excerpt (Verbatim)
- "Help exits 0 and includes showcompat."
- "Existing governed CLI artifacts remain PASS / non-zero."
- "No new flags or new routes were introduced to satisfy the check."

## Rails and Determinism Pins
- SAFE_MODE=1
- ALLOW_NETWORK=0
- APP_ENV=dev
- LC_ALL=C
- LANG=C
- TZ=UTC

## Repo Loci in Scope
- pyproject.toml
- engine/cli/__main__.py
- scripts/hdctl.py
- ci/checks/check_cli_help.sh
- artifacts/cli/guards/emitter_symbol_proof.txt
- artifacts/cli/guards/serializer_grep_guard.log
- artifacts/cli/reader_cli_parity.bytes

## Executed Actions
1. Confirmed D0 precondition (`audit/qa/hde-epic028/checks/d0/primary.log`) and ensured stable check directory `audit/qa/hde-epic028/checks/po-003`.
2. Confirmed required CLI-relevant repo loci are present.
3. Captured `python -m engine.cli --help` output into governed stdout/stderr/rc artifacts.
4. Extracted `showcompat` lines into governed presence artifact.
5. Snapshotted governed CLI guard artifacts (emitter symbol proof + serializer grep guard).
6. Probed governed Reader↔CLI parity bytes artifact for existence and non-zero size.
7. Wrote PF27 step log header in `primary.log` with exact command sequence and evidence artifact list.

## Validation Checks Performed
1. Help command return code is 0.
2. `showcompat` appears in help output.
3. Emitter symbol proof snapshot includes `summary:PASS`.
4. Serializer grep guard snapshot includes `summary: PASS`.
5. Parity probe reports `exists=True` and non-zero `size`.
6. Primary log exists with schema `pf27.step_log_header.v1`, check_id `po-003`, and governed artifact list.

## Findings Trace (Line-Level)
- `hdctl_help.rc.txt`
  - return code `0` at line 1
- `showcompat_presence.txt`
  - showcompat match at line 1
  - showcompat match at line 2
  - showcompat match at line 3
- `emitter_symbol_proof_snapshot.txt`
  - `summary:PASS` at line 4
- `serializer_grep_guard_snapshot.txt`
  - `summary: PASS` at line 3
- `reader_cli_parity_probe.txt`
  - `exists=True size=320` at line 1

## Evidence Integrity Snapshot
- audit/qa/hde-epic028/checks/po-003/primary.log
  - lines: 2
  - size_bytes: 2758
  - sha256: 5503deb1e3e029623df4adbde44c0931218ee2f56f5b88b3d21a9888d5be3327
- audit/qa/hde-epic028/checks/po-003/hdctl_help.txt
  - lines: 18
  - size_bytes: 717
  - sha256: 3dfb564807a9a2bc0358c6f4db4edb20d9c454ef476e33161cce9c92629fba6a
- audit/qa/hde-epic028/checks/po-003/hdctl_help.stderr.txt
  - lines: 0
  - size_bytes: 0
  - sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- audit/qa/hde-epic028/checks/po-003/hdctl_help.rc.txt
  - lines: 1
  - size_bytes: 2
  - sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
- audit/qa/hde-epic028/checks/po-003/showcompat_presence.txt
  - lines: 3
  - size_bytes: 200
  - sha256: 2dce5561b19878ea54d5505d6e7273503ec1d27c575e1ec830ac6657ff6fb642
- audit/qa/hde-epic028/checks/po-003/emitter_symbol_proof_snapshot.txt
  - lines: 7
  - size_bytes: 392
  - sha256: 6120d745ff554e12d9bc4b731a597f60264e6f5c8fff60c1939a71f35652bfc4
- audit/qa/hde-epic028/checks/po-003/serializer_grep_guard_snapshot.txt
  - lines: 3
  - size_bytes: 137
  - sha256: 3d5902ce7fd49185b22c2d5f51735e83017c8e38246ed5e3adc716051b8f528a
- audit/qa/hde-epic028/checks/po-003/reader_cli_parity_probe.txt
  - lines: 1
  - size_bytes: 21
  - sha256: dcefbdfdb5ec012cf9c08b51f5411f5217f0e3d6ccbc20a59c44ea96787393c6

## Full Evidence Outputs

### 1) primary.log
Path: audit/qa/hde-epic028/checks/po-003/primary.log

```text
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"po-003","check_name":"CLI compatibility surface presence and deterministic proof-surface verification","claimed_tokens":[],"command":"python -c \"from pathlib import Path; import subprocess; r=subprocess.run(['python', '-m', 'engine.cli', '--help'], capture_output=True, text=True); Path('audit/qa/hde-epic028/checks/po-003/hdctl_help.txt').write_text(r.stdout, encoding='utf-8'); Path('audit/qa/hde-epic028/checks/po-003/hdctl_help.stderr.txt').write_text(r.stderr, encoding='utf-8'); Path('audit/qa/hde-epic028/checks/po-003/hdctl_help.rc.txt').write_text(str(r.returncode)+'\\n', encoding='utf-8')\"; python -c \"from pathlib import Path; lines=Path('audit/qa/hde-epic028/checks/po-003/hdctl_help.txt').read_text(encoding='utf-8').splitlines(); hits=[str(i+1)+':'+line for i,line in enumerate(lines) if 'showcompat' in line]; Path('audit/qa/hde-epic028/checks/po-003/showcompat_presence.txt').write_text('\\n'.join(hits)+'\\n' if hits else '', encoding='utf-8')\"; python -c \"from pathlib import Path; src=Path('artifacts/cli/guards/emitter_symbol_proof.txt').read_text(encoding='utf-8').splitlines(); Path('audit/qa/hde-epic028/checks/po-003/emitter_symbol_proof_snapshot.txt').write_text('\\n'.join(src[:40])+'\\n', encoding='utf-8')\"; python -c \"from pathlib import Path; src=Path('artifacts/cli/guards/serializer_grep_guard.log').read_text(encoding='utf-8').splitlines(); Path('audit/qa/hde-epic028/checks/po-003/serializer_grep_guard_snapshot.txt').write_text('\\n'.join(src[:40])+'\\n', encoding='utf-8')\"; python -c \"from pathlib import Path; p=Path('artifacts/cli/reader_cli_parity.bytes'); Path('audit/qa/hde-epic028/checks/po-003/reader_cli_parity_probe.txt').write_text('exists='+str(p.exists())+' size='+(str(p.stat().st_size) if p.exists() else '0')+'\\n', encoding='utf-8')\"","command_provenance":"Explicitly created","evidence_artifacts":["audit/qa/hde-epic028/checks/po-003/primary.log","audit/qa/hde-epic028/checks/po-003/hdctl_help.txt","audit/qa/hde-epic028/checks/po-003/hdctl_help.stderr.txt","audit/qa/hde-epic028/checks/po-003/hdctl_help.rc.txt","audit/qa/hde-epic028/checks/po-003/showcompat_presence.txt","audit/qa/hde-epic028/checks/po-003/emitter_symbol_proof_snapshot.txt","audit/qa/hde-epic028/checks/po-003/serializer_grep_guard_snapshot.txt","audit/qa/hde-epic028/checks/po-003/reader_cli_parity_probe.txt"],"fail_status":"","intended_tokens":[],"pf_refs":["PF19 — Glow QA Guide","PF27 — Canon Plan Templates"],"schema_version":"pf27.step_log_header.v1","status":"PASS","timestamp_utc":"2026-04-01T22:20:32Z"}
planned_step: capture CLI help, showcompat presence, and governed CLI parity artifacts
```

### 2) hdctl_help.txt
Path: audit/qa/hde-epic028/checks/po-003/hdctl_help.txt

```text
usage: hdctl [-h] [--version]
             {showcompat,aux-preview,bg:resolve,dev:sampler} ...

Glow HD Engine compatibility CLI

positional arguments:
  {showcompat,aux-preview,bg:resolve,dev:sampler}
    showcompat          Emit canonical Reader v1 bytes from vendor JSON (stdin
                        or files)
    aux-preview         Preview Aux narrative text for a public tuple
    bg:resolve          Resolve BodyGraphs from db/vendor sources (Phase S8a
                        stub)
    dev:sampler         DEV/ADMIN ONLY: deterministic sampler harness
                        (seedable)

options:
  -h, --help            show this help message and exit
  --version             show program version and exit
```

### 3) hdctl_help.stderr.txt
Path: audit/qa/hde-epic028/checks/po-003/hdctl_help.stderr.txt

```text

```

### 4) hdctl_help.rc.txt
Path: audit/qa/hde-epic028/checks/po-003/hdctl_help.rc.txt

```text
0
```

### 5) showcompat_presence.txt
Path: audit/qa/hde-epic028/checks/po-003/showcompat_presence.txt

```text
2:             {showcompat,aux-preview,bg:resolve,dev:sampler} ...
7:  {showcompat,aux-preview,bg:resolve,dev:sampler}
8:    showcompat          Emit canonical Reader v1 bytes from vendor JSON (stdin
```

### 6) emitter_symbol_proof_snapshot.txt
Path: audit/qa/hde-epic028/checks/po-003/emitter_symbol_proof_snapshot.txt

```text
CLI Emitter Symbol Proof
canonical_emitters:emit_reader_public_envelope,emitter.emit_public
handler_emitter_allowlist:aux-preview=<none>,bg:resolve=emitter.emit_public,showcompat=emit_reader_public_envelope|emitter.emit_public
summary:PASS
aux-preview:aux_preview:<none> (exempt)
bg:resolve:bg_resolve:emitter.emit_public
showcompat:showcompat:emit_reader_public_envelope,emitter.emit_public
```

### 7) serializer_grep_guard_snapshot.txt
Path: audit/qa/hde-epic028/checks/po-003/serializer_grep_guard_snapshot.txt

```text
CLI Serializer Grep Guard
scope:adapter/http_reader.py,engine/cli
summary: PASS (no disallowed json serialization in governed CLI scope)
```

### 8) reader_cli_parity_probe.txt
Path: audit/qa/hde-epic028/checks/po-003/reader_cli_parity_probe.txt

```text
exists=True size=320
```

## Final Step Result
PASS. The CLI compatibility surface is present and help returns success with `showcompat`; governed CLI guard artifacts remain PASS; parity artifact probe is non-zero; and no new flags or new routes were introduced to satisfy this check.
