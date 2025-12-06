import pandas as pd
from catboost import CatBoostRegressor

from .config import TRAIN_PATH, MODEL_PATH, TARGET
from .features import split_features_labels, get_categorical_columns
from .pipelines import get_model

def train_model():
    df = pd.read_csv(TRAIN_PATH)
    print("Train data:", df.shape)

    X, y = split_features_labels(df, TARGET)

    cat_cols = get_categorical_columns()
    print("Categorical cols:", cat_cols)

    model = get_model()

    model.fit(
        X,
        y,
        cat_features=cat_cols
    )

    model.save_model(MODEL_PATH)
    print("Saved model:", MODEL_PATH)


if __name__ == "__main__":
    train_model()
