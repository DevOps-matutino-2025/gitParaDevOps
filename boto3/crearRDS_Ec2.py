import boto3

ec2 = boto3.client('ec2')

#creamos el grupo de seguridad para la DB
sg_db_boto3 = 'GrupoSeguridadDB3'

response1 = ec2.create_security_group(
	GroupName=sg_db_boto3,
	Description='Permitir el acceso al puerto 3306 para MySql desde ec2'
)

sg_db_boto3_id = response1['GroupId']


#creamos el grupo de seguridad para la instancia ec2

sg_ec2_boto3 = 'GrupoSeguridadDeMiEc2A'

response2 = ec2.create_security_group(
	GroupName=sg_ec2_boto3,
	Description='Permitir el acceso desde la instancia EC2 al security group de la DB'
)

sg_ec2_boto3_id = response2['GroupId']


#Creamos ahora las reglas para los SG

ec2.authorize_security_group_ingress(
	GroupId=sg_db_boto3_id,
	IpPermissions=[
		{
			'IpProtocol' : 'tcp',
			'FromPort' : 3306,
			'ToPort' : 3306,
			'UserIdGroupPairs' : [{'GroupId': sg_ec2_boto3_id }]
		}
	]
)

ec2.authorize_security_group_ingress(
	GroupId=sg_ec2_boto3_id,
	IpPermissions=[
		{
			'IpProtocol' : 'tcp',
			'FromPort' : 443,
			'ToPort' : 443,
			'IpRanges' : [{'CidrIp': '0.0.0.0/0' }]
		}
	]
)

#creo el cliente rds
rds = boto3.client('rds')
db_instance_identifier = 'miDB-Instancia'

response3 = rds.create_db_instance(
	DBInstanceIdentifier=db_instance_identifier,
	AllocatedStorage=20,
	DBInstanceClass='db.t3.micro',
	Engine='mysql',
	MasterUsername='admin',
	MasterUserPassword='ps1234Admin',
	VpcSecurityGroupIds=[sg_db_boto3_id]
)
print(f"Base de datos creada con el nombre {db_instance_identifier}")
print("Esperando que la base de datos quede disponible...")
waiter = rds.get_waiter('db_instance_available')
waiter.wait(DBInstanceIdentifier=db_instance_identifier)
db_instance = rds.describe_db_instances(DBInstanceIdentifier=db_instance_identifier)
db_endpoint = db_instance['DBInstances'][0]['Endpoint']['Address']


#Crear la instancia ec2 y el script para instalar mysql en la instancia creada
user_data_script = f'''#!/bin/bash
sudo yum update -y
sudo yum install -y mariadb105-server-utils-x86_64
echo "Conexion a la base de datos en: {db_endpoint}" > /home/ec2-user/db_info.txt
'''

response4 = ec2.run_instances(
	ImageId='ami-09e6f87a47903347c',
	MinCount=1,
	MaxCount=1,
	InstanceType='t2.micro',
	SecurityGroupIds=[sg_ec2_boto3_id],
	UserData=user_data_script,
	IamInstanceProfile={
		'Name': 'LabInstanceProfile'
	}
)

instace_id = response4['Instances'][0]['InstanceId']
printf(f"Instancia ec2 creada con el id {instance_id}")
print("Esperando que la instancia ec2 quede running")
waiter2 = ec2.get_waiter('instance_running')
waiter2.wait(InstanceIds=[instace_id])
print("ya ta pronta la ec2 y está corriendo")


