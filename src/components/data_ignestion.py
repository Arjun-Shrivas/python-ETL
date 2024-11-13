import pandas as pd

def read_data(file_path):
    """Reads CSV data from the given file path and returns a DataFrame."""
    return pd.read_csv(file_path)
