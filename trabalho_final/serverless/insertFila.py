import json

def insert(event, context):
    mensagem = event['pathParameters']['mensagem'];
    
    body = {
        "message": "O usuario enviado foi: " + str(mensagem)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
