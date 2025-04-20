# ⚽ Premier League Match Result Predictor

Predict football match outcomes (Home Win, Away Win, Draw) in the English Premier League using Expected Goals (xG) and a machine learning model trained on historical match data.

![Streamlit Demo](https://img.shields.io/badge/Streamlit-Deployed-brightgreen)
![Model](https://img.shields.io/badge/Model-RandomForest-blue)
![Status](https://img.shields.io/badge/Status-Complete-success)

---

## 🔍 Project Overview

This project uses **Expected Goals (xG)** as input features to predict the outcome of Premier League matches using a **Random Forest Classifier**. The app is built using **Streamlit**, allowing users to enter match data and get real-time predictions.

### ✨ Features:
- 📊 Uses xG (Expected Goals) as a reliable input feature
- 🧠 Trained with Random Forest model
- 🖥️ Streamlit GUI for interactive use
- 🇹🇭 Thai-friendly UI and predictions

---

## 🧠 Machine Learning Pipeline

1. **Data Preprocessing**: Clean, encode, and engineer features from Premier League match data.
2. **Feature Used**:
   - `homeXG`
   - `awayXG`
   - `xG_diff = homeXG - awayXG`
3. **Target**: Match result → `H` (Home Win), `A` (Away Win), or `D` (Draw)
4. **Model**: RandomForestClassifier (n_estimators=200, max_depth=10)

---

## 📂 File Structure
├── app.py # Streamlit GUI app ├── PremierLeagueMatches.csv # Dataset used for model training ├── xg_modeltest.pkl # Trained Random Forest model ├── .gitignore # Common ignore patterns ├── Premier_League_Analysis.ipynb# Exploratory Data Analysis and model training notebook ├── model/ # Folder for model artifacts │ ├── xg_modeltest.pkl │ └── label_encodertest.pkl # (Not used in current version)



---

## 🧠 Model Details

| Step                | Description                                |
|---------------------|--------------------------------------------|
| Model Type          | Random Forest Classifier                   |
| Features            | `homeXG`, `awayXG`, `xG_diff`              |
| Target Variable     | Match Result → `'H'`, `'A'`, or `'D'`      |
| Metric              | Accuracy                                   |
| Training Algorithm  | `RandomForestClassifier(n_estimators=200, max_depth=10)` |

---

## 🚀 How to Run

1. **Install dependencies**
   ```bash
   pip install streamlit joblib scikit-learn numpy pandas
2. **Run the Streamlit app**
   ```bash
   streamlit run app.py
3. **Access in browser Open http://localhost:8501 in your browser.**
   ```bash
   http://localhost:8501

