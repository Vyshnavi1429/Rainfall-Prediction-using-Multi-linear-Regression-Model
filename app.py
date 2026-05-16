import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Rain Predictor", page_icon="🌧️", layout="centered")


st.markdown("""
    <style>

    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
        color: #f8fafc;
    }
    
    .gemini-title {
        background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899, #3b82f6);
        background-size: 300% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        font-family: 'Inter', sans-serif;
        animation: shine 5s linear infinite;
        margin-bottom: 5px;
    }
    
    @keyframes shine {
        to { background-position: 300% center; }
    }
    
    .sub-title {
        text-align: center;
        color: #94a3b8;
        font-size: 16px;
        margin-bottom: 30px;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        border-radius: 16px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 20px;
    }
    
 
    label, .stSlider p {
        color: #cbd5e1 !important;
        font-weight: 600 !important;
    }


    .stButton>button {
        background: linear-gradient(90deg, #2563eb, #7c3aed, #db2777) !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        width: 100% !important;
        border-radius: 12px !important;
        padding: 14px !important;
        border: none !important;
        box-shadow: 0px 0px 20px rgba(124, 58, 237, 0.6) !important;
        transition: all 0.4s ease !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0px 0px 30px rgba(219, 39, 119, 0.9) !important;
    }
    
    /* సక్సెస్ మరియు ఎర్రర్ బాక్స్ ల కస్టమ్ డిజైన్ */
    .result-rain {
        background: linear-gradient(135deg, #7f1d1d, #450a0a);
        border-left: 6px solid #ef4444;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 0px 15px rgba(239, 68, 68, 0.4);
    }
    .result-clear {
        background: linear-gradient(135deg, #064e3b, #022c22);
        border-left: 6px solid #10b981;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 0px 15px rgba(16, 185, 129, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

with open('rain_model.pkl', 'rb') as file:
    model = pickle.load(file)


st.markdown("<div class='gemini-title'>✨ Intelligence Weather App</div>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Predicting Rainfall Probability with Machine Learning AI</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#60a5fa;'>🌡️ Temperature Control</h3>", unsafe_allow_html=True)
    maxtemp = st.number_input("Maximum Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
    temparature = st.number_input("Average Temperature (°C)", min_value=0.0, max_value=50.0, value=20.0)
    mintemp = st.number_input("Minimum Temperature (°C)", min_value=0.0, max_value=50.0, value=15.0)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#f472b6;'>💨 Wind & Dynamics</h3>", unsafe_allow_html=True)
    cloud = st.slider("Cloud Cover (%)", min_value=0, max_value=100, value=50)
    windspeed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=150.0, value=15.0)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='glass-card' style='height: 100%;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#c084fc;'>💧 Atmosphere & Pressure</h3>", unsafe_allow_html=True)
    pressure = st.number_input("Atmospheric Pressure (hPa)", min_value=900.0, max_value=1100.0, value=1015.0)
    dewpoint = st.number_input("Dew Point (°C)", min_value=-10.0, max_value=40.0, value=12.0)
    humidity = st.slider("Humidity (%)", min_value=0, max_value=100, value=70)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

ప్లే
if st.button("🚀 Run AI Weather Analysis"):
    features = np.array([[pressure, maxtemp, temparature, mintemp, dewpoint, humidity, cloud, windspeed]])
    prediction = model.predict(features)[0]
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if prediction >= 0.5:
        st.markdown(f"""
            <div class='result-rain'>
                <h2 style='color:#f87171; margin:0;'>🌧️ Rain Forecasted!</h2>
                <p style='color:#fca5a5; font-size:18px; margin-top:5px;'>AI Confidence Probability: <b>{prediction*100:.2f}%</b></p>
                <hr style='border-color:rgba(255,255,255,0.1);'>
                <p style='color:#fef08a; margin:0;'>💡 <b> Tip:</b> High chance of precipitation. Keep an umbrella handy and plan your day accordingly!</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class='result-clear'>
                <h2 style='color:#34d399; margin:0;'>☀️ Clear Skies!</h2>
                <p style='color:#a7f3d0; font-size:18px; margin-top:5px;'>Probability of Rain: <b>{prediction*100:.2f}%</b></p>
                <hr style='border-color:rgba(255,255,255,0.1);'>
                <p style='color:#fef08a; margin:0;'>💡 <b> Tip:</b> Weather looks absolutely beautiful and stable. Perfect day for outdoor work or travel!</p>
            </div>
        """, unsafe_allow_html=True)
