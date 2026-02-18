import requests
import pandas as pd

def fetch_data(symbol):
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1d&limit=30'
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data, columns=['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 'Quote Asset Volume', 'Number of Trades', 'Taker Buy Base Asset Volume', 'Taker Buy Quote Asset Volume', 'Ignore'])

def CVDOIStrategy(btc_data, eth_data):
    # Dummy backtest strategy, replace with actual strategy logic
    performance = {
        'BTC Profit': (float(btc_data.iloc[-1]['Close']) - float(btc_data.iloc[0]['Open')),
        'ETH Profit': (float(eth_data.iloc[-1]['Close']) - float(eth_data.iloc[0]['Open'])),
    }
    return performance

def main():
    btc_data = fetch_data('BTCUSDT')
    eth_data = fetch_data('ETHUSDT')
    
    performance = CVDOIStrategy(btc_data, eth_data)
    
    print("Performance Statistics:")
    print(f"BTC Profit: {performance['BTC Profit']}")
    print(f"ETH Profit: {performance['ETH Profit']}")

if __name__ == "__main__":
    main()