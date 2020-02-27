from abc import abstractmethod
import time
import os


class Strategy(object):
    def __init__(self, name, market):
        self.name = name
        self.market = self.setup(market)

    def setup(self, market):
        market.broker.on_price_event = self.on_price_event
        market.on_candle_event = self.on_candle_event
        return market

    def on_price_event(self, data, dataframe):
        pass

    def on_candle_event(self, candle, history):
        pass

