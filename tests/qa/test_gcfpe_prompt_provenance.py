"""Synthetic metadata tests; no real change flow, provider or model executes."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from tools.qa.gcfpe_prompt_provenance import component_uses, load_json, validate


FIXTURE = Path(__file__).parent / "fixtures/gcfpe/component_trace.example.json"


class ProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.record = json.loads(FIXTURE.read_text())

    def test_multiple_versions_and_review_remain_traceable(self):
        self.assertEqual(validate(self.record), [])
        matches = component_uses(self.record, "EXAMPLE-SPEC-ONLY", "example.1", "EXAMPLE-COMPONENT-A")
        self.assertEqual([u["prompt"]["version"] for u in matches], ["example.1", "example.2", "example.1"])
        self.assertEqual(component_uses(self.record, "EXAMPLE-SPEC-ONLY", "example.2", "EXAMPLE-COMPONENT-A"), [])

    def test_unknown_history_is_explicit_and_not_guessed(self):
        usage = self.record["usages"][0]
        usage["prompt"]["version"] = None
        self.assertTrue(any("prompt.version" in error for error in validate(self.record)))
        usage["unknown_fields"]["prompt.version"] = "Historical source was not retained."
        usage["state"] = "unknown_historical"
        self.assertEqual(validate(self.record), [])

    def test_pre_spec_capture_does_not_invent_work_identity(self):
        usage = self.record["usages"][0]
        usage["spec"] = dict.fromkeys(["id", "version", "source_ref"])
        usage["component_ids"] = []
        usage["work_unit_id"] = None
        for field in ["spec.id", "spec.version", "spec.source_ref", "component_ids", "work_unit_id"]:
            usage["unknown_fields"][field] = "Not yet established by this formation stage."
        self.assertEqual(validate(self.record), [])

    def test_latest_is_not_an_exact_version(self):
        self.record["usages"][0]["prompt"]["version"] = "latest"
        self.assertTrue(any("exact identity" in error for error in validate(self.record)))

    def test_later_binding_is_visible_and_must_resolve_real_fields(self):
        usage = self.record["usages"][0]
        usage["binding"] = {"bound_at_utc": "2026-09-05T00:10:00Z",
                            "source_ref": "fixture:later-approved-spec",
                            "resolved_fields": ["spec.id", "component_ids"]}
        self.assertEqual(validate(self.record), [])
        self.assertEqual(len(component_uses(self.record, "EXAMPLE-SPEC-ONLY", "example.1", "EXAMPLE-COMPONENT-A")), 3)
        usage["unknown_fields"]["spec.id"] = "Still not known"
        self.assertTrue(any("resolved field" in error for error in validate(self.record)))

    def test_missing_result_cannot_claim_recorded_use(self):
        self.record["usages"][0]["result_refs"] = []
        self.assertTrue(any("observed result" in error for error in validate(self.record)))
        self.record["usages"][0]["state"] = "started"
        self.assertEqual(validate(self.record), [])

    def test_prompt_body_and_provider_identity_mismatch_are_rejected(self):
        self.record["usages"][0]["prompt"]["body"] = "Do not store prompt bodies."
        self.assertTrue(any("unexpected field" in error for error in validate(self.record)))
        del self.record["usages"][0]["prompt"]["body"]
        self.record["usages"][0]["prompt"]["notion_page_id"] = "f" * 32
        self.assertTrue(any("disagree" in error for error in validate(self.record)))

    def test_duplicate_usage_and_unresolved_transition_are_rejected(self):
        self.record["usages"].append(copy.deepcopy(self.record["usages"][0]))
        self.assertTrue(any("duplicate usage" in error for error in validate(self.record)))
        self.record["usages"].pop()
        self.record["usages"][1]["supersedes_usage_id"] = "nonexistent"
        self.assertTrue(any("earlier use" in error for error in validate(self.record)))

    def test_bad_date_and_short_commit_are_rejected(self):
        self.record["usages"][0]["captured_at_utc"] = "2026-02-31T00:00:00Z"
        self.record["usages"][0]["result_refs"] = [{"kind": "commit", "ref": "abcdef1"}]
        errors = validate(self.record)
        self.assertTrue(any("timestamp" in error for error in errors))
        self.assertTrue(any("full observed SHA" in error for error in errors))

    def test_duplicate_json_keys_are_not_silently_discarded(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "duplicate.json"
            path.write_text('{"change_id":"a","change_id":"b"}')
            with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
                load_json(path)


if __name__ == "__main__":
    unittest.main()
