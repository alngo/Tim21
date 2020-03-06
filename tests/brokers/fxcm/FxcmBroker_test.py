from tim21.brokers.fxcm.FxcmBroker import FxcmBroker


# self.connect()
# self.__collect_account_ids__()
# self.default_account = self.account_ids[0]
# msg = 'Default account set to %s, to change use set_default_account().'
# self.logger.warning(msg % self.default_account)
# self.__collect_orders__()
# self.__collect_oco_orders__()
# self.__collect_offers__()
# self.__collect_positions__()
# self.instruments = self.get_instruments()
# self.subscribe_data_model('Order')
# self.subscribe_data_model('OpenPosition')
# self.subscribe_data_model('ClosedPosition')


class TestFxcmBroker(object):

    def test_init_fxcm(self, mocker):
        def mock__init__(self, access_token='', config_file='',
                         log_file=None, log_level='', server='demo',
                         proxy_url=None, proxy_port=None, proxy_type=None):
            self.access_token = access_token
        mocker.patch('fxcmpy.fxcmpy.__init__', mock__init__)
        token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        broker = FxcmBroker(account_id="test_account",
                            token="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        assert broker.api.access_token == token
