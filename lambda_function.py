import boto3

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
    s3.upload_file('/tmp/' + file_name, bucket_name, file_name)
    
    # Generate the URL to get 'file_name' from 'bucket_name'
    url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
    
    return {
        'statusCode': 200,
        'body': 'File uploaded successfully',
        'url': url
    }