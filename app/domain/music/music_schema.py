# app/domain/music/music_schema.py

from pydantic import BaseModel

class MelonChartItem(BaseModel):
    rank: int
    title: str
    artist: str
