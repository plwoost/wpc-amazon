
import boto3

session = boto3.session.Session()
client = session.client('ses', region_name='eu-west-1')

def send_email(to, subject, body):
    response = client.send_email(
        Source='s167792@wizard.uek.krakow.pl',
        Destination={
            'ToAddresses': [
                to,
            ]
        },
        Message={
            'Subject': {
                'Data': subject,
                'Charset': 'utf-8'
            },
            'Body': {
                'Text': {
                    'Data': body,
                    'Charset': 'utf-8'
                },
                'Html': {
                    'Data': body,
                    'Charset': 'utf-8'
                }
            }
        },
        ReplyToAddresses=[
            's167792@wizard.uek.krakow.pl',
        ],
        ReturnPath='s167792@wizard.uek.krakow.pl'
    )
    return response


print send_email('s167792@wizard.uek.krakow.pl', 'test', 'test')
