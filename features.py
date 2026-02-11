from sklearn.preprocessing import StandardScaler, OneHotEncoder,OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from category_encoders import TargetEncoder
import pandas as pd
import numpy as np
from config import num_col, ordinal_col, target_encoding_col, nominal_col



def add_credit_history_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "issue_d" in df.columns and "earliest_cr_line" in df.columns:
        df["credit_history_years"] = (
            df["issue_d"] - df["earliest_cr_line"]
        ).dt.days / 365.25
    else:
        df["credit_history_years"] = np.nan

    df.drop(
        columns=["issue_d", "earliest_cr_line", "address"],
        inplace=True,
        errors="ignore"
    )

    return df





preprocessor = ColumnTransformer(transformers=[

    ('num',
        Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ]),
        num_col
    ),

    ('ord',
        Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OrdinalEncoder())
        ]),
        ordinal_col
    ),

    ('cat_low',
        Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder(handle_unknown='ignore', drop='if_binary'))
        ]),
        nominal_col
    ),

    ('cat_high',
        Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', TargetEncoder())
        ]),
        target_encoding_col
    )

])


