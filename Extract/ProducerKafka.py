# bibliotecas
from datetime import datetime
import tweepy
from json import dumps
from kafka import KafkaProducer

# chaves de autenticação do twitter
consumer_key = 'xufyvCkI3K8cHa0gFNjPjbigl'
consumer_secret = 'uMBeDn6OGNRDeWhS4CyqO1e6VKiN3wEE0sGHOzjG9Kf86U8MCh'
access_token = 'AAAAAAAAAAAAAAAAAAAAAOCXiwEAAAAAaJGe8%2BmaJTsywF2ozyjHmAwKnwA%3DtktjdTuZaUKatSpjfPnUsujTvxQVMSVkOyNyOkmHBydxFKkMis'
access_token_secret = ''

# configuração do kafka
broker = 'localhost:9092'
topico = 'tweet'
producer = KafkaProducer(bootstrap_servers=[broker],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))


# configuração da API twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
tweets = api.search('access_token_secret')

# colhendo os dados conforme texto desejado
for tweet in tweets:
    frase = str(tb(tweet.text))
    data_e_hora_completa = datetime.now()
    data_string = data_e_hora_completa.strftime('%Y-%m-%d %H:%M:%S')
    dados = {"tweet": frase, "horario": data_string}
    producer.send(topico, value=dados)


# # bibliotecas
# from datetime import datetime
# import tweepy
# from json import dumps
# from kafka import KafkaProducer

# # chaves de autenticação do twitter
# consumer_key = ''
# consumer_secret = ''
# access_token = ''
# access_token_secret = ''

# # configuração do kafka
# broker = 'localhost:9092'
# topico = 'tweets'
# producer = KafkaProducer(bootstrap_servers=[broker],
#                          value_serializer=lambda x:
#                          dumps(x).encode('utf-8'))
                         
                         
# # configuração da API twitter
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)
# tweets = api.search('machine learning')

# # colhendo os dados conforme texto desejado
# for tweet in tweets:
#   frase = str(tb(tweet.text))
#   data_e_hora_completa = datetime.now()
#   data_string = data_e_hora_completa.strftime('%Y-%m-%d %H:%M:%S')
#   dados = {"tweet": frase, "horario": data_string}
#   producer.send(topico, value=dados)