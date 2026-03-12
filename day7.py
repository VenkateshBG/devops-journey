print("Script Executing")
import boto3

iam = boto3.client('iam')

def list_users(iam):
    try:
        response  = iam.list_users()
        for user in response['Users']:
            print(f" - {user['UserName']} | {user['UserId']}")
    
    except Exception as e:
        print(f" Error: {e}")


def list_roles(iam):
    try:
        response = iam.list_roles()
        for role in response['Roles']:
            print(f" - {role['RoleName']} | {role['RoleId']}")

    except Exception as e:
        print(f" Error: {e}")


def list_access_keys(iam, username):
    try:
        response = iam.list_access_keys(UserName = username )
        for access_keys in response['AccessKeyMetadata']:
            print(f" - {access_keys['AccessKeyId']} | {access_keys['Status']}")

    except Exception as e:
        print(f" Error: {e}")
    

#list_roles(iam)
#list_users(iam)

list_access_keys(iam, 'admin')
list_access_keys(iam, 'terrform-access')