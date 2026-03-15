"""All HTTP routes. Single entry: register_routes(app)."""
from flask import Flask, Response, render_template, send_from_directory


def register_routes(app: Flask) -> None:
    """Register all route handlers with the Flask app."""
    @app.route("/")
    def index() -> str:
        return render_template("index.html")

    @app.route("/robots.txt")
    def robots_txt() -> tuple[Response, int]:
        return send_from_directory(app.static_folder or "static", "robots.txt"), 200
