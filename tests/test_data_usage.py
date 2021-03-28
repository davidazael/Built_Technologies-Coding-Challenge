from src.convert_into_ip import create_ipv4_network, create_ipv4_address
from ipaddress import IPv4Address, IPv4Network, ip_address
import json
import pytest

def get_data_from_file() -> dict:
    """ 
    Saved requests to a file which is what is used to use data and assure that data is converted correctly.
    Converts json format text into dictionary. 
    Returns Dictionary  
    """
    filepath = 'response.txt'
    with open(filepath) as f:
        data = json.load(f)

    return data

def test_acquired_data() -> None:
    """ Test the data that is acquired from the saved request. """
    data = get_data_from_file()
    isinstance(data['data'], dict)
    isinstance(data['data']['resources'], dict)
    isinstance(data['data']['resources']['ipv4'], list)
    isinstance(data['data']['resources']['ipv4'][0], str)
    assert type(data) == dict 

@pytest.mark.parametrize("test_ipv4_network_submask, expected", [
    ('8.0.0.0/8', (2**24)), 
    ('8.8.0.0/16', (2**16)), 
    ('8.8.8.0/24', (2**8)), 
    ('8.8.8.8', (2**0)), 
] )
def test_ipv4_network(test_ipv4_network_submask, expected) -> None:
    """ Test the creation of an IPv4 Network and that the version is correct as well as the number of available addresses. """
    net = create_ipv4_network(test_ipv4_network_submask)
    assert type(net) == IPv4Network
    assert net.version == 4
    assert net.num_addresses == expected


@pytest.mark.parametrize("test_str_to_ipv4_input, expected", [ 
    ('8.0.0.0', IPv4Address),
    ('192.168.0.1', IPv4Address),
    ] 
)
def test_str_to_ipv4_conversion(test_str_to_ipv4_input, expected) -> None:
    """ Test the conversion of str to an IPv4Address """
    assert type(test_str_to_ipv4_input) == str
    test_str_to_ipv4_input = IPv4Address(test_str_to_ipv4_input)
    assert type(test_str_to_ipv4_input) == expected

@pytest.mark.parametrize("test_ipv4_addresses, expected", [
    (create_ipv4_address('192.168.0.1'), create_ipv4_network('192.168.0.0/24')),
    (create_ipv4_address('8.123.123.123'), create_ipv4_network('8.0.0.0/8')),
])
def test_ip_within_network_cidr_range(test_ipv4_addresses, expected):
    """ Test how to check if an IPv4 Address is within Network range. """
    assert test_ipv4_addresses in expected
