from __future__ import print_function

import json
import boto3

print('Loading function')


def lambda_handler(event, context):
    
    client = boto3.client('s3')
    
    response = client.put_object_acl(ACL='public-read',Bucket=event['Bucket'],Key=event['Key'])
    
    print(event)