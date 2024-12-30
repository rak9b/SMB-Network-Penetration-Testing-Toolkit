import unittest
from src.scanners.port_scanner import PortScanner
from unittest.mock import patch, MagicMock


class TestPortScanner(unittest.TestCase):
    @patch("src.scanners.port_scanner.nmap.PortScanner")
    def test_scan_target_success(self, MockPortScanner):
        # Mock Nmap PortScanner
        mock_nmap = MockPortScanner.return_value
        mock_nmap.scan.return_value = {
            'scan': {
                '192.168.1.1': {
                    'status': {'state': 'up'},
                    'tcp': {
                        80: {
                            'state': 'open',
                            'name': 'http',
                            'version': 'Apache 2.4',
                        },
                    },
                },
            },
        }

        scanner = PortScanner()
        result = scanner.scan_target("192.168.1.1")
        self.assertIn('192.168.1.1', result)
        self.assertEqual(result['192.168.1.1']['status'], 'up')
        self.assertIn(80, result['192.168.1.1']['ports'])
        self.assertEqual(result['192.168.1.1']['ports'][80]['service'], 'http')

    @patch("src.scanners.port_scanner.nmap.PortScanner")
    def test_scan_target_invalid_ip(self, MockPortScanner):
        # Test invalid IP address handling
        mock_nmap = MockPortScanner.return_value
        mock_nmap.scan.side_effect = ValueError("Invalid target")

        scanner = PortScanner()
        result = scanner.scan_target("invalid-ip")
        self.assertIn("error", result)


if __name__ == "__main__":
    unittest.main()
