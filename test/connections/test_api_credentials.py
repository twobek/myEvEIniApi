import pytest
from src.connections.api_credentials import APICredentials, ApiCredentialsError

@pytest.mark.parametrize(
    "base_url, type_, method, options, args, expected_url",
    [
        # ✅ Test with only static parameters
        ("https://some.api.net", "latest", "universe/types", {}, [],
         "https://some.api.net/latest/universe/types/")
        ,
        # ✅ Test with static parameters and query params
        ("https://some.api.net", "latest", "universe/types", {"datasource": "tranquility"}, [],
         "https://some.api.net/latest/universe/types/?datasource=tranquility")
        ,
        # ✅ Test with optional parameters (dynamic arguments)
        ("https://esi.evetech.net", "latest", "universe/types",
         {"datasource": "tranquility", "page": "$$optional$$"}, [2],
         "https://esi.evetech.net/latest/universe/types/?datasource=tranquility&page=2")
        ,
        # ✅ Test with multiple optional parameters
        ("https://some.api.net", "latest", "universe/types",
         {"datasource": "$$optional$$", "page": "$$optional$$"}, ["singularity", 5],
         "https://some.api.net/latest/universe/types/?datasource=singularity&page=5"),

        # ✅ Test with missing optional argument (should raise IndexError)
        ("https://some.api.net", "latest", "universe/types",
         {"datasource": "tranquility", "page": "$$optional$$"}, [],
         ApiCredentialsError)
         ,

        # ✅ Test with invalid base URL (should raise ValueError)
        ("", "latest", "universe/types", {"datasource": "tranquility"}, [],
         ApiCredentialsError),

        # ✅ Test with an invalid type (edge case)
        ("https://some.api.net", "", "universe/types", {}, [],
         ApiCredentialsError)
    ]
)
def test_build_url(base_url, type_, method, options, args, expected_url):
    """
    Test the build_url method with different configurations.
    """
    api_cred = APICredentials(base_url, type_, method, options)

    # Handle expected exceptions (this is where the change occurs)
    if isinstance(expected_url, type) and issubclass(expected_url, Exception):
        with pytest.raises(expected_url):
            api_cred.build_url(*args)  # If exception is expected, check for it
    else:
        api_cred.build_url(*args)
        assert api_cred.final_url == expected_url  # If no exception is expected, assert the URL
