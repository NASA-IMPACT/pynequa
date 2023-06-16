import requests
import os 
class API:
    base_url=""
    def __init__(self, config) -> None:
        self.access_token=config["access_token"]
        self.base_url= config["base_url"]
    
    def _get_headers(self) -> dict:
        headers={
            "Authorization": f"Bearer {self.access_token}"
        }
        return headers
    
    def _get_url(self, endpoint) -> str:
        return os.path.join(self.base_url, endpoint)

    def get(self, endpoint) -> dict:
        """
            This method handles GET method.
        """
        session= requests.Session()
        resp=session.get(self._get_url(endpoint=endpoint), headers=self._get_headers)
        return resp.json()

    def post(self, endpoint, payload) -> dict:
        """
            This method handles POST method.
        """
        session=requests.Session()
        resp=session.post(self._get_url(endpoint=endpoint), headers=self._get_headers, json=payload)
        return resp.json()

