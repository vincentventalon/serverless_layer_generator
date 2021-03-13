#!/usr/bin/env python


# Constant
DOWNLOAD_DIRECTORY = '/tmp/python/python/lib/python3.8/site-packages'


# Default variables
REQUIREMENT_TXT = [
    "scrapy",
    "selenium"
    ]
S3_BUCKET = "change-me"
S3_PREFIX_KEY = 'lambda_fonctions/'
ARCHIVE_NAME = "python.zip"
RUNTIMES = ["python3.7"]
LICENSE = "GNU GPL"
LAYER_NAME = 'Layer_name'
LAYER_DESCRIPTION = 'This is the description of the layer'