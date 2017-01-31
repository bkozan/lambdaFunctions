from __future__ import print_function

import json
import urllib
import boto3

print('Loading function')

s3 = boto3.client('s3')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    #key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    key = event['Records'][0]['s3']['object']['key']
    location = event['Records'][0]['awsRegion']
    #print("Bucket = " + bucket)
    #print("key = " + key)
    
    s3.put_object_acl(ACL='public-read',Bucket=bucket,Key=key)
    
    print('Object {} in bucket {} in region {}, is now available to the world.'.format(key, bucket, location))
    print('That makes the full url = https://s3-{}.amazonaws.com/{}/{}'.format(location,bucket,key))
    
    #try:
     #   response = s3.get_object(Bucket=bucket, Key=key)
     #   print("CONTENT TYPE: " + response['ContentType'])
     #   return response['ContentType']
    #except Exception as e:
    #    print(e)
     #   print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
      #  raise e