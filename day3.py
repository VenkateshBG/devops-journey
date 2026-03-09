import boto3

bucket_name = "my-devops-learning-2027"
file_name = "test-file.txt"

s3 = boto3.client('s3', region_name='ap-south-1')

# UPLOAD
print("Uploading file...")
s3.upload_file(file_name, bucket_name, file_name)
print(f"  '{file_name}' uploaded successfully!")

# LIST
print("\nFiles in bucket:")
response = s3.list_objects_v2(Bucket=bucket_name)
if 'Contents' in response:
    for obj in response['Contents']:
        print(f"  - {obj['Key']} ({obj['Size']} bytes)")

# DELETE
print("\nDeleting file...")
s3.delete_object(Bucket=bucket_name, Key=file_name)
print(f"  '{file_name}' deleted successfully!")

# CONFIRM DELETION
print("\nFiles in bucket after deletion:")
response2 = s3.list_objects_v2(Bucket=bucket_name)
if 'Contents' in response2:
    for obj in response2['Contents']:
        print(f"  - {obj['Key']}")
else:
    print("  Bucket is empty!")
