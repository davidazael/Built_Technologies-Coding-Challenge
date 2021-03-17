import pytest
import requests

@pytest.fixture
def make_request():
    url = 'https://google.com/?'
    return requests.get(url)

def test_request_response(make_request) -> None:
    """ Test if the request status code is 200.  """
    assert make_request.status_code == 200

def test_check_headers(make_request) -> None:
    """ Test for headers and content type equal to application/json. 
    Expected to fail until use of actual URL. """
    assert make_request.headers['Content-Type'] == "application/json"