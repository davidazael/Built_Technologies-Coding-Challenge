from ipaddress import IPv4Address, IPv4Network

# Converts given str into IPv4Network
def create_ipv4_network(ip_address_with_submask: str, strict_ip_host_bytes: bool=False) -> IPv4Network:
    """
    Params: String, Optional Bool to set true or false for Strict IP Host Bytes. Set to false by default, if assigned to true; Host bytes must be zero. 
    Functionality: Converts String into IPv4 Network.
    Returns: IPv4 Network.
    """
    return IPv4Network(ip_address_with_submask, strict=strict_ip_host_bytes)

# Converts given str into IPv4Address
def create_ipv4_address(ip_address: str) -> IPv4Address:
    """ 
    Params: String 
    Functionality: Converts String into IPv4 Address 
    Returns: IPv4Address object.
    """
    return IPv4Address(ip_address)