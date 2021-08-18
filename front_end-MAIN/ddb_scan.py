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
        TableName="Weather",
        Limit=1
    )
    
    r1 = response['Items'][0]['ID']['S']
    r2 = response['Items'][0]['Temperature']['S']
    r3 = response['Items'][0]['Date']['S']

    return f"The Current Weather in Dallas is {r2} on {r3}" \
        f"The ID of this result is {r1}"