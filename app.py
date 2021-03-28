""" 
Author: David Bernal
Date: March 27, 2021
Description: Built Technologies Coding Challenge.
"""
from src.convert_into_ip import create_ipv4_address
from src.challenge_solution import check_if_ip_within_network_list, convert_ipv4_block_to_networks
from src.data_requests import get_response, get_data

def user_interaction(network_list: list) -> None: 
    try:
        print('Press \'q\' at any time to exit. ')
        while True:
            provided_ip = input('Please enter a IP address: ')
            if(provided_ip == 'q'):
                return SystemExit(1)
            
            provided_ip = create_ipv4_address(provided_ip)
            if check_if_ip_within_network_list(provided_ip, network_list) == True:
                print("Pass")

    except ValueError:
        # Catch Value Error if IP isn't IPv4Address format.
        print("Fail")


def main():
    # Given Variables 
    url = ""
    # First Make Request
    make_request = get_response(url)
    # Extract content as Dictionary
    data = get_data(make_request)
    # Convert IPv4 List of strs into Ipv4 Networks and sort them by num_addresses.
    all_networks_list = convert_ipv4_block_to_networks(data)
    user_interaction(all_networks_list)


if __name__=='__main__':
    main()