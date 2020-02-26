import os
from brokers.fxcm.FxcmBroker import FxcmBroker
from dotenv import load_dotenv
load_dotenv()

symbols = ["EUR/USD"]

b = FxcmBroker(account_id=os.getenv("FXCM_ACCOUNT_ID"),
               token=os.getenv("FXCM_ACCOUNT_TOKEN"))
b.init_prices(symbols=symbols, period="H1", number=20)
