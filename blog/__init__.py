import secrets
from flask import Flask

def create_app():

    # Create a new Flask application
    app = Flask(__name__, static_folder = "")
    app.config["SECRET_KEY"] = secrets.token_hex(32)

    # Import the blueprint
    from blog.routes import home
    app.register_blueprint(home)
    return app
