import pickle
import pandas as pd
import numpy as np

def load_pipeline():
    filename = "models/sgd_regression.pkl"
    pipeline = pickle.load(open(filename, 'rb'))
    return pipeline

def gen_test_data():
    data = {"work_year":2020, "experience_level":"MI","employment_type":"FT", "job_title":"Data Scientist", "employee_residence":"DE","remote_ratio":0, "company_location":"DE", "company_size":"L"}
    test_input = pd.DataFrame(data,index=[0])
    return test_input

if __name__ == "__main__":
    pipeline = load_pipeline()
    test_input = gen_test_data()
    pred = pipeline.predict(test_input)
    res = np.round(pred[0],2)
    print(f"Predicted Salary: ${res}")