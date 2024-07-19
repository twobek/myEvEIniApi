import requests
from typing import List, Union, Tuple
from src.config.api_eve_universe_config import typesIdList
# https://esi.evetech.net/latest/universe/types/?datasource=tranquility&page=1
class EveAPIService:
    @staticmethod
    def get_types_list(page: int = 1) -> Union[Tuple[List[dict], int], None]:
        """
        Calls the EVE API to retrieve a list of types.

        Returns:
            Union[List[dict], None]: List of types retrieved from the API, or None if the request fails.
        """
        url = f"https://{typesIdList.base_url}/{typesIdList.type}/{typesIdList.method}"
        typesIdList.options[page] = page
        print(url)
        try:
            response = requests.get(url, params=typesIdList.options)
            response.raise_for_status()  # Raise an exception for HTTP errors
            json_data = response.json()
            max_pages = int(response.headers.get('x-pages', 1))
            return json_data, max_pages
        except requests.RequestException as e:
            print(f"Error while calling EVE API: {e}")
            return None




