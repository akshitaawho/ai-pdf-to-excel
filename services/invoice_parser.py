import re


import re


def parse_invoice(text):

    invoice_number = ""

    invoice_match = re.search(
        r"INV-[0-9]{4}-[0-9]+",
        text
    )

    if invoice_match:
        invoice_number = invoice_match.group(0)

    customer = ""

    customer_match = re.search(
        r"([A-Z][A-Za-z\s]+Corporation)",
        text
    )

    if customer_match:
        customer = customer_match.group(1)

    date = ""

    date_match = re.search(
        r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}",
        text
    )

    if date_match:
        date = date_match.group(0)

    return {
        "invoice_number": invoice_number,
        "customer": customer,
        "date": date
    }