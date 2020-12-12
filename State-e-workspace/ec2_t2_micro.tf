provider "aws" {
    region = "us-east-1"
        
}

resource "aws_instance" "intancias_ec2" {
    
    ami = "estado_workspace"
    
    instance_type = "t2.micro"

    count = 2

    tags = {
        Name = "Instancia_EC2-${count.index}-${terraform.workspace}"
    }

}