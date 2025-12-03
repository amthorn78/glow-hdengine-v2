#!/usr/bin/env python
# Auto-run Flask development server for glow-hdengine-v2.
#
# This script initializes and runs the Flask application in development mode.
# It auto-reloads on code changes and provides detailed output for debugging.
#
# Environment variables:
#   - FLASK_ENV: Set to 'development' for auto-reload (default)
#   - FLASK_DEBUG: Set to '1' for debug mode with interactive debugger
#   - FLASK_APP: Points to adapter.factory:create_app
#   - FLASK_RUN_PORT: Port to run on (default: 5000)
#   - FLASK_RUN_HOST: Host to bind to (default: 127.0.0.1)
#
# Usage:
#   python run_flask.py
#
# Or with environment variables:
#   FLASK_ENV=development FLASK_DEBUG=1 python run_flask.py

import os
import sys
from adapter.factory import create_app

if __name__ == "__main__":
    # Set environment defaults for development
    os.environ.setdefault("FLASK_ENV", "development")
    os.environ.setdefault("FLASK_DEBUG", "1")
    
    # Get configuration from environment or use defaults
    host = os.environ.get("FLASK_RUN_HOST", "127.0.0.1")
    port = int(os.environ.get("FLASK_RUN_PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    
    # Create and run the app
    app = create_app()
    
    print(f"\n{'='*60}")
    print(f"Starting Flask Development Server")
    print(f"{'='*60}")
    print(f"Environment: {os.environ.get('FLASK_ENV', 'production')}")
    print(f"Debug Mode: {debug}")
    print(f"Host: {host}")
    print(f"Port: {port}")
    print(f"URL: http://{host}:{port}")
    print(f"{'='*60}\n")
    
    app.run(
        host=host,
        port=port,
        debug=debug,
        use_reloader=True,
        use_debugger=debug
    )
