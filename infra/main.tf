provider "aws" {
  region = "eu-west-3"

  # Make it faster by skipping something
  skip_get_ec2_platforms      = true
  skip_metadata_api_check     = true
  skip_region_validation      = true
  skip_credentials_validation = true
  skip_requesting_account_id  = true
}

module "lambda_function" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = "Serverless_layer_generator_python3_8"
  description   = "Serverless layer generator for python3.8 runtime"
  timeout = 600
  memory_size = 1024
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.8"
  publish       = true

  source_path = "../sources/layer_generator"


  layers = [
    "arn:aws:lambda:eu-west-3:553035198032:layer:gcc-lambda2:4",
  ]



  ######################
  #  Policies
  ######################


  attach_policy_statements = true
  policy_statements = {
    layer = {
      effect    = "Allow",
      actions   = ["lambda:PublishLayerVersion"],
      resources = ["*"]
    },
    s3 = {
      effect    = "Allow",
      actions   = ["s3:HeadObject", "s3:GetObject", "s3:PutObject"],
      resources = ["arn:aws:s3:::*"]
    }
  }

  ###########################
  # END: policies
  ###########################

  tags = {
    project = "serverless"
  }
}