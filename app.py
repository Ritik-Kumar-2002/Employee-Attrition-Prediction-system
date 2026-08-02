# Import Libraries
# ------------------------------------------------------------------------------------------
import streamlit as st
import numpy as np 

# Load Dataset
# ------------------------------------------------------------------------------------------
from src.Load_dataset import load_dataset

# Import Graphs 
# ------------------------------------------------------------------------------------------
from visuals.bar_chart import plot_barChart
from visuals.pie_chart import plot_pieChart
from visuals.donut_chart import plot_donut
from visuals.histogram import plot_histogram
from visuals.scatterplot import plot_scatterplot
from visuals.boxplot import plot_boxplot
from visuals.line_chart import plot_lineChart


# ------------------------------------------------------------------------------------------


# Import preprocessing Components
# ------------------------------------------------------------------------------------------
from src.data_cleaning import clean_data
from src.feature_selection import select_features
from src.feature_encoding import encode_features
from src.train_test_split import split_data
from src.feature_scaling import scale_features

# set page configuration
# ------------------------------------------------------------------------------------------
st.set_page_config(
    page_title='HR Analytics Dashboard',
    page_icon='📊',
        layout='wide'
)
st.header('HR Analytics Dashboard', divider='grey')



# Load a dataset
# ------------------------------------------------------------------------------------------
df = load_dataset()

# Show dataset
st.write(df)

# KPIS
# ----------------------------------------------------------------------------------------------------------------------------

total_Employees = df.shape[0]
employee_left  = df[df['Attrition'] == 'Yes'].shape[0] 
current_attrition_rate = round((employee_left/total_Employees)*100, 1)
average_age = round(np.mean(df['Age']), 1)
average_MonthlyIncome = round(np.mean(df['MonthlyIncome'])/1000, 1)
average_YearAtCompany = round(np.mean(df['YearsAtCompany']), 1)
best_model='SVM'
best_modelAccuracy = 89.9
kpis = [
    ('Total Employees', df.shape[0], ''),
    ('Current Attrition Rate', current_attrition_rate, '%'),
    ('Employees Left', employee_left, ''),
    ('Average Age', average_age, ''),
    ('Average Monthly Income', average_MonthlyIncome, 'K'),
    ('Average Year at Company',average_YearAtCompany, '' ),
    ('Best Model Accuracy',  best_modelAccuracy, ''),
    ('Best Model Name', best_model, '' )
]

# ==========================================================================================
# CSS 
# ==========================================================================================
# Styling 
# ------------------------------------------------------------------------------------------
st.markdown("""
<style>

/* KPI Card */
.stApp{
    background-color: #F4F9FF;;
}

div[data-testid="stMetric"]{
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 12px;
    box-shadow: 0px 3px 8px rgba(0,0,0,0.12);
}

/* Hover Effect */
div[data-testid="stMetric"]:hover{
    transform: translateY(-3px);
    transition: 0.3s;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.18);
}

/* Label */
label[data-testid="stMetricLabel"]{
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

label[data-testid="stMetricLabel"] div {
    color: #2563EB;
    font-size: 18px;
    font-weight: bold;
    font-family: "Poppins", sans-serif;
    
}

/* Value */

div[data-testid="stMetricValue"] div {
    color: #3B82F6;
    font-size: 36px;
    font-weight: bold;
    text-align: center;
    font-family: "Inter", sans-serif;
}
</style>
""", unsafe_allow_html=True)

# KPIs Show
# ------------------------------------------------------------------------------------------
for row in range(0, len(kpis), 4):
    cols = st.columns(4)
    for i in range(4):
        j = row + i
        if(j < len(kpis)):
            with cols[i]:
                # with st.container(border=True):
                st.metric(
                    label=kpis[j][0], 
                    value=str(kpis[j][1])+kpis[j][2])


    
# =========================================================================================
# Now Perform a data analysis
#------------------------------------------------------------------------------------------

st.markdown("""
<h3 style="
    text-align:center;
    color:#003d99;
    font-size:32px;
    font-family:Poppins, sans-serif;
    font-weight:700;
">
Employee Attrition Visuals
</h3>
""", unsafe_allow_html=True)

# Plot Graphs
# -----------------------------------------------------------------------------------------------------------------------
col1, col2, col3 = st.columns([1,1,2])

