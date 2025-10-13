from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from database import is_production_or_staging


def create_session() -> Generator[Session, None, None]:
    """Create a SQLAlchemy session connected to an a database.

    Yields:
        Session: A SQLAlchemy session connected.
    """
    engine = create_engine(
        is_production_or_staging(),
        poolclass=StaticPool,
    )

    try:
        with Session(engine) as session:
            yield session
    finally:
        engine.dispose()
