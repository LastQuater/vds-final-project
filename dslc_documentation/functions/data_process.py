import pandas as pd
from functions.data_clean import get_clean_data
from functions.load_diabetes_data import load_diabetes_data



def get_process_data(
        diabetes_org,
        dummy=True,
        drop_age=True,
        drop_smoker=True,
        drop_weight=True,
        drop_bmi=True,
        drop_height=True,
):
    diabetes_clean = get_clean_data(
        diabetes_org=diabetes_org,
        drop_age=drop_age,
        drop_smoker=drop_smoker,
        drop_weight=drop_weight,
        drop_bmi=drop_bmi,
        drop_height=drop_height,
    )

    diabetes_process = diabetes_clean.copy()

    if dummy:
        diabetes_process = pd.get_dummies(diabetes_process, columns=['smoker', 'sex', 'coronary_heart_disease', 'hypertension', 'heart_condition', 'cancer', 'family_history_diabetes'])

    return diabetes_process

if __name__ == "__main__":
    process_data = get_process_data()