from app.domain.music.music_service import MusicService

class MusicController:
    def __init__(self):
        self.music_service = MusicService()

    def music_controller(self):
        return self.music_service.get_melon_chart()
