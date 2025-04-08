from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("IoT Task 4 SQL").getOrCreate()

df = spark.read.csv("sensor_data.csv", header=True, inferSchema=True)
df.createOrReplaceTempView("sensor_readings")

ranked_sensors = spark.sql("""
    SELECT
        sensor_id,
        ROUND(AVG(temperature), 1) AS avg_temp,
        DENSE_RANK() OVER (ORDER BY AVG(temperature) DESC) AS rank_temp
    FROM sensor_readings
    GROUP BY sensor_id
    ORDER BY rank_temp
    LIMIT 5
""")

ranked_sensors.coalesce(1).write.option("header", True).csv("output/task4_output")
