from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
# from .config import settings
# from app.models import users

sqlite_filename = 'database.db'
sqlite_url = f'sqlite:///{sqlite_filename}'

connect_args = {'check_same_thread': False}

class Base(DeclarativeBase):
    pass

from app.models import users

engine = create_engine(sqlite_url, connect_args=connect_args)
Session = sessionmaker(autoflush=False, bind=engine)

Base.metadata.create_all(engine)

#def create_db():
#    SQLModel.metadata.create_all(engine)
#    with engine.connect() as connection:
#        connection.execute(text('PRAGMA foreign_keys=ON'))

def get_db():
    with Session() as session:
        yield session