## ETL Pipeline — Crypto Market Data

A Python-based ETL pipeline that extracts live cryptocurrency data from the CoinGecko API, transforms it using pandas, and loads it into a local SQLite database for analysis.

## Tech Stack
Python, Pandas, SQLite3, Requests, CoinGecko API

## What it does
- **Extract:** Fetches real-time top 10 cryptocurrencies by market cap from CoinGecko API
- **Transform:** Cleans and structures the data using pandas, adds timestamps
- **Load:** Stores the processed data into a local SQLite database
- **Query:** Reads data back from the database and displays a summary report

## How to run
1. Install dependencies: `pip install requests pandas`
2. Run the pipeline: `python etl.py`

## Sample Output
| Name | Price (USD) | Market Cap | 24h Change |
|------|------------|------------|------------|
| Bitcoin | 64,553 | 1.29T | +3.28% |
| Ethereum | 1,869 | 225B | +5.05% |
| Solana | 77.49 | 45B | +3.37% |
