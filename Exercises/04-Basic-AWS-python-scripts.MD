1. List All EC2 Instances

Used to check running infrastructure.
```
import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("Instance ID:", instance['InstanceId'])
        print("State:", instance['State']['Name'])
```
✅ Use case

Infrastructure monitoring

Inventory of servers

Works with Amazon EC2


2. Start or Stop an EC2 Instance

Useful for cost optimization automation.
```
import boto3

ec2 = boto3.client('ec2')

instance_id = "i-xxxxxxxxxxxxx"

ec2.stop_instances(InstanceIds=[instance_id])

print("Instance stopping...")
```
To start:
```
ec2.start_instances(InstanceIds=[instance_id])
```

3. Upload File to S3

Automate backups or artifact uploads.
```
import boto3

s3 = boto3.client('s3')

file_name = "test.txt"
bucket_name = "my-devops-bucket"

s3.upload_file(file_name, bucket_name, file_name)

print("File uploaded successfully")
```
Works with Amazon S3

4. Create an S3 Bucket
```
import boto3

s3 = boto3.client('s3')

bucket_name = "my-new-devops-bucket"

s3.create_bucket(Bucket=bucket_name)

print("Bucket created")
```
5. Trigger a Lambda Function

Used in automation pipelines.
```
import boto3
import json

lambda_client = boto3.client('lambda')

response = lambda_client.invoke(
    FunctionName='myLambdaFunction',
    InvocationType='RequestResponse',
    Payload=json.dumps({"key": "value"})
)

print(response['StatusCode'])
```
Works with AWS Lambda

6. Get CloudWatch Metrics

Useful for monitoring CPU usage.
```
import boto3

cloudwatch = boto3.client('cloudwatch')

response = cloudwatch.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': 'i-xxxxxxxxxxxx'
        },
    ],
    StartTime='2024-01-01T00:00:00Z',
    EndTime='2024-01-01T01:00:00Z',
    Period=300,
    Statistics=['Average']
)

print(response)
```
Uses Amazon CloudWatch


7. Create an EC2 Instance Automatically
```
import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-xxxxxxxx',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='my-keypair'
)

print("Instance created:", instance[0].id)
```
8. Delete Old Snapshots (Cost Cleanup Script)
```
import boto3

ec2 = boto3.client('ec2')

snapshots = ec2.describe_snapshots(OwnerIds=['self'])

for snap in snapshots['Snapshots']:
    if snap['StartTime'].year < 2023:
        ec2.delete_snapshot(SnapshotId=snap['SnapshotId'])
        print("Deleted:", snap['SnapshotId'])
```
9. Check S3 Bucket Size
```
import boto3

s3 = boto3.resource('s3')

bucket = s3.Bucket('my-bucket')

size = 0

for obj in bucket.objects.all():
    size += obj.size

print("Total size:", size)
```
10. Auto Tag AWS Resources

Important for governance.
```
import boto3

ec2 = boto3.client('ec2')

ec2.create_tags(
    Resources=['i-xxxxxxxxxx'],
    Tags=[
        {
            'Key': 'Environment',
            'Value': 'Dev'
        }
    ]
)
```




1. Automatically Stop Idle EC2 Instances

Used to reduce cloud costs.

```
import boto3

ec2 = boto3.client('ec2')

instances = ec2.describe_instances()

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']

        if state == 'running':
            ec2.stop_instances(InstanceIds=[instance_id])
            print(f"Stopping instance: {instance_id}")
```
Works with Amazon EC2

2. Automated Daily S3 Backup

Useful for log backups or database dumps.
```
import boto3

s3 = boto3.client('s3')

local_file = "backup.sql"
bucket = "devops-backup-bucket"

s3.upload_file(local_file, bucket, local_file)

print("Backup uploaded successfully")
```
Works with Amazon S3

3. Auto Scale EC2 Based on CPU

Checks CPU utilization and scales instances.
```
import boto3

cloudwatch = boto3.client('cloudwatch')

response = cloudwatch.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Period=300,
    Statistics=['Average']
)

print(response)
```
Uses Amazon CloudWatch

4. Trigger CI/CD Pipeline Automatically

Used in deployment automation.
```
import boto3

client = boto3.client('codepipeline')

response = client.start_pipeline_execution(
    name='my-pipeline'
)

print("Pipeline triggered")
```
Works with AWS CodePipeline

5. Delete Old Logs From S3

Automates storage cleanup.
```
import boto3
from datetime import datetime, timedelta

s3 = boto3.resource('s3')

bucket = s3.Bucket('log-bucket')

for obj in bucket.objects.all():
    if obj.last_modified < datetime.now(obj.last_modified.tzinfo) - timedelta(days=30):
        obj.delete()
        print("Deleted:", obj.key)
```
6. Check EC2 Health Status
```
import boto3

ec2 = boto3.client('ec2')

status = ec2.describe_instance_status()

for instance in status['InstanceStatuses']:
    print(instance['InstanceId'], instance['InstanceState']['Name'])
```
7. Automatically Create AMI Backup

Used for disaster recovery.
```
import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId='i-xxxxxxxxxx',
    Name='AutomatedBackup'
)

print("AMI Created:", response['ImageId'])
```
8. Send Alerts Using SNS
```
import boto3

sns = boto3.client('sns')

sns.publish(
    TopicArn='arn:aws:sns:region:account-id:alerts',
    Message='Server CPU is high',
    Subject='DevOps Alert'
)

print("Alert sent")
```
Uses Amazon SNS

9. List All S3 Buckets
```
import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

for bucket in response['Buckets']:
    print(bucket['Name'])
```
10. Restart EC2 Instance Automatically
```
import boto3

ec2 = boto3.client('ec2')

instance_id = "i-xxxxxxxx"

ec2.reboot_instances(InstanceIds=[instance_id])

print("Instance rebooted")
```


11. Trigger Deployment Pipeline

Service: AWS CodePipeline
```
import boto3

cp = boto3.client('codepipeline')

cp.start_pipeline_execution(
    name='deploy-pipeline'
)
```
12. Trigger Lambda Function

Service: AWS Lambda
```
import boto3

client = boto3.client('lambda')

client.invoke(
    FunctionName="myFunction"
)
```
15. List IAM Users

Service: AWS Identity and Access Management
```
import boto3

iam = boto3.client('iam')

users = iam.list_users()

for user in users['Users']:
    print(user['UserName'])
```


