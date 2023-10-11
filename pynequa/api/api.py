from typing import Dict

import os
import requests


class API:
    '''
        API Class handles all HTTP Requests

        Attributes:
            base_url(string): REST API base URL for Sinequa instance
            access_token(string): token for Sinequa authentication
    '''

    def __init__(self, access_token: str, base_url: str) -> None:
        if not access_token or not base_url:
            raise ValueError("access_token and base_url must not be empty")

        self.access_token = access_token
        self.base_url = base_url

    def _get_headers(self) -> Dict:
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        return headers

    def _get_url(self, endpoint) -> str:
        return os.path.join(self.base_url, endpoint)

    def get(self, endpoint) -> Dict:
        """
            This method handles GET method.
        """
        session = requests.Session()
        resp = session.get(self._get_url(endpoint=endpoint),
                           headers=self._get_headers())
        session.close
        return resp.json()

    def post(self, endpoint, payload) -> Dict:
        """
            This method handles POST method.
        """
        session = requests.Session()
        resp = session.post(self._get_url(endpoint=endpoint),
                            headers=self._get_headers(), json=payload)
        return resp.json()
