import sys
sys.path.insert(0, '/opt')

from sqsHandler import SqsHandler
from env import Variables

import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

xray_recorder.configure(service='leSQS')
#plugins = ('ElasticBeanstalkPlugin', 'EC2Plugin')
#xray_recorder.configure(plugins=plugins)
patch_all()

def le(event, context):
    env = Variables()

    sqs = SqsHandler(env.get_sqs_url())

    while(True):
        msgs = sqs.getMessage(5)
        print("********* Response")
        print(str(msgs))
        print("*********")
        
        if('Messages' not in msgs):
            break
        
        if(len(msgs['Messages'])==0):
            break
    
        mensagens = []
        for msg in msgs['Messages']:
            mensagens.append({'Id':msg['MessageId'], 'ReceiptHandle':msg['ReceiptHandle']})  
            print("*********")
            print(str(msg["Body"]))
            print("*********")
            
            if(str(msg["Body"]) == "erro"):
                raise Exception('DLQ, Please!')
            
            sqs.deleteMessage(msg['ReceiptHandle'])
       
       
'''
    for record in event['Records']:
       #print ("test")
       payload = record["body"]
       print(str(payload))
'''