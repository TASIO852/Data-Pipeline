# bibliotecas
from datetime import datetime
import tweepy
from json import dumps
from kafka import KafkaProducer

# chaves de autenticação do twitter
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# configuração do kafka
broker = 'localhost:9092'
topico = 'artigo-medium'
producer = KafkaProducer(bootstrap_servers=[broker],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
                         
                         
# configuração da API twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
tweets = api.search('machine learning')

# colhendo os dados conforme texto desejado
for tweet in tweets:
  frase = str(tb(tweet.text))
  data_e_hora_completa = datetime.now()
  data_string = data_e_hora_completa.strftime('%Y-%m-%d %H:%M:%S')
  dados = {"tweet": frase, "horario": data_string}
  producer.send(topico, value=dados)