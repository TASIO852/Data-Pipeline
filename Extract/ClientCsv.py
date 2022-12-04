from pyspark.sql import SparkSession
import shutil

for item in ['/Data/src','/Data/src'] :
    try:
        shutil.rmtree(item)
    except OSError as err:
        print(f'Aviso: {err.strerror}')

spark = SparkSession.builder.appName('SparkStreaming').getOrCreate()

tweets = spark.readStream\
    .format('socket')\
    .option('host', 'localhost')\
    .option('port', 9090)\
    .load()


query = tweets.writeStream\
    .outputMode('append')\
    .option('encoding','utf-8')\
    .format('csv')\
    .option('path','/Data/src')\
    .option('checkpointLocation','/Data/src')\
    .start()

query.awaitTermination()