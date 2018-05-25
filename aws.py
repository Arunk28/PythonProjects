import boto3

client_key = 'xxxxxxxxxxxxxxx'
seckret_key = 'xxxxxxxxxxxxxxx/xxxxxxxxxxxxxxx'

client = boto3.resource('ec2',region_name='us-east-1', aws_access_key_id=client_key,aws_secret_access_key=seckret_key)
instances = client.instances.filter()
for instance in instances:
    if instance.state["Name"] == "running":
            print(instance.id, instance.instance_type)



