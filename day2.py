import boto3

try:
    s3 = boto3.client('s3', region_name='ap-south-1')
    
    # Create bucket
    bucket_name = "my-devops-learning-2027"
    
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'
        }
    )
    print(f"Bucket '{bucket_name}' created successfully!")

    # List buckets to confirm
    response = s3.list_buckets()
    print("\nYour S3 Buckets:")
    for bucket in response['Buckets']:
        print(f"  - {bucket['Name']}")

except Exception as e:
    print(f"Error: {e}")
