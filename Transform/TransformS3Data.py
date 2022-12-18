# lambda spark emr function 
import boto3
from  pyspark.sql  import SparkSession

spark = SparkSession.builder \
    .appName('transform-s3-data-parquet')\
    .config('')


client = boto3.client('emr')

