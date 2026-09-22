from .registry_loader import (
    AliasPolicyError,
    DuplicateIdError,
    RegistryConfig,
    RegistryConfigError,
    SchemaValidationError,
    UnknownIdError,
    load_registry_config,
)

__all__ = [
    "AliasPolicyError",
    "DuplicateIdError",
    "RegistryConfig",
    "RegistryConfigError",
    "SchemaValidationError",
    "UnknownIdError",
    "load_registry_config",
    "build_backend_bundle",
    "build_frontend_bundle",
    "generate_bundles",
]

_BUNDLE_EXPORTS = frozenset({"build_backend_bundle", "build_frontend_bundle", "generate_bundles"})


def __getattr__(name: str):
    # The bundle writers depend on the repository-only ``tools`` package.  They
    # are resolved lazily so runtime consumers of the admission loader (CLI,
    # HTTP) can import ``engine.config`` from an installed console script
    # without the repository root on ``sys.path``.  ``from engine.config import
    # build_backend_bundle`` keeps working through this PEP 562 hook.
    if name in _BUNDLE_EXPORTS:
        from . import bundles

        return getattr(bundles, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
