#!/usr/bin/env python3
"""Print SAFE_MODE and ALLOW_NETWORK rails as currently set in the environment."""

import os


def main() -> None:
    rails = {name: os.environ.get(name) for name in ("SAFE_MODE", "ALLOW_NETWORK")}
    for name in ("SAFE_MODE", "ALLOW_NETWORK"):
        value = rails[name]
        print(f"{name}={value if value is not None else '<unset>'}")


if __name__ == "__main__":
    main()
