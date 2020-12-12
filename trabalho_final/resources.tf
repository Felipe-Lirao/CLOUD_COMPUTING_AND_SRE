provider "aws" {
  region = "us-east-1"
}

# ---------------------------------------------------------------------------------------------------------------------
# SQS QUEUE
# ---------------------------------------------------------------------------------------------------------------------

resource "aws_sqs_queue" "sqs_principal_dev" {
    name = "sqs-principal-dev"
    redrive_policy  = "{\"deadLetterTargetArn\":\"${aws_sqs_queue.sqs_principal_dlq_queue_dev.arn}\",\"maxReceiveCount\":5}"
    visibility_timeout_seconds = 300

    tags = {
        Environment = "dev"
    }
}


resource "aws_sqs_queue" "sqs_principal_dlq_queue_dev" {
    name = "sqs-principal-dlq-queue-dev"
}

# ---------------------------------------------------------------------------------------------------------------------
# SNS TOPIC
# ---------------------------------------------------------------------------------------------------------------------

resource "aws_sns_topic" "sns_principal_dev" {
    name = "sns-principal-dev"
}

# ---------------------------------------------------------------------------------------------------------------------
# SQS POLICY
# ---------------------------------------------------------------------------------------------------------------------

resource "aws_sqs_queue_policy" "sqs_principal_dev_policy" {
    queue_url = "${aws_sqs_queue.sqs_principal_dlq_queue_dev.id}"

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
      "Resource": "${aws_sqs_queue.sqs_principal_dlq_queue_dev.arn}",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "${aws_sns_topic.sns_principal_dev.arn}"
        }
      }
    }
  ]
}
POLICY
}