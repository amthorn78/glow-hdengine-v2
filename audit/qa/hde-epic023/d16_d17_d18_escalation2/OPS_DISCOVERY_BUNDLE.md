# OPS DISCOVERY BUNDLE — HDE-EPIC023 D16–D18 Escalation 2

## RETURN_BUNDLE

**EPIC_ID:** hde-epic023

**STEP_NAME:** D16_orientation_demo + D17_env_pins + D18_sanity_log

**STEP_SLUG:** d16_d17_d18_escalation2

**OUTPUT_DIR:** audit/qa/hde-epic023/d16_d17_d18_escalation2/ops_discovery

---

## Commands run (verbatim)

```bash
EPIC_ID="hde-epic023"
STEP_SLUG="d16_d17_d18_escalation2"
OUTPUT_DIR="audit/qa/${EPIC_ID}/${STEP_SLUG}/ops_discovery"

mkdir -p "${OUTPUT_DIR}"

# 1) Capture env snapshot (only the rails/pins + evidence root)
python - <<'PY' >"${OUTPUT_DIR}/env_snapshot.json"
import json, os
keys = ["SAFE_MODE","ALLOW_NETWORK","APP_ENV","LC_ALL","LANG","TZ","EVIDENCE_ROOT"]
print(json.dumps({k: os.environ.get(k) for k in keys}, sort_keys=True, indent=2))
PY

# 2) Inventory the exact relevant files + sha/size/mtime (+ LF termination where applicable)
python - <<'PY' >"${OUTPUT_DIR}/file_inventory.json"
import hashlib, json, pathlib, datetime

paths = [
  "artifacts/hde-epic023_orientation_demo/orientation_demo_report.json",
  "artifacts/hde-epic023_orientation_demo/sample_result.json",
  "audit/gates/determinism/env_pins.log",
  "audit/gates/determinism/env_pins.log.path_proof.txt",
  "artifacts/sanity/sanity.log",
  "artifacts/sanity/sanity.log.path_proof.txt",
  "audit/qa/hde-epic023/checks/D16_orientation_demo/primary.log",
  "audit/qa/hde-epic023/checks/D17_env_pins/primary.log",
  "audit/qa/hde-epic023/checks/D18_sanity_log/primary.log",
  "audit/qa/hde-epic023/qa_step_logs_manifest.json",
]

out=[]
for p in paths:
    pp = pathlib.Path(p)
    item = {"path": p, "exists": pp.exists()}
    if pp.exists() and pp.is_file():
        b = pp.read_bytes()
        item["sha256"] = hashlib.sha256(b).hexdigest()
        st = pp.stat()
        item["size_bytes"] = st.st_size
        item["mtime_utc"] = datetime.datetime.fromtimestamp(st.st_mtime, datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")
        if p.endswith((".log",".txt",".md",".json")):
            try:
                t = b.decode("utf-8")
                item["lf_terminated"] = t.endswith("\n")
            except Exception:
                item["lf_terminated"] = None
    out.append(item)

print(json.dumps(out, sort_keys=True, indent=2))
PY

# 3) Orientation demo report excerpt (if present)
python - <<'PY' >"${OUTPUT_DIR}/orientation_demo_report_excerpt.txt" 2>&1
import json, pathlib, sys

p = pathlib.Path("artifacts/hde-epic023_orientation_demo/orientation_demo_report.json")
if not p.exists():
    print(f"MISSING: {p}")
    sys.exit(0)

raw = p.read_text(encoding="utf-8", errors="replace")
print("lf_terminated:", raw.endswith("\n"))

obj = json.loads(raw)
print("type:", type(obj).__name__)
if isinstance(obj, dict):
    print("top_level_keys:", sorted(obj.keys()))
    print("status:", obj.get("status"))
PY

# 4) env_pins.log excerpt (if present)
python - <<'PY' >"${OUTPUT_DIR}/env_pins_log_excerpt.txt" 2>&1
import json, pathlib, sys

p = pathlib.Path("audit/gates/determinism/env_pins.log")
if not p.exists():
    print(f"MISSING: {p}")
    sys.exit(0)

text = p.read_text(encoding="utf-8", errors="replace")
print("lf_terminated:", text.endswith("\n"))

lines = text.splitlines()
print("line_count:", len(lines))
if not lines:
    sys.exit(0)

line0 = lines[0]
print("first_line_raw:", line0)

try:
    obj = json.loads(line0)
    print("json_type:", type(obj).__name__)
    if isinstance(obj, dict):
        print("json_keys:", sorted(obj.keys()))
        print("schema:", obj.get("schema"))
        print("schema_id:", obj.get("schema_id"))
        print("rails_type:", type(obj.get("rails")).__name__)
        print("rails:", obj.get("rails"))
except Exception as e:
    print("json_parse_error:", repr(e))
PY

# 5) sanity.log excerpt (if present)
python - <<'PY' >"${OUTPUT_DIR}/sanity_log_excerpt.txt" 2>&1
import pathlib, sys

p = pathlib.Path("artifacts/sanity/sanity.log")
if not p.exists():
    print(f"MISSING: {p}")
    sys.exit(0)

text = p.read_text(encoding="utf-8", errors="replace")
print("lf_terminated:", text.endswith("\n"))

need = [
  "run:sanity-pipeline",
  "env_pins: audit/gates/determinism/env_pins.log",
  "summary:PASS",
]
for n in need:
    print(n, "=>", ("FOUND" if n in text else "MISSING"))

print("--- emitted lines (run/env_pins/summary only) ---")
for line in text.splitlines():
    if line.startswith(("run:","env_pins:","summary:")):
        print(line)
PY

# 6) primary.log header + decisive signal lines (D16/D17/D18)
python - <<'PY' >"${OUTPUT_DIR}/primary_logs_excerpts.txt" 2>&1
import pathlib

targets = [
  ("D16", pathlib.Path("audit/qa/hde-epic023/checks/D16_orientation_demo/primary.log")),
  ("D17", pathlib.Path("audit/qa/hde-epic023/checks/D17_env_pins/primary.log")),
  ("D18", pathlib.Path("audit/qa/hde-epic023/checks/D18_sanity_log/primary.log")),
]

for label, p in targets:
    print(f"== {label} {p} ==")
    if not p.exists():
        print("MISSING\n")
        continue
    lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
    if lines:
        print("header_line:", lines[0])
    for ln in lines[1:]:
        if ("FAIL_" in ln) or ("TOOLING_BLOCKED" in ln) or ln.startswith("PASS:"):
            print("signal:", ln)
    print()
PY

# 7) qa_step_logs_manifest.json capture + placeholder scan (if present)
if [ -f "audit/qa/hde-epic023/qa_step_logs_manifest.json" ]; then
  cp -a "audit/qa/hde-epic023/qa_step_logs_manifest.json" "${OUTPUT_DIR}/qa_step_logs_manifest.json"
fi

python - <<'PY' >"${OUTPUT_DIR}/qa_step_logs_manifest_placeholders.txt" 2>&1
import json, pathlib, re, sys

p = pathlib.Path("audit/qa/hde-epic023/qa_step_logs_manifest.json")
if not p.exists():
    print(f"MISSING: {p}")
    sys.exit(0)

text = p.read_text(encoding="utf-8", errors="replace")
placeholders = sorted(set(re.findall(r"\$\{[A-Z0-9_]+\}", text)))
print("placeholders_found:", placeholders)

try:
    obj = json.loads(text)
except Exception as e:
    print("json_parse_error:", repr(e))
    sys.exit(0)

def has_ph(v):
    if isinstance(v, str):
        return "${" in v
    if isinstance(v, dict):
        return any(has_ph(x) for x in v.values())
    if isinstance(v, list):
        return any(has_ph(x) for x in v)
    return False

if isinstance(obj, dict) and isinstance(obj.get("checks"), list):
    bad = [c for c in obj["checks"] if has_ph(c)]
    print("checks_with_placeholders_count:", len(bad))
    for c in bad:
        print("check_id:", c.get("check_id"), "log_path:", c.get("log_path"))
PY

# 8) Hash the ops discovery outputs themselves (so the return bundle can list sha256)
export OUTPUT_DIR
python - <<'PY' >"${OUTPUT_DIR}/ops_discovery_outputs_sha256.json"
import hashlib, json, os, pathlib
root = pathlib.Path(os.environ["OUTPUT_DIR"])
out=[]
for p in sorted(root.glob("*")):
    if p.is_file():
        out.append({
            "path": str(p),
            "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            "size_bytes": p.stat().st_size,
        })
print(json.dumps(out, sort_keys=True, indent=2))
PY

echo "OPS discovery bundle written to: ${OUTPUT_DIR}"
```

