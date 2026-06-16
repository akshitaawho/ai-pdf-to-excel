from services.excel_generator import generate_excel

data = {
    "invoice_number": "INV-1001",
    "customer": "ABC Corporation",
    "date": "2025-06-16"
}

generate_excel(
    data,
    "outputs/invoice.xlsx"
)

print("Excel generated")