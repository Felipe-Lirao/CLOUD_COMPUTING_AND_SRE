terraform {
  backend "s3" {
    bucket = "lab-fiap-75aoj-337930"
    key    = "75aoj"
    region = "us-east-1"
  }
}