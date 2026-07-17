# ============================================================
# FILE         : config.py
# PROJECT      : Olist Pandas Pipeline
# DESCRIPTION  : Database and path configuration
# ============================================================

from pathlib import Path

# ============================================================
# root Config
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent  


# ============================================================
# database Config
# ============================================================



DATA_PATH = PROJECT_ROOT / "data" / "olist_data_set"

OUTPUT_PATH = PROJECT_ROOT / "output"

BRONZE_PATH = OUTPUT_PATH / "bronze"

SILVER_PATH = OUTPUT_PATH / "silver"

GOLD_PATH = OUTPUT_PATH / "gold"

LOG_PATH = PROJECT_ROOT / "logs"