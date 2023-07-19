from pynequa import Sinequa
from pynequa.models import QueryParams
import os


def test_search_query():
    access_token = os.environ.get("SINEQUA_ACCESS_TOKEN")
    config = {
        "base_url": "http://ec2-100-26-187-210.compute-1.amazonaws.com/api/v1",
        "access_token": access_token,
        "app_name": "vanilla-search",
        "query_name": "query"
    }
    query_params = QueryParams()
    query_params.search_text = "NASA"

    sinequa = Sinequa(config=config)
    print(sinequa.search_query(query_params=query_params))
    # TODO: check/assert search response
