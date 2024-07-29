from typing import List, Dict, Optional
from datetime import datetime, timezone
import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from app import db

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
                                             unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    video_processings: so.Mapped[List['VideoProcessing']] = so.relationship(back_populates='user')
   
    def __repr__(self):
        return '<User {}>'.format(self.username)

class VideoProcessing(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    user_id: so.Mapped['User'] = so.relationship(back_populates='video_processings')
    original_video_path: so.Mapped[str] = so.mapped_column(sa.String(255))
    pii_settings: so.Mapped[Dict] = so.mapped_column(JSONB)
    country: so.Mapped[str] = so.mapped_column(sa.String(100))
    sector: so.Mapped[str] = so.mapped_column(sa.String(100))
    original_transcript: so.Mapped[Dict[str, str]] = so.mapped_column(JSONB)
    masked_transcript: so.Mapped[Dict[str, str]] = so.mapped_column(JSONB)
    original_frames: so.Mapped[Dict[str, str]] = so.mapped_column(JSONB)
    masked_frames: so.Mapped[Dict[str, str]] = so.mapped_column(JSONB)
    original_audio_path: so.Mapped[str] = so.mapped_column(sa.String(255))
    masked_audio_path: so.Mapped[str] = so.mapped_column(sa.String(255))
    extracted_variables: so.Mapped[List[str]] = so.mapped_column(JSONB)
    masked_variables: so.Mapped[List[str]] = so.mapped_column(JSONB)
    masked_video_path: so.Mapped[str] = so.mapped_column(sa.String(255))
    
    def __repr__(self):
        return f'<VideoProcessing {self.id} for User {self.user_id}>'


