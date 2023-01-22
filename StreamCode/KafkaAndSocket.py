# Unificar dados das duas fontes
# usar step functions para fazer a ordem de processamento   
from kafka import KafkaConsumer
import socket
import json
import boto3
import pandas as pd

# Dados do kafka
topic_name = 'twitter'

consumer = KafkaConsumer(
    topic_name,
     bootstrap_servers=['localhost:9092'], # host do ec2 ou s3 tenho que ver certinho
     auto_offset_reset='latest',
     enable_auto_commit=True,
     auto_commit_interval_ms=5000,
     fetch_max_bytes=128,
     max_poll_records=100,
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    tweets = json.loads(json.dumps(message.value))
    print(tweets)
    
# pegar dados do dynamoDB ou s3
client = boto3.client(
    service_name='s3',
    aws_access_key_id='seu_access_key_id',
    aws_secret_access_key='seu_secret_access_key',
    region_name='eu-west-1'
)

client.download_file("meu-exemplo-buteco-opensource", "Socket-Bucket", "downloaded-hello-s3.json")
socket_data = open("socketData.json")


# unificar dados das fontes

