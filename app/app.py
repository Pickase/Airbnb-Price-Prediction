import streamlit as st
import pandas as pd
import sys, os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from src.predict import predict_price

st.title("Airbnb Price Prediction")

st.write("Fill out the details below:")

inputs = {
    "accommodates": st.number_input("Accommodates", 1, 20, value=2),
    "bedrooms": st.number_input("Bedrooms", 0, 10, value=1),
    "bathrooms": st.number_input("Bathrooms", 0, 10, value=1),
    "beds": st.number_input("Beds", 0, 20, value=1),
    "room_type": st.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room"]),
    "neighbourhood": st.text_input("Neighbourhood (string value)", "Manhattan")
}

if st.button("Predict Price"):
    try:
        price = predict_price(inputs)
        st.success(f"Estimated Price: {price:.2f} (same currency as dataset)")
    except Exception as e:
        st.error("Prediction failed. Check terminal for details.")
        raise
