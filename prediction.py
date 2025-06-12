# import tkinter as tk
# from tkinter import ttk, messagebox
# from tkinter import font
# import yfinance as yf
# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_squared_error, accuracy_score
# from sklearn.preprocessing import StandardScaler
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import seaborn as sns
# import threading
# import time
# import warnings
# warnings.filterwarnings('ignore')  # Clean up sklearn warnings


# # Use these simple functions instead:
# def calculate_moving_average(data, window):
#     return data.rolling(window=window).mean()

# def calculate_rsi(data, window=14):
#     delta = data.diff()
#     gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
#     loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
#     rs = gain / loss
#     rsi = 100 - (100 / (1 + rs))
#     return rsi

# def calculate_bollinger_bands(data, window=20):
#     rolling_mean = data.rolling(window=window).mean()
#     rolling_std = data.rolling(window=window).std()
#     upper_band = rolling_mean + (rolling_std * 2)
#     lower_band = rolling_mean - (rolling_std * 2)
#     return upper_band, lower_band






# screen.mainloop()









'''''''''''''''''''''''''''

'''''''''''''''''''''''''''


import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from pytrends.request import TrendReq
import requests

pytrends = TrendReq(hl='en-US', tz=360)
# Define the stock symbol
# STOCK_SYMBOL = "NVDA"  # Nvidia's ticker symbol
STOCK_SYMBOL = "NFLX"  # Nvidia's ticker symbol

print("Starting Nvidia stock data collection...")
# Download 2 years of historical data
end_date = datetime.now()
start_date = end_date - timedelta(days=730)  # About 2 years

print(f"Downloading {STOCK_SYMBOL} data from {start_date.date()} to {end_date.date()}")

# Download the data
stock_data = yf.download(STOCK_SYMBOL, start=start_date, end=end_date)

print(f"Downloaded {len(stock_data)} days of data")
print("\nFirst 5 rows:")
print(stock_data.head())
print("\nLast 5 rows:")
print(stock_data.tail())

model = LinearRegression()

print("HELLO WORLD")



daily_percentage_change = (stock_data.Close - stock_data.Open)/stock_data.Open *100
conditions = [
    daily_percentage_change < -3,
    (daily_percentage_change >= -3) & (daily_percentage_change <= -1),
    (daily_percentage_change > -1) & (daily_percentage_change <= 1),
    (daily_percentage_change > 1) & (daily_percentage_change <= 3),
    daily_percentage_change > 3
]
values = [0, 1, 2, 3, 4]
daily_percentage_classified = np.select(conditions, values, default=-1)
print("*******Daily_Percentage*******")
# print(daily_percentage_classified)
kw_list = [
    "Netflix stock",      # Direct investment-related
    "NFLX",               # Stock ticker
    "Netflix earnings",   # Earnings reports drive big moves
    "Netflix cancel",     # People canceling subscriptions (bearish signal)
    "Netflix new shows"   # Signals buzz and engagement (bullish sentiment)
]



pytrends = TrendReq(hl='en-US', tz=360)


pytrends=TrendReq(h1='en-US',tz=360)
timeframe_str = f"{start_date.strftime('%2023-%06-%13')} {end_date.strftime('%2025-%06-%12')}" # change every day
pytrends.build_payload(kw_list, cat=0, timeframe=timeframe_str, geo='', gprop='')



iot = pytrends.interest_over_time()
iot.plot()
