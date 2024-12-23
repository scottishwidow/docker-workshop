output "ec2_public_ip" {
  value = aws_instance.node_api_host.public_ip
}