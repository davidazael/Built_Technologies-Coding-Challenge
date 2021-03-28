from ipaddress import IPv4Network
from src.challenge_solution import convert_ipv4_block_to_networks, check_if_ip_within_network_list
import pytest

# Assure that all of the networks in the IPv4 Block can be converted to IPv4Networks.
def test_conversion_of_block_values_to_IPv4Networks() -> None:
    all_networks = convert_ipv4_block_to_networks()
    all(isinstance(net, IPv4Network) for net in all_networks)
    assert all_networks[0].num_addresses >= all_networks[1].num_addresses

@pytest.mark.parametrize("test_set_of_ip_addresses, expected", [
    ( '2.56.35.250', True),
    ( '8.8.8.8', True),
    ( '15.15.15.15', True),
    ( '204.200.10.1', True),
    ( '193.201.147.229', True),
])
def test_ip_in_cidr_range(test_set_of_ip_addresses, expected) -> None:
    """ 
    Checks a list of IPv4 Address Strings that are converted into IPv4Address Objects to check if they are within any of the networks.
    """
    assert check_if_ip_within_network_list(test_set_of_ip_addresses) == expected