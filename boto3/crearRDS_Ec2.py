import boto3
from dotenv import load_dotenv
import os

load_dotenv()

DB_INSTANCE_CLASS = os.getenv('DB_INSTANCE_CLASS')
ENGINE = os.getenv('ENGINE')
USER_NAME = os.getenv('USER_NAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')

ec2 = boto3.client('ec2')

#creamos el grupo de seguridad para la DB
sg_db_boto3_name = 'GrupoSeguridadDB'
print(f"Intentando crear el grupo de seguridad '{sg_db_boto3_name}'")

try:
	response = ec2.create_security_group(
		GroupName=sg_db_boto3_name,
		Description='Permitir el acceso al puerto 3306 para MySql desde ec2'
	)
	
	sg_db_boto3_id = response['GroupId']
	print(f"SG creado con el ID: {sg_db_boto3_id} y el nombre: '{sg_db_boto3_name}'")
except Exception as e:
	if 'InvalidGroup.Duplicate' in str(e): # el grupo de seguridad ya existe
		print(f"El grupo de seguridad '{sg_db_boto3_name}' ya existe. Obteniendo su ID...")
		response = ec2.describe_security_groups(GroupNames=[sg_db_boto3_name])
		sg_db_boto3_id = response['SecurityGroups'][0]['GroupId']
		print(f"El grupo de seguridad con el nombre '{sg_db_boto3_name}' tiene el id: '{sg_db_boto3_id}'")
	else:
		raise



#creamos el grupo de seguridad para la instancia ec2

sg_ec2_boto3_name = 'GrupoSeguridadDeMiEc2'
print(f"Intentando crear el grupo de seguridad '{sg_ec2_boto3_name}'")

try:
	response2 = ec2.create_security_group(
		GroupName=sg_ec2_boto3_name,
		Description='Permitir el acceso desde la instancia EC2 al security group de la DB'
	)
	
	sg_ec2_boto3_id = response2['GroupId']
	print(f"SG creado con el ID: {sg_ec2_boto3_id} y el nombre: '{sg_ec2_boto3_name}'")
except Exception as e:
	if 'InvalidGroup.Duplicate' in str(e): # el grupo de seguridad ya existe
		print(f"El grupo de seguridad '{sg_ec2_boto3_name}' ya existe. Obteniendo su ID...")
		response = ec2.describe_security_groups(GroupNames=[sg_ec2_boto3_name])
		sg_ec2_boto3_id = response['SecurityGroups'][0]['GroupId']
		print(f"El grupo de seguridad con el nombre '{sg_ec2_boto3_name}' tiene el id: '{sg_ec2_boto3_id}'")
	else:
		raise


#Creamos ahora las reglas para los SG
print(f"Intentando crear las reglas para el grupo de seguridad '{sg_db_boto3_id}'")
try:
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
	print(f"Reglas de seguridad creadas para el grupo de seguridad '{sg_db_boto3_id}'")
except Exception as e:
	if 'InvalidPermission.Duplicate' in str(e):
		print(f"Reglas de seguridad ya existen para el grupo de seguridad '{sg_db_boto3_id}'")
	else:
		raise

print(f"Intentando crear regla de seguridad 'https' para el grupo '{sg_ec2_boto3_id}'")
try:
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
	print(f"Reglas de seguridad 'https' creadas para el grupo de seguridad '{sg_ec2_boto3_id}'")
except Exception as e:
	if 'InvalidPermission.Duplicate' in str(e):
		print(f"Reglas de seguridad ya existen para el grupo de seguridad '{sg_ec2_boto3_id}'")
	else:
		raise

print(f"Intentando crear regla de seguridad 'ssh' para el grupo '{sg_ec2_boto3_id}'")
try:
	ec2.authorize_security_group_ingress(
		GroupId=sg_ec2_boto3_id,
		IpPermissions=[
			{
				'IpProtocol' : 'tcp',
				'FromPort' : 22,
				'ToPort' : 22,
				'IpRanges' : [{'CidrIp': '0.0.0.0/0' }]
			}
		]
	)
	print(f"Reglas de seguridad 'ssh' creadas para el grupo de seguridad '{sg_ec2_boto3_id}'")
