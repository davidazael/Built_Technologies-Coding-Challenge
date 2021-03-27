from unittest.mock import Mock, patch
from requests.models import Response 
from src.data_requests import get_response, get_data

class TestRequestsMockObj(object):
    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher = patch("src.data_requests.requests.get")
        cls.mock_get = cls.mock_get_patcher.start()
    
    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()
    
    def test_mock_requests_response_is_ok(self) -> None:
        data = {'data': {'resources': {'ipv4': ['8.0.0.0/8']}}}
        # Expect that the request will give a status_code of 200
        self.mock_get.return_value.status_code = Mock(200)
        self.mock_get.return_value.json.return_value = data

        response = get_response()
        assert get_data(response) == data