# Airbnb Price Prediction and Insights

## Project Overview

This project focuses on building a machine learning model to predict Airbnb listing prices. By analyzing various features such as property type, room type, location, amenities, and host characteristics, this model aims to provide actionable insights for Airbnb hosts to optimize their listing prices and for Airbnb to refine its pricing recommendations.

## Problem Statement

The primary objective is to develop a regression model that accurately predicts the price of an Airbnb listing. The insights derived will help hosts understand key price drivers, enabling data-driven decisions, and assist Airbnb in improving host and guest satisfaction.

## Dataset

The dataset used for this project is `Airbnb_data.xlsx`. It contains comprehensive information on Airbnb listings, including:
* `log_price`: Logarithm of the listing price (target variable).
* `property_type`: Type of property (e.g., Apartment, House).
* `room_type`: Type of room (e.g., Entire home/apt, Private room).
* `accommodates`: Number of guests the listing accommodates.
* `bathrooms`: Number of bathrooms.
* `bed_type`: Type of bed.
* `cancellation_policy`: Cancellation policy.
* `cleaning_fee`: Whether a cleaning fee is charged.
* `city`: City where the listing is located.
* `amenities`: List of amenities offered.
* `host_has_profile_pic`: Whether the host has a profile picture.
* `host_identity_verified`: Whether the host's identity is verified.
* `host_response_rate`: Host's response rate.
* `number_of_reviews`: Total number of reviews.
* `review_scores_rating`: Average review score.
* `bedrooms`: Number of bedrooms.
* `beds`: Number of beds.
* And other relevant features like `latitude`, `longitude`, `description`, `first_review`, `last_review`, `host_since`, `name`, `neighbourhood`, `thumbnail_url`, and `zipcode`.

## Methodology

The project follows a standard machine learning pipeline:

1.  **Data Exploration and Cleaning:**
    * Initial inspection of dataset shape and information.
    * Handling of missing values (e.g., `log_price`, `bathrooms`, `beds`, `host_response_rate`, `bedrooms`, `review_scores_rating`, `number_of_reviews`, `amenities`).
    * Feature engineering: Created `amenities_count` and `host_years` from existing features.
    * Conversion of categorical boolean-like features (`cleaning_fee`, `host_has_profile_pic`, `host_identity_verified`, `instant_bookable`) to numerical representations.
    * Dropping irrelevant columns (`amenities`, `first_review`, `last_review`, `host_since`, `zipcode`, `thumbnail_url`, `description`).

2.  **Exploratory Data Analysis (EDA):**
    * Visualizations (e.g., histogram of `log_price`) to understand data distributions and relationships.
    * Insights derived from visualizations to guide feature selection and modeling.

3.  **Preprocessing:**
    * Categorical features were identified for one-hot encoding.
    * Numerical features were identified for scaling.
    * `ColumnTransformer` and `Pipeline` were used to streamline preprocessing steps.

4.  **Model Development:**
    * The dataset was split into training and testing sets to prevent overfitting.
    * Multiple regression models were explored and evaluated, including:
        * Linear Regression
        * Ridge Regression
        * Decision Tree Regressor
        * Random Forest Regressor
        * Gradient Boosting Regressor
        * XGBoost Regressor
    * Hyperparameter tuning (e.g., using `GridSearchCV`) was performed to optimize model performance.

5.  **Model Evaluation:**
    * Models were evaluated using metrics such as Mean Squared Error (MSE), R-squared ($R^2$), and Mean Absolute Error (MAE).
    * The final model selection balanced accuracy with interpretability to provide practical insights.

## Results and Insights

* The `log_price` distribution showed a normal distribution, indicating predictable pricing.
* The chosen regression model effectively predicts Airbnb listing prices based on the engineered features.
* Key factors influencing pricing were identified, providing actionable insights for hosts to optimize their listings.
