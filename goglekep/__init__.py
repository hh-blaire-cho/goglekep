from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()


def create_app():
    print("run: create_app()")
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'qwerty'

    # CSRF INIT
    csrf.init_app(app)

    @app.route("/")
    def index():
        return render_template('index.html')

    @app.errorhandler(404)
    def page_404(error):
        return render_template('404.html'), 404

    return app
