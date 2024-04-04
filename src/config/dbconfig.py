from src.connections.db_credentials import DB_Credential
from src.connections.db_connection import DB_Connection
from dataclasses import asdict
import psycopg2

class PostgresTest:

    def __init__(self):
        self.db_cred = DB_Credential(host='db', port=5432, user='admin', password='admin123', database='eve_uni')
        self.db_obj = DB_Connection(self.db_cred)

class PostgresDev:
    def __init__(self):
        self.db_cred = DB_Credential(host='localhost', port=5432, user='admin', password='admin123', database='eve_uni')
        self.db_obj = DB_Connection(self.db_cred)
#db_con = DB_Connection(db_cred)

#db_con = psycopg2.connect(**asdict(db_cred))