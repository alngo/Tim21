from abc import abstractmethod


class Broker(object):
    def __init__(self, name):
        self.name = name

        self.__price_event_handler = []
        self.__order_event_handler = []
        self.__position_event_handler = []

    @property
    def on_price_event(self):
        """
        Listeners will receive:
        data, dataframe
        """
        return self.__price_event_handler

    @on_price_event.setter
    def on_price_event(self, event_handler):
        self.__price_event_handler.append(event_handler)

    @property
    def on_order_event(self):
        """
        Listeners will receive:
        symbol, quantity, is_buy, transaction_id, status
        """
        return self.__order_event_handler

    @on_order_event.setter
    def on_order_event(self, event_handler):
        self.__order_event_handler.append(event_handler)

    @property
    def on_position_event(self):
        """
        Listeners will receive:
        symbol, is_buy, units, unrealized_pnl, pnl
        """
        return self.__position_event_handler

    @on_position_event.setter
    def on_position_event(self, event_handler):
        self.__position_event_handler.append(event_handler)

    @abstractmethod
    def flush_price(self, symbol):
        """
        Flush price unused dataframe
        """
        raise NotImplementedError('Method is required!')

    @abstractmethod
    def init_prices(self, symbols=[]):
        """
        Initialize price based on historical data from a broker
        """
        raise NotImplementedError('Method is required!')

    @abstractmethod
    def get_prices(self, symbols=[]):
        """
        Query market prices from a broker
        :params symbols: list of symbols recognized by your broker
        """
        raise NotImplementedError('Method is required!')

    @abstractmethod
    def stream_prices(self, symbols=[]):
        """
        Continuously stream prices from a broker
        :params symbols: list of symbols recognized by your broker
        """
        raise NotImplementedError('Method is required!')

    @abstractmethod
    def send_market_order(self, symbol, quantity, is_buy):
        raise NotImplementedError('Method is required!')
