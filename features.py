from sklearn.preprocessing import StandardScaler, OneHotEncoder,OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from category_encoders import TargetEncoder
import pandas as pd
from config import num_col, ordinal_col, target_encoding_col, nominal_col



def add_credit_history_features(df:pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["credit_history_years"] = (
        df["issue_d"] - df["earliest_cr_line"]
    ).dt.days / 365.25
    df.drop(columns=["issue_d", "earliest_cr_line","address"],inplace= True)

    return df




preprocessor = ColumnTransformer(transformers=[
    ('num',StandardScaler(),num_col),
    ('ord',OrdinalEncoder(),ordinal_col),
    ('cat_low',OneHotEncoder(handle_unknown='ignore', drop='if_binary'),nominal_col),
    ('cat_high',TargetEncoder(),target_encoding_col)
]
)
