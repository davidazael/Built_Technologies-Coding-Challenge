from src.convert_into_ip import create_ipv4_network, create_ipv4_address
from tests.test_data_usage import get_data_from_file
from typing import List

def convert_ipv4_block_to_networks(request_response_content: dict=get_data_from_file()) -> List:
    """ 
    Params: Receives Request_Response_Content in the form of a Dictionary. Default value is the dictionary that is created from extracting data from saved response. 
    Functionality: Maps every single string ipv4 network into an IPv4Network. 
    Optimization: Sorts new list of networks in reverse descending order(largets -> smallest)
     that could prevent traversing the whole list when checking if an ip is in the network list.
    Returns: List of IPv4 Networks that can be used for comparison.
    """
    ipv4_data_block = request_response_content['data']['resources']['ipv4']
    # Map list of ipv4 networks from strings to Ipv4 Networks.
    all_networks = list(map(lambda item: create_ipv4_network(item), ipv4_data_block))
    # Sorts all networks by greatest number of addresses within the cidr range
    all_networks = sorted(all_networks, key=lambda net: net.num_addresses, reverse=True)
    return all_networks

def check_if_ip_within_network_list(given_ip_address: str, all_networks: list) -> bool:
    """ 
    Params: Accepts ip address in string format. List of all networks.
    Functionality: Converts each string into a valid Ipv4 Address. Compares it to the list of networks.
    Returns: bool; true if ip in list of network, false if not in list of networks.
    """
    given_ip_address = create_ipv4_address(given_ip_address)
    for net in all_networks:
        if given_ip_address in net:
            return (given_ip_address in net)
