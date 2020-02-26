import fxcmpy
import time
import os
from brokers.Broker import Broker

folder = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(folder, 'fxcm.log')


class FxcmBroker(Broker):

    def __init__(self, account_id, token, is_live=False):
        if is_live:
            server = "real"
        else:
            server = "demo"

        super(FxcmBroker, self).__init__(8000, 3000)

        self.account_id = account_id
        self.token = token
        self.api = fxcmpy.fxcmpy(
            access_token=token,
            server=server,
            log_level='error',
            log_file=LOG_FILE)

    def get_prices(self, symbols=[]):
        register = {}
        for symbol in symbols:
            self.api.subscribe_market_data(symbol)

        subscribed_symbols = self.api.get_subscribed_symbols()

        for symbol in subscribed_symbols:
            price = self.api.get_prices(symbol)
            register[symbol] = price
            self.api.unsubscribe_market_data(symbol)

        for symbol, price in register.items():
            self.process_price(
                {'Updated': time.time(), 'Rate': [], 'Symbol': symbol}, price)

    def stream_prices(self, symbols=[]):
        for symbol in symbols:
            self.api.subscribe_market_data(symbol, [self.process_price])

    def process_price(self, data, dataframe):
        print(data)
        print(dataframe)

    def send_market_order(self, symbol, quantity, is_buy):
        if is_buy:
            order = self.api.create_market_buy_order(symbol, quantity)
        else:
            order = self.api.create_market_sell_order(symbol, quantity)