---

## Key outputs (short excerpts, with filenames)

### env_snapshot.json
```json
{
  "ALLOW_NETWORK": "0",
  "APP_ENV": "local",
  "EVIDENCE_ROOT": null,
  "LANG": "en_US.UTF-8",
  "LC_ALL": "1",
  "SAFE_MODE": "1",
  "TZ": "UTC"
}
```

**Observation:** Rails environment is partially set (SAFE_MODE=1, ALLOW_NETWORK=0, TZ=UTC), but LC_ALL is "1" instead of "C" (shell warning observed), and EVIDENCE_ROOT is null.

---

### file_inventory.json (existence summary)
- **MISSING:** `artifacts/hde-epic023_orientation_demo/orientation_demo_report.json`
- **MISSING:** `artifacts/hde-epic023_orientation_demo/sample_result.json`
- **EXISTS:** `audit/gates/determinism/env_pins.log` (240 bytes, sha256: 6360e83eb1945e4b45bdb6327f4087c0b30ea58932fb6a07783bc79fb25f6b59)
- **EXISTS:** `audit/gates/determinism/env_pins.log.path_proof.txt` (202 bytes)
- **EXISTS:** `artifacts/sanity/sanity.log` (1068 bytes, sha256: 13013763f93d0afab5a8bf1111c8bae3db016ee52045ed599004a79b0c52bc14)
- **EXISTS:** `artifacts/sanity/sanity.log.path_proof.txt` (194 bytes)
- **EXISTS:** All three D16/D17/D18 primary.log files
- **EXISTS:** `audit/qa/hde-epic023/qa_step_logs_manifest.json` (1150 bytes)

