
import psycopg2
import sys
import boto3
import os

ENDPOINT = "database-1.c4vwt1qqf3gi.us-east-1.rds.amazonaws.com"
PORT = "5432"
USER = "postgres"
REGION = "us-east-1"
DBNAME = " "

# gets the credentials from .aws/credentials
session = boto3.Session(profile_name='RDSCreds')
client = session.client('rds')

token = client.generate_db_auth_token(
    DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

try:
    conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME,
                            user=USER, password=token, sslrootcert="C:/Users/tasio.guimaraes/Documents/Data-Pipeline/aws/EC2/key/ec2.pem")
    cur = conn.cursor()
    cur.execute("""     
CREATE TABLE cobranca_paciente(
    id serial PRIMARY KEY,
    definicao VARCHAR(100) NOT NULL,
    identificacao INT NOT NULL,
    nome  VARCHAR(100) NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    codigo_postal INT NOT NULL,
    regiao VARCHAR(50) NOT NULL,
    total_cobrancas INT NOT NULL,
    media_custos_cobertos NUMERIC NOT NULL,
    media_pagamento_total NUMERIC NOT NULL,
    media_gastos_cuidados NUMERIC NOT NULL
)
CREATE TABLE dados_analises(
    id INT PRIMARY KEY,
    diagnostico VARCHAR(5) NOT NULL,
    media_raio NUMERIC NOT NULL,
    media_textura NUMERIC NOT NULL,
    media_perimetro NUMERIC NOT NULL,
    media_area NUMERIC NOT NULL,
    media_suavidade NUMERIC NOT NULL,
    media_compactacao NUMERIC NOT NULL,
    media_concavidade NUMERIC NOT NULL,
    media_concavidade_pontos NUMERIC NOT NULL,
    media_simetria NUMERIC NOT NULL,
    media_dimensao_fractal NUMERIC NOT NULL,
    se_raio NUMERIC NOT NULL,
    se_textura NUMERIC NOT NULL,
    se_perimetro NUMERIC NOT NULL,
    se_area NUMERIC NOT NULL,
    se_suavidade NUMERIC NOT NULL,
    se_compactacao NUMERIC NOT NULL,
    se_concavidade NUMERIC NOT NULL,
    se_concavidade_pontos NUMERIC NOT NULL,
    se_simetria NUMERIC NOT NULL,
    se_dimensao_fractal NUMERIC NOT NULL,
    pior_raio NUMERIC NOT NULL,
    pior_textura NUMERIC NOT NULL,
    pior_perimetro NUMERIC NOT NULL,
    pior_area NUMERIC NOT NULL,
    pior_suavidade NUMERIC NOT NULL,
    pior_compactacao NUMERIC NOT NULL,
    pior_concavidade NUMERIC NOT NULL,
    pior_concavidade_pontos NUMERIC NOT NULL,
    pior_simetria NUMERIC NOT NULL,
    pior_dimensao_fractal NUMERIC NOT NULL
)
""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))
