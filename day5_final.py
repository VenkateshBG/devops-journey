import boto3

# FUNCTION to create a bucket
def create_bucket(s3, bucket_name):
    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-south-1'
            }
        )
        print(f"  ✅ Created: {bucket_name}")
    except Exception as e:
        print(f"  ❌ Failed to create {bucket_name}: {e}")

# FUNCTION to list all buckets
def list_buckets(s3):
    try:
        response = s3.list_buckets()
        buckets = response['Buckets']
        if buckets:
            print(f"\n  Total buckets: {len(buckets)}")
            for bucket in buckets:
                print(f"  - {bucket['Name']}")
        else:
            print("  No buckets found!")
    except Exception as e:
        print(f"  ❌ Failed to list buckets: {e}")

# FUNCTION to delete a bucket
def delete_bucket(s3, bucket_name):
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"  ✅ Deleted: {bucket_name}")
    except Exception as e:
        print(f"  ❌ Failed to delete {bucket_name}: {e}")

# MAIN SCRIPT
s3 = boto3.client('s3', region_name='ap-south-1')

# List of buckets to create
bucket_names = [
    "venkatesh-devops-bucket-01",
    "venkatesh-devops-bucket-02",
    "venkatesh-devops-bucket-03"
]

# CREATE all buckets using loop
print("Creating buckets...")
for bucket in bucket_names:
    create_bucket(s3, bucket)

# LIST all buckets
print("\nListing all buckets...")
list_buckets(s3)

# DELETE all buckets using loop
print("\nDeleting buckets...")
for bucket in bucket_names:
    delete_bucket(s3, bucket)

# CONFIRM deletion
print("\nFinal bucket list...")
list_buckets(s3)