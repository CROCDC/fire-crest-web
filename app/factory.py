"""Application factory: creates Flask app, config, and registers routes."""
from datetime import date
from typing import Any

from dotenv import load_dotenv
from flask import Flask

load_dotenv()


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)

    @app.context_processor
    def inject_globals() -> dict[str, Any]:
        return {"current_year": date.today().year}

    with app.app_context():
        from app.routes import register_routes
        register_routes(app)

    return app
