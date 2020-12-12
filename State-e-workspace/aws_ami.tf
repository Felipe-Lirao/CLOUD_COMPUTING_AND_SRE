data "aws_ami" "estado_workspace" {

owners = ["099720109477"]

most_recent = true

filter {
    name  = "virtualization-type"
    values = ["hvm"]
  }
  
  filter {
    name  = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-xenial-*"]
  }

}
