import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3', region_name='us-west-2')
    s3.create_bucket(Bucket='canyon-test-lambda-bucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
    
    # Create a file and write 'hello world' to it
    with open('test.txt', 'w') as file:
        file.write('hello world')
    
    # Upload the file to the bucket
    s3.upload_file('test.txt', 'canyon-test-lambda-bucket', 'test.txt')
    
    return {
        'statusCode': 200,
        'body': 'Bucket created and file uploaded successfully'
    }