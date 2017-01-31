from __future__ import print_function

import json
import boto3

print('Loading function')


def lambda_handler(event, context):
    
    LambdaClient = boto3.client('lambda')
    
    
    kozanbucket= event['Records'][0]['s3']['bucket']['name']
    fileObject= event['Records'][0]['s3']['object']['key']
    
   
    payload={
        'Bucket' : kozanbucket,
        'Key' : fileObject
        }
    
    print(payload)
    LambdaClient.invoke(FunctionName='Lambda_MakeS3ObjectPublic',Payload=json.dumps(payload) )