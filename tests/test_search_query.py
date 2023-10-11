from pynequa import Sinequa
from pynequa.models import QueryParams
import os
import unittest

base_url = os.environ.get("SINEQUA_BASE_URL")
app_name = "vanilla-search"
query_name = "query"


class TestSinequaSearchQuery(unittest.TestCase):
    """
    A unittest class for testing Sinequa search queries.

    This class contains two test methods that evaluate the behavior of Sinequa
    search queries under different authentication scenarios.

    Test Methods:
        - `test_search_query_without_auth`: Tests a search query without
          authentication. It creates a Sinequa instance using provided
          configuration, sends a search query, and checks the error code in
          the response.

        - `test_search_query_with_auth`: Tests a search query with
          authentication. It retrieves an access token from environment
          variables, creates a Sinequa instance using provided configuration,
          sends a search query, and checks the method result in the response.

    """

    def test_search_query_without_auth(self):
        """
        Test a search query without authentication.

        This test case creates a Sinequa instance with the given configuration,
        sets up query parameters, sends a search query, and asserts that the
        expected error code is returned in the response.
        """

        config = {
            "base_url": base_url,
            "app_name": app_name,
            "access_token": "pass",
            "query_name": query_name
        }
        query_params = QueryParams()
        query_params.search_text = "NASA"

        sinequa = Sinequa.from_config(config)
        resp = sinequa.search_query(query_params=query_params)
        self.assertEqual(resp["ErrorCode"], 6)

    def test_search_query_with_auth(self):
        """
        Test a search query with authentication.

        This test case retrieves an access token from environment variables,
        creates a Sinequa instance with the given configuration, sets up query
        parameters, sends a search query, and asserts that the method result in
        the response is as expected.
        """
        access_token = os.environ.get("SINEQUA_ACCESS_TOKEN")
        config = {
            "base_url": base_url,
            "access_token": access_token,
            "app_name": "vanilla-search",
            "query_name": "query"
        }
        query_params = QueryParams()
        query_params.search_text = "NASA"

        sinequa = Sinequa.from_config(config)
        resp = sinequa.search_query(query_params=query_params)
        self.assertEqual(resp["methodresult"], "ok")


if __name__ == '__main__':
    unittest.main()