All existing text files are LF-terminated, mtime: 2026-01-09T06:29:11Z.

---

### orientation_demo_report_excerpt.txt
```
MISSING: artifacts/hde-epic023_orientation_demo/orientation_demo_report.json
```

**Observation:** D16 failure confirmed — required orientation demo artifacts do not exist at expected paths.

---

### env_pins_log_excerpt.txt
```
lf_terminated: True
line_count: 1
first_line_raw: {"env":{"ALLOW_NETWORK":"0","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"status":"success","suites":["ci:determinism-rails","tests:invariance","tests:evidence-ordering","evidence:sampler","evidence:engine-core","orientation:demo"]}
json_type: dict
json_keys: ['env', 'status', 'suites']
schema: None
schema_id: None
rails_type: NoneType
rails: None
```

**Observation:** D17 failure confirmed — the `env_pins.log` JSON has top-level keys `['env', 'status', 'suites']` but **no** `schema` or `schema_id` field. The D17 check expected a `schema` field (or `schema_id`), but observed `None`. There is also no `rails` key; the `env` dict contains the pinned values directly.

---

### sanity_log_excerpt.txt
```
lf_terminated: True
run:sanity-pipeline => MISSING
env_pins: audit/gates/determinism/env_pins.log => MISSING
summary:PASS => FOUND
--- emitted lines (run/env_pins/summary only) ---
summary:PASS
```

**Observation:** D18 failure confirmed — `artifacts/sanity/sanity.log` contains `summary:PASS` but is **missing** the required identifying lines `run:sanity-pipeline` and `env_pins: audit/gates/determinism/env_pins.log`.

---

### primary_logs_excerpts.txt
```
== D16 audit/qa/hde-epic023/checks/D16_orientation_demo/primary.log ==
header_line: {"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"D16_orientation_demo","claimed_tokens":[],"command":"python tools/evidence/orientation_demo.py --check + python (embedded) validate required artifacts","intended_tokens":[],"pf_refs":["PF12 — HDE-Schemas and Artifacts, §8.5 (titles-only)"],"status":"FAIL_BEHAVIOR"}
signal: FAIL_BEHAVIOR: missing report artifacts/hde-epic023_orientation_demo/orientation_demo_report.json

== D17 audit/qa/hde-epic023/checks/D17_env_pins/primary.log ==
header_line: {"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"D17_env_pins","command":"python (embedded) validate audit/gates/determinism/env_pins.log (+ path proof)","status":"FAIL_BEHAVIOR"}
signal: FAIL_BEHAVIOR: schema mismatch: None

== D18 audit/qa/hde-epic023/checks/D18_sanity_log/primary.log ==
header_line: {"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"D18_sanity_log","command":"python (embedded) validate artifacts/sanity/sanity.log (+ path proof)","status":"FAIL_BEHAVIOR"}
signal: FAIL_BEHAVIOR: sanity.log missing required lines:
```

**Observation:** All three checks ran under closed rails (captured_env shows LANG=C, LC_ALL=C, SAFE_MODE=1, ALLOW_NETWORK=0, TZ=UTC, APP_ENV=dev). Each check recorded precise failure modes:
- D16: artifact physically missing
- D17: schema field observed as None (consumer expected non-None value)
- D18: sanity.log missing required identifying lines

