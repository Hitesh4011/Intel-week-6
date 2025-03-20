import streamlit as st
import numpy as np

# Load the trained model
# model = xgb.XGBRegressor()
# model.load_model("xgboost_model.json")  # Ensure this file exists

# Streamlit UI
st.set_page_config(page_title="Estimate Delivery Time", layout="wide")

# Main Container
with st.container():
    st.title("📦 Estimate Delivery Time Prediction")

    # Input fields
    col1, col2 = st.columns(2)

    with col1:
        purchase_day = st.number_input("Purchase Day", min_value=1, max_value=31, value=15)
        purchase_month = st.number_input("Purchase Month", min_value=1, max_value=12, value=6)
        year = st.number_input("Year", min_value=2000, max_value=2030, value=2025)

    with col2:
        product_size_cm3 = st.number_input("Product Size (cm³)", min_value=1, value=10000)
        product_weight_g = st.number_input("Product Weight (g)", min_value=1, value=500)

    geolocation_state_customer = st.number_input("Geolocation State (Customer)", min_value=1, max_value=50, value=10)
    geolocation_state_seller = st.number_input("Geolocation State (Seller)", min_value=1, max_value=50, value=20)
    distance = st.number_input("Distance (km)", min_value=0.1, value=300.5)

    # # Button to predict estimated wait time
    # if st.button("Calculate Estimated Time"):
        
