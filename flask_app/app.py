from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Event Manager Flask App is running 🚀"

    return app


app = create_app()
