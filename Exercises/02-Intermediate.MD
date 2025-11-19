"""
11. REST API CI Data Collector
"""
```
import requests
import json

url = "https://api.github.com/repos/devops/repo/actions/runs"
resp = requests.get(url)
data = resp.json()

with open("pipeline_runs.json", "w") as f:
    json.dump(data, f, indent=4)

print("Saved workflow run info")
```
"""
12. SSH Automation (Paramiko)
"""
```
import paramiko

host = "10.0.0.12"
user = "ubuntu"
key = "/home/ubuntu/.ssh/id_rsa"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, key_filename=key)

stdin, stdout, stderr = client.exec_command("df -h")
print(stdout.read().decode())

client.close()
```
"""
13. Process Monitor → Restart if Dead
"""
```
import subprocess
import time

process = "nginx"

while True:
    result = subprocess.run(["pgrep", "-f", process], stdout=subprocess.PIPE)

    if not result.stdout:
        print("Process is down — restarting...")
        subprocess.run(["systemctl", "restart", process])
    else:
        print("OK")

    time.sleep(10)
```
"""
14. Log Rotation Script
"""
```
import os
import time
import shutil

log = "/var/log/app.log"
max_size = 50 * 1024 * 1024  # 50MB

if os.path.getsize(log) > max_size:
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    archive = f"{log}-{timestamp}"
    shutil.move(log, archive)
    open(log, "w").close()
    print("Rotated log:", archive)
```
"""
15. Nginx Access Log Analyzer
"""
```
from collections import Counter
import re

logfile = "/var/log/nginx/access.log"
ips = Counter()
statuses = Counter()

with open(logfile) as f:
    for line in f:
        parts = line.split()
        ip = parts[0]
        status = parts[8]

        ips[ip] += 1
        statuses[status] += 1

print("Top 10 IPs:")
print(ips.most_common(10))

print("HTTP Status Counts:")
print(statuses)
```
