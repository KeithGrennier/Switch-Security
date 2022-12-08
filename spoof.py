outFile="spoof.txt"
accessDenyNum="140"
accessAllowNum="120"
denyInts=["S0/0/0","S0/0/1"]
allowInts=["G0/0"]
netNum=["10","20","40","60","80","100","120"]
allowedNets=[]
for x in netNum:
    allowedNets.append(f"172.16.{x}.0")
sub24="0.0.0.255"
# Outside Interface ACL
classfulNets={
    'A':
    ["10.0.0.0","0.255.255.255"],
    'Loopback':
    ["127.0.0.0","0.255.255.255"],
    "B":
    ["172.16.0.0","0.15.255.255"],
    "C":
    ["192.168.0.0","0.0.255.255"],
    "D":
    ["224.0.0.0","15.255.255.255"]
}
extraneousNets=["0.0.0.0","255.255.255.255"]

with open(outFile,"w") as f:
    #Spoofing - deny - OUTSIDE
    for x in (denyInts):
        f.write(f"!interface {x}\n")
        f.write(f"access-list {accessDenyNum} deny host {extraneousNets[0]} any\n")
        for key in classfulNets:
            f.write(f"access-list {accessDenyNum} deny ip {classfulNets[key][0]} {classfulNets[key][1]} any\n")
        f.write(f"access-list {accessDenyNum} deny host {extraneousNets[1]} any\n")
    # spoofing - allow - INSIDE
    for x in allowInts:
        f.write(f"!interface {x}\n")
        for x in allowedNets:
            f.write(f"access-list {accessAllowNum} permit ip {x} {sub24} any\n")
