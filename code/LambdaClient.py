import tweepy
import boto3
from pyspark.sql import SparkSession
from pyspark.sql import functions as f
import json

# AWS Credentials
s3 = boto3.client('s3')

# Spark session
spark = SparkSession.builder.appName('TwitterStreaming').getOrCreate()

def lambda_handler(event, context):
    # Insert your API credentials here
    credentials = { 
        'consumer_key': "key",
        'consumer_secret': "key",
        'access_token': "key-key",
        'access_token_secret': "key",
        'bearer_token': 'key%key'
    }

    # Authentication
    client = tweepy.Client(bearer_token=credentials['bearer_token'])

    # Search for tweets
    query = 'covid -is:retweet'
    tweets = client.search_recent_tweets(query=query, max_results=100)
    
    # Write tweets to S3 in JSON format
    s3 = boto3.client('s3')
    bucket_name = 'tweets-bucket'
    object_name = 'tweets.json'
    s3.put_object(Bucket=bucket_name, Key=object_name, Body=json.dumps(tweets))
