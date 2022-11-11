import boto3
import pprint
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region):
    try:
        s3_client = boto3.client('s3', region_name=region)
        location = {'LocationConstraint': region}
        pprint.pprint(s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)) #Usamos o pprint para uma saída mais amigável do resultado.
    except ClientError as e:
        print(e)

create_bucket("hello-bucket-python", "sa-east-1")