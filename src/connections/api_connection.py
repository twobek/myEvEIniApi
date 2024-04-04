import requests
from src.connections.api_credentials import APICredentials
class URLCheckException(requests.exceptions.RequestException):
    pass

class APIConnector:
    def __init__(self, cred: APICredentials):
        self.cred = cred

    def call_api(self):
        if not self.cred.final_url:
            raise URLCheckException(f"No final-url was previously defined")
        response = requests.get(self.cred.final_url)

        if response.status_code == 200:
            json_data = response.json()

            if isinstance(json_data, list) or isinstance(json_data, dict):
                return json_data
            else:
                raise URLCheckException("Invalid JSON format: Expected a JSON array")
        else:
            raise URLCheckException(f"API request failed with status code: {response.status_code}")

    def check_url(self) -> bool:
        try:
            resp = requests.head(not self.cred.base_url)
            if resp.status_code == 200:
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            raise URLCheckException(f"An error occurred while checking the URL: {self.cred.base_url}") from e