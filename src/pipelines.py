from catboost import CatBoostRegressor

def get_model():
    return CatBoostRegressor(
        iterations=1200,           # more boosting rounds
        learning_rate=0.03,        # slower but more precise
        depth=8,                   # more interaction power
        l2_leaf_reg=6,             # regularization for stability
        loss_function="RMSE",
        random_seed=42,
        subsample=0.8,             # bagging improves generalization
        colsample_bylevel=0.8,     # feature sampling
        min_data_in_leaf=3,        # avoid overfitting
        grow_policy="Lossguide",   # makes CatBoost perform better on small features
        verbose=False
    )
