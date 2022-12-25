# **Pipeline de dados do twitter**

- Pipeline de dados feito com spark kafka e aws com os dados extraídos do twitter
- Dados salvos na AWS
- Dados dos principais assuntos do momento

1. No projeto vai ser montada uma pipeline de dados do twitter extraídas por duas apis diferentes e combinadas

- primeira api ultilizara apache kafka
- Segunda api sera um rest api

1. O tratamento de dados sera com o apache spark
2. Em seguida os dados vao ser armazenados na AWS
3. Logo apos serão requeridos novamente para a montagem de uma nuvem de palavras

![Alt text](/Mapping/Diagrama.png)

## Configuração do Kafka

- [kafka Donwload container](https://docs.confluent.io/platform/current/platform-quickstart.html#prerequisites)

1. Suba a imagem do container
2. Crie o topico com o comando

```
  kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic tweet
```

1. Rode o producer

## Configuração do Spark

[fonte](https://spark.apache.org/docs/3.1.2/api/python/getting_started/install.html)

Primeiro de tudo temos que ter as seguintes dependencias na nossa maqui

- java 8
- python 3

### Passo 1 - Instalando o Apache Spark

Selecione a versão mais estável clicando [aqui](http://spark.apache.org/downloads.html). Na criação deste projeto utilizamos a versão do Spark **3.3.1** e como tipo de pacote selecionamos **Pre-built for Apache Hadoop 3.3**.

Para instalar o Apache Spark não é necessário executar um instalador, basta descomprimir os arquivos em uma pasta de sua escolha.

<font color=red>Obs.: certifique-se de que o caminho onde os arquivos do Spark foram armazenados não contenham espaços (ex.: **"C:/spark/spark-3.1.2-bin-hadoop2.7"**).</font>

Para testar o funcionamento do Spark execute os comandos abaixo em seu _prompt_ de comando. Esses comandos assumem que você extraiu os arquivos do Spark na pasta **"C:/spark/"**.

```
cd C:/spark/spark-3.1.2-bin-hadoop2.7
```

```
bin/pyspark
```

O comando acima inicia o _shell_ do PySpark que permite trabalhar interativamente com o Spark.

Para sair basta digitar `exit()` e logo depois presionar _Enter_. Para voltar ao _prompt_ pressione _Enter_ novamente.

### Passo 2 - Instalando o findspark

```
pip install findspark
```

### Passo 3 - Instalando o winutils

Os arquivos do Spark não incluem o utilitário **winutils.exe** que é utilizado pelo Spark no Windows. Se não informar onde o Spark deve procurar este utilitário, veremos alguns erros no console e também não conseguiremos executar _scripts_ Python utilizando o utilitário `spark-submit`.

Faça o [download](https://github.com/steveloughran/winutils) para a versão do Hadoop para a qual sua instalação do Spark foi construída. Em nosso exemplo foi utilizada a [versão 2.7](https://github.com/steveloughran/winutils/tree/master/hadoop-2.7.1/bin). Faça o _download_ apenas do arquivo **winutils.exe**.

Crie a pasta **"hadoop/bin"** dentro da pasta que contém os arquivos do Spark (em nosso exemplo **"C:/spark/spark-3.3.1-bin-hadoop3"**) e copie o arquivo **winutils.exe** para dentro desta pasta.

Crie duas variáveis de ambiente no seu Windows. A primeira chamada **SPARK_HOME** que aponta para a pasta onde os arquivos Spark foram armazenados (em nosso exemplo **"C:/spark/spark-3.3.1-bin-hadoop3"**). A segunda chamada **HADOOP_HOME** que aponta para **%SPARK_HOME%/hadoop** (assim podemos modificar **SPARK_HOME** sem precisar alterar **HADOOP_HOME**).

## AWS Save data

puxar dados do twitter com apache kafka e pela api juntar os dois e
Armazenar em um s3,emr e glue da aws dados do twetter e tratar com apache spark

Usaremos 4 ferramentas do aws para essa etapa

- S3
- Glues
- EMR
- RDS
- api getway
- lambda

## Nuvem de palavras
