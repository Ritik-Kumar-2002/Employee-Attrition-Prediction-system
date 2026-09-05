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

    # print('best Model: ', best_model)
    model = None
    # Scale user input  if required
    if(best_model in  ['SVM', 'KNN', 'Logistic Regression']):
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


    print('Model Classes: ',model.classes_)
    # Prediction and prediction probability
    prediction = int(model.predict(user_input)[0])
    prediction_prob =  model.predict_proba(user_input)

    stay_prob = prediction_prob[0][0]
    leaving_prob = prediction_prob[0][1]
    
    col1, col2 = st.columns(2)

    if(prediction == 0):
        st.success('🟢 Low Attrition Risk')
        st.markdown('Employee is likely to stay with the organization')

        with col1:
            st.metric(
                "🏢 Stay Probability",
                f"{stay_prob * 100:.1f}%")

        with col2:
            st.metric(
                "Leaving Probabiltiy",
                f'{leaving_prob*100:.1f}%'
            )
    else:
        st.error('🔴 High Attrition Risk')
        st.markdown('Employee is likely to resign from the organization')

        with col1:
            st.metric(
                "🏢 Stay Probability",
                f"{stay_prob * 100:.1f}%")

        with col2:
            st.metric(
                "Leaving Probabiltiy",
                f'{leaving_prob*100:.1f}%'
            )


