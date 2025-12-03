#!/bin/bash
# Auto-run Flask development server in the glow-hdengine-v2 environment

set -e

# Get the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Activate virtual environment
if [ ! -d .venv ]; then
    echo "Error: .venv directory not found. Run 'python3 -m venv .venv' first."
    exit 1
fi

source .venv/bin/activate

# Set development environment variables
export FLASK_ENV=development
export FLASK_DEBUG=1
export FLASK_APP=adapter.factory:create_app

# Get port from argument or use default
PORT=${1:-5000}
export FLASK_RUN_PORT=$PORT

echo "==============================================="
echo "Flask Auto-Run Development Server"
echo "==============================================="
echo "Environment: $FLASK_ENV"
echo "Debug Mode: $FLASK_DEBUG"
echo "Port: $PORT"
echo "URL: http://127.0.0.1:$PORT"
echo "==============================================="
echo ""

# Run Flask development server
python run_flask.py
