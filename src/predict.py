import numpy as np
import pandas as pd
from catboost import CatBoostRegressor

from .config import MODEL_PATH, TRAIN_PATH, TARGET
from .features import get_categorical_columns

_model = None
_train_df = None

def _load():
    global _model, _train_df

    if _model is None:
        _model = CatBoostRegressor()
        _model.load_model(MODEL_PATH)

    if _train_df is None:
        _train_df = pd.read_csv(TRAIN_PATH)

    return _model, _train_df


def predict_price(ui: dict) -> float:
    model, train_df = _load()

    # Build dataframe aligned to training data
    X = train_df.drop(columns=[TARGET]).iloc[[0]].copy()

    # Insert UI values
    for col, val in ui.items():
        X[col] = val

    # Ensure correct category dtype
    for col in get_categorical_columns():
        X[col] = X[col].astype(str)

    # Predict log-price then exponentiate
    log_price = model.predict(X)[0]
    return float(np.exp(log_price))
