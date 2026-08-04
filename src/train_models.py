# Import models
# ------------------------------------------------------------------------------------------
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

# ======================================================= 
# Feature Scaling Required Model
# -------------------------------------------------------
# SVM, 
# KNN, 
# K Mean Clustering, 
# Deep Learning (Back Propagation Algorithm)
# -------------------------------------------------------


# ======================================================= 
# No Feature Scaling Require Model
# -------------------------------------------------------
# Logistic Regression
# Random Forest Classifier  
# Decision Tree
# -------------------------------------------------------

# ======================================================= 

def train_models(X_train, X_train_scaled, Y_train):

    # Support Vector Machine
    svm = SVC()

    # K Nearest Neighbor 
    knn = KNeighborsClassifier()

    # Logistic Regression
    lr = LogisticRegression()

    # Random Forest
    rf = RandomForestClassifier()

    # Decision Tree
    dt = DecisionTreeClassifier()

    # Scaled Models 
    scaled_models = {
        'SVM': svm,
        'KNN': knn
    }

    # Normal Models
    normal_models = {
        'Logistic Regression': lr,
        'Random Forest': rf,
        'Decision Tree': dt 
    }

    # Train Scaled Model
    for key in scaled_models.keys():
        scaled_models[key].fit(X_train_scaled, Y_train)

    # Train Normal Model
    for key in normal_models.keys(): 
        normal_models[key].fit(X_train, Y_train)

    return scaled_models, normal_models