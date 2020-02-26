import os
from brokers.fxcm.FxcmBroker import FxcmBroker
from dotenv import load_dotenv
load_dotenv()

symbols = ["EUR/USD"]

b = FxcmBroker(account_id=os.getenv("FXCM_ACCOUNT_ID"),
               token=os.getenv("FXCM_ACCOUNT_TOKEN"))
b.init_prices(symbols=symbols, periods=["H1", "D1"], number=20)
