from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine
# from app.core.database import Base, get_db, engine

# Set-up an in memory SQLite database for testing
TEST_SQLITE_URL = 'sqlite:///:memory:'
TEST_ENGINE = create_engine(TEST_SQLITE_URL, connect_args={'check_same_thread': False}, poolclass=StaticPool)
