from pynequa import Sinequa
import os


def test_search_dataset():
    access_token = os.environ.get("SINEQUA_ACCESS_TOKEN")
    config = {
        "base_url": "http://ec2-100-26-187-210.compute-1.amazonaws.com/api/v1",
        "access_token": access_token,
        "app_name": "vanilla-search",
        "query_name": "query"
    }
    sinequa = Sinequa(config=config)
    sinequa.search_dataset()
    # TODO: check/assert search result
