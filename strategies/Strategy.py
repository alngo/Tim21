from abc import abstractmethod
from utils.tools import period_converter
import time
import os


class Strategy(object):
    def __init__(self, name, broker, period, symbols=[], period=["H1"], initial_number=10):
        self.name = name
        self.periods = periods
        self.symbols = symbols
        self.broker = self.setup(broker, initial_number)

        self.__candle_event_handler = None

    def setup(self, broker, number):
        broker.init_prices(symbols=self.symbols,
                           period=self.periods, number=number)
        broker.on_price_event = self.on_price_event
        return broker

    def on_price_event(self, data, dataframe):
        # for candle, period, condles in generate candle
        for symbol in symbols:
            if symbol == data["Symbol"]:
                for period in period:
                    filename = f"{data.Symbol.replace('/', '_')_{period}.csv}"
                    filepath = os.path.join(broker.storage, filename)
                    candles = pd.read_csv(filepath)
                    last_time = candles.index[-1]
                    current_time = dataframe.index[-1][0: 19]
                    if current_time - last_time >= peconverter(period):
                        new_candle = pd.DataFrame({
                            "bidlow": min(dataframe["Bid"]),
                            "bidhigh": max(dataframe["Bid"]),
                            "bidopen": dataframe["Bid"][1],
                            "bidclose": dataframe["Bid"][-1],
                            "asklow": min(dataframe["Ask"]),
                            "askhigh": max(dataframe["Ask"]),
                            "askopen": dataframe["Ask"][1],
                            "askclose": dataframe["Ask"][-1],
                        })
                        candles.append(new_candle)
                        candles.to_csv(filepath)
                        # flush dataframe
                        self.__candle_event_handler(period, candles)

    @property
    def on_candle_event(self):
        """
        Listeners will receive:
        period, dataframe
        """
        return self.__candle_event_handler

    @on_candle_event.setter
    def on_candle_event(self, event_handler):
        self.__candle_event_handler = event_handler
