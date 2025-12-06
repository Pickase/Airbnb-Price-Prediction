# Airbnb Price Prediction

This project predicts the estimated price of an Airbnb listing based on key property and location features.
It uses a machine-learning pipeline trained on a processed dataset containing thousands of listings across multiple cities.

A working version of the project is deployed on Streamlit:

**Live Demo:**
https://airbnb-price-prediction-5393yqisxazm7sns7ykknz.streamlit.app/?theme=dark

---

## Project Overview

The goal of this project is to build an end-to-end machine-learning system that:

1. Loads and preprocesses large Airbnb listing datasets.
2. Handles numerical and categorical features efficiently.
3. Trains a CatBoost regression model for accurate price prediction.
4. Provides a clean, user-friendly Streamlit interface for real-time predictions.
5. Deploys the working application online for public use.

---

## Features of the Model

- Handles both numerical and categorical features.
- Automatically encodes categorical variables.
- Efficient training on large-scale Airbnb datasets.
- Produces stable and high-quality predictions.
- Includes an end-to-end pipeline:
  - Data preprocessing
  - Feature extraction
  - Model training
  - Evaluation
  - Real-time prediction API

---

## Model Performance

Evaluation metrics (on test data):

- **Mean Absolute Error (MAE):** 0.0478
- **Root Mean Squared Error (RMSE):** 0.1465
- **R² Score:** 0.9582

These values indicate that the model has a strong ability to estimate log-prices with high accuracy.

---

## Project Structure
