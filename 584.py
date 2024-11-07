import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    result = customer[(customer['referee_id'] != 2) | (pd.isnull(customer['referee_id']))][['name']]

    return result
    
