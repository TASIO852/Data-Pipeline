import json
import requests
import socket

HOST = 'localhost'
PORT = 9009
s = socket.socket()
s.bind((HOST, PORT))
print(f"Aguardando conexão na porta: {PORT}")

s.listen(5)
connection, address = s.accept()
print(f"Recebendo solicitação de {address}")

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAOCXiwEAAAAAaJGe8%2BmaJTsywF2ozyjHmAwKnwA%3DtktjdTuZaUKatSpjfPnUsujTvxQVMSVkOyNyOkmHBydxFKkMis"

keyword = "futebol"
url_rules = "https://api.twitter.com/2/tweets/search/stream/rules"
header = headers={'Authorization': f"Bearer {BEARER_TOKEN}"}
response = requests.post(url_rules,headers=header, json ={"add": [{"value": keyword}]})

url = "https://api.twitter.com/2/tweets/search/stream"
response = requests.get(url, headers=header, stream=True)

if response.status_code == 200:
    for item in response.iter_lines():
        try:
            print(json.loads(item)["data"]["text"])
            print("="*50)
            connection.send(json.loads(item)["data"]["text"].encode("latin1", "ignore"))
        except:
            continue

connection.close()