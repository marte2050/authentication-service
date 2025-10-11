from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool


def create_session() -> Generator[Session, None, None]:
    """Create a new SQLAlchemy session for testing purposes.

    This function sets up an in-memory SQLite database, creates all tables
    defined in the metadata, and provides a session for database operations.
    After the session is used, it rolls back any changes and closes the session.

    Yields:
        Session: A SQLAlchemy session connected to the in-memory database.
    """
    engine = create_engine(
        "sqlite:///database.db",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    try:
        with Session(engine) as session:
            yield session
    finally:
        engine.dispose()
