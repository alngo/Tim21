import fxcmpy
import pandas as pd
import time
import os
from brokers.Broker import Broker

FOLDER = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(FOLDER, 'fxcm.log')
STORAGE = os.path.join(FOLDER, 'storage')


class FxcmBroker(Broker):
    def __init__(self, account_id, token, is_live=False):
        if is_live:
            server = "real"
        else:
            server = "demo"

        super(FxcmBroker, self).__init__(f"FXCM_{account_id}")

        self.account_id = account_id
        self.token = token
        self.storage = STORAGE
        self.api = fxcmpy.fxcmpy(
            access_token=token,
            server=server,
            log_level='error',
            log_file=LOG_FILE)

    def init_prices(self, symbols=[], periods=[], number=10):
        for symbol in symbols:
            for period in periods:
                data = self.api.get_candles(
                    symbol, period=period, number=number)
                filename = f"{symbol.replace('/', '_')}_{period}.csv"
                data.to_csv(os.path.join(STORAGE, filename))

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
                {'Updated': pd.Timestamp(), 'Rate': [], 'Symbol': symbol}, price)

    def stream_prices(self, symbols=[]):
        for symbol in symbols:
            self.api.subscribe_market_data(symbol, [self.process_price])

    def process_price(self, data, dataframe):
        for func in self.on_price_event:
            func(data, dataframe)

    def send_market_order(self, symbol, quantity, is_buy):
        if is_buy:
            order = self.api.create_market_buy_order(symbol, quantity)
        else:
            order = self.api.create_market_sell_order(symbol, quantity)

        if order is None:
            for func in self.on_order_event:
                func(symbol, quantity, is_buy, None, 'NOT_FILLED')
        else:
            tradeId = order.get_tradeId()
            for func in self.on_order_event:
                func(symbol, quantity, is_buy, tradeId, 'FILLED')

    def get_positions(self):
        open_positions = self.api.get_open_positions()
        closed_positions = self.api.get_closed_positions()

        for index in open_positions.index:
            symbol = open_positions["currency"][index]
            units = open_positions["amountK"][index]
            unrealized_pnl = open_positions["grossPL"][index]
            is_buy = open_positions["isBuy"][index]
            for func in self.on_position_event:
                func(symbol, is_buy, units, unrealized_pnl, None)

        for index in closed_positions.index:
            symbol = closed_positions["currency"][index]
            units = closed_positions["amountK"][index]
            pnl = closed_positions["grossPL"][index]
            is_buy = closed_positions["isBuy"][index]
            for func in self.on_position_event:
                func(symbol, is_buy, units, None, pnl)
