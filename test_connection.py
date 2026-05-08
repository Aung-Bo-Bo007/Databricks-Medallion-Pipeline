from databricks.connect import DatabricksSession

# Connection settings ကို ကုဒ်ထဲမှာပဲ တိုက်ရိုက်သတ်မှတ်ခြင်း
spark = DatabricksSession.builder.remote(
    host="https://dbc-eca9a387-3473.cloud.databricks.com",
    token="dapib4e161127cec6da4ae630f2dd97cfce0",
    serverless=True
).getOrCreate()

# Connection ရှိမရှိ စမ်းသပ်ခြင်း
print("Connecting to Databricks...")
try:
    df = spark.sql("SELECT 'Connection Successful!' as status")
    df.show()
except Exception as e:
    print(f"Error: {e}")
