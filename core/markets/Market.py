from utils.tools import candle_constructor
import pandas as pd
import os


class Market(object):
    def __init__(self, broker, symbols=[], periods=[], minimal_row=10):
        self.symbols = symbols
        self.periods = periods
        self.minimal_row = minimal_row
        self.broker = self.setup_broker(broker)

        self.__candle_event_handler = []

    def setup_broker(self, broker):
        broker.init_prices(symbols=self.symbols,
                           periods=self.periods, number=self.minimal_row)
        broker.on_price_event = self.on_price_event
        return broker

    def on_price_event(self, data, dataframe):
        for symbol in self.symbols:
            if symbol == data["Symbol"]:
                for period in self.periods:
                    filename = f"{data['Symbol'].replace('/', '_')}_{period}.csv"
                    filepath = os.path.join(self.broker.storage, filename)
                    history = pd.read_csv(filepath, index_col="date")
                    candle = candle_constructor(period, history, dataframe)
                    if candle is not None:
                        print("candle !")
                        history.append(new_candle)
                        history.to_csv(filepath)
                        dataframe.iloc[0:0]
                        self.__candle_event_handler(symbol, period, history)

    @property
    def on_candle_event(self):
        """
        Listeners will receive:
        symbol, period, dataframe
        """
        return self.__candle_event_handler

    @on_candle_event.setter
    def on_candle_event(self, event_handler):
        self.__candle_event_handler.append(event_handler)
