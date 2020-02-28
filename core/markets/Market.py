from core.utils.tools import candle_constructor
import pandas as pd
import os

FREQUENCY_TABLE = {
    "m1": "1min",
    "m5": "2min",
    "m15": "15min",
    "m30": "30min",
    "H1": "1h",
    "H2": "2h",
    "H3": "3h",
    "H4": "4h",
    "H6": "6h",
    "H8": "8h",
    "D1": "1D"
}


class Market(object):
    def __init__(self, broker, symbols=[], periods=[], minimal_row=10):
        self.symbols = symbols
        self.periods = periods
        self.minimal_row = minimal_row
        self.broker = self.setup_broker(broker)
        self.histories = self.setup_histories(broker)

        self.__candle_event_handler = []
        self.__pulse_event_handler = []

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
        symbol = data["Symbol"]
        for period in self.periods:

            history = self.histories[symbol][period]["history"]
            filepath = self.histories[symbol][period]["filepath"]

            candle = None
            new_candle = False

            try:
                candle = history.loc[pd.Timestamp.now().ceil(
                    FREQUENCY_TABLE[period])]
            except KeyError:
                new_candle = True

            bid = pulse["Bid"]
            ask = pulse["Ask"]

            bidlow = candle["bidopen"] if candle is not None else 0
            bidhigh = candle["bidhigh"] if candle is not None else 0
            bidopen = candle["bidopen"] if candle is not None else None
            bidclose = candle["bidclose"] if candle is not None else 0
            asklow = candle["asklow"] if candle is not None else 0
            askhigh = candle["askhigh"] if candle is not None else 0
            askopen = candle["askopen"] if candle is not None else None
            askclose = candle["askclose"] if candle is not None else 0

            bidlow = bidlow if bidlow <= bid else bid
            bidhigh = bidhigh if bidhigh >= bid else bid
            bidopen = candle["bidopen"] if bidopen is not None else bid
            bidclose = bid
            asklow = asklow if asklow <= ask else ask
            askhigh = askhigh if askhigh >= ask else ask
            bidopen = candle["askopen"] if askopen is not None else ask
            bidclose = ask

            history.loc[pd.Timestamp.now().ceil(FREQUENCY_TABLE[period])] = [
                bidlow,
                bidhigh,
                bidopen,
                bidclose,
                asklow,
                askhigh,
                askopen,
                askclose,
                None
            ]

            history.to_csv(filepath)
            self.histories[symbol][period]["history"] = history
            if new_candle:
                for func in self.__candle_event_handler:
                    func(candle, history)

        for func in self.__pulse_event_handler:
            func(data, dataframe, history)

    @property
    def on_pulse_event(self):
        """
        Listeners will receive
        data, dataframe, history
        """
        return self.__pulse_event_handler

    @on_pulse_event.setter
    def on_pulse_event(self, event_handler):
        self.__pulse_event_handler.append(event_handler)

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
