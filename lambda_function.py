import boto3
from botocore.exceptions import NoCredentialsError

def lambda_handler(event, context):
    sns = boto3.client('sns', region_name='us-west-2')

    # Create a new SNS topic
    response = sns.create_topic(Name='MySNSTopic')
    topic_arn = response['TopicArn']

    # Create a new phone number and subscribe it to the SNS topic
    phone_number = '+1234567890'  # Replace with your phone number
    sns.subscribe(TopicArn=topic_arn, Protocol='sms', Endpoint=phone_number)

    return {
        'statusCode': 200,
        'body': 'Texting number created successfully',
        'phoneNumber': phone_number
    }