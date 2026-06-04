import pandas as pd

def dataset_summary(df):
    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum(),
        "Duplicate Rows": df.duplicated().sum()
    }

def depression_rate(df):
    return round(
        (df["depression_label"].sum() / len(df)) * 100,
        2
    )
