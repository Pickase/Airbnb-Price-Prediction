import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from catboost import CatBoostRegressor

from .config import TEST_PATH, MODEL_PATH, TARGET
from .features import split_features_labels

def evaluate_model():
    df = pd.read_csv(TEST_PATH)

    X_test, y_test = split_features_labels(df, TARGET)

    model = CatBoostRegressor()
    model.load_model(MODEL_PATH)

    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    rmse = mean_squared_error(y_test, preds) ** 0.5
    r2 = r2_score(y_test, preds)

    print("MAE:", mae)
    print("RMSE:", rmse)
    print("R²:", r2)

if __name__ == "__main__":
    evaluate_model()

    print("Evaluation finished.")