import pandas as pd
import numpy as np


def clean_emp_length(x):
    if pd.isna(x):
        return np.nan

    if isinstance(x, (int, float)):
        return float(x)

    x = str(x).strip()

    if "<" in x:
        return 0.5

    if "10+" in x:
        return 10

    return float(x.replace("years", "").replace("year", "").strip())



def clean_raw_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    
    df['mort_acc'] = df['mort_acc'].fillna(0)
    df['pub_rec_bankruptcies'] = df['pub_rec_bankruptcies'].fillna(0)

    df['revol_util'] = df['revol_util'].fillna(0)

  
    df['emp_title'] = df['emp_title'].fillna('Unknown')

    
    df['emp_length'] = df['emp_length'].apply(clean_emp_length)
    df['emp_length'] = df['emp_length'].fillna(df['emp_length'].median())

    
    df['issue_d'] = pd.to_datetime(df['issue_d'], format='%b-%Y', errors='coerce')
    df['earliest_cr_line'] = pd.to_datetime(df['earliest_cr_line'], format='%b-%Y', errors='coerce')

    return df
