---
artifact_type: OPS_TASK_PROMPT
artifact_version: "1.0"
logical_id: HDE-EPIC041-POSTCLOSE-OPS01
title: "Full compat test under open rails: live vendor compat through hdctl, plus read-only checks of the deployed service"
context: "HDE-EPIC041 is closed (CLOSE / CHANGE_CLOSED, 2026-11-01). Its QA ran under closed rails only and exercised no compat path. The Product Owner is not reopening it and directed this separate full compat test on 2026-11-01."
authorizing_principal: Nathan (Product Owner)
executor: "The Product Owner, or an automated session he delegates to in the execution venue below"
execution_venue: "GitHub Codespaces for amthorn78/glow-hdengine-v2 (the canonical QA console), or any Linux shell meeting the environment contract in section 4"
source: "main, at the commit recorded at step 0.2"
vendor_request_limit: 12
production_http_request_limit: 6
writes: "None to the repository, the production database, or any external system. Evidence is written only to a run directory outside the repository."
recorded: "2026-11-01T19:31Z"
producer: "Isis, continuing Lead Developer for HDE-EPIC041 (https://claude.ai/code/session_01Q789tyhUaytmY7x273kwes)"
---

# HDE-EPIC041-POSTCLOSE-OPS01: full compat test under open rails (v1.0)

Paste everything below the line into the session that will execute it. The Product Owner's message that delivers it must contain this exact line, or the session must stop before step 0:

`Authorized: HDE-EPIC041-POSTCLOSE-OPS01 v1.0`

**Model and reasoning setting**

- **TypeSafe v8.2: Opus 5.5 at max.** Effort score 3.91 (confidence 0.93); rung probabilities low 0.00, medium 0.00, high 0.01, extra high 0.07, max 0.91, ultracode 0.01. Model probabilities Fable 5.1 0.43, Opus 5.5 0.55, Sonnet 5.5 0.01, Haiku 5.5 0.01 (confidence 0.40). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.004, Fable 5.1 at extra high 0.030, Fable 5.1 at max 0.391, Fable 5.1 at ultracode 0.004, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.000, Opus 5.5 at high 0.006, Opus 5.5 at extra high 0.039, Opus 5.5 at max 0.501, Opus 5.5 at ultracode 0.006, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.000, Sonnet 5.5 at extra high 0.001, Sonnet 5.5 at max 0.009, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.001, Haiku 5.5 at max 0.009, Haiku 5.5 at ultracode 0.000. Flags: model near tie between Opus 5.5 and Fable 5.1. Sent 2026-11-01T19:35:37Z. Nathan picks the cell.

---

## 1. Your task

You are the Ops executor for one bounded task. Run a full compat test of the Glow HD Engine under open rails and report the result to the Product Owner. "Full compat test" here means:

* **Part V: live vendor compat.** `hdctl showcompat --source vendor` gets real charts from HumanDesignAPI v2 for synthetic birth data. It computes compat through the engine's supported path (`evaluate_pair` → `compute_core`) and emits the canonical result and the public Reader v1 bytes. You prove four things:
  * the output is well formed;
  * AB and BA give byte-identical bytes;
  * two runs give byte-identical bytes;
  * different pairs give different results.
* **Part D: the deployed service.** You make read-only HTTP checks against the production HD Engine service:
  * its release identity against `main`;
  * its production Reader routes for v1 and v2;
  * two governed error answers.
* **Part C: closed-rails refusal.** You show that the same vendor command refuses before any I/O when rails are closed.

Do only what this prompt says. If something does not match, stop and report it; do not improvise.

## 2. What a PASS proves, and what it does not

* **It proves:**
  * the engine at the recorded `main` commit computes compat from live vendor charts, deterministically and symmetrically, with correct output shape and release identity;
  * the deployed service answers its identity and Reader routes as recorded.
* **It does not prove:**
  * deployed compat for two real stored people. The production Reader scores only charts already stored in the database, and only one synthetic stored identity is documented (section 8);
  * conjunction output (section 8);
  * full vendor conformance;
  * QA of any change, acceptance, PF09 movement, deployment, release activation or closure.
* **Where the evidence belongs.** This is Ops evidence (HDE Governance §3.4). A CLI-local vendor run is not deployed-service validation (Glow QA Guide §3.5.5).

## 3. Hard rules (stop on any breach)

