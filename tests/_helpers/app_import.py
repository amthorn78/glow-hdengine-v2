from __future__ import annotations

def get_app_factory():
    """
    Returns a callable `create_app()` by trying adapter.wsgi first,
    then adapter.app. Raises ImportError with a clear message if neither works.
    """
    last = None
    # Preferred path
    try:
        from adapter.wsgi import create_app  # type: ignore
        return create_app
    except Exception as e:
        last = e
    # Fallback used elsewhere in this repo
    try:
        from adapter.app import create_app  # type: ignore
        return create_app
    except Exception:
        raise ImportError(
            f"Could not import create_app from adapter.wsgi or adapter.app; last error: {last}"
        )
