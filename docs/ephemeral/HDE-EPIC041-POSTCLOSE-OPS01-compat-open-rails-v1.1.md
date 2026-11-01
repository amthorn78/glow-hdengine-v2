---
artifact_type: OPS_TASK_PROMPT
artifact_version: "1.1"
supersedes: "docs/ephemeral/HDE-EPIC041-POSTCLOSE-OPS01-compat-open-rails-v1.0.md (v1.0, never run; preserved unchanged)"
change_from_v1_0: "Adds Part W, which stores two synthetic people in production under fixed UUIDs, and the two-person production Reader test (Product Owner, 2026-11-01: \"yes we need 2 synthetic people obviously\")"
logical_id: HDE-EPIC041-POSTCLOSE-OPS01
title: "Full compat test under open rails: live vendor compat through hdctl, two synthetic stored people, and the two-person production Reader"
context: "HDE-EPIC041 is closed (CLOSE / CHANGE_CLOSED, 2026-11-01). Its QA ran under closed rails only and exercised no compat path. The Product Owner is not reopening it and directed this separate full compat test on 2026-11-01."
authorizing_principal: Nathan (Product Owner)
executor: "The Product Owner, or an automated session he delegates to in the execution venue below"
execution_venue: "GitHub Codespaces for amthorn78/glow-hdengine-v2 (the canonical QA console), or any Linux shell meeting the environment contract in section 4"
source: "main, at the commit recorded at step 0.2"
vendor_request_limit: 14
production_http_request_limit: 10
writes: "Only Part W: at most two rows in hde.body_graphs of the production database, one per synthetic person, through the engine's own write path, and only under the separate write authorization line. Nothing else is written to the repository, the database or any external system. Evidence is written only to a run directory outside the repository."
recorded: "2026-11-01T19:50Z"
producer: "Isis, continuing Lead Developer for HDE-EPIC041 (https://claude.ai/code/session_01Q789tyhUaytmY7x273kwes)"
---

# HDE-EPIC041-POSTCLOSE-OPS01: full compat test under open rails (v1.1)

Paste everything below the line into the session that will execute it. The Product Owner's message that delivers it must contain this exact line, or the session must stop before step 0:

`Authorized: HDE-EPIC041-POSTCLOSE-OPS01 v1.1`

Part W writes to the production database. It runs only if the same message also contains this second line; without it, Part W stops at its probe and reports which synthetic people are missing:

`Authorized writes: HDE-EPIC041-POSTCLOSE-OPS01 v1.1 Part W, SYN-A and SYN-B only`

**Model and reasoning setting**

- **TypeSafe v8.2: Fable 5.1 at max.** Effort score 3.99 (confidence 0.98); rung probabilities low 0.00, medium 0.00, high 0.00, extra high 0.01, max 0.97, ultracode 0.02. Model probabilities Fable 5.1 0.50, Opus 5.5 0.49, Sonnet 5.5 0.01, Haiku 5.5 0.00 (confidence 0.33). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.005, Fable 5.1 at max 0.485, Fable 5.1 at ultracode 0.010, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.000, Opus 5.5 at high 0.000, Opus 5.5 at extra high 0.005, Opus 5.5 at max 0.475, Opus 5.5 at ultracode 0.010, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.000, Sonnet 5.5 at extra high 0.000, Sonnet 5.5 at max 0.010, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: model near tie between Fable 5.1 and Opus 5.5. Sent 2026-11-01T19:44:41Z. Nathan picks the cell.

---

## 1. Your task

You are the Ops executor for one bounded task. Run a full compat test of the Glow HD Engine under open rails and report the result to the Product Owner. "Full compat test" here means:

* **Part V: live vendor compat.** `hdctl showcompat --source vendor` gets real charts from HumanDesignAPI v2 for synthetic birth data. It computes compat through the engine's supported path (`evaluate_pair` → `compute_core`) and emits the canonical result and the public Reader v1 bytes. You prove four things:
  * the output is well formed;
  * AB and BA give byte-identical bytes;
  * two runs give byte-identical bytes;
  * different pairs give different results.
