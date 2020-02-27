import os
import pandas as pd
from datetime import datetime
from brokers.fxcm.FxcmBroker import FxcmBroker
from core.markets.Market import Market
from core.strategies.MeanReversionStrategy import MeanReversionStrategy
from dotenv import load_dotenv
load_dotenv()

symbols = ["EUR/USD"]
periods = ["m1"]

broker = FxcmBroker(account_id=os.getenv("FXCM_ACCOUNT_ID"),
                    token=os.getenv("FXCM_ACCOUNT_TOKEN"))

strat = MeanReversionStrategy(broker,
                              symbols=symbols,
                              periods=periods,
                              mean_period=5
                              )
strat.initialize()
strat.run()
