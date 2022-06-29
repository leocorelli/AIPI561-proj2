import streamlit as st
from functions import load_pipeline, gen_input_df, load_dropdown_menu_options # local, user-written functions

st.title("Data Science/Machine Learning Industry Salary Prediction")

experience_level, employment_type, job_title, employee_residence, company_location, company_size = load_dropdown_menu_options()

# get user input
INPUT_experience_level = st.selectbox("Experience level (EN: Entry, MI: Middle, SE: Senior, EX: Executive)", experience_level,index=2)
INPUT_employment_type = st.selectbox("Employment Type", employment_type)
INPUT_job_title = st.selectbox("Job Title", sorted(job_title))
INPUT_employee_residence = st.selectbox("Employee Residence (Country)", sorted(employee_residence))
INPUT_company_location = st.selectbox("Company Location (Country)", sorted(company_location))
INPUT_company_size = st.selectbox("Company Size", sorted(company_size),index=2)

button = st.button("Predict Salary")

if button:
    print("GO!")