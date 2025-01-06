import pandas as pd
from functions.load_diabetes_data import load_diabetes_data



def get_clean_data(
        diabetes_org,
        drop_age=True,
        drop_smoker=True,
        drop_weight=True,
        drop_bmi=True,
        drop_height=True,
):
    #load raw data
    diabetes = diabetes_org.copy() 

    #drop the first column
    diabetes = diabetes.drop(columns=['house_family_person_id'])

    #numerical values process
    filter_condition = pd.Series([True] * len(diabetes), index=diabetes.index)

    if drop_age:
        filter_condition &= (diabetes["age"] < 85)

    if drop_smoker:
        filter_condition &= (diabetes["smoker"] == 1) | (diabetes["smoker"] == 2)

    if drop_weight:
        filter_condition &= diabetes["weight"] <= 299

    if drop_bmi:
        filter_condition &= diabetes["bmi"] < 9995

    if drop_height:
        filter_condition &= diabetes['height'] < 96


    diabetes_clean = diabetes[filter_condition]

    return diabetes_clean

if __name__ == "__main__":
    get_clean_data()