import requests
import pandas as pd
import sqlite3
from datetime import datetime

def extract():
    print("Extracting data from CoinGecko API...")
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def transform(data):
    print("Transforming data...")
    df = pd.DataFrame(data)
    df = df[["id", "symbol", "name", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]]
    df["extracted_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df.columns = ["id", "symbol", "name", "price_usd", "market_cap", "volume_24h", "price_change_24h", "extracted_at"]
    return df

def load(df):
    print("Loading data into database...")
    conn = sqlite3.connect("crypto_data.db")
    df.to_sql("crypto_prices", conn, if_exists="append", index=False)
    conn.close()
    print(f"Successfully loaded {len(df)} records into database.")


def query_data():
    print("\n--- Sample Data from Database ---")
    conn = sqlite3.connect("crypto_data.db")
    df = pd.read_sql("SELECT name, price_usd, market_cap, price_change_24h FROM crypto_prices ORDER BY market_cap DESC", conn)
    conn.close()
    print(df.to_string(index=False))

if __name__ == "__main__":
    raw_data = extract()
    df = transform(raw_data)
    load(df)
    query_data()
    print("\nETL Pipeline completed successfully!")