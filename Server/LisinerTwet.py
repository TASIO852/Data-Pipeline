import socket
import tweepy

HOST = 'localhost'
PORT = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print(f"Aguardando conexão na porta: {PORT}")

s.listen(1)
connection, address = s.accept()
print(f"Recebendo solicitação de {address}")

keyword = 'Dados'
token = 'AAAAAAAAAAAAAAAAAAAAAOCXiwEAAAAAaJGe8%2BmaJTsywF2ozyjHmAwKnwA%3DtktjdTuZaUKatSpjfPnUsujTvxQVMSVkOyNyOkmHBydxFKkMis'


class GetTweets(tweepy.StreamingClient):
    def on_message(self, tweet):
        print(tweet.text)
        connection.send(tweet.text.encode('latin1', 'ignore'))


printer = GetTweets(token)
printer.add_rules(tweepy.StreamRule(keyword))
printer.filter()
connection.close()
