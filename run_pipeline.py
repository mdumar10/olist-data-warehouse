# ============================================================
# FILE         : run_pipeline.py
# PROJECT      : Olist Pandas Pipeline
# DESCRIPTION  : Main pipeline runner
# ============================================================

from src.bronze.bronze_pipeline import load_bronze
from src.silver.silver_pipeline import load_silver
from src.gold.gold_pipeline import load_gold


def main():

    print("=" * 50)
    print("Olist Pandas Pipeline")
    print("=" * 50)

    print("\nRunning Bronze Layer...")
    load_bronze()

    print("\nRunning Silver Layer...")
    load_silver()

    print("\nRunning Gold Layer...")
    load_gold()

    print("\nPipeline Completed Successfully.")


if __name__ == "__main__":
    main()
