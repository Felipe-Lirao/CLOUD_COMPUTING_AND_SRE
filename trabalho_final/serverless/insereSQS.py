from sqsHandler import SqsHandler
from env import Variables
import json

def insert(event, context):
    env = Variables()
    sqs = SqsHandler(env.get_sqs_url())
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