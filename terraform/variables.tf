variable "bucket_name" {
  description = "Name of the s3 bucket"
  type = string
}

variable "region" {
  description = "AWS region to deploy"
  type = string
  default = "ap-south-1"
}

variable "environment" {
  description = "Environment name - dev, stage, prod"
  type = string
  default = "dev"
}