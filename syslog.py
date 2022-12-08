#Syslog
hostIP="172.16.100.49.1"
sourceINT="lo0"
syslog=f"""
service timestamps log datetime
logging {hostIP}
logging trap informational
logging source-interface{sourceINT}
"""

with open("basic-syslog.txt","w") as f:
    f.write(f"{syslog}")