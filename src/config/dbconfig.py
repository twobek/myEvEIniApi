from src.connections.db_credentials import DB_Credential
from src.connections.db_connection import DB_Connection
import os

class PostgresTest:

    def __init__(self):
        self.db_cred = DB_Credential(host='db', port=5433, user='admin', password='admin123', database='eve_uni_stage')
        self.db_obj = DB_Connection(self.db_cred)

class PostgresDev:
    def __init__(self):
        self.db_cred = DB_Credential(host='localhost', port=5432, user='admin', password='admin123', database='eve_uni_dev')
        self.db_obj = DB_Connection(self.db_cred)

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///mydatabase.db"

class StageConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

config_by_name = {
    'dev': DevConfig,
    'stage': StageConfig,
    'prod': ProdConfig,
    'test': TestConfig
}