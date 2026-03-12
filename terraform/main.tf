# PROVIDER — tell Terraform we're using AWS
provider "aws" {
  region = "ap-south-1"
}

# RESOURCE — create an S3 bucket
resource "aws_s3_bucket" "my_first_bucket" {
  bucket = "venkatesh-terraform-bucket-2024"

  tags = {
    Name        = "venkatesh-terraform-bucket"
    Environment = "Learning"
    CreatedBy   = "Terraform"
  }
}