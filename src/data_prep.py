import pandas as pd
import requests
from io import StringIO
from sklearn.model_selection import train_test_split

from .config import RAW_DATA_URL, TRAIN_PATH, TEST_PATH, TARGET, TEST_SIZE, RANDOM_STATE

FEATURES = [
    "accommodates",
    "bedrooms",
    "bathrooms",
    "beds",
    "room_type",
    "neighbourhood"
]

def prepare_data():
    # Load raw Excel (NOT processed old CSV)
    resp = requests.get(RAW_DATA_URL)
    resp.raise_for_status()
    df = pd.read_csv(StringIO(resp.text))
    # Select only needed columns
    df = df[FEATURES + [TARGET]].dropna()

    # Ensure correct types
    df["room_type"] = df["room_type"].astype(str)
    df["neighbourhood"] = df["neighbourhood"].astype(str)

    print("After selecting features:", df.shape)

    train_df, test_df = train_test_split(
        df, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )

    train_df.to_csv(TRAIN_PATH, index=False)
    test_df.to_csv(TEST_PATH, index=False)

    print("Train:", train_df.shape, "Test:", test_df.shape)


if __name__ == "__main__":
    prepare_data()

    print("Data prep finished.")
