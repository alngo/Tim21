import os
from brokers.fxcm.FxcmBroker import FxcmBroker
from dotenv import load_dotenv
load_dotenv()

symbols = ["EUR/USD"]

b = FxcmBroker(account_id=os.getenv("FXCM_ACCOUNT_ID"),
               token=os.getenv("FXCM_ACCOUNT_TOKEN"))
b.get_positions()

#b.send_market_order("EUR/USD", 1, True)
