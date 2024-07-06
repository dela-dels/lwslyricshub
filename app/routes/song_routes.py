from fastapi import APIRouter, HTTPException, Depends
from app.core.database import get_session
from sqlmodel import Session
from app.models.songs_model import Song, SongCreate, SongUpdate, SongRead
from app.controllers.songs_controller import SongsController

router = APIRouter(prefix="/songs", tags=["songs"])


@router.get("/", response_model=list[SongRead])
def get_songs(session: Session = Depends(get_session)):
    return SongsController.get_songs(session=session)


@router.get("/{song_id}", response_model=SongRead)
async def get_song(song_id: int, session: Session = Depends(get_session)):
    return SongsController.get_song(song_id, session=session)


@router.post("/", response_model=SongCreate)
async def create_song(song_create: SongCreate, session: Session = Depends(get_session)):
    return SongsController.create_song(song_create, session=session)


@router.put("/{song_id}", response_model=SongRead)
async def update_song(song_id: int, song_update: SongUpdate, session: Session = Depends(get_session)):
    return SongsController.update_song(song_id, song_update, session=session)