1. **Synthetic data only.** Use only the four pairs of birth data in section 5. Never use a real person's data.
2. **No writes.** Do not use `--upsert`, `bg:resolve`, any database write, or any repository commit, push or pull request. Unset `DATABASE_URL` for every `hdctl` command.
3. **Request limits.**
   * At most 12 vendor acquisitions. Each `showcompat --source vendor` invocation counts as 2, one per party, so you may make at most 6 invocations.
   * At most 6 HTTP requests to the production service.
   * No retries. If a step fails for a transport or vendor reason, stop and report.
4. **Rails.** Rails are closed by default (`SAFE_MODE=1 ALLOW_NETWORK=0`). Open them only on the single command that needs them, by prefixing that command; never `export` them open.
5. **Secrets.**
   * Never print, echo, log or paste the value of `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL` or `DATABASE_URL`. Record only `SET` or `UNSET`.
   * Never use `set -x`.
   * Never save request or response headers from the vendor.
6. **Environment label.** `APP_ENV` must be exactly `dev`, the documented target for CLI-local vendor runs (Glow Infrastructure §2.7). The production vendor override gate does not yet cover `showcompat`: S19-R01 is decided in HDE Build Notes but not implemented. So never run this task with `APP_ENV=prod`, `production` or `live`.
7. **Out of scope.** Do not edit the repository, PF canon, Notion, the board or any record. Make no QA, acceptance or closure claim.

## 4. Environment contract

* Linux, `bash`, `git`, `curl`, Python 3.11 or later with `venv`, and network access to `github.com`, the vendor and `glow-hdengine-v2-production.up.railway.app`.
* These variables must be available in the shell, for example as Codespaces secrets:
  * `HD_API_BASE_URL` (its last path segment must be exactly `v2`);
  * `HD_API_KEY`;
  * `GEO_API_KEY`.
* `HDAPI_BASE_URL` must be unset; a conflicting value fails closed.

## 5. Synthetic inputs

These are invented records, not real people. P1-A is the documented EPIC011 synthetic profile.

| Pair | Party | birthdate | birthtime | location |
| :- | :- | :- | :- | :- |
| P1 | A | 1990-01-01 | 12:00 | Amsterdam, Netherlands |
| P1 | B | 1985-07-15 | 08:30 | London, United Kingdom |
| P2 | A | 1992-03-21 | 18:45 | New York, United States |
| P2 | B | 1978-11-02 | 04:10 | Sydney, Australia |

Error case E1: party A is P1-A, and party B is 1985-07-15, 08:30, at the location `Zzqx Synthetic Nowhere 000`.

## 6. Steps

Run the blocks in order, in one shell session. Each block appends to `$EV/run.log`. Stop at the first failed predicate, unless the step says to record it and go on.

### Step 0: set up and preflight (no vendor, no production traffic)

```bash
set -u
RUN="$HOME/hde-compat-ops01-$(date -u +%Y%m%dT%H%M%SZ)"; EV="$RUN/ev"; mkdir -p "$EV"
export LC_ALL=C LANG=C TZ=UTC APP_ENV=dev SAFE_MODE=1 ALLOW_NETWORK=0 PYTHONDONTWRITEBYTECODE=1
log(){ printf '%s\n' "$*" | tee -a "$EV/run.log"; }
log "run_dir=$RUN started_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
# 0.1 presence only
for k in HD_API_BASE_URL HD_API_KEY GEO_API_KEY HDAPI_BASE_URL DATABASE_URL; do
  if [ -n "${!k:-}" ]; then log "$k=SET"; else log "$k=UNSET"; fi
done
case "${HD_API_BASE_URL:-}" in */v2|*/v2/) log "hd_api_base_terminal=v2";; *) log "hd_api_base_terminal=NOT_V2";; esac
```

**Predicate 0.1.**
* `HD_API_BASE_URL`, `HD_API_KEY` and `GEO_API_KEY` are `SET`.
* `HDAPI_BASE_URL` is `UNSET`.
* `hd_api_base_terminal=v2`.

Otherwise stop with `TOOLING_BLOCKED`.

