
```markdown
# SMB Network Penetration Testing Toolkit

A comprehensive toolkit designed for penetration testing of small-to-medium business (SMB) networks. This tool automates tasks like port scanning, vulnerability detection, exploit execution, and reporting.

---

## Features
- **Port Scanning**: Identify open ports and services using Nmap integration.
- **Vulnerability Assessment**: Evaluate potential risks associated with detected services.
- **Exploit Management**: Seamlessly search and execute exploits using Metasploit.
- **Report Generation**: Generate professional reports in PDF and JSON formats.
- **Configurable Scan Profiles**: Flexible configurations for various testing scenarios.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Metasploit installed and running with RPC enabled
- Nmap installed (`nmap` binary accessible in PATH)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/username/pentest-toolkit.git
   cd pentest-toolkit
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the Metasploit RPC server:
   ```bash
   msfrpcd -P your_password -n -f
   ```

---

## Usage

### Scan a Target
Run a quick port scan:
```bash
python -m src.scanners.port_scanner --target 192.168.1.0/24
```

### Execute an Exploit
Search for an exploit related to SMB:
```bash
python -m src.exploits.exploit_manager --search smb
```

Run an exploit:
```bash
python -m src.exploits.exploit_manager --exploit_name smb_ms17_010 --target 192.168.1.10 --options RPORT=445
```

### Generate a Report
Create a detailed report:
```bash
python -m src.reporting.report_generator --scan_results scan.json --exploit_results exploits.json --output report.pdf
```

---

## Configuration
Modify `config/scan_profiles.yaml` to customize scan behaviors. Profiles include:
- **default**: Standard scan of ports 1-1024.
- **quick_scan**: Fast scan of common ports (22, 80, 443).
- **full_scan**: Comprehensive scan of all ports (1-65535).

---

## Security Notice
This toolkit is intended for educational purposes and authorized penetration testing only. Ensure proper authorization before testing any network or system.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
```

---

