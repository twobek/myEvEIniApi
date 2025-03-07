from dataclasses import dataclass

class ApiCredentialsError(Exception):
    """Base exception for all API-related errors."""
    def __init__(self, message, *args):
        super().__init__(message, *args)
        self.message = message

@dataclass
class APICredentials:
    base_url: str
    type: str
    method: str
    options: dict
    final_url: str = None

    def build_url(self, *args):
        """
        Build the final URL with dynamic parameters.
        """
        url = f"{self.base_url}/{self.type}/{self.method}/"
        n = 0
        params_list = []  # Store query parameters
        print(*args)

        if not self.base_url:
            raise ApiCredentialsError(f"No base Url given")

        if not self.type:
            raise ApiCredentialsError(f"No type for URL was given")

        if not self.method:
            raise ApiCredentialsError(f"No method was given")

        if self.options:
            for key, value in self.options.items():
                if value == "$$optional$$":
                    if not args:
                        raise ApiCredentialsError(f"No Arguments were given when needed for key {key}")
                    if n >= len(args):
                        raise ApiCredentialsError(f"Optional for key {key} has no value passed")
                    params_list.append(f"{key}={args[n]}")
                    n += 1
                else:
                    params_list.append(f"{key}={value}")

        # Join parameters with "&" and append to URL if any exist
        if params_list:
            url = f"{url}?{'&'.join(params_list)}"

        self.final_url = url