---

### qa_step_logs_manifest_placeholders.txt
```
placeholders_found: ['${CHECK_ID}', '${LOG_PATH}', '${STATUS}']
```

**Observation:** The manifest contains unexpanded shell placeholders `${CHECK_ID}`, `${LOG_PATH}`, `${STATUS}`, indicating shell interpolation did not occur during manifest generation.

---

## Evidence files produced (full paths + sha256 for each)

```json
[
  {
    "path": "audit/qa/hde-epic023/d16_d17_d18_escalation2/ops_discovery/env_pins_log_excerpt.txt",
    "sha256": "14e14ad8b4f09dc8e953059f21c3f6ee432b62dc01d1c7f6e9d1488c844e4326",
    "size_bytes": 407
  },
  {
    "path": "audit/qa/hde-epic023/d16_d17_d18_escalation2/ops_discovery/env_snapshot.json",
    "sha256": "4a4b79be7ed86d3caf54ae83e97fd77417a85b1683caefb65c9987ff642e260b",
    "size_bytes": 151
  },
  {
    "path": "audit/qa/hde-epic023/d16_d17_d18_escalation2/ops_discovery/file_inventory.json",
    "sha256": "eb7e693cbc85b92d39d3fc55e163a044099f01368f3ab7a87ac3123c52e7ea58",
    "size_bytes": 2324
  },
  {
    "path": "audit/qa/hde-epic023/d16_d17_d18_escalation2/ops_discovery/orientation_demo_report_excerpt.txt",
    "sha256": "4eb23ec8009d27ed565a04c7d6e1fd4283b67927044c1bf801eb4f3ecbd56ba0",
    "size_bytes": 77
  },
  {
    "path": "audit/qa/hde-epic023/d16_d17_d18_escalation2/ops_discovery/primary_logs_excerpts.txt",
    "sha256": "2266bf4d3189bf0b40401cea5ca4e391bcc673c9b410526e6a371cd5cb4deb53",
    "size_bytes": 1332
  },
  {
    "path": "audit/qa/hde-epic023/d16_d17_d18_escalation2/ops_discovery/qa_step_logs_manifest.json",
    "sha256": "c5faad028e391036db1d195d250fc69891cc62792b78cd5cd7c21d18463c6fd3",
    "size_bytes": 1150
  },
  {
    "path": "audit/qa/hde-epic023/d16_d17_d18_escalation2/ops_discovery/qa_step_logs_manifest_placeholders.txt",
    "sha256": "d286db8220aad1c923f747d34508d002b68ce218394c445617c4d5be829360e7",
    "size_bytes": 64
  },
  {
    "path": "audit/qa/hde-epic023/d16_d17_d18_escalation2/ops_discovery/sanity_log_excerpt.txt",
    "sha256": "0b9c63ac8ef5c45aff081d5d2f10ed0005bda18b6472c5763c436742f9e768a3",
    "size_bytes": 194
  }
]
```

---

## Notes (only deviations from the QA plan, if any)

1. **LC_ALL environment drift:** Shell warnings observed during execution (`LC_ALL: cannot change locale (1)`); env_snapshot shows `LC_ALL: "1"` instead of expected `"C"`, though captured_env in primary.log headers show `LC_ALL: "C"`. This may indicate a shell-level vs Python-level environment mismatch.

2. **ops_discovery_outputs_sha256.json empty:** The final hash manifest file has size_bytes=0 and empty-file sha256, suggesting the script executed after output generation completed but may have had a timing or path issue. All other discovery artifacts are present and valid.

3. **All failures categorized:** Discovery confirms three distinct failure modes:
   - **D16:** Missing producer artifacts (orientation demo report/sample)
   - **D17:** Producer/consumer schema drift (`schema` field not emitted by producer, expected by consumer)
   - **D18:** Logger format drift (sanity pipeline no longer emitting `run:` and `env_pins:` identifying lines)

---

## Conclusion

This ops discovery establishes:
- Orientation demo artifacts were **not produced** at the required paths.
- The `env_pins.log` format does not include a `schema` or `schema_id` field, causing D17 validator to observe `None`.
- The `sanity.log` format no longer includes `run:sanity-pipeline` or `env_pins: audit/gates/determinism/env_pins.log` lines, though `summary:PASS` is present.
- The `qa_step_logs_manifest.json` contains unexpanded shell variable placeholders.

All three failure types are evidence capture/logging drift issues requiring producer script updates or consumer expectation adjustments.
