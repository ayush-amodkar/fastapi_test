from fastapi import FastAPI
from core.config import settings
from db.session import engine
from apis.base import api_router
from db.base import Base

def create_table():
    Base.metadata.create_all(bind=engine)

def include_router(app):
    app.include_router(api_router)

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)
    create_table()
    return app

app = start_application()

@app.get("/")
def hello():
    return{"msg" : "Hello FastAPI yoo.., this is my message "}





