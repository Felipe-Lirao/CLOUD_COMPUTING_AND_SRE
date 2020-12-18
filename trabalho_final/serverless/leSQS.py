from sqsHandler import SqsHandler
from env import Variables

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