import datetime
outFile='ntp.txt'
serverIP="172.16.100.11"
#DATETIME
now=datetime.datetime.now().strftime('%H:%M:%S %b %d %Y')

ntp=(f"""
clock set {now}
ntp server {serverIP}
""")

with open(outFile,"w") as f:
    f.write(ntp)