import nmap
import logging
from typing import Dict, List


class PortScanner:
    """
    PortScanner class uses nmap to perform network port scanning and service detection.
    """

    def __init__(self):
        self.nm = nmap.PortScanner()
        self.logger = logging.getLogger(__name__)

    def scan_target(self, target: str, ports: str = '1-1024') -> Dict:
        """
        Perform a port scan on a target host or network.

        Args:
            target (str): IP address or hostname to scan.
            ports (str): Port range to scan (e.g., '1-1024').

        Returns:
            Dict: Formatted scan results.
        """
        try:
            self.logger.info(f"Initiating port scan on target: {target} for ports: {ports}")
            scan_result = self.nm.scan(target, ports, arguments='-sV -sC')
            return self._parse_results(scan_result)
        except nmap.PortScannerError as e:
            self.logger.error(f"PortScannerError occurred: {e}")
            return {"error": f"Port scanner error: {str(e)}"}
        except Exception as e:
            self.logger.error(f"Unexpected error during scanning: {e}")
            return {"error": "An unexpected error occurred."}

    def _parse_results(self, scan_result: Dict) -> Dict:
        """
        Parse and format raw nmap scan results.

        Args:
            scan_result (Dict): Raw scan data from nmap.

        Returns:
            Dict: Parsed and formatted results.
        """
        parsed_results = {}
        try:
            for host, data in scan_result.get('scan', {}).items():
                host_info = {
                    'status': data.get('status', {}).get('state', 'unknown'),
                    'ports': {}
                }
                tcp_ports = data.get('tcp', {})
                for port, details in tcp_ports.items():
                    host_info['ports'][port] = {
                        'state': details.get('state', 'unknown'),
                        'service': details.get('name', 'unknown'),
                        'version': details.get('version', 'unknown'),
                    }
                parsed_results[host] = host_info
        except Exception as e:
            self.logger.error(f"Error while parsing scan results: {e}")
        return parsed_results