* **Part W: two synthetic stored people.** The production Reader scores only people whose charts are stored in the production database. You check whether the two synthetic people SYN-A and SYN-B are stored. Under the separate write authorization, you store whichever is missing, through the engine's own write path (`hdctl bg:resolve --source vendor --upsert`).
* **Part D: the deployed service.** You make HTTP checks against the production HD Engine service:
  * its release identity against `main`;
  * the production Reader for the pair SYN-A and SYN-B, in both orders, for v1 and v2: a real two-person compat answer from the deployed service;
  * whether that answer agrees with the CLI result for the same birth data;
  * two governed error answers.
* **Part C: closed-rails refusal.** You show that the same vendor command refuses before any I/O when rails are closed.

Do only what this prompt says. If something does not match, stop and report it; do not improvise.

## 2. What a PASS proves, and what it does not

* **It proves:**
  * the engine at the recorded `main` commit computes compat from live vendor charts, deterministically and symmetrically, with correct output shape and release identity;
  * the deployed service computes a two-person compat answer for stored synthetic people, symmetrically, in both Reader versions;
  * where the releases match, whether the deployed answer agrees with the CLI answer for the same birth data.
* **It does not prove:**
  * conjunction output (section 8);
  * full vendor conformance;
  * QA of any change, acceptance, PF09 movement, deployment, release activation or closure.
* **Where the evidence belongs.** This is Ops evidence (HDE Governance §3.4). A CLI-local vendor run is not deployed-service validation (Glow QA Guide §3.5.5).

## 3. Hard rules (stop on any breach)

1. **Synthetic data only.** Use only the birth data and the two UUIDs in section 5. Never use a real person's data.
2. **One bounded write, and nothing else.**
   * The only write allowed is Part W: `hdctl bg:resolve --source vendor --upsert`, once for SYN-A and once for SYN-B, each only if its probe shows it missing, and only under the write authorization line.
   * Every other `hdctl` command runs with `DATABASE_URL` unset.
   * No other database write, no delete, and no repository commit, push or pull request.
3. **Request limits.**
   * At most 14 vendor acquisitions:
     * 12 in Part V, where each `showcompat --source vendor` invocation counts as 2, one per party, so at most 6 invocations;
     * 2 in Part W, one per stored person.
   * At most 10 HTTP requests to the production service.
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
* **For Part W only:** `DATABASE_URL` must reach the production database (`ample-illumination/production/postgres`, schema `hde`) from this shell.
  * The service's own value uses the Railway-internal host, which a Codespace cannot reach. Use the database's external connection string, kept as a secret.
  * If it is absent or unreachable, Part W reports `TOOLING_BLOCKED` and nothing is written.

## 5. Synthetic inputs

These are invented records, not real people. P1-A is the documented EPIC011 synthetic profile.

| Pair | Party | birthdate | birthtime | location |
| :- | :- | :- | :- | :- |
| P1 | A | 1990-01-01 | 12:00 | Amsterdam, Netherlands |
| P1 | B | 1985-07-15 | 08:30 | London, United Kingdom |
| P2 | A | 1992-03-21 | 18:45 | New York, United States |
| P2 | B | 1978-11-02 | 04:10 | Sydney, Australia |

Error case E1: party A is P1-A, and party B is 1985-07-15, 08:30, at the location `Zzqx Synthetic Nowhere 000`.

**The two synthetic stored people.** Each UUID is fixed: it is `uuid5(NAMESPACE_URL, <seed>)` of the seed shown. The UUID itself is the `--user` value, so the stored row's identity label is the UUID and the Reader can bind it. They carry the P1 birth data, so the deployed answer can be compared with the CLI's P1 answer.

| Person | Seed | UUID | birthdate | birthtime | location |
| :- | :- | :- | :- | :- | :- |
| SYN-A | `hde-live-qa-synthetic-a` | `9cff60ae-6eb6-5618-aec5-8acaa4f290d2` | 1990-01-01 | 12:00 | Amsterdam, Netherlands |
| SYN-B | `hde-live-qa-synthetic-b` | `57f0c055-ff09-5fdb-aedb-def880437e6f` | 1985-07-15 | 08:30 | London, United Kingdom |

The stored rows are permanent QA fixtures. Do not delete them. Both people are registered in `docs/run/EPIC011_TEST_IDENTITIES.md` ("Live QA synthetic stored people") and in `SYNTHETIC_USER_ID_MAP` in `engine/bodygraph/ingest.py`, by the pull request that carries this prompt.

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

