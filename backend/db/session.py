from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings
from typing import Generator

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database url is : ", SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SESSIONLOCAL = sessionmaker(autoflash=False, autocommit=False, bind=engine)


def get_db() -> Generator:
    db = SESSIONLOCAL() 
    try:
        yield db
    finally:
        db.close()