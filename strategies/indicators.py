class Indicators:
    def __init__(self, prices):
        self.prices = prices

    def calculate_rsi(self, period=14):
        delta = self.prices.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=period).mean()
        avg_loss = loss.rolling(window=period).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def calculate_macd(self, short_window=12, long_window=26, signal_window=9):
        short_ema = self.prices.ewm(span=short_window, adjust=False).mean()
        long_ema = self.prices.ewm(span=long_window, adjust=False).mean()
        macd = short_ema - long_ema
        signal = macd.ewm(span=signal_window, adjust=False).mean()
        return macd, signal

    def calculate_bollinger_bands(self, window=20, num_std=2):
        rolling_mean = self.prices.rolling(window).mean()
        rolling_std = self.prices.rolling(window).std()
        upper_band = rolling_mean + (rolling_std * num_std)
        lower_band = rolling_mean - (rolling_std * num_std)
        return upper_band, lower_band
