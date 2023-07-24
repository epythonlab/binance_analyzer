# data_fetch.py

import requests
from datetime import datetime

def get_binance_data(symbol, interval, limit):
    base_url = "https://api.binance.com"
    endpoint = "/api/v1/klines"
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }
    response = requests.get(base_url + endpoint, params=params)
    data = response.json()
    return data

# Extract the data
def extract_data(data):
    dates = [datetime.fromtimestamp(entry[0] / 1000) for entry in data]
    closing_prices = [float(entry[4]) for entry in data]
    return dates, closing_prices

# # test the function
# json_data = get_binance_data('BTCUSDT', '1h', 100)

# data = extract_data(json_data)

# print(data)

