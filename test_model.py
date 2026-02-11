import joblib
import os
from sklearn.metrics import (classification_report, confusion_matrix,roc_auc_score,accuracy_score,
 precision_score,recall_score,f1_score)
from config import MODEL_PATH,X_TEST_PATH,Y_TEST_PATH




# Load the model and test data
def load_artifacts():

    if not all([
        os.path.exists(MODEL_PATH),
        os.path.exists(X_TEST_PATH),
        os.path.exists(Y_TEST_PATH)
    ]):
        raise FileNotFoundError("One or more artifact files are missing.")

    logistic_model = joblib.load(MODEL_PATH)
    X_test = joblib.load(X_TEST_PATH)
    y_test = joblib.load(Y_TEST_PATH)
    
    return logistic_model,X_test,y_test




def evaluate_model(model,X_test,y_test):

    y_pred= model.predict(X_test)
    y_pred_prob = model.predict_proba(X_test)[:,1]

    metrics = {
        'accuracy': accuracy_score(y_test,y_pred),
        'precision':precision_score(y_test,y_pred),
        'recall': recall_score(y_test,y_pred),
        'f1_score': f1_score(y_test,y_pred),
        'roc_auc': roc_auc_score(y_test,y_pred_prob)
        }
    return metrics,y_pred

def print_evaluation_report(metrics):

    print("Model Evaluation Report:")
    print("-"*30)
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")
