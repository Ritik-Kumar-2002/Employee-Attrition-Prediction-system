from sklearn.preprocessing import LabelEncoder
import pandas as pd


def encode_features(df):
    # ======================================================
    # Categorical Feature Encoding
    # ======================================================

    # Binary Categorical Feature (Label Encoding)
    # ------------------------------------------------------
    # 1. Gender      : Female, Male
    # 2. Attrition   : Yes, No (Target Variable)
    # 3. OverTime    : Yes, No

    binary_columns = ['Attrition', 'Gender', 'OverTime']


    # Nominal Categorical Feature (One hot Encoding)
    # ------------------------------------------------------
    # 1. BusinessTravel     : ['Travel_Rarely' 'Travel_Frequently' 'Non-Travel']
    # 2. Department         : ['Sales' 'Research & Development' 'Human Resources']
    # 3. EducationField     : ['Life Sciences' 'Other' 'Medical' 'Marketing' 'Technical Degree' 'Human Resources']
    # 4. JobRole            : ['Sales Executive' 'Research Scientist' 'Laboratory Technician' 'Manufacturing Director' 'Healthcare Representative' 'Manager''Sales Representative' 'Research Director' 'Human Resources']
    # 5. MaritalStatus      : ['Single' 'Married' 'Divorced']


    Ont_hot_Encoding_columns = [
        'BusinessTravel',
        'Department',
        'EducationField',
        'MaritalStatus',
        'JobRole'
    ]


    le = LabelEncoder()
    # Binary Encoding  (Label Encoding)

    for col in binary_columns:
        df[col] = le.fit_transform(df[col])

    # print(df.sample(4))


    # One hot encoding

    df = pd.get_dummies(
        df, 
        columns=Ont_hot_Encoding_columns,
        drop_first=True,
        dtype=int
    )

    return df