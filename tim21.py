import os
import pandas as pd
from datetime import datetime
from brokers.fxcm.FxcmBroker import FxcmBroker
from core.markets.Market import Market
from core.strategies.Strategy import Strategy
from dotenv import load_dotenv
load_dotenv()

# symbols = ["EUR/USD"]
# periods = ["m1"]

# broker = FxcmBroker(account_id=os.getenv("FXCM_ACCOUNT_ID"),
#                     token=os.getenv("FXCM_ACCOUNT_TOKEN"))

# market = Market(broker, symbols=symbols, periods=periods)

# strat = Strategy("test", market)

# broker.stream_prices(symbols=symbols)


history = pd.read_csv(
    "./brokers/fxcm/storage/EUR_USD_m1.csv", index_col="date")

current_time = "123"

candle = pd.DataFrame({
    "bidopen": [1],
    "bidclose": [2],
    "bidhigh": [3],
    "bidlow": [4],
    "askopen": [5],
    "askclose": [6],
    "askhigh": [7],
    "asklow": [8],
}, index=[current_time])

fusion = history.append(candle)

print(history)
print(candle)
print(fusion)
