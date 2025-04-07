from app.domain.music.music_service import MusicService

class MusicController:
    def __init__(self):
        self.music_service = MusicService()

    async def music_controller(self):
        return await self.music_service.get_melon_chart()
