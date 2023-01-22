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
        'consumer_key': "E6peB7LzSvEIujBuBdSxfFrAr",
        'consumer_secret': "l19HxflcvQD4D5EH9OBg2E6A8DmnzBZoSHStMtsVkqKYaXUgXB",
        'access_token': "1186393232722333697-aWp1rr3fFd4jD6W6B60cLC4LGaT1e3",
        'access_token_secret': "UlxD2JL5C7forlkQsVK8Bd4tdbEqCM6lKi9TcgJl45xWb",
        'bearer_token': 'AAAAAAAAAAAAAAAAAAAAAA2AlQEAAAAAXmvw6IhjxRzDeNhPuU2FugjR6Rg%3DGlpPm63CVe0IxKy9l5Id7JlT7lc2ODXdR6tu3FYaUMMNpVTsfm'
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
