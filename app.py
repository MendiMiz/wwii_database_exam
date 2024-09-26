from flask import Flask
from routes.target_controller import target_blueprint


def create_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(target_blueprint, url_prefix="/api/target")
    return flask_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)