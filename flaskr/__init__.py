from flask import Flask


def create_app(test_config=None):
    # 1. Create and configure the app instance
    app = Flask(__name__, instance_relative_config=True)

    # 2. Load configuration (default first, then override via env or test config).
    app.config.from_mapping(
        SECRET_KEY='dev',  # override in instance config
    )

    # Test config overrides everything else when provided
    if test_config is not None:
        app.config.from_mapping(test_config)
    else:
        # Load any env vars like FLASKR_SECRET_KEY into app.config["SECRET_KEY"]
        app.config.from_prefixed_env()

    # 3. Initialize extensions (e.g., database, login manager) here if you have any.
    # from .extensions import db
    # db.init_app(app)

    # 4. Register blueprints (feature modules)
    from . import auth
    app.register_blueprint(auth.bp)

    # 5. A health-check route
    @app.get('/health')
    def health_check():
        return {"status": "ok"}

    return app
