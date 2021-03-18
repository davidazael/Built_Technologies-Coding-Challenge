from contextlib import contextmanager
from ipaddress import IPv4Network, ip_network, ip_address, IPv4Address, IPv6Address
from typing import Union
import pytest


@contextmanager
def does_not_raise():
    yield

@pytest.mark.parametrize( 
    "test_ip_ranges, net_address, expected", 
    [ 
       ( "192.168.10.0", "192.168.10.0/32", True ) ,
       ( "192.168.0.1", "192.168.0.0/24", True ) ,
       ( "192.168.10.240", "192.168.0.0/16", True ) ,
       ( "192.169.10.1", "192.168.0.0/8", True ) ,
    ],
)
def test_ip_in_cidr_range(test_ip_ranges, net_address, expected) -> None:
    """ 
    Asserts that ip_address and ip_network works as expected.
      - ip_network(strict=False) allows for host bits to not be forced to be 0. 
    """
    assert ( ip_address(test_ip_ranges) in ip_network(net_address, strict=False) ) == expected 

def test_ip_network() -> None:
    """ Checks the logic of creating an ip_network and being able to check the its built-in use. """

    submask = "26"
    network_address = "192.168.10.0"
    my_network = ip_network(network_address + "/" + submask)

    assert my_network.version == 4
    assert type(my_network) == IPv4Network


@pytest.mark.parametrize(
    "test_ip_input, expected", 
    [
        ("192.168.10.0", IPv4Address),
        (1, IPv4Address),
        ("1::0", IPv6Address),
    ]
)
def test_ip_types(test_ip_input: Union[str, int] == None, expected: Union[IPv4Address, IPv6Address]) -> None: 
    """ Checks how ip_address configures ip addresses to IPv4 and IPv6 Objects. """
    assert type(ip_address(test_ip_input)) == expected

@pytest.mark.parametrize(
    "test_ip_incorrect_input, expectation", 
    [
        ("192.168.10.0", does_not_raise()),
        ("1::0", does_not_raise()),
        ("0", pytest.raises(ValueError)),
        ("0::0/2", pytest.raises(ValueError)),
    ]
)
def test_ip_input_raises(test_ip_incorrect_input: str, expectation) -> None:
    with expectation:
        assert ip_address(test_ip_incorrect_input)
