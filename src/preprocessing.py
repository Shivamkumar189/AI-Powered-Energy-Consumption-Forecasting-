import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(path):
    print("📂 Loading dataset...")
    df = pd.read_csv(path)
    df.columns = ["Date", "Energy"]
    return df

def preprocess_data(df):
    print("🧹 Preprocessing data...")

    df['Date'] = pd.to_datetime(df['Date'])

    # 🔥 NEW FEATURES
    df['day'] = df['Date'].dt.day
    df['month'] = df['Date'].dt.month
    df['year'] = df['Date'].dt.year

    # Lag feature (previous day energy)
    df['lag1'] = df['Energy'].shift(1)

    # Rolling average
    df['rolling_mean'] = df['Energy'].rolling(window=3).mean()

    # Remove NaN (created due to lag)
    df = df.dropna()

    X = df[['day','month','year','lag1','rolling_mean']]
    y = df['Energy']

    return train_test_split(X, y, test_size=0.2)