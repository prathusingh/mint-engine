import requests
import pandas as pd

from config import API_KEY

symbol = 'AAPL'

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'


response = requests.get(url)
data = response.json()

if 'Time Series (Daily)' in data:
    stock_data = pd.DataFrame(data['Time Series (Daily)'])

    print(stock_data)
else:
    print("Error in fetching data")
