from fastapi import FastAPI
from fastapi.routing import APIRouter
from app.core.database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()

