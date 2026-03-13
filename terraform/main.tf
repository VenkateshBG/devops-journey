# PROVIDER — tell Terraform we're using AWS
provider "aws" {
  region = var.region
}

# RESOURCE — create an S3 bucket
resource "aws_s3_bucket" "my_first_bucket" {
  bucket = var.bucket_name

  tags = {
    Name        = var.bucket_name
    Environment = var.environment
    CreatedBy   = "Terraform"
  }
}