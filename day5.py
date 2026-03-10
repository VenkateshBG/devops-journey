import boto3

s3 = boto3.client('s3', region_name='ap-south-1')

# Test 1 - Access a bucket that doesn't exist
try:
    s3.list_objects_v2(Bucket="bucket-that-doesnt-exist")
except s3.exceptions.NoSuchBucket:
    print("Error 1: Bucket doesn't exist!")

# Test 2 - Wrong key in dictionary
try:
    response = {'Buckets': []}
    print(response['Instances'])
except KeyError as e:
    print(f"Error 2: Key {e} not found in response!")

# Test 3 - Catch ANY error
try:
    result = 10 / 0
except Exception as e:
    print(f"Error 3: Something went wrong — {e}")

print("\nAll errors handled, script completed successfully!")