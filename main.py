from fastapi import FastAPI
from fastapi.routing import APIRouter
from app.core.database import Base, engine

import os

# Base.metadata.create_all(engine)

app = FastAPI()

@app.on_event('startup')
def on_startup():
    Base.metadata.create_all(engine)

@app.on_event('shutdown')
def on_shutdown():
    try:
        os.remove('database.db')
    except:
        print('Error al borrar la base de datos')