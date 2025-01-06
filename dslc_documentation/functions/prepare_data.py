import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from functions.data_process import get_process_data
from functions.load_diabetes_data import load_diabetes_data

diabetes_org = load_diabetes_data()

diabetes_train, diabetes_val = train_test_split(diabetes_org, test_size=0.2, stratify=diabetes_org['diabetes'])

diabetes_train_default = get_process_data(diabetes_train)
diabetes_train_nodummy = get_process_data(diabetes_train, dummy=False)

diabetes_val_default = get_process_data(diabetes_val)
diabetes_val_nodummy = get_process_data(diabetes_val, dummy=False)


