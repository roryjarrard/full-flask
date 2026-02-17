from flask import Flask


def create_app(test_config=None):
    # Create and configure the app instance
    app = Flask(__name__, instance_relative_config=True)

    # Safe defaults for development; production should override via env
    app.config.from_mapping(
        SECRET_KEY='dev',  # override in instance config
    )

    # Test config overrides everything else when provided
    if test_config is not None:
        app.config.from_mapping(test_config)
    else:
        # Load any env vars like FLASKR_SECRET_KEY into app.config["SECRET_KEY"]
        app.config.from_prefixed_env()

    # A health-check route
    @app.get('/health')
    def health_check():
        return {"status": "ok"}

    # Register the auth blueprint
    from . import auth
    app.register_blueprint(auth.bp)

    return app
