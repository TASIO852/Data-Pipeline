import socket

import tweepy

HOST = 'localhost'
PORT = 9090
s = socket.socket()
s.bind((HOST, PORT))
print(f"Aguardando conexão na porta: {PORT}")

s.listen(1)
connection, address = s.accept()
print(f"Recebendo solicitação de {address}")

keyword = 'Futebol'
token = 'AAAAAAAAAAAAAAAAAAAAAOCXiwEAAAAAaJGe8%2BmaJTsywF2ozyjHmAwKnwA%3DtktjdTuZaUKatSpjfPnUsujTvxQVMSVkOyNyOkmHBydxFKkMis'


class GetTweets(tweepy.StreamingClient):
    def on_message(self, tweet):
        print(tweet.text)
        connection.send(tweet.text.encode('utf-8', 'ignore'))


printer = GetTweets(token)
printer.add_rules(tweepy.StreamRule(keyword))
printer.filter()
connection.close()
