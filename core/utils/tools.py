import pandas as pd

SECONDS = {
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


def candle_can_be_filled(start_date, end_date, period):
    return end_date.timestamp() - start_date.timestamp() >= SECONDS[period]


def candle_constructor(period, last_date, dataframe):
    start_date = last_date
    end_date = dataframe.index[-1]
    if candle_can_be_filled(start_date, end_date, period):
        candle = pd.DataFrame({
            "date": end_date.round('min'),
            "bidlow": [min(dataframe["Bid"])],
            "bidhigh": [max(dataframe["Bid"])],
            "bidopen": [dataframe["Bid"][1]],
            "bidclose": [dataframe["Bid"][-1]],
            "asklow": [min(dataframe["Ask"])],
            "askhigh": [max(dataframe["Ask"])],
            "askopen": [dataframe["Ask"][1]],
            "askclose": [dataframe["Ask"][-1]],
        })
        candle = candle.set_index('date')
        return candle
    return None
