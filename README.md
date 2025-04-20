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

