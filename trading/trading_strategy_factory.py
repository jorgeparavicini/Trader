from .trading_strategy_type import TradingStrategyType
from .strategies import *


class TradingStrategyFactory:
    @staticmethod
    def create(strategy_type: TradingStrategyType) -> TradingStrategy:
        match strategy_type:
            case TradingStrategyType.MeanReversion:
                return MeanReversionStrategy("super serious database")
            case TradingStrategyType.CoolStrategy:
                return CoolStrategy()
