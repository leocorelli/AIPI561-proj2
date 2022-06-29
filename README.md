# Data Science/Machine Learning Industry Salary Prediction
### Project by Leo Corelli for Duke AIPI561 Project 2

<p align="center">
  <img src="https://github.com/leocorelli/AIPI561-proj2/blob/main/images/money_and_computer_image.png" width="350" /> 
</p>

## About:

For this project I used an AutoML solution to train a model to predict salaries for jobs in the data science/machine learning industry. I sourced a dataset from Kaggle that had this information, including things like company size, company location (country), remote work ratio, experience (entry level vs middle vs senior), job title (machine learning engineer vs data scientist vs 3d computer vision engineer). 

I then used Databricks AutoML within Microsoft Azure to train 200 models on this dataset. From there, I selected the highest performing model based on validation RMSE and downloaded its pickle file. You can see an example of the AutoML run below: 

<p align="center">
  <img src="https://github.com/leocorelli/AIPI561-proj2/blob/main/images/AutoML_experiment.png" width="1000" /> 
</p>

After downloading the pickle file of my sklearn pipeline object (containing the model & preprocessing transformations) and writing a function that loads this model, I had successfully trained and loaded a machine learning model using an AutoML solution. 

From here, I wrote a function that accepted user input and created a pandas dataframe of input data to pass to the sklearn pipeline object for prediction. 

I used streamlit for my front-end, making sure that all categorical variables use drop-down menus for users to input their data. This is an important step to ensure the robustness of this project - if a user could put any string as input for a particular variable, the model would throw an error if it had not seen it before. 

Overall, I used Databricks AutoML on Azure to create a machine learning model that predicts the salary of jobs in the data science/machine learning industry, and then built a front-end for this model using streamlit so that users can interact with it easily. I hope you enjoy!

## How to run: 

1) ``$ git clone https://github.com/leocorelli/AIPI561-proj2.git``
2) Navigate to directory (and optionally set up a python virtual environment)
3) ``$ make install`` or ``pip install -r requirements.txt``
4) ``$ streamlit run streamlit.py``

