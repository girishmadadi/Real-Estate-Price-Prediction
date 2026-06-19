
import streamlit as st
import joblib
import numpy as np

model = joblib.load('real_estate_model.pkl')

st.title("Real Estate Price Prediction")

area = st.number_input("Area (sq.ft)")
bath = st.number_input("Bathrooms")
balcony = st.number_input("Balcony")

if st.button("Predict Price"):
    input_data = np.array([[area, bath, balcony]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Price: {prediction[0]:.2f} Lakhs")