```bash
# 0.2 fresh clone of main, install, identity
git clone -q https://github.com/amthorn78/glow-hdengine-v2 "$RUN/repo" && cd "$RUN/repo"
log "main_sha=$(git rev-parse HEAD)"
python3 -m venv "$RUN/venv" && . "$RUN/venv/bin/activate"
python -m pip install -q 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e . > "$RUN/pip.log" 2>&1; log "pip_exit=$?"
log "hdctl_version=$(hdctl --version)"
python scripts/release_id_recompute.py --check-manifest-only > "$EV/release_check.txt" 2>&1; log "release_check_exit=$?"
RID=$(sha256sum catalog/manifest.json | cut -d' ' -f1); log "local_release_id=$RID"
log "tree_clean=$([ -z "$(git status --porcelain)" ] && echo yes || echo no)"
```

**Predicate 0.2.**
* `pip_exit=0` and `release_check_exit=0`.
* `tree_clean=yes`. The editable install's `*.egg-info` is ignored by Git; if it is not, record what `git status --porcelain` shows and stop.

`local_release_id` is the release identity of `main`. `catalog/manifest.json` is stored as its canonical bytes, so its SHA-256 is the `release_id`. On 2026-11-01 it was `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` (release 1.3.0). If it differs, record the new value and continue.

### Step C: closed-rails refusal (no vendor call may happen)

```bash
P1A=(--birthdate-a 1990-01-01 --birthtime-a 12:00 --location-a "Amsterdam, Netherlands")
P1B=(--birthdate-b 1985-07-15 --birthtime-b 08:30 --location-b "London, United Kingdom")
env -u DATABASE_URL SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat --source vendor "${P1A[@]}" "${P1B[@]}" > "$EV/c0.out" 2> "$EV/c0.err"; log "C0 exit=$?"
log "C0 stdout_bytes=$(wc -c < "$EV/c0.out") stderr=$(cat "$EV/c0.err")"
```

**Predicate C.** `exit=1`, `stdout_bytes=0`, and stderr is exactly `PROVIDER_REFUSED`. Anything else is `FAIL_BEHAVIOR`: the rails did not refuse first. Stop.

### Step V: live vendor compat (6 invocations, 12 acquisitions)

```bash
VCOUNT=0
v(){ # v <name> <party args...>
  local name=$1; shift; VCOUNT=$((VCOUNT+2))
  if [ "$VCOUNT" -gt 12 ]; then log "LIMIT_REACHED before $name"; return 99; fi
  env -u DATABASE_URL SAFE_MODE=0 ALLOW_NETWORK=1 hdctl showcompat --source vendor "$@" \
      --dump-reader "$EV/$name.reader.json" > "$EV/$name.out" 2> "$EV/$name.err"
  local rc=$?; log "$name exit=$rc stderr=$(tr '\n' ' ' < "$EV/$name.err") acquisitions_so_far=$VCOUNT"; return $rc
}
# BA swaps the parties: B's birth data goes in the -a flags and A's in the -b flags.
P1A_as_b=(--birthdate-b 1990-01-01 --birthtime-b 12:00 --location-b "Amsterdam, Netherlands")
P1B_as_a=(--birthdate-a 1985-07-15 --birthtime-a 08:30 --location-a "London, United Kingdom")
P2A=(--birthdate-a 1992-03-21 --birthtime-a 18:45 --location-a "New York, United States")
P2B=(--birthdate-b 1978-11-02 --birthtime-b 04:10 --location-b "Sydney, Australia")
P2A_as_b=(--birthdate-b 1992-03-21 --birthtime-b 18:45 --location-b "New York, United States")
P2B_as_a=(--birthdate-a 1978-11-02 --birthtime-a 04:10 --location-a "Sydney, Australia")
v p1_ab_1 "${P1A[@]}" "${P1B[@]}" \
  && v p1_ab_2 "${P1A[@]}" "${P1B[@]}" \
  && v p1_ba   "${P1B_as_a[@]}" "${P1A_as_b[@]}" \
  && v p2_ab   "${P2A[@]}" "${P2B[@]}" \
  && v p2_ba   "${P2B_as_a[@]}" "${P2A_as_b[@]}" \
  && log "V-run complete" || log "STOP: a V invocation failed; run nothing further except step S"
```

**Predicate V-run.** All five invocations exit 0 with empty stderr, and the log shows `V-run complete`. The chain stops at the first failure. If the log shows `STOP`, skip E1, V-check and D, run step S, and report. Classify a stop as follows:
* `TOOLING_BLOCKED` for a vendor or network failure (stderr starting `PROVIDER_`, `VENDOR_` or `NETWORK`);
* `FAIL_BEHAVIOR` for any other code.

