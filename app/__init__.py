"""Application package. Exposes the Flask app instance."""
from app.factory import create_app

app = create_app()
