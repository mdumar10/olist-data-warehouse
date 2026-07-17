# ============================================================
# FILE         : silver_pipeline.py
# PROJECT      : Olist Pandas Pipeline
# DESCRIPTION  : Silver Layer Pipeline
# ============================================================



import pandas as pd

from config import BRONZE_PATH, SILVER_PATH
from src.utils.file_utils import get_parquet_files
from src.silver.transformations import clean_customers, clean_orders , clean_order_items , clean_products , clean_sellers ,clean_order_reviews , clean_geolocation


def load_silver():

    parquet_files = get_parquet_files(BRONZE_PATH)

    print(f"\nFound {len(parquet_files)} parquet files.\n")

    for parquet_file in parquet_files:

        print(f"Reading : {parquet_file.name}")

        df = pd.read_parquet(parquet_file)

        # =====================================================
        # Apply Transformations
        # =====================================================

        if parquet_file.name == "olist_customers_dataset.parquet":
            df = clean_customers(df)

        elif parquet_file.name == "orders.parquet":
            df = clean_orders(df)

        elif parquet_file.name == "olist_order_items_dataset.parquet":
            df = clean_order_items(df)

        elif parquet_file.name == "olist_products_dataset.parquet":
            df = clean_products(df)

        elif parquet_file.name == "olist_sellers_dataset.parquet":
            df = clean_sellers(df)

        elif parquet_file.name == "olist_order_reviews_dataset.parquet":
            df = clean_order_reviews(df)

        elif parquet_file.name == "olist_geolocation_dataset.parquet":
            df = clean_geolocation(df)

        

        # =====================================================
        # Save Silver Dataset
        # =====================================================

        output_file = SILVER_PATH / parquet_file.name

        df.to_parquet(output_file, index=False)

        print(f"Saved : {output_file.name}")

    print("\nSilver Layer Completed.")


