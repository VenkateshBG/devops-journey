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

module "s3" {
  source      = "./modules/s3"
  bucket_name = "venkatesh-${terraform.workspace}-bucket-2024"
  environment = terraform.workspace
}