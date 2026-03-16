output "ec2_public_ip" {
  description = "Public IP to SSH into EC2"
  value       = aws_instance.docker_ec2.public_ip
}

output "ec2_instance_id" {
  description = "EC2 Instance ID"
  value       = aws_instance.docker_ec2.id
}

output "security_group_id" {
  description = "Security Group ID"
  value       = aws_security_group.docker_sg.id
}
