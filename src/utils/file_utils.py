# ============================================================
# FILE         : file_utils.py
# PROJECT      : Olist Pandas Pipeline
# DESCRIPTION  : Common file handling utilities
# ============================================================

from pathlib import Path


def get_csv_files(folder_path):

    csv_files = list(folder_path.glob("*.csv"))

    if not csv_files:
        print(f"[INFO] No CSV files found in: {folder_path}")

    return csv_files


# ============================================================
# Function to get all parquet files
# ============================================================

def get_parquet_files(folder_path):

    parquet_files = list(folder_path.glob("*.parquet"))

    if not parquet_files:
        print(f"[INFO] No Parquet files found in: {folder_path}")

    return parquet_files