from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from database import table_registry


def create_session() -> Generator[Session, None, None]:
    """Create a new SQLAlchemy session for testing purposes.

    This function sets up an in-memory SQLite database, creates all tables
    defined in the metadata, and provides a session for database operations.
    After the session is used, it rolls back any changes and closes the session.

    Yields:
        Session: A SQLAlchemy session connected to the in-memory database.
    """
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    table_registry.metadata.create_all(engine)
    try:
        with Session(engine) as session:
            yield session
    finally:
        table_registry.metadata.drop_all(engine)
        engine.dispose()
