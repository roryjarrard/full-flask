import os


class BaseConfig:
    """Base configuration with defaults."""
    SECRET_KEY = os.environ.get("FLASRK_SECRET_KEY", "dev")


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    TESTING = False


class StagingConfig(BaseConfig):
    # staging should behave like production as much as possible
    DEBUG = False
    TESTING = False


class ProductionConfig(BaseConfig):
    # Production is strict
    DEBUG = False
    TESTING = False
