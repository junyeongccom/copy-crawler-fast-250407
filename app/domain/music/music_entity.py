from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import datetime

Base = declarative_base()

class MusicEntity(Base):
    __tablename__ = "melon_chart"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    rank = Column(Integer)
    title = Column(String)
    artist = Column(String)
    crawled_at = Column(DateTime, default=datetime.datetime.utcnow)