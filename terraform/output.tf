output "bucket_name" {
  description = "Name of the created S3 bucket"
  value       = aws_s3_bucket.my_first_bucket.bucket
}

output "bucket_arn" {
  description = "ARN of the created S3 bucket"
  value       = aws_s3_bucket.my_first_bucket.arn
}

output "bucket_region" {
  description = "Region where bucket is created"
  value       = aws_s3_bucket.my_first_bucket.bucket_region
}
