import yfinance as yf
import boto3

def lambda_handler(event, context):
    # Download stock information
    stock = yf.Ticker("LAME4.SA")
    stock_info = stock.info
    
    # Convert the stock information to a string
    stock_info_str = str(stock_info)
    
    # Create an S3 client
    s3 = boto3.client("s3")
    
    # Upload the stock information to S3
    s3.put_object(Bucket="my-bucket", Key="stock-info.txt", Body=stock_info_str)
    
    return "Stock information successfully uploaded to S3"