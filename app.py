import streamlit as st
import pandas as pd
import pickle as pk

# Load model and scaler
model = pk.load(open('model.pkl', 'rb'))
scaler = pk.load(open('scaler.pkl', 'rb'))

# Custom CSS
st.markdown("""
    <style>
        .stApp {
            max-width: 800px;
            margin: auto;
            padding: 2rem;
            font-family: 'Segoe UI', sans-serif;
            background-color: #0e0e0e;
            border-radius: 10px;
        }
        h1 {
            color: #ffffff;
            text-align: center;
        }
        label {
            color: #cccccc !important;
        }
        .notification {
            padding: 1.5rem;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .approved {
            background-color: #d4edda;
            color: #155724;
        }
        .disapproved {
            background-color: #f8d7da;
            color: #721c24;
        }
        .warning {
            background-color: #fff3cd;
            color: #856404;
        }
    </style>
""", unsafe_allow_html=True)

st.header('🏦 Loan Approval Predictor')

# Placeholder for result notification
notification = st.empty()

# Input widgets
no_of_dep = st.slider('👨‍👩‍👧 Number of Dependents', 0, 5)
grad = st.selectbox('🎓 Education', options=['Graduated', 'Not Graduated'], index=None, placeholder="Select")
self_emp = st.selectbox('💼 Self Employed', options=['Yes', 'No'], index=None, placeholder="Select")
annual_income = st.slider('💰 Annual Income', 0, 1000000, step=10000)
loan_ammount = st.slider('📊 Loan Amount', 0, 1000000, step=10000)
loan_dur = st.slider('🕒 Loan Duration (Years)', 0, 20)
cibil = st.slider('📈 CIBIL Score', 0, 1000)
assets = st.slider('🏘️ Assets', 0, 1000000, step=10000)

# Predict Button
if st.button('🚀 Predict'):
    # Validation
    if grad is None or self_emp is None:
        notification.markdown('<div class="notification warning">⚠️ Please select valid options for Education and Employment status.</div>', unsafe_allow_html=True)
    elif all(x == 0 for x in [no_of_dep, annual_income, loan_ammount, loan_dur, cibil, assets]):
        notification.markdown('<div class="notification warning">⚠️ Please enter your details before attempting a prediction.</div>', unsafe_allow_html=True)
    else:
        grad_s = 0 if grad == 'Graduated' else 1
        emp_s = 0 if self_emp == 'Yes' else 1
        pred_data = pd.DataFrame([[no_of_dep, grad_s, emp_s, annual_income, loan_ammount, loan_dur, cibil, assets]],
                                 columns=['no_of_dependents', 'education', 'self_employed', 'income_annum',
                                          'loan_amount', 'loan_term', 'cibil_score', 'Assets'])
        pred_data = scaler.transform(pred_data)
        predict = model.predict(pred_data)

        if predict[0] == 1:
            notification.markdown('<div class="notification approved">✅ Congratulations! Your loan is approved.</div>', unsafe_allow_html=True)
        else:
            notification.markdown('<div class="notification disapproved">❌ Unfortunately, your loan has been disapproved.</div>', unsafe_allow_html=True)
