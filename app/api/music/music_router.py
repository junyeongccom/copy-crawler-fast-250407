from fastapi import APIRouter
from app.domain.music.music_controller import MusicController

router = APIRouter()
controller = MusicController()

@router.get("/music")
async def get_music():
    result = await controller.music_controller()
    return result


