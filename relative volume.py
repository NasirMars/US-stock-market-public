from ib_insync import IB, Stock
import pandas as pd
from datetime import datetime, timedelta


def get_relative_volume(symbol: str, date: str):
    # Connect to IB Gateway
    ib = IB()
    ib.connect('127.0.0.1', 7496, clientId=2)

    # Define contract
    contract = Stock(symbol, 'SMART', 'USD')

    # Convert date to datetime object
    target_date = datetime.strptime(date, '%Y-%m-%d')

    # Get historical volume for the target date
    bars = ib.reqHistoricalData(
        contract,
        endDateTime=target_date.strftime('%Y%m%d 23:59:59'),
        durationStr='1 D',
        barSizeSetting='1 day',
        whatToShow='TRADES',
        useRTH=True,
        formatDate=1
    )

    # Get historical volume for the past 10 days (excluding the target date)
    bars_10d = ib.reqHistoricalData(
        contract,
        endDateTime=(target_date - timedelta(days=1)).strftime('%Y%m%d 23:59:59'),
        durationStr='10 D',
        barSizeSetting='1 day',
        whatToShow='TRADES',
        useRTH=True,
        formatDate=1
    )

    ib.disconnect()

    if not bars or len(bars_10d) < 10:
        print("Insufficient data for calculating relative volume.")
        return

    # Extract volume data
    target_volume = bars[0].volume if bars else None
    avg_volume_10d = sum(bar.volume for bar in bars_10d) / len(bars_10d) if bars_10d else None

    # Calculate relative volume
    relative_volume = target_volume / avg_volume_10d if avg_volume_10d else None

    # Print data
    print(f"Symbol: {symbol}")
    print(f"Date: {date}")
    print(f"Target Date Volume: {target_volume}")
    print(f"10-Day Average Volume: {avg_volume_10d:.2f}")
    print(f"Relative Volume: {relative_volume:.2f}")

    return {
        'Symbol': symbol,
        'Date': date,
        'Target Volume': target_volume,
        '10-Day Avg Volume': round(avg_volume_10d, 2),
        'Relative Volume': round(relative_volume, 2)
    }


# Example usage
symbol = "BSLK"  # Set company symbol here
date = "2025-02-13"  # Set date here
get_relative_volume(symbol, date)
