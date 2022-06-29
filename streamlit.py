import streamlit as st
from functions import load_pipeline, gen_input_df, load_dropdown_menu_options, gen_salary_pred # local, user-written functions

st.title("Data Science/Machine Learning Industry Salary Prediction")
st.image("images/money_and_computer_image.png") # this image was sourced on wikimedia commons, at: https://commons.wikimedia.org/wiki/File:Cartoon_Woman_Surprised_By_Money_Coming_Out_From_Her_Computer.svg
# all credit for this image goes to the original creator!

experience_level, employment_type, job_title, employee_residence, company_location, company_size = load_dropdown_menu_options()

# get user input
INPUT_experience_level = st.selectbox("Experience level (EN: Entry, MI: Middle, SE: Senior, EX: Executive)", experience_level,index=2)
INPUT_employment_type = st.selectbox("Employment Type", employment_type)
INPUT_job_title = st.selectbox("Job Title", sorted(job_title),index=38)
INPUT_employee_residence = st.selectbox("Employee Residence (Country)", sorted(employee_residence),index=55)
INPUT_company_location = st.selectbox("Company Location (Country)", sorted(company_location),index=48)
INPUT_company_size = st.selectbox("Company Size", sorted(company_size),index=2)
INPUT_work_year = st.number_input("Work year", min_value=2000, max_value=2100, value=2022)
INPUT_remote_ratio = st.number_input("Remote ratio (What percent of the work is remote?)", min_value=0.0, max_value=1.0)

button = st.button("Predict Salary")

if button:
    pipeline = load_pipeline()
    input_df = gen_input_df(INPUT_work_year,INPUT_experience_level,INPUT_employment_type,INPUT_job_title,INPUT_employee_residence,INPUT_remote_ratio,INPUT_company_location,INPUT_company_size)
    salary_prediction = gen_salary_pred(input_df, pipeline)
    st.subheader("Predicted Salary:")
    st.write(f"# ${salary_prediction}")