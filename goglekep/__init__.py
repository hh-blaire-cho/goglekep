from flask import Flask


def create_app():
    print("run: create_app()")
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "hello to you too!"

    return app
