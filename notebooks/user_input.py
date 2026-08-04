import streamlit as st

# It get user input and return them

def get_user_input():

    with st.sidebar:

        # Age 
        Age = st.number_input('Enter a Age', min_value=18, max_value=60, value = 25)

        # BusinessTravel
        BusinessTravel = st.selectbox('Select Business Travel', ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])

        # Daily Rate
        DailyRate = st.number_input('Enter Daily Rate', step = 1)

        # Department
        Department = st.selectbox('Select Department', ['Sales', 'Research & Development', 'Human Resources'])

        # DistanceFromHome
        DistanceFromHome = st.number_input('DistanceFromHome', max_value=60, value = 2, step=1)

        # Education
        Education = st.number_input('Education Level', min_value=1, max_value=5, step = 1)

        # EducationField
        EducationField = st.selectbox('Education Field', ['Life Sciences', 'Medical', 'Marketing', 'Technical Degree',
 'Human Resources', 'Other'])

        # EnvironmentSatisfaction
        EnvironmentSatisfaction = st.number_input('EnvironmentSatisfaction',min_value=1, max_value=4, value=2)

        # Gender
        Gender = st.selectbox('Gender', ['Female', 'Male'])

        # HourlyRate
        HourlyRate = st.number_input('Enter Hourly Rate', step = 1)

        # JobInvolvement
        JobInvolvement = st.number_input('Enter Job Involvement',min_value=1, max_value=4, value = 2)

        # JobLevel
        JobLevel = st.number_input('Enter Job Level',min_value=1, max_value=5, value = 2)

        # JobRole
        JobRole = st.selectbox('Job Role', ['Sales Executive', 'Research Scientist', 'Laboratory Technician',
 'Manufacturing Director', 'Healthcare Representative', 'Manager', 'Sales Representative', 'Research Director', 'Human Resources'])

        # JobSatisfaction
        JobSatisfaction = st.number_input('JobSatisfaction',min_value=1, max_value=4, value = 2)

        # MaritalStatus
        MaritalStatus = st.selectbox('MaritalStatus', ['Single' 'Married' 'Divorced'])

        # MonthlyIncome
        MonthlyIncome = st.number_input('Enter your MonthlyIncome')


