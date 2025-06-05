import boto3

s3_client = boto3.client('s3')
bucket_name = 'el-bucket-del-chuelmo-tres'

try:
    s3_client.create_bucket(Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint':'us-east-2'})
    print(f"Bucket '{bucket_name}' creado exitosamente en la región 'us-east-2'")
except Exception as e:
    print(f"Error al crear el bucket: {e}")

