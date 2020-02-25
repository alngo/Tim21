import fxcmpy
import os
from ..Broker import Broker

fxcm_folder = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(fxcm_folder, 'fxcm.cfg')
log_file = os.path.join(fxcm_folder, 'log.txt')


class BrokerFxcm(Broker):
    def __init__(self, name):
        self.id = name
        self.fx = fxcmpy.fxcmpy(config_file=config_file, log_file=log_file)
        self.tickers = self.fx.get_instruments()

    def __str__(self):
        return "fxcm broker interface"
