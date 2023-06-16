from sinequa_py import Sinequa
import pytest 

def test_search_dataset():
    config={
        "base_url":"http://ec2-100-26-187-210.compute-1.amazonaws.com/api/v1",
        "access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJTaW5lcXVhIiwiaWF0IjoxNjgyNDYxNDI2LCJzaWQiOiJDMkY4QzhGQ0U3Mjk0MjEyOTJDOUM0NEQ4NDM2ODQ3MyIsImtpbmQiOiJhY2Nlc3MiLCJleHAiOjE2OTAyMzc0MjYsInN1YiI6IlNpbmVxdWF8and0LXVzZXIifQ.267q0E-h9jX3TnjUUXbn9ZybkSzv0kssx_mhCw_H55c",
        "app_name":"vanilla-search",
        "query_name":"query"
    }
    sinequa=Sinequa(config=config)
    sinequa.search_dataset()