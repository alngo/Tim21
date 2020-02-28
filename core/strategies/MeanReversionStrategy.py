from core.strategies.Strategy import Strategy
from core.markets.Market import Market
import datetime as dt
import pandas as pd


class MeanReversionStrategy(Strategy):
    def __init__(self, broker, symbols, periods, mean_period):
        self.symbols = symbols
        self.periods = periods
        self.mean_period = mean_period
        self.market = None
        super(MeanReversionStrategy, self).__init__("Mean reversion", broker)

    def initialize(self):
        market = Market(self.broker, symbols=self.symbols,
                        periods=self.periods, minimal_row=self.mean_period)
        self.market = market
        self.market.on_candle_event = self.on_candle_event
        self.broker.on_price_event = self.on_price_event
        self.broker.on_order_event = self.on_order_event
        self.broker.on_position_event = self.broker.on_position_event
        self.broker.get_positions()

    def on_candle_event(self, candle, history):
        print("mean reversion candle event")

    def on_price_event(self, data, dataframe):
        print(dt.datetime.now(), '[PRICE]',
              data['Symbol'], dataframe.index[-1])

    def on_order_event(seld, symbol, quantity, is_buy, tradeId, status):
        pass

    def on_position_event(self, symbol, is_buy, units, unrealized_pnl, pnl):
        pass

    def run(self):
        self.broker.stream_prices(self.symbols)
        pass
