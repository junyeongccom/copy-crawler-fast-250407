from fastapi import APIRouter
from app.api.music.music_router import router as music_router

router = APIRouter()

router.include_router(music_router)
