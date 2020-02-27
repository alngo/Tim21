from abc import abstractmethod
import time
import os


class Strategy(object):
    def __init__(self, name, broker):
        self.name = name
        self.broker = broker

    @abstractmethod
    def initialize(self):
        """
        initialize strategy
        """
        raise NotImplementedError('Method is required!')

    @abstractmethod
    def run(self):
        """
        run strategy
        """
        raise NotImplementedError('Method is required!')
