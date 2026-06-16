import pdfplumber


def extract_tables(pdf_path):

    all_tables = []

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            tables = page.extract_tables()

            if tables:
                all_tables.extend(tables)

    return all_tables