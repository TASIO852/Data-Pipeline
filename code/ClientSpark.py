# twitter dos pais da copa
import tweepy
import socket
import boto3
from pyspark.sql import SparkSession
from pyspark.sql import functions as f
import findspark
import os

# colocar PATH da instancia EC2
os.environ["JAVA_HOME"] = "C:/Program Files/Java/jre1.8.0_351"
os.environ["SPARK_HOME"] = "C:/Users/tasio.guimaraes/Documents/Spark/spark-3.3.1-bin-hadoop3"
findspark.init()

# Lisiner para receber dados com lambda
HOST = socket.gethostbyaddr('aws.ec2.private.ip')
PORT = 9009
s = socket.socket()
s.bind((HOST, PORT))
print(f"Aguardando conexão na porta: {PORT}")

s.listen(5)
connection, address = s.accept()
print(f"Recebendo solicitação de {address}")

token = "seu token "
keyword = "Pais da copa"

class GetTweets(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        print("="*50)
        connection.send(tweet.text.encode('utf-8', 'ignore'))


printer = GetTweets(token)
printer.add_rules(tweepy.StreamRule(keyword))
printer.filter()
connection.close()

# Pega dados para o spark fazer tratamento
spark = SparkSession.builder.appName('SparkStreaming').getOrCreate()

#! consumir api criada com o socket que ta no s3 e vai para ec2
lines = spark.readStream\
    .format('socket')\
    .option('host', 'localhost')\
    .option('port', 9009)\
    .load()

# tratamento dos dados
words = lines.select(f.explode(f.split(lines.value, ' ')).alias('word'))

wordCounts = words.groupBy('word').count()

# Escreve os dados em um s3 ou dynamoDB
query = wordCounts.writeStream\
    .outputMode('append') \
    .option('encoding', 'utf-8')\
    .format("s3selectJson") \
    .schema(...) \
    .load("s3://path/to/my/datafiles")\
    .start()


query.awaitTermination()
