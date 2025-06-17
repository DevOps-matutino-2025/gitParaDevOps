import boto3

ec2_client = boto3.client('ec2')

instance_params = {
	'ImageId': 'ami-09e6f87a47903347c',
	'MinCount' : 1,
	'MaxCount' : 1,
	'InstanceType' : 't2.micro',
	'TagSpecifications' : [
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'PC-prueba-con-nombre'  # Reemplaza con el nombre deseado
                }
            ]
        }
    ]
}

response = ec2_client.run_instances(**instance_params)

for instance in response['Instances']:
	print(f"El id de la instancia creada es {instance['InstanceId']}")
