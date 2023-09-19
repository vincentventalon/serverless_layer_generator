variable "region" {
  description = "Region to deploy"
  type        = string
  # default     = "eu-west-3"
  validation {
    condition     = contains(["ap-northeast-1", "ap-northeast-2", "ap-south-1", "ap-southeast-1", "ap-southeast-2", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "sa-east-1", "us-east-1", "us-east-2", "us-west-1", "us-west-2"], var.region)
    error_message = "Not a valid AWS region."
  }
}

variable "lambda_runtimes" {
  description = "Map of Python runtimes and their description"
  type        = map(object({
    description = string
  }))
  default     = {
    "python3.7" = { description = "Serverless layer generator for Python 3.7 runtime" },
    "python3.9" = { description = "Serverless layer generator for Python 3.9 runtime" },
    # Add more runtimes and descriptions as needed
  }
}

