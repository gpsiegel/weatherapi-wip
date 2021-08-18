import boto3
import os

AWS_KEY = os.environ.get('AWS_KEY')
AWS_SECRET = os.environ.get('AWS_SECRET')

def ddb_return():
    client = boto3.client('dynamodb', \
        aws_access_key_id=f'{AWS_KEY}', \
        aws_secret_access_key=f'{AWS_SECRET}', \
        region_name="us-east-1")
        
    
    response = client.scan(
        TableName="Weather"
    )
    
    r1 = response['Items'][-1]['Temperature']['S']
    r2 = response['Items'][-1]['Date']['S']
    
    return f"The Current Weather in Dallas is {r1} on {r2}"