from flask import Flask
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)

    from web.head import bp as head_bp
    app.register_blueprint(head_bp)
    return app
