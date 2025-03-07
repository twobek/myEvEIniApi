from src.connections import api_credentials as cred

typesIdList = cred.APICredentials("https://esi.evetech.net", "latest", "universe/types", {"datasource": "tranquility", "page": "$$optional$$"})
