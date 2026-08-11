# Standard Scaler used in data preprocessing and prediction user Input 
from sklearn.preprocessing import LabelEncoder, StandardScaler

scaler = StandardScaler()

attrition_encoder = LabelEncoder()
gender_encoder = LabelEncoder()
overtime_encoder = LabelEncoder()