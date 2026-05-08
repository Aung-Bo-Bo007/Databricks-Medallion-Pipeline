from pyspark.sql.functions import col, to_timestamp, sha2, current_timestamp

def apply_silver_transformations(df):
    """
    Applies data transformation and PII masking for the Silver Layer.
    Includes: 
    - Date formatting
    - CustomerID hashing (SHA-256)
    - Data quality flag (is_valid)
    """
    return df.withColumn(
        "InvoiceTimestamp", to_timestamp(col("InvoiceDate"), "M/d/yyyy H:mm")
    ).withColumn(
        "CustomerID", sha2(col("CustomerID").cast("string"), 256)
    ).withColumn(
        "processed_at", current_timestamp()
    ).withColumn(
        "is_valid", 
        (col("CustomerID").isNotNull()) & (col("Quantity") > 0) & (col("UnitPrice") > 0)
    )