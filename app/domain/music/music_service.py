from bs4 import BeautifulSoup
import requests
from datetime import datetime
from app.domain.infra.db.builder import DBSessionBuilder
from app.domain.music.music_entity import MusicEntity


class MusicService:
    def __init__(self):
        self.url = "https://www.melon.com/chart/index.htm"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "Referer": "https://www.melon.com/"
        }

    async def get_melon_chart(self):
        soup = BeautifulSoup(requests.get(self.url, headers=self.headers).text, "html.parser")
        title_tags = soup.select("div.ellipsis.rank01 > span > a")
        artist_tags = soup.select("div.ellipsis.rank02 > a")

        db_builder = DBSessionBuilder().build_engine().build_session()
        async with db_builder.get_session()() as session:
            for rank, (title_tag, artist_tag) in enumerate(zip(title_tags, artist_tags), start=1):
                music = MusicEntity(
                    rank=rank,
                    title=title_tag.text.strip(),
                    artist=artist_tag.text.strip(),
                    crawled_at=datetime.now()
                )
                session.add(music)
            await session.commit()

        return {"status": "success", "saved": rank}




