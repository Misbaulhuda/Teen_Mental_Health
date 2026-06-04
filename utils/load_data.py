import pandas as pd

def load_data():
    df = pd.read_csv("data/Teen_Mental_Health_Dataset.csv")
    return df
