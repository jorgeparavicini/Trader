from trading import TradingStrategy, TradingStrategyFactory, TradingStrategyType


def trade(strategy: TradingStrategy):
    strategy.should_buy(10, [])
    strategy.should_sell(10, [])


def main():
    strategy = TradingStrategyFactory.create(TradingStrategyType.CoolStrategy)
    trade(strategy)


if __name__ == '__main__':
    main()
