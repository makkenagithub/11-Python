"""
1. Parse Log Files (filter ERROR lines)

Task:
Read /var/log/syslog, extract lines containing "ERROR", write them to errors.log.
"""
```
input_file = "/var/log/syslog"
output_file = "errors.log"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        if "ERROR" in line:
            outfile.write(line)

print("Filtered errors written to errors.log")
```

"""
2. Disk Usage Alert ( > 80% )

Task:
Use Python to check disk usage and print a warning.
"""
```
import shutil

total, used, free = shutil.disk_usage("/")

usage_percent = used / total * 100

print(f"Disk usage: {usage_percent:.2f}%")

if usage_percent > 80:
    print("WARNING: Disk usage above 80%!")

```

or by using psutil
```
import psutil

disk = psutil.disk_usage('/')

print("Total:", disk.total / (1024**3), "GB")
print("Used:", disk.used / (1024**3), "GB")
print("Free:", disk.free / (1024**3), "GB")
print("Percentage:", disk.percent, "%")
```

TO check FS usage of each file system mount

```
import psutil

def show_disk_usage(path='/'):
    """
    Prints disk usage statistics for the given path.
    """
    usage = psutil.disk_usage(path)
    
    print(f"Disk Usage for '{path}':")
    print(f"  Total: {usage.total / (1024**3):.2f} GB")
    print(f"  Used: {usage.used / (1024**3):.2f} GB")
    print(f"  Free: {usage.free / (1024**3):.2f} GB")
    print(f"  Usage: {usage.percent}%\n")

# Check root filesystem
show_disk_usage('/')

# Optional: check other mounted directories
mount_points = [partition.mountpoint for partition in psutil.disk_partitions()]
for mount in mount_points:
    show_disk_usage(mount)
```

### file having columns of datat and in 2nd column a number exists. Find the average / max  of numbers in second column
```
input="C:\\Users\\MakkenaSuresh\\Desktop\\test\\FEB22_Python\\logs.txt"
l=[]
with open(input, "r") as f:
    for line in f:
        column = line.strip().split()
        l.append(int(column[1]))

print(l)
average= sum(l)/len(l)
print(f"average = {average:.2f}")
print(f"max of l = {max(l)}")
print(f"min of l = {min(l)}")

```


"""
3. Ping Servers from File

Task:
Read hostnames/IPs from servers.txt; print reachable/unreachable.
"""
```
import subprocess

with open("servers.txt") as f:
    servers = [line.strip() for line in f.readlines()]

for server in servers:
    result = subprocess.run(["ping", "-c", "1", server], stdout=subprocess.DEVNULL)
    
    if result.returncode == 0:
        print(f"{server} is reachable")
    else:
        print(f"{server} is NOT reachable")

```


"""
4. Validate Required Environment Variables

Task:
Check if essential environment variables exist.

✅ Solution:
"""
```
import os
import sys

required = ["DB_HOST", "DB_USER", "DB_PASSWORD"]

missing = [var for var in required if var not in os.environ]

if missing:
    print("Missing env variables:", missing)
    sys.exit(1)
else:
    print("All required env variables are set!")
```
"""
5. Basic File Backup Script

Task:
Zip a folder and name backup with timestamp.

✅ Solution:
"""
```
import shutil
import datetime

folder = "mydata"
timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
backup_name = f"backup-{timestamp}.zip"

shutil.make_archive(backup_name.replace(".zip", ""), "zip", folder)

print(f"Backup created: {backup_name}")
```
"""
6. Simple REST API GET Request

Task:
Call a public API and save response to JSON.

✅ Solution:
"""
```
import requests
import json

response = requests.get("https://api.github.com/repos/python/cpython")

data = response.json()

with open("repo_info.json", "w") as f:
    json.dump(data, f, indent=4)

print("Saved GitHub API response to repo_info.json")
```
"""
7. Check If a Process Is Running

Task:
Check if a process (e.g., "nginx") exists.

✅ Solution:
"""
```
import subprocess

process = "nginx"
cmd = ["pgrep", "-f", process]

result = subprocess.run(cmd, stdout=subprocess.PIPE)

if result.stdout:
    print(f"{process} is running")
else:
    print(f"{process} is NOT running")
```
"""
8. Automate Cleanup of Temp Files

Task:
Delete files older than 7 days.

✅ Solution:
"""
```
import os
import time

path = "/tmp"
days = 7
cutoff = time.time() - days * 86400

for root, dirs, files in os.walk(path):
    for filename in files:
        file_path = os.path.join(root, filename)
        if os.path.getmtime(file_path) < cutoff:
            os.remove(file_path)
            print(f"Deleted {file_path}")
```
"""
9. Convert CSV Inventory to JSON

Task:
Read an inventory CSV (servers, IPs) and convert to JSON.

✅ Solution:
"""
```
import csv
import json

servers = []

with open("inventory.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        servers.append(row)

with open("inventory.json", "w") as f:
    json.dump(servers, f, indent=4)

print("Converted CSV to JSON")
```
"""
10. Basic System Info Script (uptime, memory, hostname)

Task:
Use subprocess to gather system info.

✅ Solution:
"""
```
import subprocess

def run(cmd):
    return subprocess.check_output(cmd, text=True).strip()

print("Hostname:", run(["hostname"]))
print("Uptime:", run(["uptime", "-p"]))
print("Memory:", run(["free", "-h"]))
```
