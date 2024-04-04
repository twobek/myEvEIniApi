from dataclasses import dataclass

@dataclass
class APICredentials:
    base_url: str
    type: str
    method: str
    options: dict
    final_url: str = None
