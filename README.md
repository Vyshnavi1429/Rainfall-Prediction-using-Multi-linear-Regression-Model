# 🌧️ Advanced Rainfall Prediction System using Machine Learning

An interactive, Gemini-themed web application that predicts the probability of rainfall based on real-time atmospheric conditions. This project utilizes a **Multiple Linear Regression** model trained on weather datasets and is deployed live via **Streamlit Cloud**.

🚀 **Live Demo:** https://rainfall-prediction-using-multi-linear-regression-model-3tfxjm.streamlit.app/

---

## 📊 Project Overview
Predicting rainfall is a complex task due to the highly dynamic nature of atmospheric variables. This project builds a Machine Learning pipeline to analyze key weather parameters and calculate the exact percentage probability of rain. 

### Key Features:
* **Machine Learning Core:** Multiple Linear Regression model built using `scikit-learn`.
* **Gemini-Inspired UI:** A premium, dark-themed user interface featuring neon glowing accents, interactive sliding controllers, and sleek glassmorphism panels.
* **Real-time Insights:** Dynamic prediction output with custom behavioral recommendations (e.g., automated safety tips based on rain likelihood).

---

## 🛠️ Tech Stack & Architecture

* **Language:** Python 3.12
* **Machine Learning Library:** Scikit-Learn
* **Data Processing:** Pandas, NumPy
* **Web Framework:** Streamlit (Community Cloud)
* **Design Styling:** Custom CSS Embedded Graphics (Glassmorphism)

---

## 🗂️ Dataset Features
The model makes predictions using 8 distinct meteorological parameters:
1. `Atmospheric Pressure (hPa)` - Barometric weight of the air
2. `Maximum Temperature (°C)` - Highest recorded daily temperature
3. `Average Temperature (°C)` - Mean temperature of the day
4. `Minimum Temperature (°C)` - Lowest recorded daily temperature
5. `Dew Point (°C)` - Atmospheric moisture saturation point
6. `Humidity (%)` - Current relative moisture levels
7. `Cloud Cover (%)` - Percentage of sky obscured by clouds
8. `Wind Speed (km/h)` - Velocity of wind currents

---

## 📈 Model Performance
After rigorous training and data cleansing (handling string mappings, space strips, and mean imputations), the Multiple Linear Regression model achieved the following baseline results on the testing subset:

* **Mean Absolute Error (MAE):** 0.2968
* **Mean Squared Error (MSE):** 0.1616
* **Root Mean Squared Error (RMSE):** 0.4019
* **R-squared ($R^2$) Score:** 0.2458

---

## 💻 Local Installation & Setup

If you wish to run this weather intelligence system locally on your environment, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vyshnavi1429/Rainfall-Prediction-using-Multi-linear-Regression-Model.git
   cd rainfall-prediction-using-multi-linear-regression-model
