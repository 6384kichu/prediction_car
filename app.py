import streamlit as st
import pickle
import pandas as pd
import numpy as np

model = pickle.load(open("model_lr.pkl", "rb"))

st.title("🚗 Car Price Prediction App")
st.write("Enter car details to predict its price.")

year = st.number_input("Year of Manufacture", min_value=1990, max_value=2023, value=2015)
mileage = st.number_input("Mileage (km driven)", min_value=0, max_value=500000, value=50000)
engine_size = st.number_input("Engine Size (CC)", min_value=500, max_value=5000, value=1500)
max_power = st.number_input("Max Power (in bph)", min_value=50, max_value=500, value=100)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"])

fuel_dict = {"Petrol": [1, 0, 0], "Diesel": [0, 1, 0], "LPG": [0, 0, 1], "CNG": [0, 0, 0], "Electric": [0, 0, 0]}
transmission_dict = {"Manual": [1], "Automatic": [0]}

fuel_encoded = fuel_dict[fuel] 
transmission_encoded = transmission_dict[transmission]  

user_data = np.array([[year, mileage, engine_size, max_power] + fuel_encoded + transmission_encoded])

prediction = model.predict(user_data)

if st.button("Predict Price"):
    st.success(f"💰 Estimated Car Price: ${prediction[0]:,.2f}")
import os
import pickle
import streamlit as st



