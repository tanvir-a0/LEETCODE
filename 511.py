import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    new_df = pd.DataFrame()
    print(new_df)
    result = activity.groupby('player_id')['event_date'].min().reset_index()
    result = result.rename(columns={'event_date': 'first_login'})

    return result
    
