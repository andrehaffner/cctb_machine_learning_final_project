from .views import Views
from flask import Flask


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder="../static")
    app.config["SECRET_KEY"] = "super_secret_key"

    app.register_blueprint(Views, url_prefix="/")
    return app
