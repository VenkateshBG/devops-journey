print("Script started")
import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')

def launch_instance(name, ami_id, instance_type, subnet_id, sg_id):
    try:
        response = ec2.run_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            MinCount=1,
            MaxCount=1,
            SubnetId=subnet_id,
            SecurityGroupIds=[sg_id],
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {'Key': 'Name', 'Value': name}
                    ]
                }
            ]
        )
        instance_id = response['Instances'][0]['InstanceId']
        print(f"  ✅ Launched: {name} — {instance_id}")
        return instance_id
    except Exception as e:
        print(f"  ❌ Failed to launch {name}: {e}")

def list_instances(ec2):
    try:
        response = ec2.describe_instances()
        print("\nYour EC2 Instances:")
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                name = 'Unknown'
                for tag in instance.get('Tags', []):
                    if tag['Key'] == 'Name':
                        name = tag['Value']
                print(f"  - {name} | {instance_id} | {state}")
    except Exception as e:
        print(f"  ❌ Error: {e}")


def wait_for_running(ec2, instance_id):
    print(f"  ⏳ Waiting for instance to reach running state...")
    waiter = ec2.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instance_id])
    print(f"  ✅ Instance is now running!")

def stop_instance(ec2, instance_id):
    try:
        response = ec2.stop_instances(InstanceIds=[instance_id])
        state = response['StoppingInstances'][0]['CurrentState']['Name']
        print(f"  ✅ Instance {instance_id} is now: {state}")
    except Exception as e:
        print(f"  ❌ Failed to stop {instance_id}: {e}")

# MAIN SCRIPT
print("Launching instance...")
instance_id = launch_instance(
    name="my-web-server",
    ami_id="ami-019715e0d74f695be",
    instance_type="t2.micro",
    subnet_id="subnet-046134eca002a8c78",
    sg_id="sg-08b855a104c531977"
)

print("\nWaiting for instance...")
wait_for_running(ec2, instance_id)

print("\nListing all instances...")
list_instances(ec2)

print("\nStopping instance...")
stop_instance(ec2, instance_id)

print("\nFinal instance list...")
list_instances(ec2)
