import pytest

@pytest.fixture
def get_data() -> dict:
    """ Is a Pytest fixture that will use a service function to obtain the dictionary from the response. 
    Returns a Dictionary that will be used throughout the file. 

    Will be updated once functions are implemented in src directory. 
    """
    pass

def test_check_data_blocks(get_data) -> None:
    """ Accepts the Data from the Requests as a dictionary and confirms that the format is correct. """
    isinstance(get_data['data'], list)
    isinstance(get_data['data'][0]['resources'], list)
    isinstance(get_data['data'][0]['resources'][0]['ipv4'], str)