import re


def parse_invoice(text):

    invoice_number = re.search(
        r"Invoice Number:\s*(.*)",
        text
    )

    customer = re.search(
        r"Customer:\s*(.*)",
        text
    )

    date = re.search(
        r"Date:\s*(.*)",
        text
    )

    return {
        "invoice_number": invoice_number.group(1) if invoice_number else "",
        "customer": customer.group(1) if customer else "",
        "date": date.group(1) if date else ""
    }