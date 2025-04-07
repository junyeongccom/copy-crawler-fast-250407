from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.domain.infra.db.singleton import db_singleton  


class DBSessionBuilder:
    def __init__(self):
        self._engine = None
        self._session = None

    def build_engine(self):
        db_url = db_singleton.get_db_url()  
        self._engine = create_async_engine(db_url, echo=True)
        return self

    def build_session(self):
        if not self._engine:
            raise Exception("Engine must be built before session")
        self._session = sessionmaker(
            self._engine, expire_on_commit=False, class_=AsyncSession
        )
        return self

    def get_session(self):
        return self._session
