import pandas as pd
from datetime import datetime

PERIOD = {
    "m1": 60,
    "m5": 60 * 5,
    "m15": 60 * 15,
    "m30": 60 * 30,
    "H1": 60 * 60,
    "H2": 60 * 60 * 2,
    "H3": 60 * 60 * 3,
    "H4": 60 * 60 * 4,
    "H6": 60 * 60 * 4,
    "H8": 60 * 60 * 8,
    "D1": 60 * 60 * 24
}


def period_is_filled(last, curr, period):
    a_time = datetime.strptime(last, '%Y-%m-%d %H:%M:%S')
    b_time = datetime.strptime(curr, '%Y-%m-%d %H:%M:%S')
    print(b_time.timestamp(), a_time.timestamp(), PERIOD[period])
    return b_time.timestamp() - a_time.timestamp() <= PERIOD[period]


def candle_constructor(period, history, dataframe):
    last_time = history.index[-1][0: 19]
    current_time = str(dataframe.index[-1])[0: 19]
    if period_is_filled(last_time, current_time, period):
        print("candle!")
        new_candle = pd.DataFrame({
            "date": current_time,
            "bidlow": [min(dataframe["Bid"])],
            "bidhigh": [max(dataframe["Bid"])],
            "bidopen": [dataframe["Bid"][1]],
            "bidclose": [dataframe["Bid"][-1]],
            "asklow": [min(dataframe["Ask"])],
            "askhigh": [max(dataframe["Ask"])],
            "askopen": [dataframe["Ask"][1]],
            "askclose": [dataframe["Ask"][-1]],
        })
        return new_candle
    return None
