"""Scratch prototype only: exempt a change's own QA primary paths in evidence_inputs from the
feedback-dependency refusal, to find any other close blocker. Never pushed."""
import json, sys
from pathlib import Path
root = Path(sys.argv[1])
s = root / "schemas/close_candidate_source.v2.json"
schema = json.loads(s.read_text())
schema["$defs"]["qa_primary_path"] = {"type": "string", "maxLength": 512,
    "pattern": "^audit/qa/hde-(?:epic[0-9]{3}|crd-[0-9]{4,})/checks/[a-z0-9][a-z0-9._-]*/primary\\.log$"}
schema["properties"]["evidence_inputs"]["items"]["properties"]["path"] = {
    "anyOf": [{"$ref": "#/$defs/causal_repository_path"}, {"$ref": "#/$defs/qa_primary_path"}]}
s.write_text(json.dumps(schema, indent=2) + "\n")
w = root / "tools/qa/generate_epic_close_pack.py"
t = w.read_text()
old = """    for value in (source_rel, *values):
        if (
            value.casefold().startswith("catalog/manifest.json")"""
new = """    for value in (source_rel, *values):
        if re.fullmatch(r"audit/qa/hde-(?:epic[0-9]{3}|crd-[0-9]{4,})/checks/[a-z0-9][a-z0-9._-]*/primary\\.log", value):
            continue
        if (
            value.casefold().startswith("catalog/manifest.json")"""
assert t.count(old) == 1
w.write_text(t.replace(old, new))
print("prototype applied")
