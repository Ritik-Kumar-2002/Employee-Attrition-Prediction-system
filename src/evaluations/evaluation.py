from sklearn.metrics import ( accuracy_score, f1_score, precision_score, recall_score)

def model_evaluation(scaled_predictions, normal_predictions, Y_test):
    evaluation = [] # Store evaluation of the model

    # Scaled Model Evaluation
    for name, y_pred in scaled_predictions.items():
        #    {
        #         "Model":"SVM",
        #         "Accuracy":0.91,
        #         "Precision":0.90,
        #         "Recall":0.89,
        #         "F1":0.89
        #     },

        model_result = {}
        model_result['Model'] = name
        model_result['Accuracy'] = accuracy_score(Y_test, y_pred)
        model_result['Precision'] = precision_score(Y_test, y_pred)
        model_result['Recall'] = recall_score(Y_test, y_pred)
        model_result['F1'] = f1_score(Y_test, y_pred)

        evaluation.append(model_result)


    # Normal Model Evaluation
    for name, y_pred in normal_predictions.items():
        #    {
        #         "Model":"SVM",
        #         "Accuracy":0.91,
        #         "Precision":0.90,
        #         "Recall":0.89,
        #         "F1":0.89
        #     },

        model_result = {}
        model_result['Model'] = name
        model_result['Accuracy'] = accuracy_score(Y_test, y_pred)
        model_result['Precision'] = precision_score(Y_test, y_pred)
        model_result['Recall'] = recall_score(Y_test, y_pred)
        model_result['F1'] = f1_score(Y_test, y_pred)

        evaluation.append(model_result)

    return evaluation 