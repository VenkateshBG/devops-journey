terraform {
  backend "s3" {
    bucket         = "venkatesh-terraform-state-2024"
    key            = "terraform-advanced/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "terraform-state-lock"
    encrypt        = true
  }
}

provider "aws" {
  region = var.region
}

# Create 3 S3 buckets using same module!
module "s3_dev" {
  source      = "./modules/s3"
  bucket_name = "venkatesh-dev-bucket-2024"
  environment = "dev"
}

module "s3_staging" {
  source      = "./modules/s3"
  bucket_name = "venkatesh-staging-bucket-2024"
  environment = "staging"
}

module "s3_prod" {
  source      = "./modules/s3"
  bucket_name = "venkatesh-prod-bucket-2024"
  environment = "prod"
}