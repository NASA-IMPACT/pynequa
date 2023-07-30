from pynequa import Sinequa
from pynequa.models import QueryParams
import os
import unittest

base_url = os.environ.get("SINEQUA_BASE_URL")
app_name = "vanilla-search"
query_name = "query"


class TestSinequaSearchQuery(unittest.TestCase):
    def test_search_query_without_auth(self):
        config = {
            "base_url": base_url,
            "app_name": app_name,
            "access_token": "pass",
            "query_name": query_name
        }
        query_params = QueryParams()
        query_params.search_text = "NASA"

        sinequa = Sinequa(config=config)
        resp = sinequa.search_query(query_params=query_params)
        self.assertEqual(resp["ErrorCode"], 6)

    def test_search_query_with_auth(self):
        access_token = os.environ.get("SINEQUA_ACCESS_TOKEN")
        config = {
            "base_url": base_url,
            "access_token": access_token,
            "app_name": "vanilla-search",
            "query_name": "query"
        }
        query_params = QueryParams()
        query_params.search_text = "NASA"

        sinequa = Sinequa(config=config)
        resp = sinequa.search_query(query_params=query_params)
        self.assertEqual(resp["methodresult"], "ok")


if __name__ == '__main__':
    unittest.main()
