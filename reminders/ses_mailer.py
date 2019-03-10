import boto3
import os
import settings

CHARSET = "UTF-8"
AWS_REGION = os.environ['AWS_SES_REGION_NAME']
SENDER = os.environ['SENDER_MAIL']
RECIPIENT = os.environ['RECIPIENT_MAIL']


def send_email(subject, body):
    client = boto3.client('ses', region_name=AWS_REGION)

    response = client.send_email(
        Destination={
            'ToAddresses': [RECIPIENT],
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': CHARSET,
                    'Data': body,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': subject,
            },
        },
        Source=SENDER,
    )
