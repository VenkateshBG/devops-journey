output "dev_bucket" {
  value = module.s3_dev.bucket_name
}

output "staging_bucket" {
  value = module.s3_staging.bucket_name
}

output "prod_bucket" {
  value = module.s3_prod.bucket_name
}