```bash
# E1: one deliberate vendor-side input error (the 6th invocation)
v e1 "${P1A[@]}" --birthdate-b 1985-07-15 --birthtime-b 08:30 --location-b "Zzqx Synthetic Nowhere 000"; log "E1 recorded rc=$?"
log "vendor_acquisitions_upper_bound=$VCOUNT"
```

**Predicate E1.**
* exit is not 0;
* `e1.out` is empty;
* `e1.err` is exactly one line, a single uppercase token, with no URL, header, key or vendor payload text.

Record the token. If E1 exits 0, record `E1_ACCEPTED_UNRESOLVABLE_LOCATION` as a finding; it is not a stop.

```bash
cat > "$RUN/check.py" <<'PY'
import json, pathlib, sys
ev = pathlib.Path(sys.argv[1]); rid = sys.argv[2]
CATS = {"heat","harmony","communication","alignment","comfort","consistency","expansion","creativity","drive","balance"}
BANDS = {"Cool","Open","Warm","Glow"}
TOP = {"schema","config_id","release_id","pair_key","signals","categories"}
ROW = {"category_id","score","band","shared_key","personal_lo_to_hi_key","personal_hi_to_lo_key"}
READER = {"reader_version","eligible","categories","meta","release_id","idempotence_hash"}
fails = []
def raw(p):
    b = p.read_bytes()
    if not b.endswith(b"\n") or b.endswith(b"\n\n") or b"\r" in b or b.startswith(b"\xef\xbb\xbf"):
        fails.append(f"{p.name}: not exactly one final LF, or CR/BOM present")
    return b
def compat(n):
    b = raw(ev/f"{n}.out"); d = json.loads(b)
    if set(d) != TOP: fails.append(f"{n}: top-level keys {sorted(d)}"); return b, d
    if d["schema"] != "magic10_compat_result.v1": fails.append(f"{n}: schema {d['schema']!r}")
    if d["release_id"] != rid: fails.append(f"{n}: release_id {d['release_id']} != local {rid}")
    cats = d["categories"]
    if len(cats) != 10 or {c.get("category_id") for c in cats} != CATS: fails.append(f"{n}: category set")
    for c in cats:
        if set(c) != ROW: fails.append(f"{n}: row keys {sorted(c)}"); continue
        if c["band"] not in BANDS: fails.append(f"{n}: band {c['band']!r}")
        if type(c["score"]) is not int or not 0 <= c["score"] <= 100: fails.append(f"{n}: score {c['score']!r}")
    return b, d
def reader(n, harmony_band):
    b = raw(ev/f"{n}.reader.json"); d = json.loads(b)
    if set(d) != READER: fails.append(f"{n}.reader: keys {sorted(d)}"); return b
    if d["eligible"] is not True: fails.append(f"{n}.reader: eligible {d['eligible']!r}")
    if d["release_id"] != rid: fails.append(f"{n}.reader: release_id mismatch")
    for c in d["categories"]:
        if set(c) != {"id","band"} or c["band"] not in BANDS: fails.append(f"{n}.reader: category {c!r} (must be id and band only)")
    h = [c["band"] for c in d["categories"] if c.get("id") == "harmony"]
    if h != [harmony_band]: fails.append(f"{n}.reader: harmony band {h} != compat {harmony_band!r}")
    return b
res = {}
for n in ("p1_ab_1","p1_ab_2","p1_ba","p2_ab","p2_ba"):
    b, d = compat(n)
    hb = next((c.get("band") for c in d.get("categories", []) if c.get("category_id") == "harmony"), None)
    res[n] = (b, reader(n, hb), d.get("pair_key"))
def same(x, y, what):
    if res[x][0] != res[y][0]: fails.append(f"{what}: compat bytes differ ({x} vs {y})")
    if res[x][1] != res[y][1]: fails.append(f"{what}: reader bytes differ ({x} vs {y})")
same("p1_ab_1","p1_ab_2","two-run identity")
same("p1_ab_1","p1_ba","AB/BA identity P1")
same("p2_ab","p2_ba","AB/BA identity P2")
if res["p1_ab_1"][2] == res["p2_ab"][2] or res["p1_ab_1"][0] == res["p2_ab"][0]:
    fails.append("P1 and P2 produced the same pair_key or the same bytes: output is not driven by the charts")
for n in ("p1_ab_1","p2_ab"):
    print(n, "bands:", " ".join(f"{c.get('category_id')}={c.get('band')}" for c in json.loads(res[n][0]).get("categories", [])))
print("CHECK_FAILS=" + str(len(fails)))
for f in fails: print("FAIL:", f)
sys.exit(1 if fails else 0)
PY
python "$RUN/check.py" "$EV" "$RID" > "$EV/check.txt" 2>&1; log "check_exit=$?"; cat "$EV/check.txt" | tee -a "$EV/run.log"
```

