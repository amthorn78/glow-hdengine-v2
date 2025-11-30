import json

from adapter.factory import create_app
from engine.serializer.canon import sercanon


def _app(monkeypatch, app_env: str = "dev"):
    monkeypatch.setenv("APP_ENV", app_env)
    return create_app()


def _post(client, payload: dict):
    return client.post(
        "/internal/dev/sampler",
        data=json.dumps(payload),
        headers={"Content-Type": "application/json; charset=utf-8"},
    )


def test_dev_sampler_happy_path_and_canonical(monkeypatch):
    app = _app(monkeypatch, "dev")
    payload = {
        "viewer_id": "viewer-123",
        "candidate_ids": ["charlie", "alpha", "bravo"],
        "seed": "s-1",
    }

    with app.test_client() as client:
        resp = _post(client, payload)

    assert resp.status_code == 200
    assert resp.data.endswith(b"\n")

    body = resp.get_data(as_text=True)
    data = json.loads(body)
    assert data == {
        "viewer_id": "viewer-123",
        "meta": {"seed": "s-1"},
        "candidate_ids": ["alpha", "bravo", "charlie"],
    }

    expected = sercanon(data, sort_keys=True)
    assert resp.data == expected


def test_dev_sampler_determinism(monkeypatch):
    app = _app(monkeypatch, "dev")
    payload = {
        "viewer_id": "viewer-abc",
        "candidate_ids": ["c-3", "c-1", "c-2"],
        "seed": "seed",
    }

    with app.test_client() as client:
        first = _post(client, payload)
        second = _post(client, payload)

    assert first.status_code == 200
    assert second.status_code == 200
    assert first.data == second.data


def test_dev_sampler_seed_only_changes_seed(monkeypatch):
    app = _app(monkeypatch, "dev")
    base = {
        "viewer_id": "viewer-xyz",
        "candidate_ids": ["delta", "echo", "foxtrot"],
    }

    with app.test_client() as client:
        with_seed_a = _post(client, {**base, "seed": "111"})
        with_seed_b = _post(client, {**base, "seed": "222"})

    assert with_seed_a.status_code == 200
    assert with_seed_b.status_code == 200

    payload_a = json.loads(with_seed_a.data)
    payload_b = json.loads(with_seed_b.data)

    assert payload_a["candidate_ids"] == payload_b["candidate_ids"]
    assert payload_a["meta"]["seed"] == "111"
    assert payload_b["meta"]["seed"] == "222"


def test_dev_sampler_rejected_in_prod(monkeypatch):
    app = _app(monkeypatch, "prod")
    payload = {"viewer_id": "viewer-123", "candidate_ids": ["one", "two"]}

    with app.test_client() as client:
        resp = _post(client, payload)

    assert resp.status_code == 403
    # Writer-style envelope from _writer_error.
    assert json.loads(resp.data) == {
        "schema": "v1",
        "ok": False,
        "code": "forbidden",
        "error": "insufficient scope",
    }
