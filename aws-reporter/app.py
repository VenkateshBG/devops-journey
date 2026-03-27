from flask import Flask
import boto3

app = Flask(__name__)

s3 = boto3.client('s3', region_name='ap-south-1')
ec2 = boto3.client('ec2', region_name='ap-south-1')

def get_buckets():
    try:
        response = s3.list_buckets()
        buckets = response['Buckets']
        return [bucket['Name'] for bucket in buckets]
    except Exception as e:
        return [f"Error: {e}"]

def get_instances():
    try:
        response = ec2.describe_instances()
        instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append({
                    'id': instance['InstanceId'],
                    'state': instance['State']['Name'],
                    'type': instance['InstanceType']
                })
        return instances
    except Exception as e:
        return [f"Error: {e}"]

@app.route('/')
def home():
    buckets = get_buckets()
    instances = get_instances()

    bucket_list = ""
    for bucket in buckets:
        bucket_list += f"<li>{bucket}</li>"

    instance_list = ""
    for instance in instances:
        instance_list += f"<li>{instance['id']} | {instance['state']} | {instance['type']}</li>"

    return f"""
    <h1>🚀 AWS Resource Reporter</h1>

    <h2>S3 Buckets</h2>
    <ul>{bucket_list}</ul>

    <h2>EC2 Instances</h2>
    <ul>{instance_list}</ul>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
