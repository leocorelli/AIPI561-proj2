import pickle
import pandas as pd
import numpy as np

def load_pipeline():
    filename = "models/sgd_regression.pkl"
    pipeline = pickle.load(open(filename, 'rb'))
    return pipeline

def load_dropdown_menu_options():
    data = pd.read_csv("data/ds_salaries.csv")
    experience_level = data["experience_level"].unique() # RETURN
    employment_type = data["employment_type"].unique() # RETURN
    job_title = data["job_title"].unique() # RETURN
    employee_residence = data["employee_residence"].unique() # RETURN
    company_location = data["company_location"].unique() # RETURN
    company_size = data["company_size"].unique() # RETURN

    return experience_level, employment_type, job_title, employee_residence, company_location, company_size



def gen_input_df():
    data = {"work_year":2020, "experience_level":"MI","employment_type":"FT", "job_title":"Data Scientist", "employee_residence":"DE","remote_ratio":0, "company_location":"DE", "company_size":"L"}
    test_input = pd.DataFrame(data,index=[0])
    return test_input
    

# if __name__ == "__main__":
#     pipeline = load_pipeline()
#     test_input = gen_test_data()
#     pred = pipeline.predict(test_input)
#     res = np.round(pred[0],2)
#     print(f"Predicted Salary: ${res}")