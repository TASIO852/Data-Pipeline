from pyspark.sql import SparkSession
from pyspark.sql import functions as f

spark = SparkSession.builder.appName('SparkStreaming').getOrCreate()
# criação do dataframe spark
lines = spark.readStream\
    .format('socket')\
    .option('host', 'localhost')\
    .option('port', 9009)\
    .load()

words = f.split(lines.value)

query = lines.writeStream\
    .outputMode('append')\
    .format('console')\
    .start()

query.awaitTermination()