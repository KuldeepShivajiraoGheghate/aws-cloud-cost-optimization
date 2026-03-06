# Project Explanation

This project demonstrates an automated cloud cost optimization system.

The system monitors EC2 CPU utilization using CloudWatch. When the CPU remains idle below a defined threshold, a CloudWatch alarm triggers a Lambda function that automatically stops the EC2 instance.

The Lambda function also stores a log of this action in an S3 bucket.

Services used:
- EC2
- CloudWatch
- Lambda
- S3
- IAM
