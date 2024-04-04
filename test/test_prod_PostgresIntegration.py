import unittest
from src.config.dbconfig import PostgresTest as db


class ProdPostgres(unittest.TestCase):

    def setUp(self) -> None:
        self.dbObj = db()
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
