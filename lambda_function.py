import boto3
import datetime

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

def lambda_handler(event, context):

    instance_id = "YOUR_INSTANCE_ID"
    bucket_name = "cloud-cost-optimization-logs"

    ec2.stop_instances(InstanceIds=[instance_id])

    log_message = f"Instance {instance_id} stopped at {datetime.datetime.now()} because CPU was idle."

    s3.put_object(
        Bucket=bucket_name,
        Key=f"log-{datetime.datetime.now()}.txt",
        Body=log_message
    )

    print(log_message)
