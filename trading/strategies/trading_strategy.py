from abc import ABC, abstractmethod


class TradingStrategy(ABC):
    @abstractmethod
    def should_buy(self, price: int, history: list[int]) -> bool:
        pass

    @abstractmethod
    def should_sell(self, price: int, history: list[int]) -> bool:
        pass
