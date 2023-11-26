from .trading_strategy import TradingStrategy


class CoolStrategy(TradingStrategy):
    def should_buy(self, price: int, history: list[int]) -> bool:
        print("Buying from cool strategy")
        return False

    def should_sell(self, price: int, history: list[int]) -> bool:
        print("Selling from cool strategy")
        return False
