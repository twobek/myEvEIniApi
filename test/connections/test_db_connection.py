import unittest
import psycopg2
import os
#from src.config.dbconfig import PostgresDev as dbObj
#from src.config.dbconfig import PostgresTest as dbObj
from src.config import dbconfig
from src.connections.db_credentials import DB_Credential
from src.connections.db_connection import DB_Connection, DB_Connection_Error

"""
für locale Entwicklung umstellen des dbObj von Test zu Dev
"""

class TestDBConnection(unittest.TestCase):

    def setUp(self) -> None:
        self.env = os.getenv('EVE_APP_ENV', 'dev')
        if self.env == 'test':
            self.dbCredTrue = dbconfig.PostgresTest().db_cred
        elif self.env == 'dev':
            self.dbCredTrue = dbconfig.PostgresDev().db_cred
        self.dbCredFalse = DB_Credential('wrongHost', 1111, 'whatElse', 'test', 'ups')
        self.dbObj = DB_Connection(self.dbCredTrue)
    def test_get_connection_false(self):
        with self.assertRaises(DB_Connection_Error):
            DB_Connection(self.dbCredFalse).get_connection()

    def test_get_connection_success(self):
        self.dbObj.get_connection()
        self.assertIsInstance(self.dbObj.connection, psycopg2.extensions.connection)
        self.dbObj.exit()
        self.assertFalse(self.dbObj.is_connected())
        self.assertIsNone(self.dbObj.cursor)

    def test_get_cursor_without_connection_success(self):
        self.dbObj.get_cursor()
        self.assertIsInstance(self.dbObj.connection, psycopg2.extensions.connection)
        self.assertIsInstance(self.dbObj.cursor, psycopg2.extensions.cursor)
        self.dbObj.exit()
        self.assertFalse(self.dbObj.is_connected())

    def test_exit(self):
        self.dbObj.get_cursor()
        self.assertIsInstance(self.dbObj.connection, psycopg2.extensions.connection)
        self.assertIsInstance(self.dbObj.cursor, psycopg2.extensions.cursor)
        self.dbObj.exit()
        self.assertFalse(self.dbObj.is_connected())
        self.assertIsNone(self.dbObj.connection)
        self.assertIsNone(self.dbObj.cursor)
        self.assertIsInstance(self.dbObj.cred, DB_Credential)

if __name__ == '__main__':
    unittest.main()
