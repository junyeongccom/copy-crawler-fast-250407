from bs4 import BeautifulSoup
import requests
from datetime import datetime
from app.domain.infra.db.builder import DBSessionBuilder
from app.domain.music.music_repository import MusicRepository


class MusicService:
    def __init__(self):
        self.url = "https://www.melon.com/chart/index.htm"
        self.headers = {
            "User-Agent": "...",
        }
        self.repository = MusicRepository()

    async def get_melon_chart(self):
        soup = BeautifulSoup(requests.get(self.url, headers=self.headers).text, "html.parser")
        title_tags = soup.select("div.ellipsis.rank01 > span > a")
        artist_tags = soup.select("div.ellipsis.rank02 > a")

        chart_list = []
        for rank, (title_tag, artist_tag) in enumerate(zip(title_tags, artist_tags), start=1):
            chart_list.append({
                "rank": rank,
                "title": title_tag.text.strip(),
                "artist": artist_tag.text.strip(),
                "crawled_at": datetime.now()
            })

        db_builder = DBSessionBuilder().build_engine().build_session()
        async with db_builder.get_session()() as session:
            await self.repository.save_chart(session, chart_list)

        return {"status": "success", "saved": len(chart_list)}
    
    async def get_latest_chart_from_db(self):
        db_builder = DBSessionBuilder().build_engine().build_session()
        async with db_builder.get_session()() as session:
            chart = await self.repository.get_latest_chart(session)
            return {"status": "from_db", "data": chart}




