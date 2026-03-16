variable "region" {
  default = "ap-south-1"
}

variable "ami_id" {
  description = "Ubuntu AMI ID"
  type        = string
}

variable "instance_type" {
  default = "t2.micro"
}

variable "vpc_id" {
  description = "Default VPC ID"
  type        = string
}

variable "subnet_id" {
  description = "Public Subnet ID"
  type        = string
}

variable "key_name" {
  description = "EC2 Key Pair name"
  type        = string
}