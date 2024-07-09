import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['increase'] = weather['temperature'].diff().gt(0)
    increasing_ids = weather[weather['increase']]['id']
    return pd.DataFrame({'id': increasing_ids})




    