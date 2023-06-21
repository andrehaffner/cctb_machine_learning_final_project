from app_views import Views
from flask import Flask


app = Flask(__name__, template_folder='templates')
app.config["SECRET_KEY"] = "super_secret_key"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


if __name__ == "__main__":
    app.register_blueprint(Views, url_prefix="/")
    app.run(port=5432, debug=True)
