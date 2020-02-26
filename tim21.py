import os
import pandas as pd
from datetime import datetime
from brokers.fxcm.FxcmBroker import FxcmBroker
from dotenv import load_dotenv
load_dotenv()

symbols = ["EUR/USD"]
dataframe = pd.read_csv(
    "./brokers/fxcm/storage/EUR_USD_D1.csv", index_col="date")
date = dataframe.index[-1]
print(type(date))
date_time_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
print(type(date_time_obj))

da = "2020-02-26 22:00:00.123"
print(da[0: 19])

# b = FxcmBroker(account_id=os.getenv("FXCM_ACCOUNT_ID"),
# token = os.getenv("FXCM_ACCOUNT_TOKEN"))
# b.init_prices(symbols=symbols, periods=["H1", "D1"], number=20)
