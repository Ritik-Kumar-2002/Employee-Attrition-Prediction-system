from sklearn.model_selection import train_test_split

def split_data(X,Y):
    X_train, X_test, Y_train, Y_test  = train_test_split(X,Y, test_size=0.2, random_state=42)
    return X_train, X_test, Y_train, Y_test