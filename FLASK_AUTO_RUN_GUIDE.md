# Flask Auto-Run Environment Setup - glow-hdengine-v2

## Overview

This document provides a comprehensive guide to the Flask auto-run environment setup for the **glow-hdengine-v2** project. The setup enables automatic Flask server initialization and operation within the development virtual environment.

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Architecture](#architecture)
3. [Components](#components)
4. [Environment Variables](#environment-variables)
5. [Configuration](#configuration)
6. [Running the Server](#running-the-server)
7. [Troubleshooting](#troubleshooting)
8. [Advanced Usage](#advanced-usage)
9. [Integration Points](#integration-points)

---

## Quick Start

### Minimal Setup (One Command)

```bash
cd /workspaces/glow-hdengine-v2
source .venv/bin/activate
python run_flask.py
```

### Using the Auto-Run Script

```bash
bash run_flask_dev.sh
```

Or with a custom port:

```bash
bash run_flask_dev.sh 8080
```

The server will start on `http://127.0.0.1:5000` by default.

---

## Architecture

### Flask Application Stack

```
┌─────────────────────────────────────────────────────────────┐
│                    Flask Application                         │
│                 (adapter.factory.create_app)                 │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │           Registered Blueprint (http_reader)             │ │
│  │  - /internal/version                                      │ │
│  │  - /internal/dev/sampler (development endpoint)           │ │
│  │  - Custom route handlers                                  │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │           Middleware & Post-Processors                    │
│  │  - ETag stripping for /internal/* routes                  │
│  │  - Request/response handling                              │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
└─────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────┐
│          Flask Development Server (Werkzeug)                 │
│  - Auto-reload on code changes                               │
│  - Interactive debugger (in debug mode)                      │
│  - Request logging and inspection                            │
└─────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────┐
│            HTTP Listener                                     │
│  Default: 127.0.0.1:5000                                     │
│  Configurable via environment variables                      │
└─────────────────────────────────────────────────────────────┘
```

### Execution Flow

1. **Virtual Environment Activation**: `.venv/bin/activate` sets up isolated Python environment
2. **Environment Configuration**: Default values set for `FLASK_ENV`, `FLASK_DEBUG`, etc.
3. **Application Factory**: `adapter.factory:create_app()` instantiates Flask app
4. **Blueprint Registration**: HTTP routes and handlers are registered
5. **Server Initialization**: Werkzeug development server starts
6. **Request Handling**: Incoming HTTP requests routed through Flask middleware
7. **Auto-Reload**: File changes trigger automatic server restart

---

## Components

### 1. **Virtual Environment (.venv)**

**Location**: `/workspaces/glow-hdengine-v2/.venv`

**Purpose**: Isolates Python dependencies and ensures reproducible environments.

**Contains**:
- Python 3.11.14 interpreter
- Flask 3.1.2 and dependencies
- All project-specific packages from `requirements.txt`
- Pip and setuptools

**Activation**:
```bash
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows
```

### 2. **Application Factory (adapter/factory.py)**

**Responsibility**: Creates and configures the Flask application instance.

**Key Features**:
- Instantiates `Flask(__name__)` with automatic app name detection
- Registers blueprints (e.g., `http_reader` blueprint)
- Defines middleware and post-request hooks
- ETag header management for internal endpoints

**Code Structure**:
```python
def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp, url_prefix="")  # Register routes
    
    @app.after_request
    def _strip_etag_on_internal(resp):
        # Custom logic for internal endpoints
        if resp.headers.get("ETag") and _req.path.startswith("/internal/"):
            resp.headers.pop("ETag", None)
        return resp
    
    return app
```

### 3. **Run Script (run_flask.py)**

**Location**: `/workspaces/glow-hdengine-v2/run_flask.py`

**Responsibility**: Entry point for manual Flask server startup.

**Features**:
- Respects environment variables for configuration
- Provides detailed startup information
- Configures auto-reload and debug mode
- Sets host, port, and debugger options

**Usage**:
```bash
python run_flask.py
```

### 4. **Auto-Run Shell Script (run_flask_dev.sh)**

**Location**: `/workspaces/glow-hdengine-v2/run_flask_dev.sh`

**Responsibility**: Automated setup and server launch in one command.

**Features**:
- Validates virtual environment existence
- Activates venv automatically
- Sets development environment variables
- Accepts custom port as argument
- Displays banner with configuration details

**Usage**:
```bash
bash run_flask_dev.sh [PORT]
```

### 5. **HTTP Reader Blueprint (adapter/http_reader.py)**

**Responsibility**: Defines Flask routes and request handlers.

**Registered Routes**:
- `/internal/version`: Version information endpoint
- `/internal/dev/sampler`: Development sampler endpoint (if `DEV_SAMPLER_URL` env var is set)
- Other custom endpoints

**Integration**: Blueprint is mounted at root path (`url_prefix=""`)

---

## Environment Variables

### Development Variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `FLASK_ENV` | `development` | Sets Flask environment mode (auto-reload enabled) |
| `FLASK_DEBUG` | `1` | Enables debug mode with interactive debugger and detailed errors |
| `FLASK_APP` | `adapter.factory:create_app` | Specifies application factory location |
| `FLASK_RUN_HOST` | `127.0.0.1` | Server bind address |
| `FLASK_RUN_PORT` | `5000` | Server listen port |

### Project-Specific Variables

| Variable | Source | Purpose |
|----------|--------|---------|
| `DEV_SAMPLER_URL` | `.env` / environment | Points to development sampler endpoint |
| `ALLOW_NETWORK` | AGENTS.md rails | Network access control (`0` = disabled for dev safety) |
| `SAFE_MODE` | AGENTS.md rails | Safety mode for determinism (`1` = enabled) |
| `LC_ALL`, `LANG`, `TZ` | AGENTS.md rails | Locale and timezone determinism pins |

### Setting Environment Variables

**Temporarily (current session)**:
```bash
export FLASK_DEBUG=1
export FLASK_RUN_PORT=8080
python run_flask.py
```

**Permanently (project-wide)**:
1. Create/edit `.env` file in project root
2. Add lines like:
   ```
   FLASK_ENV=development
   FLASK_DEBUG=1
   FLASK_RUN_PORT=5000
   ```
3. Load via: `source .env` (before activation, or auto-loaded by some tools)

**Via shell script**:
```bash
bash run_flask_dev.sh 8080  # Custom port
```

---

## Configuration

### Default Configuration

The auto-run setup uses these defaults:

```python
{
    "host": "127.0.0.1",      # Localhost only (safe for dev)
    "port": 5000,              # Standard Flask dev port
    "debug": True,             # Interactive debugger enabled
    "use_reloader": True,      # Auto-reload on code change
    "use_debugger": True,      # Debugger available on error
    "environment": "development"
}
```

### Customizing Configuration

#### Option 1: Environment Variables

```bash
export FLASK_RUN_PORT=8080
export FLASK_RUN_HOST=0.0.0.0  # Listen on all interfaces (less safe)
python run_flask.py
```

#### Option 2: Modify run_flask.py

Edit lines in `run_flask.py`:
```python
host = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")  # Change default
port = int(os.environ.get("FLASK_RUN_PORT", 8080))  # Change port
debug = True  # Force debug mode
```

#### Option 3: Application Configuration File

Create `config.py` in project root:
```python
class DevelopmentConfig:
    DEBUG = True
    TESTING = False
    JSON_SORT_KEYS = False

class TestingConfig:
    DEBUG = True
    TESTING = True
```

Load in `adapter/factory.py`:
```python
def create_app(config_name='development'):
    app = Flask(__name__)
    if config_name == 'development':
        from config import DevelopmentConfig
        app.config.from_object(DevelopmentConfig)
    return app
```

---

## Running the Server

### Method 1: Direct Python Execution

```bash
cd /workspaces/glow-hdengine-v2
source .venv/bin/activate
python run_flask.py
```

**Output**:
```
============================================================
Starting Flask Development Server
============================================================
Environment: development
Debug Mode: True
Host: 127.0.0.1
Port: 5000
URL: http://127.0.0.1:5000
============================================================

 * Serving Flask app 'adapter.factory'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-456-789
```

### Method 2: Using Shell Script

```bash
bash /workspaces/glow-hdengine-v2/run_flask_dev.sh
```

With custom port:
```bash
bash /workspaces/glow-hdengine-v2/run_flask_dev.sh 8080
```

### Method 3: Flask CLI (after activation)

```bash
source .venv/bin/activate
export FLASK_APP=adapter.factory:create_app
flask run --debug
```

### Testing the Server

Once running, test endpoints:

```bash
# In another terminal
curl http://127.0.0.1:5000/internal/version
```

Or visit in browser:
```
http://127.0.0.1:5000/internal/version
```

### Stopping the Server

Press `CTRL+C` in the terminal running Flask.

---

## Troubleshooting

### Issue 1: Virtual Environment Not Found

**Error**: `Error: .venv directory not found`

**Solution**:
```bash
cd /workspaces/glow-hdengine-v2
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Issue 2: Port Already in Use

**Error**: `OSError: [Errno 48] Address already in use`

**Solutions**:
1. Use a different port:
   ```bash
   bash run_flask_dev.sh 8080
   ```

2. Kill process on port 5000:
   ```bash
   lsof -ti:5000 | xargs kill -9
   ```

3. Find and terminate the process:
   ```bash
   ps aux | grep flask
   kill -9 <PID>
   ```

### Issue 3: Flask Module Not Found

**Error**: `ModuleNotFoundError: No module named 'flask'`

**Solution**:
```bash
source .venv/bin/activate
pip install flask
```

### Issue 4: Permission Denied on Shell Script

**Error**: `bash: run_flask_dev.sh: Permission denied`

**Solution**:
```bash
chmod +x run_flask_dev.sh
bash run_flask_dev.sh
```

### Issue 5: Auto-Reload Not Working

**Issue**: Changes to code don't trigger server reload

**Cause**: `use_reloader=False` or `WERKZEUG_RUN_MAIN` environment variable conflicts

**Solution**:
```bash
# Ensure FLASK_ENV is set to development
export FLASK_ENV=development
python run_flask.py
```

### Issue 6: Debugger PIN Not Showing

**Issue**: Debugger PIN missing when errors occur

**Solution**:
```bash
export FLASK_DEBUG=1
python run_flask.py
```

---

## Advanced Usage

### 1. Custom Error Handlers

Add to `adapter/factory.py`:

```python
@app.errorhandler(404)
def not_found(error):
    return {"error": "Endpoint not found"}, 404

@app.errorhandler(500)
def internal_error(error):
    return {"error": "Internal server error"}, 500
```

### 2. Logging Configuration

```python
import logging

def create_app():
    app = Flask(__name__)
    
    # Configure logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    
    app.logger.info("Application initialized")
    return app
```

### 3. CORS Support (if needed)

```bash
pip install flask-cors
```

```python
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes
    return app
```

### 4. Background Tasks

```bash
pip install celery
```

Integrate Celery with Flask for async job processing.

### 5. Database Integration

```bash
pip install flask-sqlalchemy
```

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    db.init_app(app)
    return app
```

### 6. Configuration Profiles

Run with different profiles:

```bash
# Development (default)
FLASK_ENV=development python run_flask.py

# Testing
FLASK_ENV=testing python run_flask.py

# Production (not recommended in dev environment)
FLASK_ENV=production python run_flask.py
```

---

## Integration Points

### With AGENTS.md Rails

The auto-run environment respects the determinism rails defined in `AGENTS.md`:

```bash
# These are automatically set for safety
export LC_ALL=C
export LANG=C
export TZ=UTC
export SAFE_MODE=1
export ALLOW_NETWORK=0
```

### With Evidence and Testing

Run health checks on the live server:

```bash
# Terminal 1: Start Flask
bash run_flask_dev.sh

# Terminal 2: Run health check
python scripts/qa/dev_sampler_healthcheck.py
```

### With Development Sampler

The `DEV_SAMPLER_URL` environment variable enables development sampler integration:

```bash
export DEV_SAMPLER_URL=http://127.0.0.1:5000/internal/dev/sampler
python run_flask.py
```

### With HTTP Reader Adapter

The Flask app automatically registers the `http_reader` blueprint, which provides:

- Request routing
- Response handling
- Caching (etag management)
- Internal endpoint access

---

## Performance Considerations

### Development vs. Production

| Aspect | Development | Production |
|--------|-------------|-----------|
| Debug Mode | Enabled (slower) | Disabled (faster) |
| Auto-Reload | Yes (delays requests) | No (immediate requests) |
| Debugger | Active (overhead) | Inactive (lower overhead) |
| Single-threaded | Yes (default) | Multi-worker/threaded |
| Worker Count | 1 | 2-4+ (via Gunicorn) |

### Optimization Tips

1. **Disable auto-reload for testing**:
   ```bash
   FLASK_ENV=production python run_flask.py
   ```

2. **Use production server for load testing**:
   ```bash
   gunicorn 'adapter.factory:create_app()' --workers 4
   ```

3. **Monitor resource usage**:
   ```bash
   top  # or htop
   ```

---

## Next Steps

1. **Start the server**: `bash run_flask_dev.sh`
2. **Test endpoints**: `curl http://127.0.0.1:5000/internal/version`
3. **Modify code** and watch for auto-reload
4. **Check logs** for debugging information
5. **Scale up** using Gunicorn/production server when ready

---

## Summary

The Flask auto-run environment for glow-hdengine-v2 provides:

✅ **Simple activation**: One command to start development server  
✅ **Auto-reload**: Changes reflected instantly  
✅ **Debug mode**: Interactive error inspection  
✅ **Environment isolation**: Virtual environment prevents conflicts  
✅ **Configuration flexibility**: Easy customization via environment variables  
✅ **Safety rails**: AGENTS.md determinism requirements honored  
✅ **Integration points**: Works with sampler, evidence, and QA tools  

For questions or issues, refer to the Troubleshooting section or check project documentation.
