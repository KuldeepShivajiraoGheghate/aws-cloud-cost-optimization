# AWS Cloud Cost Optimization System

## Overview
This project demonstrates how cloud infrastructure costs can be reduced by automatically detecting and stopping idle EC2 instances.

The system monitors EC2 CPU utilization using AWS CloudWatch. When the CPU usage remains below a defined threshold, a CloudWatch alarm triggers an AWS Lambda function which automatically stops the EC2 instance and records the action in Amazon S3.

## Technologies Used
- AWS EC2
- AWS CloudWatch
- AWS Lambda
- Amazon S3
- Python (boto3)

## Architecture
EC2 Instance → CloudWatch Monitoring → CloudWatch Alarm → Lambda Function → Stop Instance → Log stored in S3

## Features
- Detects idle EC2 instances
- Automatically stops unused instances
- Stores logs in S3
- Reduces unnecessary cloud costs
- Demonstrates serverless automation

## How It Works
1. EC2 instance runs normally
2. CloudWatch monitors CPU utilization
3. When CPU < threshold, alarm triggers
4. Lambda function executes
5. Lambda stops EC2 instance
6. Log file is stored in S3

## Future Improvements
- Add dashboard for monitoring
- Implement automated instance start scheduling
- Add email notifications
- Support multiple instances