**Predicate V-check.** `check_exit=0` and `CHECK_FAILS=0`.
* Each `FAIL:` line is `FAIL_BEHAVIOR`.
* A Python traceback (the checker itself broke) is `FAIL_TOOLING`, not a product failure.

The two `bands:` lines are the actual compat results; include them in the report.

### Step D: the deployed service (read-only, 5 requests, no vendor)

```bash
BASE=https://glow-hdengine-v2-production.up.railway.app
SYN=3fa85f64-5717-4562-b3fc-2c963f66afab   # EPIC011 synthetic identity (docs/run/EPIC011_TEST_IDENTITIES.md)
h(){ # h <name> <curl args...>
  local name=$1; shift
  local code; code=$(curl -sS --max-time 30 -o "$EV/$name.body" -w '%{http_code}' "$@"); log "$name http=$code body=$(head -c 400 "$EV/$name.body")"
}
h d1_version "$BASE/internal/version"
h d2_reader_v1 -X POST -H 'Content-Type: application/json' --data "{\"a_id\":\"$SYN\",\"b_id\":\"$SYN\"}" "$BASE/api/reader?v=1"
h d3_reader_v2 -X POST -H 'Content-Type: application/json' --data "{\"a_id\":\"$SYN\",\"b_id\":\"$SYN\"}" "$BASE/api/reader?v=2"
h d4_bad_version -X POST -H 'Content-Type: application/json' --data "{\"a_id\":\"$SYN\",\"b_id\":\"$SYN\"}" "$BASE/api/reader?v=3"
h d5_bad_body -X POST -H 'Content-Type: application/json' --data '{"a_id":"not-a-uuid"}' "$BASE/api/reader?v=1"
python3 -c "import json,sys; d=json.load(open(sys.argv[1])); print('deployed_release_id='+str(d.get('release_id'))); print('deployed_build_commit='+str(d.get('build_commit')))" "$EV/d1_version.body" | tee -a "$EV/run.log"
```

**Predicates D.**
* **D1.** `http=200`, and `deployed_release_id` equals `local_release_id`. A mismatch is a **finding**: production is not running the release on `main`. Record both values and `deployed_build_commit`; it is not a stop.
* **D2 and D3.** These are recorded, not passed or failed.
  * `http=200` with `"eligible":false` and `"categories":[]` means the route works and the synthetic row exists. A self-pair is ineligible by design, so this proves the route and the database read, not the compat math.
  * `http=404` with code `ERR_M10_PERSON_UNRESOLVED` means the synthetic row is not in production.
  * Any `5xx` is `FAIL_BEHAVIOR`: the deployed Reader is broken.
* **D4.** `http=400` with code `ERR_READER_INVALID_VERSION`.
* **D5.** `http=422` with code `ERR_READER_INVALID_INPUT`.

### Step S: secret scan and seal

```bash
leak=0
for k in HD_API_KEY GEO_API_KEY HD_API_BASE_URL DATABASE_URL; do
  val="${!k:-}"; [ -n "$val" ] && grep -rqF -- "$val" "$EV" && { log "SECRET_FOUND key=$k"; leak=1; }
done
grep -rqiE 'bearer |hd-api-key:|hd-geocode-key:|authorization:' "$EV" && { log "HEADER_TEXT_FOUND"; leak=1; }
log "secret_scan=$([ $leak -eq 0 ] && echo CLEAN || echo LEAK)"
(cd "$EV" && sha256sum * > "$RUN/SHA256SUMS"); log "sha256sums_digest=$(sha256sum "$RUN/SHA256SUMS" | cut -d' ' -f1)"
log "finished_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
```

