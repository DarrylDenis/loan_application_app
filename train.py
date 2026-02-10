from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from features import preprocessor,add_credit_history_features
from preprocessing import clean_raw_data
import pandas as pd
import joblib
import os


df = pd.read_csv('loan_data.csv')



y = df['loan_status'].map({'Fully Paid':0,'Charged Off':1})
X_1 = df.drop(columns= ['loan_status'], axis=1)
X_2= clean_raw_data(X_1)
X= add_credit_history_features(X_2)

X_cv,X_test,y_cv,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
X_train,X_cv,y_train,y_cv = train_test_split(X_cv,y_cv,test_size=0.25, random_state=42)

model_lr= Pipeline(steps=[('processor',preprocessor),
                      ('classifier',LogisticRegression(max_iter=1000))]
)
model_lr.fit(X_train,y_train)

os.makedirs('artifacts', exist_ok=True)
joblib.dump(model_lr,'artifacts/loan_default_model.joblib')
joblib.dump(X_test,'artifacts/X_test.joblib')
joblib.dump(y_test,'artifacts/y_test.joblib')
