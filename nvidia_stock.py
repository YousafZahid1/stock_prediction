from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

# Create Pytrends session with higher timeout
pytrends = TrendReq(hl='en-US', tz=360, timeout=(10, 30))

# Only 1 keyword to reduce load
kw_list = [
    "Netflix stock",      # Direct investment-related
    "NFLX",               # Stock ticker
    "Netflix earnings",   # Earnings reports drive big moves
    "Netflix cancel",     # People canceling subscriptions (bearish signal)
    "Netflix new shows"   # Signals buzz and engagement (bullish sentiment)
]


try:
    # Use 'now 1-d' for past 24 hours
    pytrends.build_payload(kw_list=kw_list, timeframe='now 1-d', geo='US')

    # Get interest over time
    data = pytrends.interest_over_time()

    if not data.empty:
        print("Successfully fetched data for the last 24 hours.")
        print(data.head())

        # Plot
        data.drop(columns=['isPartial']).plot(figsize=(12, 6), title="Netflix Stock - Google Search Trend (Past 24h)")

        plt.ylabel("Search Interest")
        plt.xlabel("Time")
        plt.grid(True)
        plt.show()
        data =  {"Netflix stock": data["Netflix stock"].tolist(),
                 "NFLX": data["NFLX"].tolist(),
                 "Netflix earnings": data["Netflix earnings"].tolist(),
                 "Netflix cancel": data["Netflix cancel"].tolist(),
                 "Netflix new shows": data["Netflix new shows"].tolist()}
        print("Data ready for further analysis or model training.")
        df = pd.DataFrame(data)
        df.to_csv("netflix_stock_trends.csv", index=False)
    else:
        print("No data returned.")
except Exception as e:
    print("Error occurred:")
    print(e)







# Every single data Add the Data into in by .concat()
