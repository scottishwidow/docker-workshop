resource "aws_security_group" "node_api_sg" {
  name        = "node-api-sg"
  description = "Nodejs API security group"
  vpc_id      = data.aws_vpc.default.id

  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 443
    to_port = 443
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


resource "aws_instance" "node_api_host" {
  ami = data.aws_ami.ubuntu.id
  instance_type = "t2.micro"  
  associate_public_ip_address = true
  key_name = "k.michael"
  security_groups = [ aws_security_group.node_api_sg.name ]

  root_block_device {
    volume_size = 15
    volume_type = "gp2"
  }

  provisioner "remote-exec" {
    inline = [
      "echo 'Wait until SSH is ready'"
    ]

    connection {
      type = "ssh"
      user = local.ssh_user
      private_key = file(var.private_key_path)
      host = aws_instance.node_api_host.public_ip
    } 
  }

  provisioner "local-exec" {
    command = "ansible-playbook -i ${aws_instance.node_api_host.public_ip}, --private-key ${var.private_key_path} ./ansible/docker.yaml"
  }
}