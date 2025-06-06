from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, IntegerType, DoubleType, StringType, TimestampType

# 1. Create Spark session
spark = SparkSession.builder.appName("IoT Sensor Analysis - Task 1").getOrCreate()

# 2. Define schema (optional, you can also infer)
schema = StructType() \
    .add("sensor_id", IntegerType()) \
    .add("timestamp", StringType()) \
    .add("temperature", DoubleType()) \
    .add("humidity", DoubleType()) \
    .add("location", StringType()) \
    .add("sensor_type", StringType())

# 3. Load the CSV
df = spark.read.csv("sensor_data.csv", header=True, schema=schema)

# 4. Create a temp view
df.createOrReplaceTempView("sensor_readings")

# 5. Basic Queries
df.show(5)

spark.sql("SELECT COUNT(*) AS total_rows FROM sensor_readings").show()

spark.sql("SELECT DISTINCT location FROM sensor_readings").show()

# 6. Save DataFrame to output CSV
df.limit(5).write.mode("overwrite").option("header", True).csv("output/task1_output")