**Predicate V-run.** All five invocations exit 0 with empty stderr, and the log shows `V-run complete`. The chain stops at the first failure. If the log shows `STOP`, skip E1, V-check, W and D, run step S, and report. Classify a stop as follows:
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

### Step W: the two synthetic stored people (2 probes; at most 2 writes and 2 vendor acquisitions)

```bash
BASE=https://glow-hdengine-v2-production.up.railway.app
SYNA=9cff60ae-6eb6-5618-aec5-8acaa4f290d2; SYNB=57f0c055-ff09-5fdb-aedb-def880437e6f
HCOUNT=0
h(){ # h <name> <curl args...>
  local name=$1; shift; HCOUNT=$((HCOUNT+1))
  if [ "$HCOUNT" -gt 10 ]; then log "HTTP_LIMIT_REACHED before $name"; return 99; fi
  local code; code=$(curl -sS --max-time 30 -o "$EV/$name.body" -w '%{http_code}' "$@"); log "$name http=$code body=$(head -c 400 "$EV/$name.body")"
}
post(){ # post <name> <v> <a_id> <b_id>
  h "$1" -X POST -H 'Content-Type: application/json' --data "{\"a_id\":\"$3\",\"b_id\":\"$4\"}" "$BASE/api/reader?v=$2"
}
# W.1 probe: a self-pair answers 200 and ineligible when the row exists, 404 when it does not
post w_probe_a 1 "$SYNA" "$SYNA"
post w_probe_b 1 "$SYNB" "$SYNB"
```

**Predicate W.1.** Read each probe.
* **Present:** `http=200`, with `"eligible":false`.
* **Missing:** `http=404`, with code `ERR_M10_PERSON_UNRESOLVED`.
* **Anything else:** stop with `FAIL_BEHAVIOR`; a 5xx means the deployed Reader is broken.

If both are present, skip W.2.

If one is missing and the Product Owner's message has no `Authorized writes:` line, skip W.2 and D, run S, and report `TOOLING_BLOCKED: synthetic people missing, write not authorized`.

```bash
# W.2 store each missing person. Run a line only if its probe showed 404 and writes are authorized.
w(){ # w <name> <uuid> <birthdate> <birthtime> <location>
  VCOUNT=$((VCOUNT+1)); if [ "$VCOUNT" -gt 14 ]; then log "LIMIT_REACHED before $1"; return 99; fi
  SAFE_MODE=0 ALLOW_NETWORK=1 hdctl bg:resolve --user "$2" --source vendor \
      --birthdate "$3" --birthtime "$4" --location "$5" --upsert > "$EV/$1.out" 2> "$EV/$1.err"
  local rc=$?; log "$1 exit=$rc stderr=$(tr '\n' ' ' < "$EV/$1.err") acquisitions_so_far=$VCOUNT"
  python3 -c "import json,sys; d=json.load(open(sys.argv[1])); i=d.get('ingest',{}); c=d.get('cache',{}); print(sys.argv[2], 'status='+str(d.get('status')), 'adapter='+str(d.get('adapter',{}).get('status')), 'user_id='+str(c.get('user_id')), 'rows_after='+str(i.get('rows_after')), 'rows_written='+str(i.get('rows_written')), 'read_back_match='+str(i.get('read_back_match')))" "$EV/$1.out" "$1" | tee -a "$EV/run.log"
  return $rc
}
# w w_store_a "$SYNA" 1990-01-01 12:00 "Amsterdam, Netherlands"
# w w_store_b "$SYNB" 1985-07-15 08:30 "London, United Kingdom"
```

**Predicate W.2.** For each line run, all of these hold:
* `exit=0`;
* `status=ok` and `adapter=mapped`;
* `user_id` equals that person's UUID;
* `rows_after=1`, `rows_written=1` (or `0` if the row already existed), and `read_back_match=True`.

Classify a failure as follows:
* `DB_WRITER_UNAVAILABLE` or a connection error is `TOOLING_BLOCKED`, with nothing written;
* a `PROVIDER_` code is `TOOLING_BLOCKED`;
* any other failure is `FAIL_BEHAVIOR`.

