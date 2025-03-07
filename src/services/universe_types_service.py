from src.connections.api_connection import APIConnector, URLCheckException
from src.config.api_eve_universe_config import typesIdList
from src.crud.universe_types import insert_universe_types

class UniverseTypesService:
    def __init__(self):
        self.api_connector = APIConnector(typesIdList)

    def fetch_and_store_universe_types(self):
        """Fetch universe type IDs from API and store them using the CRUD method."""
        try:
            typesIdList.build_url(1)  # Example of setting an optional parameter
            data = self.api_connector.call_api()

            if not isinstance(data, list):
                raise ValueError("Unexpected API response: Expected a list of type IDs")

            insert_universe_types(data)  # ✅ Use the CRUD function for inserting

        except URLCheckException as e:
            print(f"API connection error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")