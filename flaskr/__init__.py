import os
from flask import Flask


def create_app(test_config=None):
    # 1. Create and configure the app instance
    app = Flask(__name__, instance_relative_config=True)

    # 2. Load a base profile selected by environment
    env = os.environ.get("FLASKR_ENV", "development").lower()

    if env == "production":
        from .config import ProductionConfig as Config
    elif env == "staging":
        from .config import StagingConfig as Config
    else:
        from .config import DevelopmentConfig as Config

    app.config.from_object(Config)

    # 3. if tests provide config, they override everything
    if test_config is not None:
        app.config.from_mapping(test_config)
    else:
        # 4. Load secrets / machine-specific overrides from
        #    instance config file
        app.config.from_pyfile('application.cfg', silent=True)

    # 4. Finally, allow env vars with a prefi to override
    #    This supports deployment platforms that provide env vars
    #    instead of config files.
    app.config.from_prefixed_env()

    # 5. Initialize extensions (e.g., database,
    #    login manager) here if you have any.
    # from .extensions import db
    # db.init_app(app)

    # 6. Register blueprints (feature modules)
    from . import auth
    app.register_blueprint(auth.bp)

    # 7. A health-check route
    @app.get('/health')
    def health_check():
        return {"status": "ok"}

    return app
