import os
import pandas as pd
import numpy as np
from datetime import datetime
from brokers.fxcm.FxcmBroker import FxcmBroker
from strategies.mean_reversions.MeanReversionStrategy import MeanReversionStrategy
from dotenv import load_dotenv
import talib
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


# df = pd.read_csv("./brokers/fxcm/storage/EUR_USD_m1.csv",
#                  index_col='date', parse_dates=True)

# candle = df.iloc[-1]
# print(type(candle["bidopen"]))
