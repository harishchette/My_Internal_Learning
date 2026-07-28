from pyspark.sql import SparkSession
import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Test") \
    .getOrCreate()

data = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]
schema = ["id", "name"]
df = spark.createDataFrame(data, schema)

# Show the DataFrame
print("Sample DataFrame:")
df.show()

# Perform a simple transformation
result = df.filter(df.id > 1)
print("Filtered DataFrame:")
result.show()

spark.stop()