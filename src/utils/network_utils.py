import socket
import ipaddress
import logging

logger = logging.getLogger(__name__)

def validate_ip(ip: str) -> bool:
    """
    Validate if the provided string is a valid IP address.

    Args:
        ip (str): IP address to validate.

    Returns:
        bool: True if the IP is valid, False otherwise.
    """
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        logger.error(f"Invalid IP address: {ip}")
        return False


def resolve_hostname(hostname: str) -> str:
    """
    Resolve a hostname to its corresponding IP address.

    Args:
        hostname (str): Hostname to resolve.

    Returns:
        str: Resolved IP address, or an empty string if resolution fails.
    """
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.error as e:
        logger.error(f"Failed to resolve hostname {hostname}: {e}")
        return ""
