import pdfplumber

with pdfplumber.open("sample_invoice.pdf") as pdf:
    for page in pdf.pages:
        print(page.extract_text())