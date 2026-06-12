import pickle
from turtle import st

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

if st.button("Predict"):

    features = scaler.transform([[cgpa, iq]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Student is likely to be Placed")
    else:
        st.error("Student is likely NOT to be Placed")