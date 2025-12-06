import pandas as pd
import numpy as np

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleaning:
    - drop duplicate rows
    - replace obvious missing markers with NaN
    - fill remaining NaN with 0 (or you can change this later)
    """
    df = df.drop_duplicates()

    # If your dataset uses things like "NA", "?" etc, treat them as missing
    df = df.replace(["?", "NA", "NaN", "nan", ""], np.nan)

    # For now, fill missing values with 0 (simple but safe for running the pipeline)
    df = df.fillna(0)

    return df
