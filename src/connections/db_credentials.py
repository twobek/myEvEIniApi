from dataclasses import dataclass

@dataclass
class DB_Credential:
    host: str
    port: int
    user: str
    password: str
    database: str