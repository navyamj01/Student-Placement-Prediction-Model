import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Student Placement Prediction")

cgpa = st.number_input(
    "Enter CGPA",
    min_value=0.0,
    max_value=10.0,
    step=0.1
)

iq = st.number_input(
    "Enter IQ",
    min_value=50,
    max_value=200,
    step=1
)

if st.button("Predict"):

    prediction = model.predict([[cgpa, iq]])

    if prediction[0] == 1:
        st.success("Student is likely to be Placed")
    else:
        st.error("Student is likely NOT to be Placed")