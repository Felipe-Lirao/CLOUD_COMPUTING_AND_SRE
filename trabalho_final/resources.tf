provider "aws" {
  region = "us-east-1"
}

locals {
  env = "${terraform.workspace}"
}

# ---------------------------------------------------------------------------------------------------------------------
# SQS QUEUE
# ---------------------------------------------------------------------------------------------------------------------

resource "aws_sqs_queue" "sqs_principal" {
    name = "sqs-principal-${local.env}"
    redrive_policy  = "{\"deadLetterTargetArn\":\"${aws_sqs_queue.sqs_dlq_queue.arn}\",\"maxReceiveCount\":5}"
    visibility_timeout_seconds = 300

    tags = {
        Environment = "${local.env}"
    }
}


resource "aws_sqs_queue" "sqs_dlq_queue" {
    name = "sqs-dlq-queue-${local.env}"
}

# ---------------------------------------------------------------------------------------------------------------------
# SNS TOPIC
# ---------------------------------------------------------------------------------------------------------------------

resource "aws_sns_topic" "sns_principal" {
    name = "sns-principal-${local.env}"
}

# ---------------------------------------------------------------------------------------------------------------------
# SQS POLICY
# ---------------------------------------------------------------------------------------------------------------------

resource "aws_sqs_queue_policy" "sqs_principal_policy" {
    queue_url = "${aws_sqs_queue.sqs_dlq_queue.id}"

    policy = <<POLICY
{
  "Version": "2012-10-17",
  "Id": "sqspolicy",
  "Statement": [
    {
      "Sid": "First",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "sqs:SendMessage",
      "Resource": "${aws_sqs_queue.sqs_dlq_queue.arn}",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "${aws_sns_topic.sns_principal.arn}"
        }
      }
    }
  ]
}
POLICY
}