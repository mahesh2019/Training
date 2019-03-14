# Drill vs Spark

The Drill is designed to be a distributed SQL query engine for pretty much everything.
Spark is a general computation engine which offers some limited SQL capabilities.
If you are considering Spark only for SparkSQL my suggestion is to reconsider and move in the direction of Apache Drill.
If you need to perform complex math, statistics, or machine learning, then Apache Spark is a good place for you to start. 
If that isn't the case, then Apache Drill is where you want to be.

Performance analysis among Spark & Drill:

Spark : In spark is module towork with structured data. we can query the data from Scala, Python, Java. We can use get access with tools like Spark Streaming and the MLlib machine learning libraries.

Drill : In Drill  can use a number of data formats, including Parquet, MongoDB etc. Drill especially useful for business intelligence.
Conclusion : If, we need mainly to query data quickly, across multiple data source.

#### Code for Drill
- SELECT * FROM dfs.`hdfs/company.csv` limit 5;

#### Code for spark

import pyspark

from pyspark.sql import SparkSession

from pyspark.sql import SQLContext

spark = SparkSession .builder .appName("Python Spark SQL basic example") .config("spark.some.config.option", "some-value") .getOrCreate()

sparkSession = SparkSession.builder.appName("example-pyspark-read-and-write").getOrCreate()

df_load = sparkSession.read.csv("hdfs://localhost:54310/hdfs/demolarge4.csv")

df_load.show(29693, False)

csvFile = spark.read.csv('hdfs://localhost:54310/hdfs/demolarge4.csv')

csvFile.printSchema()

csvFile.createOrReplaceTempView("demolarge4")

value = spark.sql("SELECT * FROM demolarge4 limit 5")

value.show()

#### Results are:

##### Drill execution time for csv,paraquent and json respectively:
- 2.84 sec
- 3.76 sec
- 1.92 sec

##### Spark execution time is:
- 1.9  sec
- 3.89 sec
- 1.17 sec


