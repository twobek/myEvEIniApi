from src.connections import api_credentials as cred

types = cred.APICredentials("https://esi.evetech.net", "latest", "universe/types", {"datasource": "tranquility", "page": "$$optional$$"})
