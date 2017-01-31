from __future__ import print_function

import json
import boto3

print('Loading function')


def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('S3ObjectInfo')
    
    #Define Variables
    bucketName = event['Records'][0]['s3']['bucket']['name']
    objectKey = event['Records'][0]['s3']['object']['key']
    objectCreator = event['Records'][0]['userIdentity']['principalId']
    
    #print("Bucket: " + bucketName)
    #print("ObjectName: " + objectKey)
    #print("Creator ID: " + objectCreator)
    table.put_item(Item={'ObjectName': objectKey,
    'CreatorrName' : objectCreator,
    'BucketName' : bucketName})
    print("Received event: " + json.dumps(event, indent=2))
    #print("value1 = " + event['key1'])
    #print("value2 = " + event['key2'])
    #print("value3 = " + event['key3'])
    #return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')