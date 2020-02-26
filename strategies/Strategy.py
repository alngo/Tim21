from abc import abstractmethod


class Strategy(object):
    def __init__(self, name, broker, period, symbols=[], period="H1"):
        self.name = name
        self.period = period
        self.symbols = symbols
        self.broker = self.setup(broker)

        self.__candle_event_handler = None

    def setup(self, broker):
        broker.init_prices(symbols=self.symbols, period=self.period, number=10)
        broker.on_price_event = self.on_price_event
        return broker

    def on_price_event(self, data, dataframe):
        pass

    @property
    def on_candle_event(self):
        """
        Listeners will receive:
        dataframe
        """
        return self.__candle_event_handler

    @on_candle_event.setter
    def on_candle_event(self, event_handler):
        self.__candle_event_handler = event_handler
