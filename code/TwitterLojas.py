import tweepy
import boto3

def lambda_handler(event, context):
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
    query = 'Lojas Americanas -is:retweet'
    tweets = client.search_recent_tweets(query=query, max_results=100)

    # tweets legiveis
    tweet_texts = [tweet for tweet in tweets]

    # Acesso ao S3
    s3 = boto3.client("s3")

    # Nome do bucket S3
    bucket_name = "my-tweet-data"

    # Nome do arquivo S3
    file_name = "tweets.txt"

    # Escrita dos dados do Twitter no S3
    s3.put_object(Bucket=bucket_name, Key=file_name,
                  Body="\n".join(tweet_texts))

    return "Twitter data written to S3"
