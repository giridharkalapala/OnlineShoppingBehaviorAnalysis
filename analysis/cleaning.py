import pandas as pd


def load_and_clean_data(file_path):
    """
    Load dataset and perform data cleaning.
    """

    df = pd.read_csv(file_path)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Fill missing values
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].fillna(df[column].mode()[0])
        else:
            df[column] = df[column].fillna(df[column].median())

    # Remove outliers from Purchase Amount
    if "Purchase Amount (USD)" in df.columns:
        q1 = df["Purchase Amount (USD)"].quantile(0.25)
        q3 = df["Purchase Amount (USD)"].quantile(0.75)
        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        df = df[
            (df["Purchase Amount (USD)"] >= lower)
            & (df["Purchase Amount (USD)"] <= upper)
        ]

    return df


if __name__ == "__main__":

    df = load_and_clean_data("../data/online_shopping_behavior.csv")

    print(df.head())

    print(df.info())