import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Your raw Excel file
RAW_DATA_URL = "https://docs.google.com/spreadsheets/d/182TQXHhwLbBa-Z3PGxPTGqny_v3iIwKP/export?format=csv"


# Processed CSVs
TRAIN_PATH = os.path.join(BASE_DIR, "data", "processed", "train.csv")
TEST_PATH = os.path.join(BASE_DIR, "data", "processed", "test.csv")

MODEL_PATH = os.path.join(BASE_DIR, "models", "price_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "models", "encoder.pkl")

# Target column name in your dataset
# Change to the exact name if it's "Price" or something else
TARGET = "log_price"

TEST_SIZE = 0.2
RANDOM_STATE = 42
