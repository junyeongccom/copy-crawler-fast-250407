from fastapi import APIRouter
from app.domain.music.music_controller import MusicController

router = APIRouter()
controller = MusicController()

@router.get("/music")
async def get_music():
    return await controller.music_controller()

@router.get("/music/latest")
async def get_latest_music():
    return await controller.latest_chart_controller()

