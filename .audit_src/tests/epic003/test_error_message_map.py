from engine.compat.errors import ERROR_MESSAGES
def test_error_message_map_exact_strings():
    assert "invalid_json" in ERROR_MESSAGES
    assert "invalid_prefs" in ERROR_MESSAGES
    assert "missing_narrative_key" in ERROR_MESSAGES
    assert ERROR_MESSAGES["invalid_json"] == \
        "malformed or mixed id/payload: supply either a_id/b_id or a/b objects"
