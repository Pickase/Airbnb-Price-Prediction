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


airbnb-price-prediction/
|-- app/
|   |-- app.py
|-- data/
|   |-- processed/
|   |   |-- train.csv
|   |   |-- test.csv
|   |-- raw/ (optional if using Google Drive)
|-- models/
|   |-- final_catboost_model.cbm (ignored in GitHub due to size)
|-- src/
|   |-- __init__.py
|   |-- config.py
|   |-- data_prep.py
|   |-- features.py
|   |-- pipelines.py
|   |-- train.py
|-- evaluate.py
|-- predict.py
|-- requirements.txt
|-- README.md


## How to Run the Project Locally

### 1. Create a virtual environment

python -m venv venv
source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windows


### 2. Install dependencies

pip install -r requirements.txt


### 3. Prepare data  
If raw data is stored in a Drive link, ensure `TRAIN_PATH` and `TEST_PATH` are correctly set in `src/config.py`.

Then run:

python -m src.data_prep


### 4. Train model

python -m src.train


### 5. Evaluate model

python -m src.evaluate


### 6. Run Streamlit App

streamlit run app/app.py


---

## Live Demo (Working Application)

The deployed project is available here:

**https://airbnb-price-prediction-5393yqisxazm7sns7ykknz.streamlit.app/?theme=dark**

You can interact with the model, enter property details, and instantly receive a price prediction.

---

## Technologies Used

- Python
- Pandas
- NumPy
- CatBoost
- Scikit-learn
- Streamlit
- Joblib
- GitHub + Streamlit Cloud for deployment

---

## Notes

- The `/models` folder is excluded from GitHub due to file size; the model is loaded directly in the deployed version.
- The dataset used is large and not stored in the repository to avoid exceeding GitHub's storage limits.

---

## Conclusion

This project demonstrates a complete machine-learning pipeline, from preprocessing large Airbnb datasets to deploying a production-ready prediction app.  
All steps—cleaning, modeling, evaluation, and deployment—are automated and reproducible.