except Exception as e:
	if 'InvalidPermission.Duplicate' in str(e):
		print(f"Reglas de seguridad ya existen para el grupo de seguridad '{sg_ec2_boto3_id}'")
	else:
		raise


#creo el cliente rds
rds = boto3.client('rds')
db_instance_identifier = 'miDB-Instancia'

try: 
	response3 = rds.create_db_instance(
		DBInstanceIdentifier=db_instance_identifier,
		AllocatedStorage=20,
		DBInstanceClass=DB_INSTANCE_CLASS,
		Engine=ENGINE,
		MasterUsername=USER_NAME,
		MasterUserPassword=DB_PASSWORD,
		VpcSecurityGroupIds=[sg_db_boto3_id]
	)
	print(f"Base de datos creada con el nombre {db_instance_identifier}")
	print("Esperando que la base de datos quede disponible...")
	waiter = rds.get_waiter('db_instance_available')
	waiter.wait(DBInstanceIdentifier=db_instance_identifier)
	db_instance = rds.describe_db_instances(DBInstanceIdentifier=db_instance_identifier)
	db_endpoint = db_instance['DBInstances'][0]['Endpoint']['Address']
	print(f"Instancia de Base de Datos disponible en: '{db_endpoint}'")
except Exception as e:
	if 'DBInstanceAlreadyExists' in str(e):
		print(f"La base de datos RDS '{db_instance_identifier}' ya existe. Obteniendo su endpoint...")
		db_instance = rds.describe_db_instances(DBInstanceIdentifier=db_instance_identifier)
		db_endpoint = db_instance['DBInstances'][0]['Endpoint']['Address']
		print(f"Base de datos disponible en: '{db_endpoint}'")
	else:
		raise


#Crear la instancia ec2 y el script para instalar mysql en la instancia creada

user_data_script = f'''#!/bin/bash
sudo yum update -y
sudo yum install -y mariadb105-server-utils.x86_64
echo "Conexion a la base de datos en: {db_endpoint}" > /home/ec2-user/db_info.txt
#mysql -h {db_endpoint} -u admin < obli.sql
'''

TAG_VALUE_NAME = "El-buenito-ec2"

print(f"Intentando crear la instancia ec2 con nombre: '{TAG_VALUE_NAME}'")

#Primero busco si ya no existe una ec2 con el nombre TAG_VALUE_NAME

filters = [
	{"Name": "tag:Name", "Values": [TAG_VALUE_NAME]},
	{"Name": "instance-state-name", "Values": ["pending", "running", "stopping", "stopped"]},
]

paginator = ec2.get_paginator("describe_instances")
ids = []

for page in paginator.paginate(Filters=filters):
	for reservation in page["Reservations"]:
		for instance in reservation["Instances"]:
			ids.append(instance["InstanceId"])

if ids: #si ya hay alguna ec2 con el mismo nombre
	print(f"Ya existe(n) {len(ids)} instancia(s) con Name='{TAG_VALUE_NAME}': {', '.join(ids)}")
else:
	try:
		response4 = ec2.run_instances(
			ImageId='ami-09e6f87a47903347c',
			MinCount=1,
			MaxCount=1,
			InstanceType='t2.micro',
			SecurityGroupIds=[sg_ec2_boto3_id],
			UserData=user_data_script,
			TagSpecifications=[
				{
					"ResourceType": "instance",
					"Tags": [{"Key": "Name", "Value": TAG_VALUE_NAME}]
				}
			]
		)
		
		instance_id = response4['Instances'][0]['InstanceId']
		print(f"Instancia ec2 creada con el id {instance_id}")
		print("Esperando que la instancia ec2 quede running")
		waiter2 = ec2.get_waiter('instance_running')
		waiter2.wait(InstanceIds=[instance_id])
		print("ya ta pronta la ec2 y está corriendo")
	except Exception as e:
		print(f"No se puedo crear la instancia con nombre: '{TAG_VALUE_NAME}'")
		print(e)

# Desde AWS conectarse a la instancia ec2
# En la terminal abierta en el navegador verificar que nos podemos conectar a la base de datos con el siguiente comando:
# mysql -h {endpoint} -u admin -p
# ejemplo: mysql -h midb-instancia.c5t016sh9j96.us-east-1.rds.amazonaws.com -u admin -p




