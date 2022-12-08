outFile="icmp-atk.txt"
accessOutside="140"
accessAllowNum="120"
outInts=["S0/0/0","S0/0/1"]
allowInt=["G0/0"]
netNum=["10","20","40","60","80","100","120"]
#sub ints
subInts=[]
for x in netNum:
    subInts.append(f"G0/0.{x}")
allowedNets=[]
for x in netNum:
    allowedNets.append(f"172.16.{x}.0")
sub24="0.0.0.255"

with open(outFile,"w") as f:
    #ICMP Outside
    for x in (outInts):
        f.write(f"!interface {x}\n")
        f.write(f"access-list {accessOutside} allow icmp any any echo-reply\n")
        f.write(f"access-list {accessOutside} allow icmp any any source-quench\n")
        f.write(f"access-list {accessOutside} allow icmp any any unreachable\n")
        f.write(f"access-list {accessOutside} deny icmp any any\n")
        f.write(f"access-list {accessOutside} permit ip any any\n")
    # ICMP - INSIDE
    for x in allowedNets:
        f.write(f"!interface {subInts[allowedNets.index(x)]}\n")
        
        f.write(f"access-list {accessAllowNum} permit icmp {x} {sub24} any echo\n")
        f.write(f"access-list {accessAllowNum} permit icmp {x} {sub24} any parameter-problem\n")
        f.write(f"access-list {accessAllowNum} permit icmp {x} {sub24} any packet-too-big\n")
        f.write(f"access-list {accessAllowNum} permit icmp {x} {sub24} any source-quench\n")
        f.write(f"access-list {accessAllowNum} deny icmp any any\n")
        f.write(f"access-list {accessAllowNum} permit ip any any\n")