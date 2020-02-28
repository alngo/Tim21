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
        self.portfolio = None
        super(MeanReversionStrategy, self).__init__("Mean reversion", broker)

    def initialize(self):
        market = Market(self.broker, symbols=self.symbols,
                        periods=self.periods, minimal_row=self.mean_period)
        portfolio
        self.market = market
        self.market.on_candle_event = self.on_candle_event
        self.market.on_pulse_event = self.on_price_event

    def on_pulse_event(self, candle, history):
        print("mean reversion: pulse event")

    def on_candle_event(self, candle, history):
        print("mean reversion: canle event")

    def run(self):
        self.broker.stream_prices(self.symbols)
        pass
