import pytest
from unittest.mock import patch
from tim21.brokers.fxcm.FxcmBroker import FxcmBroker


@patch('fxcm.request.get')
def test_init_fxcm(mock_get):
    mock_get_patcher = patch('fxcm.request.get')
    mock_get = mock_get_patcher.start()
    mock_get.return_value.ok = True
    broker = FxcmBroker(account_id="test_account", tokent="test_token")
    mock_get_patcher.stop()
    print(broker)
