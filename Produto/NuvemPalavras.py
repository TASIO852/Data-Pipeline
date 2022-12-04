# importando as bibliotecas
from kafka import KafkaConsumer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import json
from IPython.display import clear_output

# Pegando dados da AWS s3

    
# geração da nuvem de palavras em tempo real
frases = ''
for messagem in consumer:
    texto = json.loads(messagem.value.decode('utf-8'))
    frases = frases + texto['tweet']
    clear_output()
    wordcloud = WordCloud(max_font_size=100, width=1520,
                          height=535).generate(frases)
    plt.figure(figsize=(16, 9))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
