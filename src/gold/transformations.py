import pandas as pd


# ==========================================================
# Create Customer Dimension
# ==========================================================

def create_dim_customer(df):

    print("Creating Customer Dimension...")

    df = df.copy()

    df.insert(
        0,
        "customer_key",
        range(1, len(df) + 1)
    )

    dim_customer = df[
        [
            "customer_key",
            "customer_id",
            "customer_unique_id",
            "customer_zip_code_prefix",
            "customer_city",
            "customer_state",
        ]
    ]

    return dim_customer


# ==========================================================
# Create Product Dimension
# ==========================================================

def create_dim_product(products, category_translation):

    print("Creating Product Dimension...")

    products = products.copy()

    products.insert(
        0,
        "product_key",
        range(1, len(products) + 1)
    )

    dim_product = pd.merge(
        products,
        category_translation,
        on="product_category_name",
        how="left"
    )

    dim_product = dim_product[
        [
            "product_key",
            "product_id",
            "product_category_name",
            "product_name_lenght",
            "product_description_lenght",
            "product_category_name_english",
        ]
    ]

    return dim_product


# ==========================================================
# Create Seller Dimension
# ==========================================================

def create_dim_seller(sellers):

    print("Creating Seller Dimension...")

    sellers = sellers.copy()

    sellers.insert(
        0,
        "seller_key",
        range(1, len(sellers) + 1)
    )

    dim_seller = sellers[
        [
            "seller_key",
            "seller_id",
            "seller_zip_code_prefix",
            "seller_city",
            "seller_state",
        ]
    ]

    return dim_seller



# ==========================================================
# Create Payment Dimension
# ==========================================================





