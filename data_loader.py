import pandas as pd

def load_data():
    # Cargar el conjunto de datos
    path = "data\E-commerce_data.xlsx"
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df