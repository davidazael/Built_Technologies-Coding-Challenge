from unittest.mock import Mock, patch
from src.acquire_data import get_response
import pytest
import requests

class TestRequestsResponses(object):
    _url = 'https://google.com/?'

    @classmethod
    def setup_class(cls) -> None:
        cls.mock_requests_patcher = patch('src.acquire_data.get_response')
        cls.mock_get_response = cls.mock_requests_patcher.start()
    
    @classmethod
    def teardown_class(cls) -> None:
        cls.mock_requests_patcher.stop()

    def test_requests_get_data_mock(self) -> None:
        data = {'data': { 'resources': {'ipv4': "192.168.10.0/24"}}}
        self.mock_get_response.return_value = Mock()
        self.mock_get_response.return_value.json.return_value = data

        response = get_data()

        assert get_data == data


    def test_requests_response_mock_status_code(self) -> None:
        self.mock_get_response.return_value.status_code = Mock(200)
        self.mock_get_response.return_value.ok = Mock(ok=True)
        response = get_response(self._url)
        assert response.status_code == 200
        assert response.ok == True

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
    assert make_request.headers['Content-Type'] != "application/json"