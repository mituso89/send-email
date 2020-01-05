import os
import boto3
import json
import sys


def send_email_redis():

    sqs = boto3.client('sqs',
                       aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                       aws_secret_access_key=os.getenv(
                           "AWS_SECRET_ACCESS_KEY"),
                       region_name=os.getenv("AWS_REGION"),)

    response = sqs.create_queue(
        QueueName=os.getenv("QUEUE_NAME"),
        Attributes={
            'MessageRetentionPeriod': '60'
        }
    )

    print(response['QueueUrl'])

    response = sqs.send_message(
        QueueUrl=response['QueueUrl'],
        DelaySeconds=10,
        MessageBody=json.dumps({
            "email_type": "ticket",
            "supplier": "apollo",
            "message": "err",
            "boking_reference": "PL_000052",
            "status": "failed"
        })

    )

