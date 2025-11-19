"""
16. AWS EC2 Instance Manager (boto3)
"""
```
import boto3

ec2 = boto3.client("ec2")

instances = ec2.describe_instances()

for r in instances["Reservations"]:
    for i in r["Instances"]:
        print(i["InstanceId"], i["State"]["Name"])
```
"""
17. Kubernetes Automation Tool
"""
```
import subprocess
import argparse

def run(cmd):
    return subprocess.check_output(cmd, text=True)

parser = argparse.ArgumentParser()
parser.add_argument("action", choices=["pods", "logs", "restart"])
parser.add_argument("--name")
args = parser.parse_args()

if args.action == "pods":
    print(run(["kubectl", "get", "pods", "-A"]))
elif args.action == "logs":
    print(run(["kubectl", "logs", args.name]))
elif args.action == "restart":
    print(run(["kubectl", "rollout", "restart", f"deployment/{args.name}"]))
```
"""
18. Detect Config Drift
"""
import yaml
import json

with open("desired.yaml") as f:
    desired = yaml.safe_load(f)

with open("actual.json") as f:
    actual = json.load(f)

drift = {}

for key in desired:
    if desired[key] != actual.get(key):
        drift[key] = {"desired": desired[key], "actual": actual.get(key)}

print("Drift detected:\n", json.dumps(drift, indent=4))
```
"""
19. Canary Deployment Script
"""
```
import subprocess

def deploy(percent):
    print(f"Deploying new version to {percent}% of servers")
    subprocess.run(["ansible-playbook", "deploy.yaml", "-e", f"canary={percent}"])

deploy(10)

# monitor
errors = int(subprocess.check_output(["scripts/check_errors.sh"]))
if errors > 5:
    print("Rolling back...")
    deploy(0)
else:
    print("Rolling forward...")
    deploy(100)

20. Prometheus Metrics Extractor
import requests

def push_metric(name, value):
    data = f"{name} {value}\n"
    requests.post("http://localhost:9091/metrics/job/log_metrics", data=data)

count_500 = 0

with open("/var/log/nginx/access.log") as f:
    for line in f:
        if " 500 " in line:
            count_500 += 1

push_metric("nginx_http_500_total", count_500)
print("Pushed metrics to Prometheus Pushgateway")
```
