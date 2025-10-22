import os, json, pathlib
from wsgiref.util import setup_testing_defaults
from adapter.app import app

# Try jsonschema; if unavailable, use a minimal structural checker
try:
    import jsonschema
    def _validate(instance, schema):
        jsonschema.validate(instance=instance, schema=schema)
except Exception:
    def _validate(instance, schema):
        # Minimal fallback: enforce required keys and types; ignore patterns
        assert schema.get("type") == "object"
        required = set(schema.get("required", []))
        props = schema.get("properties", {})
        assert set(instance.keys()).issuperset(required)
        # additionalProperties:false
        if schema.get("additionalProperties") is False:
            for k in instance.keys():
                assert k in props
        for k, p in props.items():
            if k not in instance: continue
            t = p.get("type")
            if t == "object":
                assert isinstance(instance[k], dict)
            elif t == "string":
                assert isinstance(instance[k], str)
            elif t == "boolean":
                assert isinstance(instance[k], bool)

def _call(path, env_overrides=None, headers=None):
    if env_overrides: os.environ.update(env_overrides)
    environ = {}
    setup_testing_defaults(environ)
    environ["REQUEST_METHOD"] = "GET"
    environ["PATH_INFO"] = path
    headers = headers or {}
    for k, v in headers.items():
        environ["HTTP_" + k.upper().replace("-", "_")] = v
    status_meta = {}
    def start_response(status, hdrs):
        status_meta["status"] = status
        status_meta["headers"] = dict(hdrs)
    body = b"".join(app(environ, start_response))
    return status_meta["status"], status_meta["headers"], body

def _load_schema(rel):
    with open(rel, "r", encoding="utf-8") as f:
        return json.load(f)

HEALTH = _load_schema("adapter/schemas/healthz_v1.schema.json")
READY  = _load_schema("adapter/schemas/readyz_v1.schema.json")
VER    = _load_schema("adapter/schemas/version_v1.schema.json")
ERR    = _load_schema("adapter/schemas/error_v1.schema.json")

def test_healthz_schema_ok():
    st, h, b = _call("/internal/healthz", env_overrides={"ENGINE_ENV": "dev"})
    assert st.startswith("200")
    assert b.endswith(b"\n")
    _validate(json.loads(b), HEALTH)

def test_readyz_schema_ok_and_deterministic():
    # ensure no override file present for success
    ov = pathlib.Path("config/runtime_overrides.json")
    if ov.exists(): ov.unlink()
    st1, h1, b1 = _call("/internal/readyz", env_overrides={"ENGINE_ENV": "dev"})
    assert st1.startswith("200")
    assert b1.endswith(b"\n")
    _validate(json.loads(b1), READY)
    # determinism: call again and expect identical bytes
    st2, h2, b2 = _call("/internal/readyz", env_overrides={"ENGINE_ENV": "dev"})
    assert st2.startswith("200")
    assert b2 == b1

def test_version_schema_ok_dev():
    st, h, b = _call("/internal/version", env_overrides={"ENGINE_ENV": "dev"})
    assert st.startswith("200")
    assert b.endswith(b"\n")
    _validate(json.loads(b), VER)

def test_error_envelope_schema_on_unauthorized_prod():
    st, h, b = _call("/internal/version", env_overrides={"ENGINE_ENV": "prod", "ENGINE_SERVICE_TOKEN": "s3cr3t"})
    assert st.startswith("401")
    assert b.endswith(b"\n")
    _validate(json.loads(b), ERR)

def test_notfound_uses_error_schema():
    st, h, b = _call("/nope", env_overrides={"ENGINE_ENV": "dev"})
    assert st.startswith("404")
    assert b.endswith(b"\n")
    _validate(json.loads(b), ERR)