def create_dim_payment(payments) :

    print("Creating Payments Dimension...")

    payments = payments.copy()

    payments = (
        payments[["payment_type"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    payments.insert(
        0,
        "payment_key",
        range(1, len(payments) + 1)
    )

    dim_payment = payments[
        [
            "payment_key",
            "payment_type",
        ]
    ]

    return dim_payment


# ==========================================================
# Create Date Dimension
# ==========================================================


def create_dim_date(start_date, end_date):

    print("Creating Date Dimension...")

    # ------------------------------------------------------
    # Create Calendar
    # ------------------------------------------------------

    dim_date = pd.DataFrame(
        {
            "full_date": pd.date_range(
                start=start_date,
                end=end_date,
                freq="D"
            )
        }
    )



    # ------------------------------------------------------
    # Date Attributes
    # ------------------------------------------------------

    dim_date["year"] = dim_date["full_date"].dt.year

    dim_date["quarter"] = dim_date["full_date"].dt.quarter

    dim_date["month"] = dim_date["full_date"].dt.month

    dim_date["month_name"] = dim_date["full_date"].dt.month_name()

    dim_date["day"] = dim_date["full_date"].dt.day

    dim_date["day_name"] = dim_date["full_date"].dt.day_name()

    dim_date["week_of_year"] = (
        dim_date["full_date"]
        .dt
        .isocalendar()
        .week
        .astype(int)
    )

    dim_date["month_year"] = (
        dim_date["full_date"]
        .dt
        .strftime("%Y-%m")
    )

    dim_date["is_weekend"] = dim_date["day_name"].isin(
        ["Saturday", "Sunday"]
    )

    # ------------------------------------------------------
    # Date Key
    # ------------------------------------------------------

    dim_date.insert(
        0,
        "date_key",
        dim_date["full_date"]
        .dt
        .strftime("%Y%m%d")
        .astype(int)
    )

    return dim_date




# =========================================================================


# ==========================================================
# Create Fact Sales
# ==========================================================

def create_fact_sales(
    orders,
    order_items,
    dim_customer,
    dim_product,
    dim_seller,
):

    print("Creating Fact Sales...")

    # ------------------------------------------------------
    # Copy
    # ------------------------------------------------------

    orders = orders.copy()
    order_items = order_items.copy()

    # ------------------------------------------------------
    # Merge Orders + Order Items
    # ------------------------------------------------------

    fact_sales = pd.merge(
        order_items,
        orders,
        on="order_id",
        how="left"
    )

    # ------------------------------------------------------
    # Customer Key
    # ------------------------------------------------------

    fact_sales = pd.merge(
        fact_sales,
        dim_customer[
            [
                "customer_id",
                "customer_key"
            ]
        ],
        on="customer_id",
        how="left"
    )

    # ------------------------------------------------------
    # Product Key
    # ------------------------------------------------------

    fact_sales = pd.merge(
        fact_sales,
        dim_product[
            [
                "product_id",
                "product_key"
            ]
        ],
        on="product_id",
        how="left"
    )

    # ------------------------------------------------------
    # Seller Key
    # ------------------------------------------------------

    fact_sales = pd.merge(
        fact_sales,
        dim_seller[
            [
                "seller_id",
                "seller_key"
            ]
        ],
        on="seller_id",
        how="left"
    )

    # ------------------------------------------------------
    # Date Key
    # ------------------------------------------------------

    fact_sales["date_key"] = (
        fact_sales["order_purchase_timestamp"]
        .dt
        .strftime("%Y%m%d")
        .astype(int)
    )

    # ------------------------------------------------------
    # Final Schema
    # ------------------------------------------------------

    fact_sales = fact_sales[
        [
            "order_id",
            "order_item_id",

            "customer_key",
            "product_key",
            "seller_key",
            "date_key",

            "price",
            "freight_value"
        ]
    ]

    return fact_sales





# ==========================================================
# Create Fact Payments
# ==========================================================




def create_fact_payment(
        orders,
        order_payments,
        dim_payment,
):


    print("Creating Fact Payments...")


    # -----------------------------------------------------------
    # copy
    # ------------------------------------------------------------

    orders = orders.copy()
    order_payments = order_payments.copy()


    # ------------------------------------------------------
    # Merge orders + order_payments 
    # ------------------------------------------------------

    fact_payment = pd.merge(
            order_payments,
            orders,
            on="order_id",
            how="left"
        )


    # ------------------------------------------------------
    # payment_key
    # ------------------------------------------------------

    fact_payment = pd.merge(
        fact_payment,
        dim_payment[
            [
                "payment_type",
                "payment_key"
            ]
        ],
        on="payment_type",
        how="left"
    )

    # ------------------------------------------------------
    # Final Schema
    # ------------------------------------------------------

    fact_payment = fact_payment[
        [
            "order_id",
            "payment_sequential",
            "payment_key",
            "payment_value",
            "payment_installments",
        ]
    ]    


    return fact_payment



# ==========================================================
# Create Fact Reviwes
# ==========================================================


def create_fact_reviews( 
     order_reviews 
      ):

    print("Creating Fact Reviews...")


    # -----------------------------------------------------------
    # copy
    # ------------------------------------------------------------    


    fact_reviews = order_reviews.copy()



    # ------------------------------------------------------
    # Date Key
    # ------------------------------------------------------

    fact_reviews["review_date_key"] = (
        fact_reviews["review_creation_date"]
        .dt
        .strftime("%Y%m%d")
        .astype(int)
    )

    fact_reviews   = fact_reviews [
        [
            "review_id",
            "order_id",

            "review_date_key",
            "review_score",

        ]
    ]


    return fact_reviews
   

# ==========================================================
# Create Fact Delivery
# ==========================================================

def create_fact_delivery(orders):

    print("Creating Fact Delivery...")

    # ------------------------------------------------------
    # Copy
    # ------------------------------------------------------

    fact_delivery = orders.copy()

    # ------------------------------------------------------
    # Date Keys
    # ------------------------------------------------------

    fact_delivery["purchase_date_key"] = (
        fact_delivery["order_purchase_timestamp"]
        .dt.strftime("%Y%m%d")
    )

    fact_delivery["approved_date_key"] = (
        fact_delivery["order_approved_at"]
        .dt.strftime("%Y%m%d")
    )

    fact_delivery["delivered_date_key"] = (
        fact_delivery["order_delivered_customer_date"]
        .dt.strftime("%Y%m%d")
    )

    fact_delivery["estimated_delivery_date_key"] = (
        fact_delivery["order_estimated_delivery_date"]
        .dt.strftime("%Y%m%d")
    )

    # ------------------------------------------------------
    # Keep NULLs instead of crashing
    # ------------------------------------------------------

    fact_delivery["purchase_date_key"] = pd.to_numeric(
        fact_delivery["purchase_date_key"],
        errors="coerce"
    ).astype("Int64")

    fact_delivery["approved_date_key"] = pd.to_numeric(
        fact_delivery["approved_date_key"],
        errors="coerce"
    ).astype("Int64")

    fact_delivery["delivered_date_key"] = pd.to_numeric(
        fact_delivery["delivered_date_key"],
        errors="coerce"
    ).astype("Int64")

    fact_delivery["estimated_delivery_date_key"] = pd.to_numeric(
        fact_delivery["estimated_delivery_date_key"],
        errors="coerce"
    ).astype("Int64")

    # ------------------------------------------------------
    # Final Schema
    # ------------------------------------------------------

    fact_delivery = fact_delivery[
        [
            "order_id",
            "purchase_date_key",
            "approved_date_key",
            "delivered_date_key",
            "estimated_delivery_date_key",
            "order_status",
        ]
    ]

    return fact_delivery

    # ------------------------------------------------------
    # Final Schema
    # ------------------------------------------------------

    fact_delivery = fact_delivery[
        [
            "order_id",

            "purchase_date_key",
            "approved_date_key",
            "delivered_date_key",
            "estimated_delivery_date_key",

            "order_status",

        ]
    ]

    return fact_delivery










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





# dim_payment
# payment_key
# payment_type

# def create_dim_payment(payments) :

#     print("Creating Payments Dimension...")

#     payments = payments.copy()

#     payments.insert(
#         0,
#         "payment_key",
#         range(1, len(payments) + 1)
#     )

#     dim_payment = payments[
#         [
#             "payment_key",
#             "order_id",
#             "payment_sequential",
#             "payment_value",
#             "payment_installments",
#         ]
#     ]

#     return dim_payment










    #           fact_payments
# -----------------------------------
# order_id
# payment_sequential
# payment_key
# -----------------------------------
# payment_value
# payment_installments
