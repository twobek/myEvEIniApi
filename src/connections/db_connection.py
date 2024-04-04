from src.connections.db_credentials import DB_Credential
import psycopg2
from dataclasses import asdict

class DB_Connection_Error(Exception):
    pass

class DB_Connection:
    """A class to manage a connection to PostgresSQL database"""
    def __init__(self, cred: DB_Credential):
        """initialize the DB_CONNECTIOn instance.

        Args:
            cred (DB_Credential): Object which holdes the Database credentials
        """
        self.cred = cred
        self.connection = None
        self.cursor = None


    def get_connection(self) -> psycopg2.extensions.connection:
        """Establish a connection to the database.

        Returns:
            psycopg2.extensions.connection: The database connection.

        Raises:
            DB_Connection_Error: If an error occurs while establishing the connection.
        """
        try:
            self.connection = psycopg2.connect(**asdict(self.cred))
        except:
            raise DB_Connection_Error(f'Error while building for db Credential {str(self.cred)}')
        return self.connection


    def get_cursor(self) -> psycopg2.extensions.cursor:
        """Retrieve a cursor for executing SQL statements.

        Returns:
            psycopg2.extensions.cursor: The database cursor.

            Raises:
                DB_Connection_Error: If an error occurs while retrieving the cursor.
        """
        if not self.connection:
            self.get_connection()
        try:
            self.cursor = self.connection.cursor()
        except:
            raise DB_Connection_Error(f'Error while getting cursor')
        return self.cursor

    def exit(self):
        """Close the database connection."""
        if self.connection is not None:
            self.connection.close()
            self.connection = None
            self.cursor = None

    def is_connected(self) -> bool:
        """Check if the database connection is open.

        Returns:
            bool: True if the connection is open, False otherwise.
        """
        if self.connection:
            return True
        else:
            return False

