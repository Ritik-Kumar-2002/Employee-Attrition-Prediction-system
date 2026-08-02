

def select_features(df):

    # Identify Single value Columns
    # -------------------------------------------------------------------------------
    single_val_col = []
    for col in df.columns:
        if(len(df[col].unique()) == 1): 
            single_val_col.append(col)
    
    df = df.drop(columns = single_val_col)

    # Also delete employee number columns(Not required to train a model)
    # -------------------------------------------------------------------------------
    df = df.drop(columns = ['EmployeeNumber'])

    return df