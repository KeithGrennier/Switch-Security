outFile="cisco-router-ospf.txt"
interfaceOSPF="0/1"
ospfMD5Digest="H5h6qUq8ZzJUVsyv"
ospfSHAName="vaultKey120822"
ospfSHAKeyID="3"
ospfSHAKeySTR="dK487YpnHYmfUvsM"
ospfSHACryptoList=["hmac-sha-1","hmac-sha-256","hmac-sha-384","hmac-sha-512","md5"]
ospfSHACryptoSel=ospfSHACryptoList[3]
#OSPF MD5 Auth
ospfMD5=f"""
interface {interfaceOSPF}
ip ospf message-digest-key 1 md5 {ospfMD5Digest}
ip ospf authentication message-digest
interface {interfaceOSPF}
"""
ospfSHA=f"""
key chain {ospfSHAName}
key {ospfSHAKeyID}
key-string {ospfSHAKeySTR}
crypto-algorithm {ospfSHACryptoSel}
send-lifetime start-time infinite
interface {interfaceOSPF}
ip ospf authentication key-chain {ospfSHAName}
"""
ospfChoice=ospfSHA
with open(outFile,"w") as f:
    f.write(
f"""{ospfChoice}"""
    )