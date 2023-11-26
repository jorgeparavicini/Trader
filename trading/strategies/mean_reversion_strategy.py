from .trading_strategy import TradingStrategy


class MeanReversionStrategy(TradingStrategy):
    def __init__(self, database):
        self.database = database

    def should_sell(self, price: int, history: list[int]) -> bool:
        print("Selling from mean reversion strategy")
        return False

    def should_buy(self, price: int, history: list[int]) -> bool:
        print("Buying from mean reversion strategy")
        return False
