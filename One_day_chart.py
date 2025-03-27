# Step 0: Install required libraries if not already installed
!pip install yfinance
!pip install pytz

# Import libraries
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import pytz  # For timezone conversion
from datetime import datetime, timedelta

# Step 1: Get the list of S&P 500 tickers
sp500 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
tickers = sp500['Symbol'].tolist()

# Limit the number of tickers to avoid excessive processing in Colab
tickers = tickers[:500]  # Use the first 5 tickers as an example

# Step 2: Define the period for intraday data
interval = "5m"  # 5-minute interval
period = "1d"    # 1-day data

# Define U.S. Eastern Standard Time zone
us_est = pytz.timezone("America/New_York")

# Loop through each ticker and plot the chart
for ticker in tickers:
    try:
        # Download the data
        company_data = yf.download(ticker, period=period, interval=interval)

        # Check if data is downloaded successfully
        if company_data.empty:
            print(f"Data not available for {ticker}. Skipping...")
            continue

        # Convert the timestamp to U.S. Eastern Time
        company_data.index = company_data.index.tz_convert(us_est)

        # Plot the intraday stock chart
        plt.figure(figsize=(12, 6))
        plt.plot(company_data.index, company_data['Close'], label=f"{ticker} Intraday Price")
        plt.title(f"{ticker} Intraday Price Chart")
        plt.xlabel("Time (EST)")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.grid()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error downloading data for {ticker}: {e}")
