#!/usr/bin/env python
import logging
import boto3
import subprocess
from botocore.exceptions import ClientError
from default_values import REQUIREMENT_TXT, S3_BUCKET, S3_PREFIX_KEY, ARCHIVE_NAME, RUNTIMES, LICENSE, LAYER_NAME, LAYER_DESCRIPTION
    
def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
    
def install_requirement(download_directory, requirement_txt: list):
    for elt in requirement_txt:
        subprocess.call(f"pip install {elt} -t {download_directory} --no-cache-dir".split()) 
    
def get_variables(event):
    yield event["requirement_txt"] if event.get("requirement_txt") else REQUIREMENT_TXT
    yield event["s3_bucket"] if event.get("s3_bucket") else S3_BUCKET
    archive_name = event["archive_name"] if event.get("archive_name") else ARCHIVE_NAME
    yield archive_name
    s3_prefix_key = event["s3_prefix_key"] if event.get("s3_prefix_key") else S3_PREFIX_KEY
    yield s3_prefix_key
    yield event["licence"] if event.get('licence') else LICENSE
    yield event["layer_name"] if event.get('layer_name') else LAYER_NAME
    yield event["layer_description"] if event.get('layer_description') else LAYER_DESCRIPTION
    yield event["runtimes"] if event.get('runtimes') else RUNTIMES
    yield s3_prefix_key + archive_name    
    yield '/tmp/' + archive_name.split(".")[0]
