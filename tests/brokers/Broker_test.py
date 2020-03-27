import pytest
from tim21.brokers.Broker import Broker


class TestEmptyBroker:
    broker = Broker("empty")

    def test_init_prices(self):
        with pytest.raises(NotImplementedError) as err:
            self.broker.init_prices()
        assert "Method is required!" in str(err.value)

    def test_get_prices(self):
        with pytest.raises(NotImplementedError) as err:
            self.broker.get_prices()
        assert "Method is required!" in str(err.value)

    def test_stream_prices(self):
        with pytest.raises(NotImplementedError) as err:
            self.broker.stream_prices()
        assert "Method is required!" in str(err.value)

    def test_send_market_order(self):
        with pytest.raises(NotImplementedError) as err:
            self.broker.send_market_order("EUR/USD", 1, True)
        assert "Method is required!" in str(err.value)
