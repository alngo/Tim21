from .brokers.fxcm.FxcmBroker import FxcmBroker


class Tim21:
    def __init__(self, config_path):
        self.config_path = config_path
        self.broker = None
        self.market = None
        self.strategy = None
        self.portfolio = None

    def run(self):
        print("coucou")
