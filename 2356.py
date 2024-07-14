import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    temp_dict = {}

    for index, row in teacher.iterrows():
        teacher_id = row['teacher_id']
        if teacher_id not in temp_dict:
            temp_dict[teacher_id] = set()
        temp_dict[teacher_id].add(row['subject_id'])

    print(temp_dict)
    unique_subjects_count = {}
    for x in temp_dict:
        unique_subjects_count[x] = len(temp_dict[x])
    print(unique_subjects_count)
    result_df = pd.DataFrame(
        {
            "teacher_id": list(unique_subjects_count.keys()),
            "cnt": list(unique_subjects_count.values())
        }
    )

    return result_df