# **Pipeline de dados do twitter**

- Pipeline de dados feito com spark kafka e airflow com os dados extraidos do twitter
- Dados salvos no postgres
- Dados dos principais assuntos do momento

## Configuração do Docker

- Faça o download do docker no seu ambiente e configure os container a baixo vai esta o link de cada container usado no projeto

  - [spark](https://hub.docker.com/r/bitnami/spark)
  - [kafka](https://docs.confluent.io/platform/current/platform-quickstart.html#prerequisites)
  - [Airflow](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)

### Configuração do Kafka

1. Suba a imagem do container
2. Crie o topico com o comando

```
  kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic tweet
```

1. Rode o producer

### Configuração do Spark

1. Suba a imagem do container

```
docker exec -it <id_container> \
spark-submit \
--packages "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0" \
--master "spark://spark-master:7077" \
--py-files ConsumerSpark.py
```

### Configuração do Airflow (Automatizar)

## Referências:
