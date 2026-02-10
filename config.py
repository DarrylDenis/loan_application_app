import os 

num_col = ['loan_amnt',
'int_rate',
 'installment',
 'annual_inc',
 'dti',
 'open_acc',
 'pub_rec',
 'revol_bal',
 'revol_util',
 'total_acc',
 'mort_acc',
 'pub_rec_bankruptcies',
 'credit_history_years']


ordinal_col = ['grade','sub_grade','emp_length']
target_encoding_col = ['emp_title','title']
nominal_col= ['term', 'home_ownership', 'verification_status', 'purpose', 'initial_list_status', 'application_type']

ARTIFACTS_DIR = 'artifacts'
MODEL_PATH = os.path.join(ARTIFACTS_DIR,'loan_default_model.joblib')
X_TEST_PATH = os.path.join(ARTIFACTS_DIR , 'X_test.joblib')
Y_TEST_PATH = os.path.join(ARTIFACTS_DIR , 'y_test.joblib')
