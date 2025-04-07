# app/domain/music/music_repository.py
from app.domain.music.music_entity import MusicEntity
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from datetime import datetime

class MusicRepository:

    async def save_chart(self, session: AsyncSession, chart_list: list[dict]):
        for item in chart_list:
            music = MusicEntity(
                rank=item['rank'],
                title=item['title'],
                artist=item['artist'],
                crawled_at=item.get('crawled_at', datetime.now())
            )
            session.add(music)
        await session.commit()

    async def get_latest_chart(self, session: AsyncSession) -> list[dict]:
        query = text("""
            SELECT rank, title, artist, crawled_at
            FROM melon_chart
            WHERE crawled_at = (
                SELECT MAX(crawled_at) FROM melon_chart
            )
            ORDER BY rank ASC
        """)
        result = await session.execute(query)
        rows = result.fetchall()
        return [dict(row._mapping) for row in rows]
