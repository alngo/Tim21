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

        if order is None:
            self.on_order_event(symbol, quantity, is_buy, None, 'NOT_FILLED')
            return

        tradeId = order.get_tradeId()
        self.on_order_event(symbol, quantity, is_buy, tradeId, 'FILLED')

    def get_positions(self):
        open_positions = self.api.get_open_positions()
        closed_positions = self.api.get_closed_positions()

        for index in open_positions.index:
            symbol = open_positions["currency"][index]
            units = open_positions["amountK"][index]
            unrealized_pnl = open_positions["grossPL"][index]
            is_buy = open_positions["isBuy"][index]
            self.on_position_event(symbol, is_buy, units, unrealized_pnl, None)

        for index in closed_positions.index:
            symbol = closed_positions["currency"][index]
            units = closed_positions["amountK"][index]
            pnl = closed_positions["grossPL"][index]
            is_buy = closed_positions["isBuy"][index]
            self.on_position_event(symbol, is_buy, units, None, pnl)

        print("ok")
