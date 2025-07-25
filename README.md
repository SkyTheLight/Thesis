Loan Approval Predictor for Microfinance Institutions

This project provides a Loan Approval Predictor for Microfinance Institutions, leveraging a machine learning model to predict loan approval based on various applicant details.

Introduction
The Loan Approval Predictor is designed to assist microfinance institutions in making informed decisions regarding loan applications. By utilizing a trained machine learning model, it can predict whether a loan should be approved or disapproved based on the input data of the applicant.

Features
The application features include:
Loan Prediction: Predicts loan approval status (Approved/Disapproved).



User-friendly Interface: Built with Streamlit for an interactive web application.
Input Fields: Allows users to input various details such as Number of Dependents , Education (Graduated/Not Graduated) , Self-Employed status (Yes/No) , Your Annual Income , Loan Amount , Loan Term , Cibil Score , and Assets.





Installation
To set up and run the application, follow these steps:

Ensure you have all project files in a folder. The main application file is 

app.py.

Navigate to the project directory using your terminal or command prompt. For example:

"cd C:\Users\chi\Downloads\Loan Approval Predictor ML"

Ensure you have Python installed. The project was last run with Python 3.13 (64-bit).

Install the necessary Python packages. You will likely need 

streamlit, pandas, scikit-learn, and possibly joblib or pickle for loading the model and scaler.


pip install streamlit pandas scikit-learn
Usage
Run the Streamlit application:
Open your terminal or PowerShell within the project directory and execute the command:

"streamlit run app.py"

Access the application:
Once the command is executed, the application will open in your web browser, typically at 

localhost:8501.

Enter loan applicant details:
Fill in the required information in the provided input fields on the web interface.

Click "Predict":
After entering all details, click the "Predict" button. The application will then display "Loan is Approved" or "Loan is Disapproved".

File Structure
The core files of the project include:


app.py: This is the main Streamlit application script.


scaler.pkl: This file likely contains a pre-trained data scaler.


model.pkl (or Fmodel.pkl): This file contains the trained machine learning model.

Dependencies
Python 3.x (specifically tested with Python 3.13 64-bit) 

Streamlit

Pandas

Scikit-learn
