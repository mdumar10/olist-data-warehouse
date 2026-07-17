# ==========================================================
# FILE        : gold_pipeline.py
# PROJECT     : Olist Pandas Pipeline
# DESCRIPTION : Gold Layer Pipeline
# ==========================================================

import pandas as pd

from config import SILVER_PATH, GOLD_PATH
from src.gold.transformations import (
    create_dim_customer,
    create_dim_product,
    create_dim_seller,
    create_dim_payment,
    create_dim_date,
    create_fact_sales,
    create_fact_payment,
    create_fact_reviews,
    create_fact_delivery,
)


def load_gold():

    print("\nCreating Gold Layer...\n")

    # ======================================================
    # Load Silver Datasets
    # ======================================================

    customers = pd.read_parquet(
        SILVER_PATH / "olist_customers_dataset.parquet"
    )

    products = pd.read_parquet(
        SILVER_PATH / "olist_products_dataset.parquet"
    )

    category_translation = pd.read_parquet(
        SILVER_PATH / "product_category_name_translation.parquet"
    )

    sellers = pd.read_parquet(
        SILVER_PATH / "olist_sellers_dataset.parquet"
    )


    payments = pd.read_parquet(
        SILVER_PATH / "olist_order_payments_dataset.parquet"
    )
    # ----------------------------------------------------------------
    orders = pd.read_parquet(
    SILVER_PATH / "orders.parquet"
    )

    start_date = orders["order_purchase_timestamp"].min()

    end_date = orders["order_purchase_timestamp"].max()

    # ======================================================
    # Create Dimensions
    # ======================================================

    dim_customer = create_dim_customer(customers)

    dim_product = create_dim_product(
        products,
        category_translation
    )

    dim_seller = create_dim_seller(sellers)

    dim_payment = create_dim_payment(payments)

    dim_date = create_dim_date(
        start_date,
        end_date
    )

    # ======================================================
    # Save Dimensions
    # ======================================================

    output_file = GOLD_PATH / "dim_customer.parquet"
    dim_customer.to_parquet(output_file, index=False)
    print(f"Saved : {output_file.name}")

    output_file = GOLD_PATH / "dim_product.parquet"
    dim_product.to_parquet(output_file, index=False)
    print(f"Saved : {output_file.name}")

    output_file = GOLD_PATH / "dim_seller.parquet"
    dim_seller.to_parquet(output_file, index=False)
    print(f"Saved : {output_file.name}")


    output_file = GOLD_PATH / "dim_payment.parquet"
    dim_payment.to_parquet(output_file, index=False)
    print(f"Saved : {output_file.name}")

    output_file = GOLD_PATH / "dim_date.parquet"

    dim_date.to_parquet(
        output_file,
        index=False
    )

    print(f"Saved : {output_file.name}")


    # ======================================================
    # Load Silver Fact Datasets
    # ======================================================

    order_items = pd.read_parquet(
        SILVER_PATH / "olist_order_items_dataset.parquet"
    )

    order_reviews = pd.read_parquet(
        SILVER_PATH / "olist_order_reviews_dataset.parquet"
    )




    # ======================================================
    # Create Facts
    # ======================================================

    fact_sales = create_fact_sales(
        orders,
        order_items,
        dim_customer,
        dim_product,
        dim_seller
    )

    fact_payment = create_fact_payment(
        orders,
        payments,
        dim_payment
    )

    fact_reviews = create_fact_reviews(
        order_reviews
    )

    fact_delivery = create_fact_delivery(
        orders
    )



    # ======================================================
    # Save Facts
    # ======================================================

    output_file = GOLD_PATH / "fact_sales.parquet"
    fact_sales.to_parquet(output_file, index=False)
    print(f"Saved : {output_file.name}")

    output_file = GOLD_PATH / "fact_payment.parquet"
    fact_payment.to_parquet(output_file, index=False)
    print(f"Saved : {output_file.name}")

    output_file = GOLD_PATH / "fact_reviews.parquet"
    fact_reviews.to_parquet(output_file, index=False)
    print(f"Saved : {output_file.name}")

    output_file = GOLD_PATH / "fact_delivery.parquet"
    fact_delivery.to_parquet(output_file, index=False)
    print(f"Saved : {output_file.name}")


    print("\nGold Layer Completed.")








# load_gold()

# │

# ├── Create Customer Dimension

# ├── Create Product Dimension

# ├── Create Seller Dimension

# ├── Create Payment Dimension

# ├── Create Date Dimension

# │

# ├── Create Fact Sales

# ├── Create Fact Payments

# ├── Create Fact Reviews

# └── Create Fact Delivery


# =========================================================





# fact_sales
# fact_payments
# fact_reviews
# fact_delivery





# dim_customer
# dim_product
# dim_seller
# dim_date
# dim_payment





#                  fact_sales
# -------------------------------------------------
# order_id
# order_item_id
# customer_key
# product_key
# seller_key
# date_key
# -------------------------
# price
# freight_value





#           fact_payments
# -----------------------------------
# order_id
# payment_sequential
# payment_key
# -----------------------------------
# payment_value
# payment_installments






#               fact_reviews
# ----------------------------------------
# review_id
# order_id
# review_date_key
# -------------------
# review_score





# fact_delivery
# -----------------------------------
# order_id

# purchase_date_key
# approved_date_key
# delivered_date_key
# estimated_delivery_date_key

# order_status
# -----------------------------------
# delivery_days


# =================================================================================




# dim_customer
# ------------------------
# customer_key

# customer_id

# customer_unique_id

# customer_zip_code_prefix

# customer_city

# customer_state






# dim_product
# -----------------------------------

# product_key

# product_id

# product_category_name

# product_category_name_english

# product_name_lenght

# product_description_lenght








# dim_seller
# ---------------------

# seller_key

# seller_id

# seller_zip_code_prefix

# seller_city

# seller_state



# dim_payment
# payment_key
# payment_type





# dim_date
# date_key
# full_date
# day
# month
# month_name
# quarter
# year
# weekday
# is_weekend