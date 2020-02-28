import os
import pandas as pd
import numpy as np
from datetime import datetime
from brokers.fxcm.FxcmBroker import FxcmBroker
from core.markets.Market import Market
from core.strategies.MeanReversionStrategy import MeanReversionStrategy
from dotenv import load_dotenv
import talib
load_dotenv()

close = np.random.random(100)
print(close)
output = talib.SMA(close)
print(output)

# symbols = ["EUR/USD"]
# periods = ["m1"]

# broker = FxcmBroker(account_id=os.getenv("FXCM_ACCOUNT_ID"),
#                     token=os.getenv("FXCM_ACCOUNT_TOKEN"))

# strat = MeanReversionStrategy(broker,
#                               symbols=symbols,
#                               periods=periods,
#                               mean_period=5
#                               )
# strat.initialize()
# strat.run()

