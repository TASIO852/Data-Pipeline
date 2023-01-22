import boto3

# Create Bucket
Config_bucket = {
    'region': 'us-east-1',
    'bucket_name': 'tweets-bucket'
}
s3_client = boto3.client('s3', region_name=Config_bucket['region'])
location = {'LocationConstraint': Config_bucket['region']}
s3_client.create_bucket(
    Bucket=Config_bucket['bucket_name'], CreateBucketConfiguration=location)
