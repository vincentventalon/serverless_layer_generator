#!/usr/bin/env python

"""
Licence : GNU GPL

This function is used to download, store on S3 and create a new layer for python3 librairies.

Limitations
    Only python3.8 runtime is fully supported with this Lambda Layer maker as gcc packaged in this lambda is v7.3.1. 
    Please checkout python3.7- branch for Python 3.7 and less support    

"""

import os
import sys 
import shutil
import boto3 
from utils import upload_file, get_variables, install_requirement

def lambda_handler(event, context):

    # Get variables from event or default values
    requirement_txt, s3_bucket,archive_name,s3_prefix_key, licence, layer_name , layer_description, runtimes, s3_key, download_directory = get_variables(event)

    # Download requirement in download directory
    install_requirement(download_directory, requirement_txt)
    
    # Make archive of this directory
    shutil.make_archive('/tmp/python', 'zip', '/tmp/python')

    #Upload it on s3 bucket
    upload_file('/tmp/python.zip', s3_bucket, s3_key )
    
    # Publish the layer
    client = boto3.client('lambda')
    response = client.publish_layer_version(
        LayerName= layer_name,
        Description= layer_description,
        Content={
            'S3Bucket': s3_bucket,
            'S3Key': s3_key,
        },
        CompatibleRuntimes=runtimes,
        LicenseInfo= licence)
        
    # Clean the response
    del response["ResponseMetadata"]
    
    return {
        'statusCode': 200,
        "body" : {
        "archive_s3_bucket" : s3_bucket,
        "archive_s3_key" : s3_key,
        "publish_layer_version_response" : response
        }
        
    }