**Predicate S.** The scan must report `secret_scan=CLEAN`. On `LEAK`, the result is `FAIL_TOOLING` (HDE Governance §3.4):
* do not share the evidence;
* delete the affected files;
* report only the key name.

## 7. Overall classification

| Result | When |
| :- | :- |
| `PASS` | C, V-run, E1, V-check, D4, D5 and S all met, and D1 returned 200 |
| `FAIL_BEHAVIOR` | Any product predicate failed (C, V-check, a non-vendor V-run code, a D 5xx, D4 or D5) once the environment, inputs and tooling were proven correct |
| `FAIL_TOOLING` | The checker or scripts broke, or evidence leaked a secret |
| `TOOLING_BLOCKED` | Preflight failed, credentials were missing, or the vendor or network was unavailable |

Report the D1 release mismatch, the D2 and D3 outcomes and the E1 token beside the result, as findings. They do not change it.

## 8. Not covered, and why

* **Deployed compat for two stored people.**
  * The production Reader (`POST /api/reader`) scores only charts already stored in the database, and only one synthetic stored identity is documented.
  * Storing a second one is a production database write. This task forbids that, and the production write path refuses it anyway.
  * Covering this needs a Product Owner decision on how a second synthetic stored person gets into production.
* **Conjunction** (`hdctl showcompat --conjunction`). Its vendor path looks up the database first for user keys. The exact read-only command has not been established, so it is left out rather than guessed.
* **The compat-determinism generator** (`scripts/make_compat_determinism_artifacts.py`). It has exited 2 since HDE-EPIC040 PR-04 (FND-005). This task replaces nothing it was meant to prove for the HDE Governance §12.2 `GATE:CORE-DET` evidence list.

## 9. Report back to the Product Owner

Reply with exactly these items:

1. **The result**, as one word from section 7, in the first line.
2. **A table of steps** (0.1, 0.2, C, each V invocation, E1, V-check, D1 to D5, S). Give each step's exit code or HTTP status and its predicate outcome.
3. **Identities:**
   * `main_sha`;
   * `local_release_id`;
   * `deployed_release_id`;
   * `deployed_build_commit`;
   * `hdctl_version`.
4. **Compat results:** the two `bands:` lines from `check.txt`.
5. **Findings:** the D1 mismatch, if any; the D2 and D3 outcomes; the E1 token.
6. **Counts and seal:**
   * the vendor acquisition upper bound, at most 12;
   * the production request count, at most 6;
   * `secret_scan`;
   * `sha256sums_digest`;
   * the run directory path.
7. **Confirmation of no writes:** no writes, no commits, no retries, and rails were never exported open.

Do not commit the evidence. The Product Owner decides whether and where it lands.

## Canon relied on

Read on `main` at `5a046cb2`.

* **HDE Governance:**
  * §3.4 "Open rails (controlled)", including "HDAPI v2 open-rails vendor proof posture", "Production-functional epic live-proof requirement", "Route-family proof is not workflow proof" and the secret-safety paragraph;
  * §12.1, `GATE:CORE-DET`, `GATE:CORE-READER` and `GATE:CORE-MATCH`;
  * §12.2, D.1 and D.3.
* **Glow QA Guide:** §3.5.5 "PO Live QA sessions (vendor-first rails)".
* **Glow Infrastructure:**
  * §2.2 (production service and base URL; a single shared database instance);
  * §2.4 (production key names);
  * §2.6;
  * §2.7, "CLI-local vendor smoke target distinction" (command target, key names, `APP_ENV=dev`).
* **HDE Build Notes:** addendum 2.1, D-1 (the production override must cover showcompat; not yet implemented) and D-2 (a terminal v2 base is required).
* **Code read on `main`:**
  * `engine/cli/main.py` (showcompat arguments, sources, exit codes);
  * `engine/bodygraph/resolver.py` (rails refusal, read-only v2 chart acquisition, environment classification);
  * `adapter/http_reader.py` (production Reader body, version selection, `/internal/version`);
  * `engine/compat/compute.py` (result schema);
  * `engine/bodygraph/ingest.py` (synthetic identity).
* **Expected refusal:** `tests/cli/test_cli_usage_and_errors.py` and `tests/cli/test_showcompat_sources.py`.

Nonclaims: this prompt runs nothing itself, authorizes nothing without the Product Owner's line above, and makes no QA, acceptance, PF09, deployment or closure claim.