Uncomment only the lines you need. These are the only `hdctl` commands that run with `DATABASE_URL` set. Keep it set until step S, so the secret scan can look for its value.

**Why this write passes the engine's production guard.** The guard keys on `APP_ENV`, and this shell says `dev`. But every environment shares one database instance (Glow Infrastructure §2.2), so this row lands in production. That is why it needs the Product Owner's separate line.

**Unverified risk the Product Owner accepts with that line.** No check has been made that no production consumer, such as the Glow backend, lists stored HD Engine people to users. The rows carry no name, only a UUID and a chart.

### Step D: the deployed service (7 requests, no vendor)

```bash
h d1_version "$BASE/internal/version"
post d2_v1_ab 1 "$SYNA" "$SYNB"
post d3_v1_ba 1 "$SYNB" "$SYNA"
post d4_v2_ab 2 "$SYNA" "$SYNB"
post d5_v2_ba 2 "$SYNB" "$SYNA"
post d6_bad_version 3 "$SYNA" "$SYNB"
h d7_bad_body -X POST -H 'Content-Type: application/json' --data '{"a_id":"not-a-uuid"}' "$BASE/api/reader?v=1"
log "production_requests=$HCOUNT"
cat > "$RUN/check_d.py" <<'PY'
import json, pathlib, sys
ev = pathlib.Path(sys.argv[1]); rid = sys.argv[2]
CATS = ["heat","harmony","communication","alignment","comfort","consistency","expansion","creativity","drive","balance"]
BANDS = {"Cool","Open","Warm","Glow"}
READER = {"reader_version","eligible","categories","meta","release_id","idempotence_hash"}
fails, findings = [], []
ver = json.loads((ev/"d1_version.body").read_bytes())
dep = ver.get("release_id"); print("deployed_release_id=" + str(dep)); print("deployed_build_commit=" + str(ver.get("build_commit")))
if dep != rid: findings.append(f"D1: deployed release {dep} != main release {rid}")
def body(n):
    b = (ev/f"{n}.body").read_bytes(); d = json.loads(b)
    if set(d) != READER: fails.append(f"{n}: keys {sorted(d)}"); return b, d
    if d["eligible"] is not True: fails.append(f"{n}: eligible {d['eligible']!r}")
    if d["release_id"] != dep: fails.append(f"{n}: release_id differs from /internal/version")
    for c in d["categories"]:
        if set(c) != {"id","band"} or c["band"] not in BANDS: fails.append(f"{n}: category {c!r}")
    return b, d
b2, d2 = body("d2_v1_ab"); b3, _ = body("d3_v1_ba"); b4, d4 = body("d4_v2_ab"); b5, _ = body("d5_v2_ba")
if [c.get("id") for c in d2.get("categories", [])] != ["harmony"]: fails.append("d2: v1 must carry exactly one harmony category")
if sorted(c.get("id") for c in d4.get("categories", [])) != sorted(CATS): fails.append("d4: v2 must carry the ten categories")
if b2 != b3: fails.append("deployed Reader v1: AB and BA bytes differ")
if b4 != b5: fails.append("deployed Reader v2: AB and BA bytes differ")
for n, code in (("d6_bad_version","ERR_READER_INVALID_VERSION"), ("d7_bad_body","ERR_READER_INVALID_INPUT")):
    e = json.loads((ev/f"{n}.body").read_bytes())
    if e.get("code") != code: fails.append(f"{n}: code {e.get('code')!r}, expected {code}")
dep_bands = {c.get("id"): c.get("band") for c in d4.get("categories", [])}
print("deployed_v2 bands: " + " ".join(f"{k}={dep_bands.get(k)}" for k in CATS))
cli = json.loads((ev/"p1_ab_1.out").read_bytes())
cli_bands = {c["category_id"]: c["band"] for c in cli.get("categories", [])}
if dep == rid:
    diff = [k for k in CATS if dep_bands.get(k) != cli_bands.get(k)]
    print("reader_cli_parity=" + ("MATCH" if not diff else "DIFFER:" + ",".join(diff)))
    if diff: findings.append("deployed v2 bands differ from CLI P1 bands for " + ",".join(diff))
else:
    print("reader_cli_parity=NOT_COMPARED (releases differ)")
print("CHECK_D_FAILS=" + str(len(fails)))
for f in fails: print("FAIL:", f)
for f in findings: print("FINDING:", f)
sys.exit(1 if fails else 0)
PY
python3 "$RUN/check_d.py" "$EV" "$RID" > "$EV/check_d.txt" 2>&1; log "check_d_exit=$?"; cat "$EV/check_d.txt" | tee -a "$EV/run.log"
```

