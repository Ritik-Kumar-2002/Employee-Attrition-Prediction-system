from preprocessing.preprocessing import scaler
import streamlit as st

# Import Model Instances
# --------------------------------------------------------------
from models.decision_tree import dt
from models.knn import knn
from models.logistic_regression import lr
from models.random_forest import rf
from models.svm import svm

# function predict attrition result
# --------------------------------------------------------------
def predict_employee_attrition(user_input, best_model):

    print('best Model: ', best_model)
    model = None
    # Scale user input  if required
    if(best_model in  ['SVM', 'KNN']):
        scaled_Input = scaler.transform(user_input)
        user_input = scaled_Input
    
    if(best_model == 'SVM'):
        model = svm
    elif(best_model == 'KNN'): 
        model = knn
    elif(best_model == 'Random Forest'): 
        model = rf
    elif(best_model == 'Logistic Regression'):
        model = lr
    elif(best_model == 'Decision Tree'):
        model = dt

    st.write('Prediction: ',model.predict(user_input))

