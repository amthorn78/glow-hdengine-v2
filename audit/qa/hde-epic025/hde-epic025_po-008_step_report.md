# HDE-EPIC025 — po-008 Step Report

## Step summary
- **Epic:** HDE-EPIC025
- **Step:** po-008
- **Primary evidence:** [audit/qa/hde-epic025/checks/po-008/primary.log](audit/qa/hde-epic025/checks/po-008/primary.log)
- **Status:** PASS

## Evidence files produced
- [audit/qa/hde-epic025/checks/po-008/primary.log](audit/qa/hde-epic025/checks/po-008/primary.log)
- [audit/qa/hde-epic025/checks/po-008/success_head.txt](audit/qa/hde-epic025/checks/po-008/success_head.txt)
- [audit/qa/hde-epic025/checks/po-008/success_head.txt.sha256](audit/qa/hde-epic025/checks/po-008/success_head.txt.sha256)
- [audit/qa/hde-epic025/checks/po-008/success_get.txt](audit/qa/hde-epic025/checks/po-008/success_get.txt)
- [audit/qa/hde-epic025/checks/po-008/success_get.txt.sha256](audit/qa/hde-epic025/checks/po-008/success_get.txt.sha256)

## Full evidence contents

### audit/qa/hde-epic025/checks/po-008/primary.log
```log
{"artifacts": ["audit/qa/hde-epic025/checks/po-008/primary.log", "audit/qa/hde-epic025/checks/po-008/success_head.txt", "audit/qa/hde-epic025/checks/po-008/success_head.txt.sha256", "audit/qa/hde-epic025/checks/po-008/success_get.txt", "audit/qa/hde-epic025/checks/po-008/success_get.txt.sha256"], "captured_env": {"LANG": "C", "LC_ALL": "C", "MODO_AI_BUNDLE": "", "MODO_AI_VERBOSE": "", "MODO_RAILS": "", "TZ": "UTC"}, "check_id": "po-008", "check_name": "po-008", "claimed_tokens": [], "command": "HDE_WRITE_A7_PROOFS=1 python -m pytest tests/http/test_reader_a7_transport.py\ncp artifacts/proofs/success_head.txt audit/qa/hde-epic025/checks/po-008/success_head.txt\nsha256sum audit/qa/hde-epic025/checks/po-008/success_head.txt > audit/qa/hde-epic025/checks/po-008/success_head.txt.sha256\ncp artifacts/proofs/success_get.txt audit/qa/hde-epic025/checks/po-008/success_get.txt\nsha256sum audit/qa/hde-epic025/checks/po-008/success_get.txt > audit/qa/hde-epic025/checks/po-008/success_get.txt.sha256", "command_provenance": "Copy/paste from plan", "fail_status": "", "intended_tokens": [], "pf_refs": ["PF10", "PF05"], "status": "PASS", "timestamp_utc": "2026-02-04T00:18:33Z"}
== CHECK po-008 ==
Running reader transport harness test + collecting A7 proof snapshots

$ HDE_WRITE_A7_PROOFS=1 /workspaces/glow-hdengine-v2/.venv/bin/python -m pytest tests/http/test_reader_a7_transport.py
============================= test session starts ==============================
platform linux -- Python 3.11.14, pytest-9.0.2, pluggy-1.6.0
rootdir: /workspaces/glow-hdengine-v2
configfile: pytest.ini
collected 1 item

tests/http/test_reader_a7_transport.py .                                 [100%]

============================== 1 passed in 0.35s ===============================
pytest exit code: 0

$ cp artifacts/proofs/success_head.txt audit/qa/hde-epic025/checks/po-008/success_head.txt
$ sha256sum audit/qa/hde-epic025/checks/po-008/success_head.txt > audit/qa/hde-epic025/checks/po-008/success_head.txt.sha256
$ cp artifacts/proofs/success_get.txt audit/qa/hde-epic025/checks/po-008/success_get.txt
$ sha256sum audit/qa/hde-epic025/checks/po-008/success_get.txt > audit/qa/hde-epic025/checks/po-008/success_get.txt.sha256

```

### audit/qa/hde-epic025/checks/po-008/success_head.txt
```text
HTTP/1.0 200 OK
etag: "1cbd848103ac56efd7bc284db333bd70e879a963ddb0c12a570fc05354291fac"
content-type: application/json; charset=utf-8
cache-control: private, max-age=0, must-revalidate
vary: Authorization, Accept-Encoding
content-length: 314

```

### audit/qa/hde-epic025/checks/po-008/success_head.txt.sha256
```text
582d9c10423cb93cb6b0fa8f2973ff1814ad0c72db5fdd2f49bc8f7bede458d8  audit/qa/hde-epic025/checks/po-008/success_head.txt

```

### audit/qa/hde-epic025/checks/po-008/success_get.txt
```text
HTTP/1.0 200 OK
etag: "1cbd848103ac56efd7bc284db333bd70e879a963ddb0c12a570fc05354291fac"
content-type: application/json; charset=utf-8
cache-control: private, max-age=0, must-revalidate
vary: Authorization, Accept-Encoding
content-length: 314

```

### audit/qa/hde-epic025/checks/po-008/success_get.txt.sha256
```text
582d9c10423cb93cb6b0fa8f2973ff1814ad0c72db5fdd2f49bc8f7bede458d8  audit/qa/hde-epic025/checks/po-008/success_get.txt

```
