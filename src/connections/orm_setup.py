import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

import src.config.dbconfig
from src.models.universe_types import universeTypeIds
from src.config import dbconfig


class Database:
    def __init__(self, db_cred):
        self.db_cred = db_cred
        self.engine = create_engine(
            f'postgresql://{self.db_cred.user}:{self.db_cred.password}@{self.db_cred.host}:{self.db_cred.port}/{self.db_cred.database}'
        )
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    @contextmanager
    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()


def get_database():
    env = os.getenv('EVE_APP_ENV', 'dev')
    if env == 'test':
        db_config = dbconfig.PostgresTest()
    else:
        db_config = dbconfig.PostgresDev()

    return Database(db_config.db_cred)


db_instance = get_database()

# Create tables if they don't exist
universeTypeIds.metadata.create_all(bind=db_instance.engine)
