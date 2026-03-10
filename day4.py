# FUNCTIONS
def greet(name):
    print(f"Hello {name}, welcome to DevOps!")

greet("Venkatesh")
greet("AWS")

# LOOPS
clouds = ["S3", "EC2", "VPC", "IAM", "Lambda"]

for service in clouds:
    print(f"AWS Service: {service}")


services = ['s3', 'EC2', 'VPC']

print(services[0])
print(services[1])
print(services[2])

bucket={
    "name": "my-bucket",
    "region" : "ap-south-1",
    "size" : "100"
}

print(bucket["name"])
print(bucket["region"])
print(bucket["size"])


buckets = [
    {"name" : "my-bucket-1", "region" : "ap-south-1"},
    {"name" : "my-bucket-2", "region": "us-east-1"},
    {"name" : "my-bucket-3", "region" : "eu-west-1"}
]

for bucket in buckets:
    print(f"Bucket: {bucket['name']} is in {bucket['region']}")

response = {
    'Buckets': [
        {'Name': 'my-devops-learning-2027'}
    ]
}

print(f"Bucket name: {response['Buckets'][0]['Name']}")
