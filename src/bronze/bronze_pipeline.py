

# ============================================================
# FILE         : bronze_pipeline.py
# PROJECT      : Olist Pandas Pipeline
# DESCRIPTION  : Bronze Layer Pipeline
# ============================================================

import pandas as pd

from config import BRONZE_PATH
from config import DATA_PATH, BRONZE_PATH
from src.utils.file_utils import get_csv_files


def load_bronze():

    csv_files = get_csv_files(DATA_PATH)

    print(f"\nFound {len(csv_files)} CSV files.\n")

    for csv_file in csv_files:

        print(f"Reading : {csv_file.name}")

        # Read CSV
        df = pd.read_csv(csv_file)

        # Create parquet filename
        parquet_file = BRONZE_PATH / f"{csv_file.stem}.parquet"

        # Save as parquet
        df.to_parquet(parquet_file, index=False)

        print(f"Saved   : {parquet_file.name}")

        print("-" * 50)

    print("\nBronze Pipeline Finished.")