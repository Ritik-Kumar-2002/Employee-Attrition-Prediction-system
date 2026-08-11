# Dataset is Imbalanced 
# Parameter Importance in such a way that
# best_model = max(0.4*F1_score + 0.3*Recall + 0.3*Precision + 0.1*Accuracy, best_model)
# Calculate it for every row and take max gives the best model

def select_best_model(df):
    best_model ={}
    parameter = float("-inf")
    for row in df.itertuples():
        # print(row)
        # print(row.Accuracy)
        
        eval = 0.4*row.F1 + 0.3*row.Recall + 0.3*row.Precision + 0.1*row.Accuracy
        # print("Result are ", eval)
        # print(f'Eval: {eval} for {row.Model}')

        if(eval > parameter):
            parameter = eval
            best_model['Model'] = row.Model
            best_model['Accuracy'] = row.Accuracy
            best_model['Precision'] = row.Precision
            best_model['Recall'] = row.Recall
            best_model['F1'] = row.F1

    return best_model
        