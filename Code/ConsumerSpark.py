# importando as bibliotecas
from pyspark.sql import SparkSession
from pyspark.sql import Row
from kafka import KafkaConsumer

if __name__ == "__main__":

# configuração do spark
    spark = SparkSession \
        .builder \
        .appName("Kafka tweet") \
        .master("spark://spark-master:7077") \
        .config("spark.mongodb.input.uri", "mongodb://localhost:27017/twitter") \
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0") \
        .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.12:3.0.1') \
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

# Gravando os dados no Mongodb
    df = spark.createDataFrame([
        Row(id=1, name='vijay', marks=67),
        Row(id=2, name='Ajay', marks=88),
        Row(id=3, name='jay', marks=79),
        Row(id=4, name='binny', marks=99),
        Row(id=5, name='omair', marks=99),
        Row(id=6, name='divya', marks=98),
    ])


    df.select("id", "name", "marks").write\
        .format('com.mongodb.spark.sql.DefaultSource')\
        .option("url", "mongodb://localhost:27017//twitter") \
        .save()
