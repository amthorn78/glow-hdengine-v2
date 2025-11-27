import os


_CLOSED_RAILS = {
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
}


def closed_rails_env() -> dict[str, str]:
    env = os.environ.copy()
    env.update(_CLOSED_RAILS)
    return env
