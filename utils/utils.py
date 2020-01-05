import os
import boto3


def init():
    sqs = boto3.resource('sqs',
                       aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                       aws_secret_access_key=os.getenv(
                           "AWS_SECRET_ACCESS_KEY"),
                       region_name=os.getenv("AWS_REGION"),)
    return sqs


def create_queue():
    sqs = init()
    response = sqs.create_queue(
        QueueName=os.getenv("QUEUE_NAME"),
        Attributes={
            'MessageRetentionPeriod': '60'
        }
    )
    return response
