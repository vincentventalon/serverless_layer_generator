# Serverless Python Layer Generator for AWS

A serverless python layer generator to create python layer using lambda. 

You can use it for fast prototyping, IaaC or just to deploy a layer using the AWS Console only.

It's compatible with C++ librairies.

And it's lightnight fast.
## Getting Started

These instructions will get you a copy of the project up prior to deploy it on AWS using terraform.

As it's compatible with C++ libraries, there is a dependency with gcc which vary with python runtime.
Please use main branch for layer with python3.8 runtime and python37- for layer with Python 3.6 and 3.7 runtimes.

There is a file call default_values.py where default values can be setup. This is optional as json feed in lamdba event take over default values (see Installing).


### Prerequisites

```
Git
AWS credentials set
Terraform
```

### Installing

First clone the repo
```
git clone https://github.com/vincentventalon/serverless_layer_generator.git
```

Make some optional configurations :
In variables.tf, you can set a defaut region or you will be asked during deploy
Optional: In default_values.py set the bucket where you code will be uploaded and other default values
```
S3_BUCKET = "change-me"
```
Optional: If you use always the same bucket you should also refine policies in main.tf : 
 ```
s3 = {
      effect    = "Allow",
      actions   = ["s3:HeadObject", "s3:GetObject", "s3:PutObject"],
      resources = ["arn:aws:s3:::*"]
    }
```


Deploy in the cloud :
```
terraform init
terraform plan
terraform apply
```

Run with default values or use a json event :
```
{
requirement_txt :["selenium", "scrapy"]  
s3_bucket : "s3_bucket_where_zip_will_be_uploaded"
s3_prefix_key = "lambda_function/" # Will upload archive in this folder
archive_name = "name_of_archive.zip" 
licence = "GNU GPL"
layer_name = "name_of_the_layer"
layer_description = "Description of the layer"
runtimes = ["python3.8"]
}
```

## Thanks to 

* [LamCI](https://github.com/lambci/gcc-lambda-layer) - GCC layers for lambda

## Authors

* **Vincent Ventalon** - (https://github.com/vincentventalon)


## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE 3 - see the [LICENSE.md](LICENSE.md) file for details
