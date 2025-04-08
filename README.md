# Iot-sensor-data-spark-sql
---

## Overview

This project involves analyzing IoT sensor data using **Apache Spark SQL**. The dataset contains temperature, humidity, timestamp, location, and sensor type details from various sensors deployed across multiple building floors.

The analysis includes:
- Loading and exploring data
- Filtering and aggregating sensor readings
- Time-based analytics
- Sensor performance ranking using window functions
- Pivot table creation for pattern interpretation
  
---

## **Prerequisites**

Before starting the assignment, ensure you have the following software installed and properly configured on your machine:

1. **Python 3.x**:
   - [Download and Install Python](https://www.python.org/downloads/)
   - Verify installation:
     ```bash
     python3 --version
     ```

2. **PySpark**:
   - Install using `pip`:
     ```bash
     pip install pyspark
     ```

3. **Faker**:
   - Install using `pip`:
     ```bash
     pip install faker
     ```

4. **Apache Spark**:
   - Ensure Spark is installed. You can download it from the [Apache Spark Downloads](https://spark.apache.org/downloads.html) page.
   - Verify installation by running:
     ```bash
     spark-submit --version
     ```
---

## Dataset
Each record includes:
- `sensor_id`: Unique identifier for each sensor
- `timestamp`: Time when the reading was recorded
- `temperature`: Temperature in Celsius
- `humidity`: Humidity percentage
- `location`: Floor/building where the sensor is located
- `sensor_type`: Type of sensor (e.g., TypeA, TypeB)
---

## 📁 Project Structure

```bash
assignment-3-spark-structured-api-Krishna-coder12-main/
├── README.md
├── data_generator.py
├── sensor_data.csv
├── output/
│   ├── task1_output
│   ├── task2_output
│   ├── task3_output
│   ├── task4_output
│   ├── task5_output
├── src/
│   ├── task1.py
│   ├── task2.py
│   ├── task3.py
│   ├── task4.py
│   └── task5.py
```
---

## 💻 Execution Commands

```bash
#Generating Dataset
python data_generator.py

# Run any task
spark-submit src/task1.py
spark-submit src/task2.py
spark-submit src/task3.py
spark-submit src/task4.py
spark-submit src/task5.py
```

---

## Tasks Completed
### Task 1: Load & Basic Exploration
- Loaded the `sensor_data.csv` file using Spark with inferred schema.
- Registered a temporary view `sensor_readings`.
- Ran basic SQL queries:
  - Displayed first 5 records.
  - Counted total records.
  - Retrieved distinct sensor locations.
- ✅ Output: `task1_output`
---
### Task 2: Filtering & Simple Aggregations
- Filtered out temperature readings <18 or >30.
- Counted number of in-range and out-of-range readings.
- Grouped by location to compute:
  - Average temperature
  - Average humidity
- Sorted by average temperature to find hottest location.
- ✅ Output: `task2_output`
---
### Task 3: Time-Based Analysis
- Converted `timestamp` column to Spark `TimestampType`.
- Extracted hour (0–23) from timestamps.
- Grouped by hour to compute average temperature.
- Identified hour with highest average temperature.
- ✅ Output: `task3_output`
---
### Task 4: Window Function - Sensor Ranking
- Computed each `sensor_id`'s average temperature.
- Applied `DENSE_RANK()` to rank sensors in descending order.
- Displayed top 5 sensors based on temperature.
- ✅ Output: `task4_output`
---
### Task 5: Pivot & Interpretation
- Created a pivot table:
  - Rows: `location`
  - Columns: `hour_of_day` (0–23)
  - Values: Average `temperature`
- Identified `(location, hour)` pair with the highest average temperature.
- ✅ Output: `task5_output`

---

## Outputs
---
## Task 1: Load & Basic Exploration

| sensor_id | timestamp           | temperature | humidity | location         | sensor_type |
|-----------|---------------------|-------------|----------|------------------|-------------|
| 1030      | 2025-04-06 11:13:43 | 33.59       | 40.94    | BuildingA_Floor2 | TypeC       |
| 1083      | 2025-04-07 02:33:05 | 20.89       | 49.43    | BuildingA_Floor1 | TypeA       |
| 1066      | 2025-04-05 13:10:19 | 31.07       | 52.75    | BuildingB_Floor2 | TypeA       |
| 1022      | 2025-04-06 16:31:19 | 30.19       | 39.59    | BuildingA_Floor2 | TypeA       |
| 1094      | 2025-04-03 05:30:20 | 31.10       | 59.99    | BuildingA_Floor1 | TypeC       |

---
## Task 2: Filtering & Simple Aggregations

| location         | avg_temperature | avg_humidity |
|------------------|-----------------|--------------|
| BuildingB_Floor1 | 25.8            | 54.8         |
| BuildingA_Floor2 | 25.0            | 54.4         |
| BuildingA_Floor1 | 24.8            | 55.7         |
| BuildingB_Floor2 | 24.5            | 53.8         |

---
## Task 3: Time-Based Analysis

| hour_of_day | avg_temp |
|-------------|----------|
| 0           | 24.8     |
| 1           | 26.4     |
| 2           | 25.7     |
| 3           | 24.1     |
| 4           | 24.7     |
| 5           | 26.6     |
| 6           | 24.2     |
| 7           | 24.2     |
| 8           | 24.0     |
| 9           | 24.3     |
| 10          | 25.1     |
| 11          | 26.2     |
| 12          | 25.0     |
| 13          | 25.7     |
| 14          | 24.4     |
| 15          | 24.7     |
| 16          | 25.0     |
| 17          | 24.5     |
| 18          | 26.0     |
| 19          | 24.2     |
| 20          | 23.7     |
| 21          | 25.0     |
| 22          | 25.3     |
| 23          | 27.1     |

---
## Task 4: Window Function - Sensor Ranking

| sensor_id | avg_temp | rank_temp |
|-----------|----------|-----------|
| 1002      | 31.8     | 1         |
| 1047      | 29.4     | 2         |
| 1020      | 29.2     | 3         |
| 1053      | 29.1     | 4         |
| 1099      | 28.4     | 5         |

---
## Task 5: Pivot & Interpretation

| Location          | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   | 11   | 12   | 13   | 14   | 15   | 16   | 17   | 18   | 19   | 20   | 21   | 22   | 23   |
|-------------------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| BuildingA_Floor1  | 25.5 | 24.6 | 26.3 | 22.4 | 24.2 | 26.6 | 25.0 | 23.9 | 21.6 | 23.4 | 27.7 | 25.4 | 23.0 | 25.5 | 24.5 | 24.0 | 24.5 | 24.3 | 28.8 | 21.4 | 24.5 | 25.2 | 27.6 | 25.7 |
| BuildingB_Floor2  | 25.8 | 24.2 | 26.5 | 24.8 | 22.3 | 24.0 | 22.2 | 21.8 | 25.0 | 23.1 | 25.6 | 25.9 | 26.9 | 26.4 | 22.9 | 23.3 | 25.0 | 22.2 | 23.6 | 24.4 | 22.9 | 22.7 | 24.4 | 28.3 |
| BuildingA_Floor2  | 24.9 | 27.2 | 24.5 | 25.3 | 25.8 | 26.9 | 22.1 | 25.6 | 22.8 | 24.4 | 24.1 | 26.2 | 25.1 | 23.4 | 24.6 | 25.0 | 27.7 | 26.8 | 27.1 | 21.0 | 20.8 | 25.2 | 22.7 | 27.7 |
| BuildingB_Floor1  | 22.7 | 28.7 | 24.8 | 23.9 | 27.1 | 28.4 | 26.8 | 25.1 | 25.9 | 25.8 | 23.1 | 28.8 | 25.0 | 26.6 | 25.2 | 26.1 | 22.8 | 24.2 | 25.3 | 25.9 | 25.2 | 27.1 | 28.3 | 26.5 |

---
