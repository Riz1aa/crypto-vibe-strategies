import ccxt

class DataFetcher:
    def __init__(self, exchange_name, symbols):
        self.exchange = getattr(ccxt, exchange_name)()
        self.symbols = symbols

    def fetch_ohlcv(self, symbol, timeframe='1d', limit=100):
        if symbol not in self.symbols:
            raise ValueError(f'Symbol {symbol} not supported.')
        return self.exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)\n    
    def fetch_all_ohlcv(self, timeframe='1d', limit=100):
        data = {}
        for symbol in self.symbols:
            data[symbol] = self.fetch_ohlcv(symbol, timeframe, limit)
        return data
