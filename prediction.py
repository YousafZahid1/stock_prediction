import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

STOCK_SYMBOL = "NFLX"
end_date = datetime.now()
start_date = end_date - timedelta(days=180)

stock_data = yf.download(STOCK_SYMBOL, start=start_date, end=end_date)
stock_data.dropna(inplace=True)

daily_percentage_change = (stock_data["Close"] - stock_data["Open"]) / stock_data["Open"] * 100

conditions = [
    daily_percentage_change < -3,
    (daily_percentage_change >= -3) & (daily_percentage_change <= -1),
    (daily_percentage_change > -1) & (daily_percentage_change <= 1),
    (daily_percentage_change > 1) & (daily_percentage_change <= 3),
    daily_percentage_change > 3
]
values = [0, 1, 2, 3, 4]
daily_percentage_classified = np.select(conditions, values, default=2)  

print("******* Daily Percentage Classified *******")
print(daily_percentage_classified[:5])

df = pd.read_csv("netflix_stock_trends.csv")

min_len = min(len(df), len(daily_percentage_classified))
x_input = df.iloc[:min_len].values
y_data = daily_percentage_classified[:min_len]

print("x_input shape:", x_input.shape)
print("y_data shape:", y_data.shape)
print("Unique classes:", np.unique(y_data))


scaler = StandardScaler()
x_scaled = scaler.fit_transform(x_input)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y_data, test_size=0.3, random_state=42)

model = RandomForestClassifier(n_estimators=300, random_state=42)
model.fit(x_train, y_train)


y_pred = model.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
