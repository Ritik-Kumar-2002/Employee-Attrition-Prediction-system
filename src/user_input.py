import streamlit as st

# It get user input and return them

def get_user_input():

    with st.sidebar.form('prediction_form'):

       st.title("Enter Employee Detail!")
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
       MaritalStatus = st.selectbox('MaritalStatus', ['Single', 'Married', 'Divorced'])

       # MonthlyIncome
       MonthlyIncome = st.number_input('Enter your MonthlyIncome')

       # MonthlyRate
       MonthlyRate = st.number_input('Enter your MonthlyRate')

       # NumCompaniesWorked
       NumCompaniesWorked = st.number_input('Number of Companies worked', min_value=0, step = 1)

       # OverTime
       OverTime = st.selectbox('OverTime', ['Yes', 'No'])

       # PercentSalaryHike
       PercentSalaryHike = st.number_input('Salary hike in percent', min_value=1, step =1 )

       # PerformanceRating 
       PerformanceRating = st.number_input('Performance rating', min_value=1, max_value=4, value=2)

       # RelationshipSatisfaction
       RelationshipSatisfaction = st.number_input('Relationship Satisfaction', min_value=1, max_value=4, value=2)

       # StockOptionLevel
       StockOptionLevel = st.number_input('Stock Option Level', min_value=0, max_value=4, value=2)

       # TotalWorkingYears
       TotalWorkingYears = st.number_input('TotalWorkingYears', min_value=0, max_value=40)

       # WorkLifeBalance
       WorkLifeBalance = st.number_input('WorkLife Balance', min_value=1, max_value=4, value=2)

       # YearsAtCompany
       YearsAtCompany = st.number_input('Years at Company', min_value=1, max_value=4, value=2)

       # YearsInCurrentRole
       YearsInCurrentRole = st.number_input('Years in current Role', min_value=0, max_value=20, value=2)

       # YearsSinceLastPromotion
       YearsSinceLastPromotion = st.number_input('Years since last promotion', min_value=1, max_value=20, value=2)

       # YearsWithCurrManager
       YearsWithCurrManager = st.number_input('Years with current manager', min_value=0, max_value=20, value=2)

       # Submit Form
       # ---------------------------------------------------------------------------------------------------------------
       submit = st.form_submit_button('Predict')

       if(submit):
           st.success('Form Successfully Submitted')

           



