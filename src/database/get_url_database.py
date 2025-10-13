import os

from settings import Settings


def is_production_or_staging() -> bool:
    """Check if the application is running in a production or staging environment."""
    production_or_staging = os.getenv("PRODUCTION_OR_STAGING", "development")

    if production_or_staging in ["production", "staging"]:
        return os.getenv("DATABASE_URL")

    return Settings().DATABASE_URL
