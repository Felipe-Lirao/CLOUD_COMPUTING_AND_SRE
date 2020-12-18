import sys
sys.path.insert(0, '/opt')

from sqsHandler import SqsHandler
from env import Variables
import json

import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all


def insert(event, context):
    xray_recorder.configure(service='insereSQS')
    #plugins = ('ElasticBeanstalkPlugin', 'EC2Plugin')
    #xray_recorder.configure(plugins=plugins)
    patch_all()
    
    env = Variables()
    sqs = SqsHandler(env.get_sqs_url())
    
    print(str(env.get_sqs_url()))
    
    mensagem = event['pathParameters']['mensagem'];

    sqs.send(mensagem)
    
    body = {
        "message": "A mensagem enviada foi: " + str(mensagem)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response