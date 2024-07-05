from sqlmodel import SQLModel, create_engine
from sqlalchemy import URL
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# "mysql+pymysql://username:password@localhost:3306/task_management"
DATABASE_URL = URL.create(
    drivername=os.environ.get("DB_CONNECTION"),
    username=os.environ.get("DB_USERNAME"),
    password=os.environ.get("DB_PASSWORD"),
    host=os.environ.get("DB_HOST"),
    port=os.environ.get("PORT"),
    database=os.environ.get("DB_DATABASE"),
)

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
