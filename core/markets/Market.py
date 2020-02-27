from utils.tools import candle_constructor
import pandas as pd
import os


class Market(object):
    def __init__(self, broker, symbols=[], periods=[], minimal_row=10):
        self.symbols = symbols
        self.periods = periods
        self.minimal_row = minimal_row
        self.broker = self.setup_broker(broker)
        self.histories = self.setup_histories(broker)

        self.__candle_event_handler = []

    def setup_broker(self, broker):
        broker.init_prices(symbols=self.symbols,
                           periods=self.periods, number=self.minimal_row)
        broker.on_price_event = self.on_price_event
        return broker

    def setup_histories(self, broker):
        histories = {}
        for symbol in self.symbols:
            histories[symbol] = {}
            for period in self.periods:
                filename = f"{symbol.replace('/', '_')}_{period}.csv"
                filepath = os.path.join(self.broker.storage, filename)
                data = pd.read_csv(filepath, index_col="date",
                                   parse_dates=True)
                histories[symbol][period] = {
                    "history": data,
                    "symbol": symbol,
                    "period": period,
                    "filepath": filepath,
                }
                return histories

    def on_price_event(self, data, dataframe):
        for symbol in self.symbols:
            if symbol == data["Symbol"]:
                for period in self.periods:
                    history = self.histories[symbol][period]["history"]
                    filepath = self.histories[symbol][period]["filepath"]
                    start_date = history.index[-1]
                    candle = candle_constructor(period, start_date, dataframe)
                    if candle is not None:
                        history = history.append(candle)
                        self.histories[symbol][period]["history"] = history
                        history.to_csv(filepath)
                        del self.broker.api.prices[symbol]
                        for func in self.__candle_event_handler:
                            func(candle, history)

    @property
    def on_candle_event(self):
        """
        Listeners will receive:
        candle, history
        """
        return self.__candle_event_handler

    @on_candle_event.setter
    def on_candle_event(self, event_handler):
        self.__candle_event_handler.append(event_handler)
