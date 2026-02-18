class DataProcessor:
    def calculate_cvd(self, volume_data, price_data):
        """
        Calculates the Cumulative Volume Delta (CVD).
        :param volume_data: List of volume data.
        :param price_data: List of price data.
        :return: List of CVD values.
        """
        cvd = []
        cumulative = 0.0
        for volume, price in zip(volume_data, price_data):
            if price > price_data[0]:
                cumulative += volume
            else:
                cumulative -= volume
            cvd.append(cumulative)
        return cvd

    def calculate_oi_expansion(self, oi_data):
        """
        Calculates Open Interest (OI) expansion.
        :param oi_data: List of Open Interest data.
        :return: List of OI expansion values.
        """
        expansion = []
        for i in range(1, len(oi_data)):
            change = oi_data[i] - oi_data[i - 1]
            expansion.append(change)
        return expansion

    def calculate_price_stagnation(self, price_data, threshold=0.01):
        """
        Detects price stagnation based on a specified threshold.
        :param price_data: List of price data.
        :param threshold: The acceptable price change threshold.
        :return: Boolean indicating if stagnation occurred.
        """
        for i in range(1, len(price_data)):
            if abs(price_data[i] - price_data[i - 1]) > threshold:
                return False
        return True

    def calculate_atr(self, high_prices, low_prices, close_prices, period=14):
        """
        Calculates the Average True Range (ATR) indicator.
        :param high_prices: List of high prices.
        :param low_prices: List of low prices.
        :param close_prices: List of close prices.
        :param period: The period for the ATR calculation.
        :return: List of ATR values.
        """
        atr = []
        for i in range(1, len(close_prices)):
            tr = max(high_prices[i] - low_prices[i],
                     abs(high_prices[i] - close_prices[i - 1]),
                     abs(low_prices[i] - close_prices[i - 1]))
            atr.append(tr)
        # Calculate the average of the ATR values over the specified period
        # This part can include a more refined calculation.
        return atr[-period:] if len(atr) > period else atr
