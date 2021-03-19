from typing import Union
from ipaddress import IPv4Network, ip_network, IPv4Address

class MyNetwork():
    """ 
    Functionality: 
        - Ability to check if a given IP is within the Network CIDR range. 
        - Use to create an Object that stores an IPv4Network instance.   
        - Use to create IPv4 Addresses.

    Attributes: 
        network_address (str): The IP that is used to create an IPv4Network Instance

    Purpose:
        - Used to minimize the passing of IPv4Network Instance through fuctions. 
    """

    def __init__(self, network_address: str=None) -> None:
        """ Constructor """
        self.specific_network = network_address 
            
    @property
    def specific_network(self) -> IPv4Network:
        """ Getter Property """
        return self._my_network

    @specific_network.setter
    def specific_network(self, value):
        """ Setter Property """
        self._my_network = ip_network(value)

    def check_ip_within_network_range(self, ip_address: Union[ IPv4Address, str, int ]) -> bool:
        """ 
        Paramaters:
            ip_address (IPv4, str, int): The IP Address to be checked if within Network Address range.

        Returns:
            Bool: 
                True: if it is in the CIDR Range.
                False: if it is not in the CIDR Range.
        """
        if isinstance(ip_address, (str, int)):
            ip_address = self.construct_ipv4_address(ip_address)

        return ip_address in self.specific_network

    @staticmethod
    def construct_ipv4_address(ip: Union[str, int]) -> IPv4Address:
        """ 
        Parameters:
            ip_address (str, int): The IP Address that will be used to instantiate an IPv4Address instance.

        Returns:
            IPv4Address Instance with assigned ip_address.
        """
        return IPv4Address(ip)