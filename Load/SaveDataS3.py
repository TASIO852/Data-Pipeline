import logging
from botocore.exceptions import ClientError
import boto3

s3 = boto3.resource('s3')
client = boto3.client('s3')

s3_client = boto3.client(
    's3',
    aws_access_key_id='seu_id_de_acesso',
    aws_secret_access_key='sua_chave_de_acesso'
)


def create_bucket(bucket_name):
    try:
        s3_client.create_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False

    return True


create_bucket('cjmm-primeirobucket')


def upload_object(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False

    return True

    upload_object('sample_data/mnist_test.csv', 'cjmm-primeirobucket')

    response = s3_client.list_buckets()

    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

# Resultado:
# Existing buckets:
#   cjmm-primeirobucket


def list_objects_bucket(bucket_name):

    response = s3_client.list_objects(Bucket=bucket_name)

    for object in response['Contents']:
        print(object['Key'])


list_objects_bucket('cjmm-primeirobucket')

# Resultado:
#   sample_data/mnist_test.csv


def download_object(bucket_name, object_name, file_name):

    s3_client.download_file(bucket_name, object_name, file_name)

    s3_client.download_file('cjmm-primeirobucket',
                            'sample_data/mnist_test.csv', 'mnist_test.csv')