**Predicates D.**
* Each request returns its expected status:
  * D1 `200`;
  * D2 to D5 `200`;
  * D6 `400`;
  * D7 `422`.
* `check_d_exit=0` and `CHECK_D_FAILS=0`.
* Each `FAIL:` line is `FAIL_BEHAVIOR`. A Python traceback is `FAIL_TOOLING`.
* The `FINDING:` lines are reported, not passed or failed.
  * **A release mismatch** means production is not running the release on `main`.
  * **A parity difference with matching releases** means the deployed answer and the CLI answer differ for the same birth data. Report it first, under findings. The two runs bind different identities (stored UUIDs against birth-derived UUIDs), so the difference needs analysis before anyone calls it a defect.

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
| `PASS` | All of these met: C, V-run, E1, V-check, W.1, W.2 (where run), D and S |
| `FAIL_BEHAVIOR` | Once the environment, inputs and tooling were proven correct, a product predicate failed: C, V-check, a non-vendor V-run or W.2 code, W.1, D, or any 5xx |
| `FAIL_TOOLING` | The checker or scripts broke, or evidence leaked a secret |
| `TOOLING_BLOCKED` | Preflight failed; credentials or `DATABASE_URL` were missing or unreachable; the vendor or network was unavailable; or a synthetic person was missing without write authorization |

Report these beside the result, as findings; they do not change it:
* the D1 release mismatch;
* the Reader and CLI parity line;
* the E1 token;
* which synthetic people W.2 stored.

## 8. Not covered, and why

* **Conjunction** (`hdctl showcompat --conjunction`). Its vendor path looks up the database first for user keys. The exact read-only command has not been established, so it is left out rather than guessed.
* **The compat-determinism generator** (`scripts/make_compat_determinism_artifacts.py`). It has exited 2 since HDE-EPIC040 PR-04 (FND-005). This task replaces nothing it was meant to prove for the HDE Governance §12.2 `GATE:CORE-DET` evidence list.

## 9. Report back to the Product Owner

Reply with exactly these items:

1. **The result**, as one word from section 7, in the first line.
2. **A table of steps** (0.1, 0.2, C, each V invocation, E1, V-check, W.1, W.2, D1 to D7, check D, S). Give each step's exit code or HTTP status and its predicate outcome.
3. **Identities:**
   * `main_sha`;
   * `local_release_id`;
   * `deployed_release_id`;
   * `deployed_build_commit`;
   * `hdctl_version`.
4. **Compat results:**
   * the two `bands:` lines from `check.txt`;
   * the `deployed_v2 bands:` line and the `reader_cli_parity` line from `check_d.txt`.
5. **Findings:**
   * the D1 mismatch, if any;
   * a parity difference, if any;
   * the E1 token;
   * which synthetic people were already stored and which W.2 stored, with `rows_written`.
6. **Counts and seal:**
   * the vendor acquisition upper bound, at most 14;
   * the production request count, at most 10;
   * `secret_scan`;
   * `sha256sums_digest`;
   * the run directory path.
7. **Confirmation of writes:** no write other than W.2's named rows, no commits, no retries, and rails were never exported open.

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
  * `engine/bodygraph/ingest.py` (synthetic identity);
  * `engine/bodygraph/mapped_cache.py` (the write to `hde.body_graphs`, its read-back, and the current-row read);
  * `engine/bodygraph/projection.py` and the resolver's identity binding (why the UUID is the `--user` value).
* **Expected refusal:** `tests/cli/test_cli_usage_and_errors.py` and `tests/cli/test_showcompat_sources.py`.

Nonclaims: this prompt runs nothing itself and authorizes nothing without the Product Owner's lines above. It makes no QA, acceptance, PF09, deployment or closure claim.
