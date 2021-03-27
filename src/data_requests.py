import requests
from requests.models import Response

def get_response(url: str=None) -> Response:
    requests_response = requests.get(url)
    return requests_response

def get_data(response_obj: Response) -> dict:
    return response_obj.json()