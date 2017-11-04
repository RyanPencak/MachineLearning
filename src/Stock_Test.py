# Ryan Pencak and James Freeland
# Machine Learning Implementation for High Frequency Trading
# Stock_Test.py

import sys
import pandas as pd
import matplotlib.pyplot as plt
import json
import googlefinance.client as gf
# from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data

# Example stock parameter dictionary
param = {
    'q': "AAPL",   # Stock Symbol for Apple
    'i': "86400",  # Interval size in seconds ("86400" = 1 day intervals)
    'x': "NASD",    # Stock exchange symbol on which stock is traded
    'p': "1M"      # Period (Ex: "1Y" = 1 year)
}

# List of parameters
params = [
    # S&P 500
    {
        'q': ".INX",
        'x': "INDEXSP"
    },

    # Dow Jones
    {
        'q': ".DJI",
        'x': "INDEXDJX"
    }
]

period = "1Y"       # 1 year period
interval = 86400    # 30 minute interval

# Get price data for AAPL and return pandas dataframe
df = gf.get_price_data(param)

# Plot price data
plt.figure()
df.plot(kind='line')
plt.title("Apple Stock Price")
plt.xlabel("Date (year-month-day)")
plt.ylabel("Price")
plt.savefig('stock_APPL.png')

# Get price data for AAPL and return pandas dataframe
df = gf.get_prices_data(params,period)

# Plot price data
plt.figure()
df.plot(kind='line')
plt.title("Stock Prices")
plt.xlabel("Date (year-month-day)")
plt.ylabel("Price")
plt.savefig('stock.png')
