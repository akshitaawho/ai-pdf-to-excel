import pandas as pd


def generate_excel(data, output_path):

    df = pd.DataFrame([data])

    df.to_excel(
        output_path,
        index=False
    )

    return output_path