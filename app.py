# Import Libraries
# ------------------------------------------------------------------------------------------
import streamlit as st
import numpy as np 

from dataset.Load_dataset import load_dataset
from visuals.bar_chart import plotbar_chart

# ------------------------------------------------------------------------------------------
# set page configuration
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
#------------------------------------------------------------------------------------------
col1, col2, col3, col4 = st.columns([1,1,1,1])

# Attrition by Gender wise
with col1:
    gender_attrition = df[df['Attrition'] == 'Yes'].groupby('Gender').size()
    print('Gender Attrition: ',gender_attrition)
    # plotbar_chart(gender_attrition)
    st.bar_chart(gender_attrition)

# Attrition by Department wise
with col2:
    department_attrition = df[df['Attrition'] == 'Yes'].groupby('Department').size()
    st.bar_chart(department_attrition)

# Attrition by Job Role wise
with col3:
    jobRole_attrition = df[df['Attrition'] == 'Yes'].groupby('JobRole').size()
    st.bar_chart(jobRole_attrition)

# Attrition by Education wise
with col4:
    education_attrition = df[df['Attrition'] == 'Yes'].groupby('Education').size()
    st.bar_chart(education_attrition, color='#80b3ff')
    



