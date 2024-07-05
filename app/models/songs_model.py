from datetime import datetime
import uuid
from dotenv import load_dotenv
from sqlmodel import SQLModel, Field
from sqlalchemy import Column

load_dotenv()


class SongBase(SQLModel):
    title: str
    content: str


class SongCreate(SongBase):
    title: str
    content: str = Field(sa_column=Column('TEXT'))


class SongRead(SongBase):
    id: int
    uuid: str
    title: str
    content: str
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class SongUpdate(SQLModel):
    title: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Song(SongBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    title: str
    uuid: str = Field(default=str(uuid.uuid4()), index=True)
    content: str

    class Config:
        orm_mode = True
