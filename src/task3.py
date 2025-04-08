from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp

spark = SparkSession.builder.appName("IoT Task 3 SQL").getOrCreate()

df = spark.read.csv("sensor_data.csv", header=True, inferSchema=True)
df = df.withColumn("timestamp", to_timestamp("timestamp"))
df.createOrReplaceTempView("sensor_readings")

# Hour-based aggregation
hourly_temp = spark.sql("""
    SELECT
        HOUR(timestamp) AS hour_of_day,
        ROUND(AVG(temperature), 1) AS avg_temp
    FROM sensor_readings
    GROUP BY HOUR(timestamp)
    ORDER BY hour_of_day
""")

hourly_temp.coalesce(1).write.option("header", True).csv("output/task3_output")
