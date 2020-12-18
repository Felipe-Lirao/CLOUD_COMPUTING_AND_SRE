import os

class Variables:
    def __init__(self):
        self.__sqs_url = os.environ.get('sqs_url', '')
        self.__sqs_arn = os.environ.get('sqs_arn', '')
        self.__sqs_dlq_url = os.environ.get('sqs_dlq_url', '')
        self.__sqs_dlq_arn = os.environ.get('sqs_dlq_arn', '')
        self.__sns_arn = os.environ.get('sns_arn', '')

    def get_sqs_url(self):
        return self.__sqs_url
    def get_sqs_arn(self):
        return self.__sqs_arn
    def get_sqs_dlq_url(self):
        return self.__sqs_dlq_url
    def get_sqs_dlq_arn(self):
        return self.__sqs_dlq_arn
    def get_sns_arn(self):
        return self.__sns_arn
    