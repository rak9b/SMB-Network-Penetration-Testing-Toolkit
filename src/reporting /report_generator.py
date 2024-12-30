import json
from typing import Dict, List
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import logging


class ReportGenerator:
    """
    ReportGenerator class produces reports from scan and exploit data.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def generate_pdf(self, scan_results: Dict, exploit_results: List[Dict], output_file: str):
        """
        Generate a PDF report.

        Args:
            scan_results (Dict): Results from port and vulnerability scans.
            exploit_results (List[Dict]): Results from exploit attempts.
            output_file (str): Path to the output PDF file.
        """
        try:
            self.logger.info(f"Generating PDF report: {output_file}")
            pdf = canvas.Canvas(output_file, pagesize=letter)
            pdf.setFont("Helvetica", 12)

            pdf.drawString(50, 750, "SMB Network Penetration Testing Report")
            pdf.drawString(50, 735, "-" * 50)

            y = 715
            pdf.drawString(50, y, "Scan Results:")
            y -= 20
            for host, details in scan_results.items():
                pdf.drawString(60, y, f"Host: {host} - Status: {details['status']}")
                y -= 15
                for port, info in details.get("ports", {}).items():
                    pdf.drawString(70, y, f"Port: {port}, State: {info['state']}, "
                                          f"Service: {info['service']}, Version: {info['version']}")
                    y -= 15

            pdf.drawString(50, y - 20, "Exploit Results:")
            y -= 40
            for exploit in exploit_results:
                pdf.drawString(60, y, f"Exploit: {exploit['name']}")
                pdf.drawString(70, y - 15, f"Description: {exploit['description']}")
                y -= 40

            pdf.save()
            self.logger.info("PDF report generated successfully.")
        except Exception as e:
            self.logger.error(f"Failed to generate PDF report: {e}")

    def generate_json(self, scan_results: Dict, exploit_results: List[Dict], output_file: str):
        """
        Generate a JSON report.

        Args:
            scan_results (Dict): Results from port and vulnerability scans.
            exploit_results (List[Dict]): Results from exploit attempts.
            output_file (str): Path to the output JSON file.
        """
        try:
            self.logger.info(f"Generating JSON report: {output_file}")
            report = {
                "scan_results": scan_results,
                "exploit_results": exploit_results,
            }
            with open(output_file, "w") as file:
                json.dump(report, file, indent=4)
            self.logger.info("JSON report generated successfully.")
        except Exception as e:
            self.logger.error(f"Failed to generate JSON report: {e}")
