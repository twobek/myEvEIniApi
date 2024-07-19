from src.connections import api_credentials as cred

typesIdList = cred.APICredentials("https://esi.evetech.net", "latest", "universe/typesIdList", {"datasource": "tranquility", "page": "$$optional$$"})
