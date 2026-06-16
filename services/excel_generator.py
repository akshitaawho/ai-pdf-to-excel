import pandas as pd


def generate_excel(data, output_path):

    with pd.ExcelWriter(output_path) as writer:

        for sheet in data["sheets"]:

            df = pd.DataFrame(
                sheet["rows"],
                columns=sheet["columns"]
            )

            sheet_name = sheet["sheet_name"][:31]

            df.to_excel(
                writer,
                sheet_name=sheet_name,
                index=False
            )

    return output_path