# importando as bibliotecas
from pyspark.sql import SparkSession
from pyspark.sql import Row

from kafka import KafkaConsumer
from wordcloud import WordCloud

import matplotlib.pyplot as plt
import json
from IPython.display import clear_output

if __name__ == "__main__":

    # configuração do spark
    spark = SparkSession \
        .builder \
        .appName("Kafka consultas em lote") \
        .master("spark://spark-master:7077") \
        .config("spark.mongodb.input.uri", "mongodb://hduser:bigdata@127.0.0.1:27017/dezyre") \
        .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.12:3.0.1') \
        .getOrCreate()

# configuração do kafka
    KAFKA_BOOTSTRAP_SERVERS_CONS = ['localhost:9092']
    KAFKA_TOPIC_NAME_CONS = 'topic-name'
    CONSUMER = KafkaConsumer(KAFKA_TOPIC_NAME_CONS, group_id='group1',
                             bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS_CONS)


# geração da nuvem de palavras em tempo real

    frases = ''
    for messagem in CONSUMER:
        texto = json.loads(messagem.value.decode('utf-8'))
        frases = frases + texto['tweet']
        clear_output()
        wordcloud = WordCloud(max_font_size=100, width=1520,
                              height=535).generate(frases)
        plt.figure(figsize=(16, 9))
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.show()
# Construir um DataFrame que leia topic-name
    batch_df = spark \
        .read \
        .format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS_CONS) \
        .option("subscribe", KAFKA_TOPIC_NAME_CONS) \
        .load()

    batch_df.printSchema()

# Escrevendo os dados do kafka no spark

    batch_df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
        .write \
        .format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS_CONS) \
        .option("topic", KAFKA_TOPIC_NAME_CONS) \
        .save()

# ver dados
    batch_df.printSchema()
    batch_df.show(5)

# Gravando os dados no Mongodb
    batch_df = spark.createDataFrame([
        Row(id=1, name='vijay', marks=67),
        Row(id=2, name='Ajay', marks=88),
        Row(id=3, name='jay', marks=79),
        Row(id=4, name='binny', marks=99),
        Row(id=5, name='omair', marks=99),
        Row(id=6, name='divya', marks=98),
    ])


    batch_df.select("id", "name", "marks").write\
        .format('com.mongodb.spark.sql.DefaultSource')\
        .option("url", "mongodb://http:bigdata@127.0.0.1:27017/twitter") \
        .save()
