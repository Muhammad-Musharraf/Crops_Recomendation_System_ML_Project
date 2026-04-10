import streamlit as st
import pickle
import pandas as pd
import os

# ------------------ Page Config ------------------
# st.set_page_config(
#     page_title="Crop Recommendation System",
#     page_icon="🌾",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

st.markdown("""
    <h1 style='text-align: center; font-size: 52px; color: #2c7a7b; font-weight: bold;'>
        🌾 Crop Recommendation System
    </h1>
""", unsafe_allow_html=True)

# ------------------ Custom CSS ------------------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #2c7a7b;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: gray;
    }
    .stButton>button {
        background-color: #2c7a7b;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ Header ------------------
st.markdown('<p class="subtitle">Get the best crop suggestion based on soil and weather conditions</p>', unsafe_allow_html=True)

st.write("")

# ------------------ Load Model ------------------
@st.cache_resource
def load_model():
    try:
        # Try to load from current directory first (for deployment)
        if os.path.exists('pipe.pkl'):
            with open('pipe.pkl', 'rb') as file:
                model = pickle.load(file)
        # Otherwise try common upload locations
        elif os.path.exists('/mnt/user-data/uploads/pipe.pkl'):
            with open('/mnt/user-data/uploads/pipe.pkl', 'rb') as file:
                model = pickle.load(file)
        else:
            st.error("❌ Model file (pipe.pkl) not found!")
            return None
        return model
    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        return None

model = load_model()

# Only show UI if model loaded successfully
if model is not None:
    # ------------------ Layout ------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧪 Soil Nutrients")
        N = st.number_input("Nitrogen (N)", 0, 140, 50)
        P = st.number_input("Phosphorus (P)", 0, 140, 50)
        K = st.number_input("Potassium (K)", 0, 200, 50)

    with col2:
        st.subheader("🌦️ Environmental Conditions")
        temperature = st.number_input("Temperature (°C)", 0.0, 50.0, 25.0)
        humidity = st.number_input("Humidity (%)", 0.0, 100.0, 60.0)
        ph = st.number_input("pH Value", 0.0, 14.0, 6.5)
        rainfall = st.number_input("Rainfall (mm)", 0.0, 300.0, 100.0)

    st.write("")

    # ------------------ Prediction ------------------
    if st.button("🌱 Recommend Crop"):
        try:
            input_data = [[N, P, K, temperature, humidity, ph, rainfall]]
            input_df = pd.DataFrame(input_data, columns=['Nitrogen','phosphorus','potassium','temperature','humidity','ph','rainfall'])
            prediction = model.predict(input_df)[0]
            st.success(f"🌾 Recommended Crop: **{prediction}**")


        except Exception as e:
            st.error(f"❌ Prediction error: {str(e)}")