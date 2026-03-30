def greet_devops(name):
    print(f"Hello {name}! Welcome to DevoOps Month 2!")



def list_aws_services(services_list):
    for i in range(len(services_list)):
        print("AWS services: ",services_list[i])



service_aws = ["s3", "ec2", "vpc", "iam", "bedrock"]


def describe_instances(instances):
    for key, value in instances.items():
        print(f"instances {key} : {value} ")

instance_details = {
    'id': 'i-1234567',
    'type': 't2.micro',
    'state': 'running'
}

describe_instances(instance_details)
#list_aws_services(service_aws)

#greet_devops("Venkatesh")