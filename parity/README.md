Error parity artifacts between HTTP Reader/Compat endpoints and CLI error handling.
Scenarios: invalid_json (compat GET without ids) and invalid_viewer_prefs (compat POST with invalid prefs).
Artifacts include HTTP error envelopes, CLI stderr snapshots, schema validation logs, and token map snapshot.
