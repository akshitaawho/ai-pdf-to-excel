from services.invoice_parser import parse_invoice

text = """
Sample Invoice
Invoice Number: INV-1001
Date: 2025-06-16
Customer: ABC Corporation
"""

print(parse_invoice(text))