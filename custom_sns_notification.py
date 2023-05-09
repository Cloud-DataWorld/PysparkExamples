

import boto3
import json

def lambda_handler(event, context):
    
    s3_resource =  boto3.resource('s3')
    
    my_bucket =  s3_resource.Bucket('TestBucket')
    
    key = 'employee.csv'
    
    objs = list(my_bucket.objects.filter(Prefix = key))
    
    sns_client =  boto3.client('sns')
    
    if objs:
        
        print('the file is present inside the bucket and send the sns notifications')
        
        sns_client.publish(TopicArn = 'xxxxxxxxxxxxxxxx',message = 'Hello, the file is present in the bucket ' ,  subject = 'File Check ')
    else:
        print('no file is present inside the bucket')
        
        
    