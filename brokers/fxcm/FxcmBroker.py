import fxcmpy
import os
from brokers.Broker import Broker

folder = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(folder, 'log.log')


class FxcmBroker(Broker):

    def __init__(self, account_id, token, is_live=False):
        if is_live:
            server = "real"
        else:
            server = "demo"

        super(FxcmBroker, self).__init__(0, 0)

        self.account_id = account_id
        self.token = token
        self.api = fxcmpy.fxcmpy(
            access_token=token,
            server=server,
            log_level='error',
            log_file=LOG_FILE)

        def get_prices(self, symbols=[]):
            prices = []
            for symbol in symbols:
                self.api.subscribe_market_data(symbols)

            subscribed_symbols = self.api.get_subscribed_symbols()

            for symbol in subscribed_symbols:
                price = self.api.get_prices(symbol)
                prices.append(price)
                self.api.unsubscribe_market_data(symbol)

            for price in prices:
                self.process_price(price)

        def stream_prices(self, symbols=[]):
            for symbol in symbols:
                self.api.subscribe_market_data(symbol, self.process_price)

        def process_price(self, price):
            print(price)
