import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine
from app.core.database import Base
# from app.core.database import Base, get_db, engine

# Set-up an in memory SQLite database for testing
TEST_SQLITE_URL = 'sqlite:///:memory:'
TEST_ENGINE = create_engine(TEST_SQLITE_URL, connect_args={'check_same_thread': False}, poolclass=StaticPool)

# General test database setup/teardown fixture

@pytest.fixture(scope='package', autouse=True)
def setup_database():
    # Create the database tables
    Base.metadata.create_all(bind=TEST_ENGINE)
    TestingSession = sessionmaker(autoflush=False, bind=TEST_ENGINE)
    yield TestingSession
    # Drop the database tables after tests
    Base.metadata.drop_all(bind=TEST_ENGINE)


@pytest.fixture(scope='class')
def db_session(request):
    """Provide a Session to test classes.

    Attach the session to the test class as `self.session` so test methods
    don't need to request or call the setup fixture repeatedly.
    """
    TestingSession = sessionmaker(autoflush=False, bind=TEST_ENGINE)
    session = TestingSession()
    # If the fixture is used with a test class, attach the session to it
    if request and hasattr(request, 'cls') and request.cls is not None:
        request.cls.session = session
    yield session
    session.close()