output "arn_sqs" {
  value = "${aws_sqs_queue.sqs_principal.arn}"
}

output "url_sqs" {
  value = "${aws_sqs_queue.sqs_principal.id}"
}

output "arn_sqs_dlq" {
  value = "${aws_sqs_queue.sqs_dlq_queue.arn}"
}

output "url_sqs_dlq" {
  value = "${aws_sqs_queue.sqs_dlq_queue.id}"
}

output "arn_sns" {
  value = "${aws_sns_topic.sns_principal.arn}"
}