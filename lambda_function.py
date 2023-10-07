import boto3
from botocore.exceptions import NoCredentialsError

def lambda_handler(event, context):
    s3 = boto3.client('s3', region_name='us-west-2')
    bucket_name = 'canyon-test-lambda-bucket'
    file_name = 'test.txt'
    
    # Check if bucket already exists
    response = s3.list_buckets()
    bucket_exists = any(bucket['Name'] == bucket_name for bucket in response['Buckets'])
    
    # Create bucket if it doesn't exist
    if not bucket_exists:
        try:
            s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
        except s3.exceptions.BucketAlreadyOwnedByYou:
            pass
    
    # Create a file in /tmp directory and write 'hello world' to it
    with open('/tmp/' + file_name, 'w') as file:
        file.write('hello world')
    
    # Upload the file to the bucket
    try:
        s3.upload_file('/tmp/' + file_name, bucket_name, file_name)
    except NoCredentialsError:
        return {
            'statusCode': 400,
            'body': 'No AWS credentials found'
        }
    
    # Generate a presigned URL for the object
    url = s3.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': file_name}, ExpiresIn=3600)
    
    return {
        'statusCode': 200,
        'body': 'File uploaded successfully',
        'url': url
    }