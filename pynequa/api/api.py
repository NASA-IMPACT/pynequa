import requests
import os
from typing import Dict


class API:
    '''
        API Class handles all HTTP Requests 

        Attributes:        
            base_url(string): REST API base URL for Sinequa instance
            access_token(string): token for Sinequa authentication
    '''
    base_url: str
    access_token: str

    def __init__(self, config) -> None:
        self.access_token = config["access_token"]
        self.base_url = config["base_url"]

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
