# singleton.py (최종 형태)
import os
from dotenv import load_dotenv

class SingletonDB:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            load_dotenv()
            cls._instance = super().__new__(cls)
            cls._instance._db_url = cls._instance._build_db_url()
        return cls._instance

    def _build_db_url(self):
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST")
        port = os.getenv("DB_PORT")
        db = os.getenv("DB_NAME")
        return f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}"

    def get_db_url(self):
        return self._db_url

# ✅ 전역 인스턴스 생성 (중요!)
db_singleton = SingletonDB()
