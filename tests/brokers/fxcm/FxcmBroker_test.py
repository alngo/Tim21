from tim21.brokers.fxcm.FxcmBroker import FxcmBroker
import re
import pandas as pd


class mock_fxcmpy(object):
    def __init__(self, access_token='', config_file='',
                 log_file=None, log_level='', server='demo',
                 proxy_url=None, proxy_port=None, proxy_type=None):
        self.access_token = access_token
        self.prices = {}

    def get_candles(self, instrument='', offer_id=None, period='H1', number=10,
                    start=None, end=None, with_index=True, columns=[],
                    stop=None):
        return pd.DataFrame(columns=[
            'bidopen',
            'bidclose',
            'bidhigh',
            'bidlow'
            'askopen',
            'askclose',
            'askhigh',
            'asklow'
        ])
        pass

    def subscribe_market_data(self, symbol='', add_callbacks=()):
        self.prices[symbol] = pd.DataFrame(
            columns=['Bid', 'Ask', 'High', 'Low'])
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
        broker = FxcmBroker(account_id="test_account", token=token)

        assert broker.api.access_token == token

    def test_init_prices(self, mocker):
        def mock_dataframe_to_csv(self, path):
            pattern = '.*fxcm/storage/EUR_USD_H1.csv$'
            assert re.match(pattern, path) is not None

        mocker.patch('fxcmpy.fxcmpy', mock_fxcmpy)
        mocker.patch('pandas.DataFrame.to_csv', mock_dataframe_to_csv)

        spy = mocker.spy(mock_fxcmpy, 'get_candles')

        token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        broker = FxcmBroker(account_id="test_account", token=token)

        broker.init_prices(symbols=["EUR/USD"], periods=["H1"], number=10)

        spy.assert_called_once_with(broker.api,
                                    'EUR/USD', period='H1', number=10)

    def test_get_prices(self, mocker):
        mocker.patch('fxcmpy.fxcmpy', mock_fxcmpy)

        spy_subscribe_market = mocker.spy(mock_fxcmpy, 'subscribe_market_data')
        spy_get_prices = mocker.spy(mock_fxcmpy, 'get_prices')
        spy_get_subscribed = mocker.spy(mock_fxcmpy, 'get_subscribed_symbols')

        token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        broker = FxcmBroker(account_id="test_account", token=token)

        broker.get_prices(symbols=["EUR/USD"])

        spy_subscribe_market.assert_called_once_with(broker.api, "EUR/USD")
        spy_get_subscribed.assert_called_once()
        spy_get_prices.assert_called_once_with(broker.api, "EUR/USD")
