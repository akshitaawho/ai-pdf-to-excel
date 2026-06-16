import pandas as pd


def generate_excel(data, output_path):

    summary_data = {
        "invoice_number": data.get("invoice_number", ""),
        "customer": data.get("customer", ""),
        "date": data.get("date", ""),
        "total_amount": data.get("total_amount", "")
    }

    summary_df = pd.DataFrame([summary_data])

    items_df = pd.DataFrame(
        data.get("items", [])
    )

    with pd.ExcelWriter(output_path) as writer:

        summary_df.to_excel(
            writer,
            sheet_name="Summary",
            index=False
        )

        items_df.to_excel(
            writer,
            sheet_name="Items",
            index=False
        )

    return output_path