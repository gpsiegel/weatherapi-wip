import os
import requests
import boto3
import datetime

AWS_KEY = os.environ.get('AWS_KEY')
AWS_SECRET = os.environ.get('AWS_SECRET')

ddb = boto3.resource('dynamodb', \
    aws_access_key_id=f'{AWS_KEY}', \
    aws_secret_access_key=f'{AWS_SECRET}', \
    region_name="us-east-1")

def weather_results():
    API_KEY = os.environ.get('API_KEY')
    url = "https://api.tomorrow.io/v4/timelines"

    querystring = {
    "location":"32.7767, 96.7970",
    "fields":["temperature", "cloudCover"],
    "units":"imperial",
    "timesteps":"1d",
    "apikey": f'{API_KEY}'}

    response = requests.request("GET", url, params=querystring)
    temps = response.json()['data']['timelines'][0]['intervals'][0]['values']['temperature']
    return temps

def ddb_load(temp):
    
    date_now = datetime.datetime.now()
    current = date_now.strftime('%Y-%m-%d-%H:%M:%S')

    table = ddb.Table('Weather')
    loads = table.put_item(
        Item={
            'Date': f'{current}',
            'Temperature': f'{temp}'
        }
    )
    
    return loads

if __name__ == '__main__':
    try:
        tmp = weather_results()
        ddb_load(tmp)
    except Exception as e:
        print(e)