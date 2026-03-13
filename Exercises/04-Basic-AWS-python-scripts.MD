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


