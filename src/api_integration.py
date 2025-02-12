import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.api_config import api_key

import requests

def fetch_data(symbol):
    url  = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}'
    data = requests.get(url)
    return data.json()

def get_symbols():
    url  = f'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={api_key}'
    data = requests.get(url)
    return data