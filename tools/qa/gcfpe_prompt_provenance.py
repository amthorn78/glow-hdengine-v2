#!/usr/bin/env python3
"""Read-only validation/query of GCFPE prompt-use metadata, without network I/O.

The small schema evaluator deliberately supports only the keywords used by this
repository's provenance schema. An unsupported keyword is a tooling failure.
Validation is a metadata check, never proof of prompt execution or QA acceptance.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "schemas/gcfpe_prompt_usage.v1.json"
KEYWORDS = {"$schema", "$id", "title", "description", "type", "properties",
            "required", "additionalProperties", "items", "minItems", "minLength",
            "enum", "const", "pattern"}


def load_json(path: Path):
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_pairs)


def check_schema(value, schema, path="$", errors=None):
    """Evaluate the declared bounded schema; return field-specific errors."""
    errors = [] if errors is None else errors
    unsupported = set(schema) - KEYWORDS
    if unsupported:
        raise RuntimeError(f"unsupported schema keywords: {sorted(unsupported)}")
    kinds = schema.get("type", [])
    kinds = [kinds] if isinstance(kinds, str) else kinds
    types = {"object": dict, "array": list, "string": str, "null": type(None)}
    if any(kind not in types for kind in kinds):
        raise RuntimeError("unsupported schema type")
    if kinds and not any(isinstance(value, types[kind]) for kind in kinds):
        errors.append(f"{path}: expected {'|'.join(kinds)}")
        return errors
    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: unexpected constant")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: value outside allowed set")
    if isinstance(value, str):
        if len(value.strip()) < schema.get("minLength", 0):
            errors.append(f"{path}: empty value")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{path}: invalid format")
    if isinstance(value, dict):
        properties = schema.get("properties", {})
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}.{key}: missing")
        for key, child in value.items():
            child_schema = properties.get(key, schema.get("additionalProperties", {}))
            if child_schema is False:
                errors.append(f"{path}.{key}: unexpected field")
            else:
                check_schema(child, child_schema, f"{path}.{key}", errors)
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path}: too few entries")
        for index, child in enumerate(value):
            check_schema(child, schema.get("items", {}), f"{path}[{index}]", errors)
    return errors


def validate(record, schema=None):
    errors = check_schema(record, load_json(SCHEMA) if schema is None else schema)
    if errors:
        return errors
    seen = {}
    for index, usage in enumerate(record["usages"]):
        prefix = f"$.usages[{index}]"
        identity = usage["usage_id"]
        if identity in seen:
            errors.append(f"{prefix}.usage_id: duplicate usage identity")
        previous = usage["supersedes_usage_id"]
        if previous is not None and previous not in seen:
            errors.append(f"{prefix}.supersedes_usage_id: must identify an earlier use")
        seen[identity] = usage
        fields = {
            "spec.id": usage["spec"]["id"],
            "spec.version": usage["spec"]["version"],
            "spec.source_ref": usage["spec"]["source_ref"],
            "component_ids": usage["component_ids"] or None,
            "work_unit_id": usage["work_unit_id"],
            "ecosystem_release": usage["ecosystem_release"],
            "actual_model": usage["actual_model"],
            **{f"prompt.{k}": v for k, v in usage["prompt"].items()
               if k != "content_sha256"},
        }
        for field, value in fields.items():
            if value is None and not usage["unknown_fields"].get(field):
                errors.append(f"{prefix}.{field}: null/empty needs an unknown_fields reason")
            if isinstance(value, str) and value.lower() in {"latest", "current", "unknown"}:
                errors.append(f"{prefix}.{field}: use exact identity or null with a reason")
        if len(set(usage["component_ids"])) != len(usage["component_ids"]):
            errors.append(f"{prefix}.component_ids: duplicate component")
        if usage["state"] == "recorded" and not usage["result_refs"]:
            errors.append(f"{prefix}.result_refs: recorded use needs an observed result reference")
        timestamps = {"captured_at_utc": usage["captured_at_utc"]}
        if "binding" in usage:
            timestamps["binding.bound_at_utc"] = usage["binding"]["bound_at_utc"]
            for field in usage["binding"]["resolved_fields"]:
                if fields[field] is None or field in usage["unknown_fields"]:
                    errors.append(f"{prefix}.binding: resolved field still absent/unknown: {field}")
        for field, raw in timestamps.items():
            try:
                stamp = dt.datetime.fromisoformat(raw.replace("Z", "+00:00"))
                if stamp.utcoffset() != dt.timedelta(0):
                    raise ValueError("not UTC")
            except ValueError:
                errors.append(f"{prefix}.{field}: invalid UTC timestamp")
        prompt = usage["prompt"]
        page_id, url = prompt["notion_page_id"], prompt["notion_url"]
        if page_id and url:
            normalized = page_id.replace("-", "").lower()
            if normalized not in url.replace("-", "").lower():
                errors.append(f"{prefix}.prompt: Notion page identity and URL disagree")
        for result in usage["result_refs"]:
            if result["kind"] == "commit" and not re.fullmatch(r"[0-9a-f]{40,64}", result["ref"]):
                errors.append(f"{prefix}.result_refs: commit needs a full observed SHA")
    return errors


def component_uses(record, spec_id, spec_version, component_id):
    return [usage for usage in record["usages"]
            if usage["spec"]["id"] == spec_id
            and usage["spec"]["version"] == spec_version
            and component_id in usage["component_ids"]]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    parser.add_argument("--spec-id")
    parser.add_argument("--spec-version")
    parser.add_argument("--component-id")
    args = parser.parse_args(argv)
    selector = (args.spec_id, args.spec_version, args.component_id)
    if any(selector) and not all(selector):
        parser.error("component queries require --spec-id, --spec-version and --component-id")
    try:
        record = load_json(args.record)
        errors = validate(record)
    except (OSError, ValueError, RuntimeError) as exc:
        print(json.dumps({"status": "FAIL_TOOLING", "error": str(exc)}))
        return 2
    if errors:
        print(json.dumps({"status": "FAIL_BEHAVIOR", "scope": "metadata contract", "errors": errors}))
        return 1
    output = {"status": "PASS", "scope": "metadata contract only", "change_id": record["change_id"],
              "record_kind": record["record_kind"], "usage_count": len(record["usages"])}
    if all(selector):
        output["matches"] = component_uses(record, *selector)
        output["trace_found"] = bool(output["matches"])
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
