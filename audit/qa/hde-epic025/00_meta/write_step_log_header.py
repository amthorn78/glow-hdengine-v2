import os, json, datetime
required = ["CHECK_ID","CHECK_NAME","COMMANDS_JSON","PASS_FAIL","ARTIFACTS_JSON","PF_REFS_JSON"]
for k in required:
    if k not in os.environ:
        raise SystemExit("missing env: " + k)
raw_status = os.environ["PASS_FAIL"]
raw_fail_status = os.environ.get("FAIL_STATUS", "")
if raw_status == "pass":
    status = "PASS"
    fail_status = ""
else:
    status = raw_status
if status == "fail":
    status = raw_fail_status if raw_fail_status else "FAIL_BEHAVIOR"
if status == "FAIL_ENVIRONMENT":
    status = "FAIL_TOOLING"
allowed_status = ["PASS","FAIL_BEHAVIOR","FAIL_TOOLING","TOOLING_BLOCKED","SKIPPED","WARN"]
if status not in allowed_status:
    status = "FAIL_BEHAVIOR"
if status == "PASS":
    fail_status = ""
elif status in ["FAIL_BEHAVIOR","FAIL_TOOLING"]:
    fail_status = status
else:
    fail_status = raw_fail_status if raw_fail_status in ["FAIL_BEHAVIOR","FAIL_TOOLING","FAIL_ENVIRONMENT"] else "FAIL_TOOLING"
commands_list = json.loads(os.environ["COMMANDS_JSON"])
command = "\n".join(commands_list) if commands_list else "N/A"
command_provenance = "Copy/paste from plan"
captured_env = {
    "MODO_AI_BUNDLE": os.environ.get("MODO_AI_BUNDLE", ""),
    "MODO_AI_VERBOSE": os.environ.get("MODO_AI_VERBOSE", ""),
    "MODO_RAILS": os.environ.get("MODO_RAILS", ""),
    "LC_ALL": os.environ.get("LC_ALL", ""),
    "LANG": os.environ.get("LANG", ""),
    "TZ": os.environ.get("TZ", ""),
}
hdr = {
    "check_id": os.environ["CHECK_ID"],
    "check_name": os.environ["CHECK_NAME"],
    "captured_env": captured_env,
    "timestamp_utc": datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z",
    "command": command,
    "command_provenance": command_provenance,
    "status": status,
    "fail_status": fail_status,
    "intended_tokens": [],
    "claimed_tokens": [],
    "artifacts": json.loads(os.environ["ARTIFACTS_JSON"]),
    "pf_refs": json.loads(os.environ["PF_REFS_JSON"]),
}
print(json.dumps(hdr, sort_keys=True))
