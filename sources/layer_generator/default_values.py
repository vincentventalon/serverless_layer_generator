#!/usr/bin/env python
import os

# Constant
DOWNLOAD_DIRECTORY = f"/tmp/python/python/lib/{os.environ['RUNTIME']}/site-packages"


# Default variables
REQUIREMENT_TXT = [
    "scrapy",
    "selenium"
    ]
S3_BUCKET = "change-me"
S3_PREFIX_KEY = 'lambda_fonctions/'
ARCHIVE_NAME = "python.zip"
RUNTIMES = [f"{os.environ['RUNTIME']}"]
LICENSE = "GNU GPL"
LAYER_NAME = 'Layer_name'
LAYER_DESCRIPTION = 'This is the description of the layer'