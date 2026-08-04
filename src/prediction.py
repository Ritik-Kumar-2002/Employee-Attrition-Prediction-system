

def model_prediction(scaled_models, normal_models, X_test, X_test_scaled):
    
    scaled_predictions = {}
    normal_predictions = {}

    # Scaled Model Prediction 
    for name, model, in scaled_models.items():
        y_pred = model.predict(X_test_scaled)
        scaled_predictions[name] = y_pred

    # Normal Model Prediction 
    for name, model, in normal_models.items():
        y_pred = model.predict(X_test)
        normal_predictions[name] = y_pred

    return scaled_predictions, normal_predictions