import streamlit as st
import numpy as np
import pickle
import requests

# Load the trained model from the same repository
model_url = "xgboost_model.pkl"

@st.cache_resource()
def load_model():
    try:
        # Ensure the model file exists
        if not os.path.exists(model_url):
            raise FileNotFoundError(f"Model file not found at {model_url}")
        
        with open(model_url, "rb") as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

model = load_model()

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

    # Button to predict estimated wait time
    if st.button("Calculate Estimated Time"):
        # input_features = np.array([[
        #     purchase_day, purchase_month, year, product_size_cm3,
        #     product_weight_g, geolocation_state_customer,
        #     geolocation_state_seller, distance
        # ]])
        
        # prediction = model.predict(input_features)
        # estimated_days = round(prediction[0], 2)

        estimated_days = 1
        
        st.success(f"📅 Estimated Delivery Time: {estimated_days} days")
        
