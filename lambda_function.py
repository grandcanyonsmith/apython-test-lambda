import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3', region_name='us-west-2')
    s3.create_bucket(Bucket='canyon-test-lambda-bucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
    return {
        'statusCode': 200,
        'body': 'Bucket created successfully'
    }