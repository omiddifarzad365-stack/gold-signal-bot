import pandas as pd
import pandas as pd

def calculate_indicators(df):

    df["EMA20"] = ta.ema(df["close"], length=20)

    df["EMA50"] = ta.ema(df["close"], length=50)

    df["EMA200"] = ta.ema(df["close"], length=200)

    adx = ta.adx(
        high=df["high"],
        low=df["low"],
        close=df["close"],
        length=14
    )

    df["ADX"] = adx["ADX_14"]

    return df
