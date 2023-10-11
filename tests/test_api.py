import unittest
from unittest.mock import patch
from pynequa.api import API
import logging

mock_config = {
    "access_token": "hzyasdfewr.asdfdsafdsaf.zsdfsdafdsafdsafdsafdsafdsafdsafdsafdsafdsafdsafdsafds",
    "base_url": "https://api.sinequa.com"
}

sample_response = {"msg": "success"}


class TestAPI(unittest.TestCase):

    @patch('pynequa.api.API.get')
    def test_get(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = sample_response

        api = API(mock_config["access_token"], mock_config["base_url"])
        resp = api.get("search.query")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), sample_response)

    @patch('pynequa.api.API.post')
    def test_post(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = sample_response

        api = API(mock_config["access_token"], mock_config["base_url"])
        endpoint = "search.query"
        payload = {
            "app": "sba",
            "query": {
                "query_name": "sba-angular",
                "text": "When was Landsat-9 launched?"
            }
        }
        resp = api.post(endpoint=endpoint, payload=payload)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), sample_response)


if __name__ == '__main__':
    unittest.main()
