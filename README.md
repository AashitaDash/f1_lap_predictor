# 🏎️ FastLap AI – Formula 1 Lap Time Prediction

FastLap AI is a machine learning project that predicts **Formula 1 lap times** using historical race data.  
The project combines **Python-based machine learning** with a **web-based visualization interface**.

---

## 🔍 Project Overview

- **Domain:** Machine Learning, Sports Analytics  
- **Problem Type:** Regression  
- **Goal:** Predict lap time (in seconds) using race-related features  
- **Inspiration:** Love for Formula 1 🏁

This project focuses on understanding lap time behavior and the challenges of applying ML to real-world sports data.

---

## 📊 Dataset

- **Source:** Formula 1 World Championship Dataset (Kaggle)
- **Granularity:** Lap-level race data
- **Key Features Used:**
  - Lap Number
  - Race Position
  - Driver ID
  - Race ID
  - Lap Time (milliseconds → seconds)

### Preprocessing Steps
- Converted lap time from milliseconds to seconds
- Removed abnormal laps caused by pit stops and race interruptions
- Filtered unrealistic lap times
- Performed basic feature selection

---

## 🤖 Machine Learning Model

- **Model Used:** Linear Regression (baseline model)
- **Reason:** Simple, interpretable starting point
- **Train–Test Split:** 80% training, 20% testing

### 📈 Evaluation Metrics
Since this is a regression problem, accuracy is not applicable.

- **Mean Absolute Error (MAE):** ~**11.58 seconds**
- **R² Score:** ~**0.08**

### Interpretation
The modest R² score reflects the complexity of Formula 1 racing, where lap time is influenced by factors such as tyre strategy, fuel load, weather, and race incidents that are not present in the dataset.

---

## 📉 Visualizations

The following plots were generated using **Matplotlib** and are included in the project:

- **Figure 1:** Actual vs Predicted Lap Times  
- **Figure 2:** Distribution of Formula 1 Lap Times  
- **Figure 3:** Lap Number vs Lap Time  
- **Figure 4:** Position vs Lap Time  
- **Figure 5:** Model Performance with Ideal Reference Line  

These visualizations help analyze data patterns and model behavior.

---

## 🌐 Web Interface

A frontend webpage was built using:
- HTML
- Tailwind CSS
- JavaScript

### Features:
- Project overview and explanations
- Embedded ML visualizations
- A **demo prediction section** (frontend simulation)

⚠️ Note:  
The prediction shown on the webpage is a **frontend simulation**.  
The actual machine learning model is implemented and evaluated offline in Python.

---

## 🚀 Deployment

- **Frontend:** Deployed on **Vercel**
- **Backend ML:** Python (offline, not live inference)

The complete codebase (ML + frontend + graphs) is hosted on GitHub.

---

## 📁 Project Structure

fastlap-ai/
│── index.html
│── Figure_1.png
│── Figure_2.png
│── Figure_3.png
│── Figure_4.png
│── Figure_5.png
│── f1_lap_model.py
│── lap_times.csv
│── README.md


---

## 💡 Key Learnings

- Real-world datasets are noisy and complex
- Feature availability impacts model performance more than algorithms
- Evaluation metrics must be chosen correctly for regression problems
- Honest interpretation of results is crucial in applied ML

---

## 🔮 Future Improvements

- Use advanced models (Random Forest, Gradient Boosting)
- Add tyre, weather, and strategy-related features
- Convert regression into lap-speed classification
- Deploy a real-time ML API using Flask/FastAPI

---

## 👩‍💻 Author

**Aashita Dash**  
Machine Learning & Data Science Enthusiast  
Formula 1 Fan 🏎️  

---

⭐ If you find this project interesting, feel free to star the repository!