# Attrition by Gender wise
with col1:
    with st.container(border=False):
        gender_attrition = df[df['Attrition'] == 'Yes'].groupby('Gender').size().reset_index(name='Attrition')
        plot_barChart(gender_attrition, 'Gender', 'Attrition', 'Gender based Attrition')

# Attrition by Department wise
with col2:
    with st.container(border=False):
        department_attrition = df[df['Attrition'] == 'Yes'].groupby('Department').size().reset_index(name='Attrition')
        plot_barChart(department_attrition, 'Department', 'Attrition', 'Department based Attrition')

# Attrition by Job Role wise
with col3:
    with st.container(border=False):
        jobRole_attrition = df[df['Attrition'] == 'Yes'].groupby('JobRole').size().reset_index(name='Attrition')
        plot_pieChart(jobRole_attrition, 'JobRole', 'Attrition', 'Job Role based Attrition')


# -----------------------------------------------------------------------------------------------------------------------
col1, col2, col3, col4 = st.columns([1,1,1,1])

# Attrition by Education wise
with col1:
    with st.container(border=False):
        education_attrition = df[df['Attrition'] == 'Yes'].groupby('Education').size().reset_index(name='Attrition')
        plot_barChart(education_attrition, 'Education', 'Attrition', 'Education wise Attrition')

# Attrition based on Overtime
with col2:
    with st.container(border=False):
            overtime_attrition = df[df['Attrition'] == 'Yes'].groupby('OverTime').size().reset_index(name='Attrition')
            plot_barChart(overtime_attrition, 'OverTime', 'Attrition', 'OverTime wise Attrition')

# Attrition based on Marital Status
with col3:
    with st.container(border=False):
            maritalStatus_attrition = df[df['Attrition'] == 'Yes'].groupby('MaritalStatus').size().reset_index(name='Attrition')
            plot_donut(maritalStatus_attrition, 'MaritalStatus', 'Attrition', 'MaritalStatus wise Attrition')

# Attrition based on Worklife balance
with col4:  
    with st.container(border=False):
            education_attrition = df[df['Attrition'] == 'Yes'].groupby('WorkLifeBalance').size().reset_index(name='Attrition')
            plot_histogram(education_attrition, 'Attrition', 'WorkLifeBalance', 'WorkLifeBalance Attrition')


# -----------------------------------------------------------------------------------------------------------------------
col1, col2, col3 = st.columns([1,1,2])

# Monthly Salary based Attrition
with col1:
    with st.container(border=False):
        MonthlyIncome_attrition = df[df['Attrition'] == 'Yes'].groupby('MonthlyIncome').size().reset_index(name='Attrition')
        plot_histogram(MonthlyIncome_attrition, 'Attrition', 'MonthlyIncome', 'MonthlyIncome Attrition')

# Age Based Attrition
with col2:
    with st.container(border=False):
        Age_attrition = df[df['Attrition'] == 'Yes'].groupby('Age').size().reset_index(name='Attrition')
        plot_lineChart(Age_attrition,'Age', 'Attrition', 'Age based Attrition')

# Education field based Attrition
with col3:
    with st.container(border=False):
        EducationField_attrition = df[df['Attrition'] == 'Yes'].groupby('EducationField').size().reset_index(name='Attrition')
        plot_donut(EducationField_attrition, 'EducationField', 'Attrition', 'Education field wise Attrition')

# ============================================================================================================================
# DATA CLEARNING AND DATA PREPROCESSING 
# ============================================================================================================================

# Clean dataframe
# ------------------------------------------------------------------------------------------
preprocessed_df = clean_data(df)


# feature Selection
# ------------------------------------------------------------------------------------------
preprocessed_df = select_features(preprocessed_df)


# feature Encoding
# ------------------------------------------------------------------------------------------
preprocessed_df = encode_features(preprocessed_df)


# Split dataset into training and testing
# ------------------------------------------------------------------------------------------
X = preprocessed_df.drop(columns=['Attrition'])
Y = preprocessed_df['Attrition']
X_train, X_test, Y_train, Y_test = split_data(X,Y)


# Feature Scaling
# ------------------------------------------------------------------------------------------
X_train_scaled, X_test_scaled = scale_features(X_train, X_test)

