from sqsHandler import SqsHandler
from env import Variables
import boto3

def push(event, context):
    # Create an SNS client
    sns = boto3.client('sns')
    env = Variables()
    sqs = SqsHandler(env.get_sqs_dlq_url())
    
    while(True):
        response = sqs.getMessage(5)
        print(response)
        
        if('Messages' not in response):
            break
        
        if(len(response['Messages'])==0):
            break
    
        for msg in response['Messages']:
            
            # Publish a simple message to the specified SNS topic
            retorno = sns.publish(
                TopicArn = env.get_sns_arn(),
                Message = msg['Body'],
            )
            
            sqs.deleteMessage(msg["ReceiptHandle"])
            
            # Print out the response
            print(retorno)
            
'''
    for record in event['Records']:
        #print ("test")
        payload = record["body"]
        print(str(payload))
    
        retorno = sns.publish(
            TopicArn = env.get_sns_arn(),
            Message = record["body"],
        )
        
        sqs.deleteMessage(record["receipthandle"])
    
'''    
    
    