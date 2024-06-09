#### Code Snippets

---

**boto3**

Setup
```python
# boto3 solution
import boto3
session = boto3.session.Session()
s3_client = session.client(
    service_name = 's3',
    aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY'],
    endpoint_url = '',
)
```

| Command | Description |
| -------- | -------- |
| `c = s3_client.list_objects_v2(Bucket='sg....', Prefix='folder/path/')`| List files|
| `s3_client.download_file(BUCKET_NAME, s3_filepath, local_filepath)`| Download files from S3|
| `s3_client.upload_file(local_filepath, BUCKET_NAME, s3_filepath)`| Upload files to S3|

---

**awscli**

Setup
```bash
pip3 install awscli
pip3 show awscli
aws configure # enter key id and access key
```

| Command | Description |
| -------- | -------- |
| `aws s3 ls s3://bucket_name/ --no-verify-ssl --endpoint-url=https://... --recursive --human-readable --summarize`| List files|
| `aws s3 cp s3://bucket_name/ <local-file> --no-verify-ssl --endpoint-url=https://...`| Download files from S3|
| `aws s3 cp <local-file> s3://bucket_name/ --no-verify-ssl --endpoint-url=https://...`| Upload files to S3|
| `aws s3 rm <s3-file-path>`| Remove files in S3|
| `--dryrun`| Dry run|

#### Common Issues

| Issue | Solution |
| -------- | -------- |
| Took a really long time but no outcome displayed| `pip3 install awscli`|
| `bash: aws: command not found`| `pip3 install awscli`|