# importando as bibliotecas
from pyspark.sql import SparkSession
from pyspark.sql import Row
from kafka import KafkaConsumer
import findspark
import os

os.environ["JAVA_HOME"] = "C:/Program Files/Java/jre1.8.0_351"
os.environ["SPARK_HOME"] = "C:/Users/tasio.guimaraes/Documents/Spark/spark-3.3.1-bin-hadoop3"

findspark.init()

if __name__ == "__main__":

# configuração do spark
    spark = SparkSession \
        .builder \
        .appName("Kafka tweet") \
        .master("spark://spark-master:7077") \
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0") \
        .enableHiveSupport() \
        .getOrCreate()
        
# log information    
    spark.sparkContext.setLogLevel('INFO ')

# configuração do kafka
    KAFKA_BOOTSTRAP_SERVERS_CONS = ['localhost:9092']
    KAFKA_TOPIC_NAME_CONS = 'tweet'

# Construir um DataFrame que leia tweet
    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS_CONS) \
        .option("subscribe", KAFKA_TOPIC_NAME_CONS) \
        .option("startingOffsets", "earliest") \
        .load()

# Escrevendo os dados do kafka no spark
    df.selectExpr("CAST(twitter AS STRING)", "CAST(twitternw AS STRING)") \
        .writeStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS_CONS) \
        .option("topic", KAFKA_TOPIC_NAME_CONS) \
        .save()

# ver dados
    df.printSchema()
    df.show(5)

# Gravando os dados na AWS

