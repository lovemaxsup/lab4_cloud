import logging
from botocore.exceptions import ClientError
import os
import boto3

filename = 'val_rate.csv'
backet = 'lab2suprunmaksymfb05'
def upload_file(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)
    # Upload the file
    s3_client = boto3.client(service_name='s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
print(upload_file(filename, backet))