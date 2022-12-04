# importando as bibliotecas
from pyspark.sql import SparkSession
from pyspark.sql import Row
from kafka import KafkaConsumer
import findspark
import os
from datetime import datetime
import tweepy
from json import dumps

os.environ["JAVA_HOME"] = "C:/Program Files/Java/jre1.8.0_351"
os.environ["SPARK_HOME"] = "C:/Users/tasio.guimaraes/Documents/Spark/spark-3.3.1-bin-hadoop3"

findspark.init()

# configuração do kafka consumer
brokers = ['localhost:9092']
topic = 'tweets'
consumer = KafkaConsumer(topic, group_id = 'group1', bootstrap_servers = brokers)

# configuração da API twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
tweets = api.search('machine learning')

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
    spark.sparkContext.setLogLevel('INFO')

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
    df.selectExpr("CAST(twitter AS STRING)", "CAST(twitter AS STRING)") \
        .writeStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS_CONS) \
        .option("topic", KAFKA_TOPIC_NAME_CONS) \
        .save()

# ver dados
    df.printSchema()
    df.show(5)

# Gravando os dados na AWS

# # importando as bibliotecas
# from kafka import KafkaConsumer
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# import json
# from IPython.display import clear_output

# #configuração do kafka
# brokers = ['localhost:9092']
# topic = 'tweets'
# consumer = KafkaConsumer(topic, group_id = 'group1', bootstrap_servers = brokers)

# # geração da nuvem de palavras em tempo real
# frases = ''
# for messagem in consumer:
#     texto = json.loads(messagem.value.decode('utf-8'))
#     frases = frases + texto['tweet']
#     clear_output()
#     wordcloud = WordCloud(max_font_size=100, width = 1520, height = 535).generate(frases)
#     plt.figure(figsize=(16,9))
#     plt.imshow(wordcloud)
#     plt.axis("off")
#     plt.show()