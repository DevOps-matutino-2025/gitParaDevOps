import boto3


file_name = 'otrosPerritos.webp'
bucket = 'aws-chuelmo-001'
object_name = 'perritos'

s3 = boto3.client('s3')
s3.download_file(bucket, object_name, file_name)
