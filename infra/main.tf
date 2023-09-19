provider "aws" {
  region = var.region

}


module "lambda_function" {
  source = "terraform-aws-modules/lambda/aws"

  for_each = var.lambda_runtimes

  function_name = "Serverless_layer_generator_${replace(each.key, ".", "_")}"
  description   = each.value.description
  runtime       = each.key

  timeout = 600
  memory_size = 1024
  handler       = "lambda_function.lambda_handler"
  publish       = true

  source_path = "../sources/layer_generator"

  ######################
  #  Layers
  ######################

  # layers depend on your python runtime for compatibility
  layers = each.key == "python3.6" || each.key == "python3.7" ? ["arn:aws:lambda:${var.region}:553035198032:layer:gcc72-lambda1:4",] : [
    "arn:aws:lambda:${var.region}:553035198032:layer:gcc-lambda2:4",
  ]


  environment_variables = {
    RUNTIME = each.key
  }

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

