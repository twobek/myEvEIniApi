from src.connections.db_credentials import DB_Credential
from src.connections.db_connection import DB_Connection
import os

class PostgresTest:

    def __init__(self):
        self.db_cred = DB_Credential(host='db', port=5432, user='admin', password='admin123', database='eve_uni_dev')
        self.db_obj = DB_Connection(self.db_cred)

class PostgresDev:
    def __init__(self):
        self.db_cred = DB_Credential(host='localhost', port=5432, user='admin', password='admin123', database='eve_uni_dev')
        self.db_obj = DB_Connection(self.db_cred)

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class StagingConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

config_by_name = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}