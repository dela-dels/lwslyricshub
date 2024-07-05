from fastapi import HTTPException, Depends
from typing import List
from sqlmodel import Session
from app.core.database import get_session
from app.models.songs_model import Song, SongUpdate, SongCreate


class SongsController:
    @staticmethod
    def get_songs(session: Session = Depends(get_session)) -> List[Song]:
        return session.query(Song).all()
        # return session.query(Song).all()

    @staticmethod
    def get_song(song_id: int, session: Session = Depends(get_session)) -> Song:
        song = session.get(Song, song_id)
        if not song:
            raise HTTPException(status_code=404, detail="Song not found")
        return song

    @staticmethod
    def create_song(song: SongCreate, session: Session = Depends(get_session)) -> Song:
        song = Song.model_validate(song)
        session.add(song)
        session.commit()
        session.refresh(song)
        return song

    @staticmethod
    def update_song(
        song_id: int, song_update: SongUpdate, session: Session = Depends(get_session)
    ) -> Song:
        existing_song = session.get(Song, song_id)
        if not existing_song:
            raise HTTPException(status_code=404, detail="Song not found")
        song_data = song_update.dict(exclude_unset=True)
        for key, value in song_data.items():
            setattr(existing_song, key, value)
        session.commit()
        session.refresh(existing_song)
        return existing_song

    @staticmethod
    def delete_song(song_id: int, session: Session = Depends(get_session)) -> None:
        song = session.get(Song, song_id)
        if not song:
            raise HTTPException(status_code=404, detail="Song not found")
        session.delete(song)
        session.commit()
