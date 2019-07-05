from flask import Flask
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options


photos = UploadSet('photos', IMAGES)
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()

login_manager.login_view = 'auth.login'
login_manager.session_protection = 'strong'


def create_app(config_name):

    app = Flask(__name__)

    # App Configurations
    app.config.from_object(config_options[config_name])

    # Initialize flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # configure UploadSet
    configure_uploads(app, photos)

    # Register main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Register auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    return app
