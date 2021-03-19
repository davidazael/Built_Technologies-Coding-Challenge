import requests
from requests.models import Response

def get_response(url: str) -> Response:
    """ 
    Parameters:
        url (str): Accepts URL string that is used to make the request.

    Returns:
        Response: Request Response from Request.
    """
    requests_response = requests.get(url)

    return requests_response

def get_data(request_response: Response) -> dict:
    """
    Parameters:
        request_response (Response): accepts this request_response and uses builtin JSON Decoder.
    Returns:
        Dictionary: from Requests Response 
    """
    return request_response.json()