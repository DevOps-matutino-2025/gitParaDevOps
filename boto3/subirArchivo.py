import boto3


file_name = 'perritos.webp'
bucket = 'aws-chuelmo-001'
object_name = 'perritos'


s3_client = boto3.client('s3')
response = s3_client.upload_file(file_name, bucket, object_name)

