import os
import pandas as pd
from datetime import datetime
from brokers.fxcm.FxcmBroker import FxcmBroker
from core.markets.Market import Market
from core.strategies.MeanReversionStrategy import MeanReversionStrategy
from dotenv import load_dotenv
load_dotenv()

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

df = pd.read_csv("./brokers/fxcm/storage/EUR_USD_m1.csv",
                 index_col="date", parse_dates=True)

# print(df)

for i in range(70):
    df.loc[pd.Timestamp.now().ceil("5min")] = [1, 2, 3, 4, 5, 6, 7, 8, None]

print("---------------")
candle = df.loc[pd.Timestamp.now().ceil('5min')]
print(candle)
print(candle["bidopen"])

if df.loc[pd.Timestamp.now().ceil("10min")] is None:
    print("errororor")
