import pandas as pd
from tim21.brokers.fxcm.FxcmBroker import FxcmBroker


class mock_fxcmpy(object):
    def __init__(self, access_token='', config_file='',
                 log_file=None, log_level='', server='demo',
                 proxy_url=None, proxy_port=None, proxy_type=None):
        self.access_token = access_token
        self.prices = []

    def get_candles(self, instrument='', offer_id=None, period='H1', number=10,
                    start=None, end=None, with_index=True, columns=[],
                    stop=None):
        pass

    def subscribe_market_data(self, symbol='', add_callbacks=()):
        pass

    def get_subscribed_symbols(self):
        return self.prices.keys()

    def get_prices(self, symbol):
        if symbol in self.prices:
            return self.prices[symbol]
        else:
            return pd.DataFrame(columns=['Bid', 'Ask', 'High', 'Low'])

    def unsubscribe_market_data(self, symbol=''):
        pass

    def create_market_buy_order(self, symbol, amount, account_id=None):
        pass

    def create_market_sell_order(self, symbol, amount, account_id=None):
        pass

    def get_open_positions(self, kind='dataframe'):
        pass


class TestFxcmBroker(object):

    def test_init_fxcm(self, mocker):
        mocker.patch('fxcmpy.fxcmpy', mock_fxcmpy)
        token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        broker = FxcmBroker(account_id="test_account",
                            token="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        assert broker.api.access_token == token
