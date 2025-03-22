# import streamlit as st
# import joblib
# import numpy as np

# model = joblib.load("model.pkl")


# st.title("🏚️House Price Prediction App")

# st.divider()

# st.write("This App uses Machine Learning for House Price Prediction with the given feature of the house. For using this App you need to Enter the given Field and you can use the predict button.")

# st.divider()

# bedrooms = st.number_input("Number of Bedrooms", min_value = 0, value = 0)
# bathrooms = st.number_input("Number of Bathrooms", min_value = 0, value = 0)
# LivingArea = st.number_input("Living Area", min_value = 0, value = 2000)
# condition = st.number_input("Condition of the House", min_value = 0, value = 3)
# numberofschools = st.number_input("Number of Schools Nearby", min_value = 0, value = 0)
# Distancefromtheairport = st.number_input("Distance from the airport", min_value = 0, value = 0)

# st.divider()

# X = [[bedrooms,bathrooms,LivingArea,condition,numberofschools,Distancefromtheairport]]

# predictbutton = st.button("Predict!")

# if predictbutton:
#     st.balloons()
#     X_array = np.array(X)
#     prediction = model.predict(X_array)
#     st.write(f"Price Prediction is {prediction}")

# else:
#     st.write(" Please use predict button after entering values")




# #Order of X ['number of bedrooms', 'number of bathrooms', 'living area', 'condition of the house', 'Number of schools nearby', 'Distance from the airport']

import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

# Page Configuration
st.set_page_config(page_title="House Price Predictor", page_icon="🏡", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
    .stButton button {
        background-color: #4CAF50 !important;
        color: white !important;
        font-size: 18px !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with Icon
st.markdown("<h1 style='text-align: center;'>🏡 House Price Prediction App</h1>", unsafe_allow_html=True)
st.markdown("---")

# Introduction
st.info("🔍 **Enter the details below and click 'Predict' to estimate the house price.**")

# Layout: Using Columns for Better Spacing
col1, col2 = st.columns(2)

with col1:
    bedrooms = st.number_input("🛏️ Number of Bedrooms", min_value=0, value=3, step=1)
    bathrooms = st.number_input("🛁 Number of Bathrooms", min_value=0, value=2, step=1)
    living_area = st.number_input("🏠 Living Area (sqft)", min_value=0, value=2000, step=100)

with col2:
    condition = st.selectbox("🏚️ Condition of the House", [1, 2, 3, 4, 5], index=2)
    num_schools = st.number_input("🏫 Number of Schools Nearby", min_value=0, value=2, step=1)
    distance_airport = st.number_input("✈️ Distance from Airport (miles)", min_value=0, value=10, step=1)

st.markdown("---")

# Prediction Button
predict_button = st.button("🔮 Predict Price")

if predict_button:
    st.balloons()
    X = np.array([[bedrooms, bathrooms, living_area, condition, num_schools, distance_airport]])
    prediction = model.predict(X)[0]
    
    # Display Result
    st.success(f"💰 **Estimated House Price:** ₹{prediction:,.2f}")
else:
    st.warning("⚠️ Please enter values and click 'Predict'.")

