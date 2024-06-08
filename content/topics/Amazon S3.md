#### Code Snippets

List files in S3 bucket
```python
import boto3
session = boto3.session.Session()
s3_client = session.client(
    service_name = 's3',
    aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY'],
    endpoint_url = '',
)
c = s3_client.list_objects_v2(Bucket='sg....', Prefix='folder/path/')
[i['Key'] for i in c['Contents']]
```

Download files from S3 bucket
```python
s3_client.download_file(BUCKET_NAME, s3_filepath, local_filepath)
```

Upload files to S3 bucket
```python
s3_client.upload_file(local_filepath, BUCKET_NAME, s3_filepath)
```