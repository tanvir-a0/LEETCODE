import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    print(employee)
    new_df = employee.merge(right=employee, how='left', left_on='managerId', right_on='id')

    name = new_df[new_df['salary_x'] > new_df['salary_y']]['name_x'].tolist()
    return pd.DataFrame{"Employee": name}
    print(new_df)
