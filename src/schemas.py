from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType

def get_bronze_schema():
    """
    Defines the schema for the raw E-commerce data in the Bronze layer.
    """
    return StructType([
        StructField("InvoiceNo", StringType(), True),
        StructField("StockCode", StringType(), True),
        StructField("Description", StringType(), True),
        StructField("Quantity", IntegerType(), True),
        StructField("InvoiceDate", StringType(), True),
        StructField("UnitPrice", DoubleType(), True),
        StructField("CustomerID", DoubleType(), True),
        StructField("Country", StringType(), True)
    ])