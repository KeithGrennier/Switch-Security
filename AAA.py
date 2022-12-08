#AAA Server based File
outFile='aaa.txt'
serverName='Server-R'
serverIP = '172.16.100.14'
authPort='1812'
acctPort='1813'
keyName='uF943ZDgAPYNRhS7'
permitIP=serverIP
accessListName='VTY_ACCESS'
aaa=f"""
aaa new-model
radiuse server {serverName}
address ipv4 {serverIP} auth-port {authPort} acct-port {acctPort}
exit
aaa authentication login default group radius {serverName} local-case
ip access-list standard {accessListName}
permit {permitIP}
deny any
exit
line vty 0 15
access-class {accessListName}
end
"""
with open(outFile,"w") as f:
    f.write(aaa)