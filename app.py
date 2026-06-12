import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("Student Placement Prediction")

# Get inputs from the user
CGPA = st.number_input('CGPA', min_value=0.0, max_value=10.0, value=7.0, step=0.01, format="%.2f")
IQ = st.number_input('IQ', min_value=0, max_value=200, value=100, step=1)

if st.button("Predict"):
    features = scaler.transform([[CGPA, IQ]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Student is likely to be Placed")
    else:
        st.error("Student is likely NOT to be Placed")