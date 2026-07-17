# ============================================================
# FILE         : transformations.py
# PROJECT      : Olist Pandas Pipeline
# DESCRIPTION  : All Silver Layer cleaning functions
# ============================================================

import pandas as pd


# ===================================================================
# Clean Customers Table
# ===================================================================

def clean_customers(df):

    print("Cleaning Customers Dataset...")

    df["customer_zip_code_prefix"] = (
        df["customer_zip_code_prefix"]
        .astype(str)
        .str.zfill(5)
    )

    return df


# ===================================================================
# Clean Orders Table
# ===================================================================

def clean_orders(df):

    print("Cleaning Orders Dataset...")

    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    for column in date_columns:
        df[column] = pd.to_datetime(df[column])

    return df



# ===================================================================
# Clean order_items_dataset Table
# ===================================================================



def clean_order_items(df):

    print("Cleaning Orders item Dataset...")

    df["shipping_limit_date"] = pd.to_datetime(df["shipping_limit_date"])

    return df



# ===================================================================
# Clean products Table
# ===================================================================




def clean_products(df):

    print("Cleaning Products Dataset...")

    df["product_category_name"] = (
        df["product_category_name"]
        .fillna("Unknown")
    )

    return df


# ===================================================================
# Clean sellers Table
# ===================================================================



def clean_sellers(df):

    print("Cleaning Sellers Dataset...")

    df["seller_zip_code_prefix"] = (
        df["seller_zip_code_prefix"]
        .astype(str)
        .str.zfill(5)
    )

    return df







# ===================================================================
# Clean order reviews Table
# ===================================================================


def clean_order_reviews(df):

    print("Cleaning Order Reviews Dataset...")

    date_columns = [
        "review_creation_date",
        "review_answer_timestamp"
    ]

    for column in date_columns:
        df[column] = pd.to_datetime(df[column])

    return df


# ===================================================================
# Clean Geolocation Table
# ===================================================================

def clean_geolocation(df):

    print("Cleaning Geolocation Dataset...")

    # Convert ZIP code to 5-digit string
    df["geolocation_zip_code_prefix"] = (
        df["geolocation_zip_code_prefix"]
        .astype(str)
        .str.zfill(5)
    )

    # Remove leading/trailing spaces from city names
    df["geolocation_city"] = (
        df["geolocation_city"]
        .str.strip()
    )

    # Remove exact duplicate rows
    df = df.drop_duplicates()

    return df





# ============================================================
# NO TRANSFORMATION REQUIRED
# ============================================================
# product_category_name_translation.parquet
#   - Data types are correct
#   - No null values
#   - No duplicate rows
#   - No leading/trailing spaces


#--------------------------------------------------------------------


# olist_order_payments_dataset.parquet
#   - Data types are correct
#   - No null values
#   - No duplicate rows
#   - No leading/trailing spaces
#   - Found 2 records with payment_installments = 0
#     (Documented as a data quality issue, not automatically corrected)
# ============================================================



