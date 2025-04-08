from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("IoT Task 2 SQL").getOrCreate()

df = spark.read.csv("sensor_data.csv", header=True, inferSchema=True)
df.createOrReplaceTempView("sensor_readings")

# Count in-range and out-of-range temperatures
in_range = spark.sql("""
    SELECT * FROM sensor_readings
    WHERE temperature BETWEEN 18 AND 30
""")
print("In-range count:", in_range.count())

out_range = spark.sql("""
    SELECT * FROM sensor_readings
    WHERE temperature < 18 OR temperature > 30
""")
print("Out-of-range count:", out_range.count())

# Aggregation by location
agg_result = spark.sql("""
    SELECT
        location,
        ROUND(AVG(temperature), 1) AS avg_temperature,
        ROUND(AVG(humidity), 1) AS avg_humidity
    FROM sensor_readings
    GROUP BY location
    ORDER BY avg_temperature DESC
""")

agg_result.coalesce(1).write.option("header", True).csv("output/task2_output")
