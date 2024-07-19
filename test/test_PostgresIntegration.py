import unittest
import os
from src.config import dbconfig


class TestPostgresIntegration(unittest.TestCase):

    def setUp(self) -> None:
        self.env = os.getenv('EVE_APP_ENV', 'dev')
        if self.env == 'test':
            self.dbObj = dbconfig.PostgresTest()
        elif self.env == 'dev':
            self.dbObj = dbconfig.PostgresDev()

        self.cursor = self.dbObj.db_obj.get_cursor()

    def test_check_if_db_is_connected(self):
        self.dbObj.db_obj.is_connected()

    def test_check_table_param_exists(self):
        self.cursor.execute("select exists (select * from information_schema.tables where table_name = 'param')")
        self.assertTrue(self.cursor.fetchone()[0])

    def test_check_table_universe_types_exists(self):
        self.cursor.execute(
            "select exists (select * from information_schema.tables where table_name = 'universe_types')")
        self.assertTrue(self.cursor.fetchone()[0])

    def test_check_table_universe_types_dogma_attributes_exists(self):
        self.cursor.execute(
            "select exists (select * from information_schema.tables where table_name = 'universe_types_dogma_attributes')")
        self.assertTrue(self.cursor.fetchone()[0])

    def test_check_table_universe_types_dogma_effects_exists(self):
        self.cursor.execute(
            "select exists (select * from information_schema.tables where table_name = 'universe_types_dogma_effects')")
        self.assertTrue(self.cursor.fetchone()[0])

    def test_check_table_universe_types_roh_exists(self):
        self.cursor.execute(
            "select exists (select * from information_schema.tables where table_name = 'universe_types_roh')")
        self.assertTrue(self.cursor.fetchone()[0])

    def tearDown(self) -> None:
        self.dbObj.db_obj.exit()




if __name__ == '__main__':
    unittest.main()
