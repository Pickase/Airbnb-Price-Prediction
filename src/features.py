import pandas as pd

# SAME 6 FEATURES AS UI
FEATURES = [
    "accommodates",
    "bedrooms",
    "bathrooms",
    "beds",
    "room_type",
    "neighbourhood",
]

def split_features_labels(df, target):
    X = df[FEATURES].copy()
    y = df[target].copy()
    return X, y

def get_categorical_columns():
    return ["room_type", "neighbourhood"]
