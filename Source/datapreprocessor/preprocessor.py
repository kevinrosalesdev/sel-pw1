import pandas as pd


def load_test_dataset() -> pd.DataFrame:
    return pd.read_csv('Data/lenses.csv')
