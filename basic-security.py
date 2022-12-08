#Cisco Switch Dynamic
#basic config
outFile="basic-security.txt"
enpass="6utX4!@H9VPVkC3E"
linepass="7j$6F8ARq^4#ktvY"
domainName="thevault.com"
hostname="VaultSW1"
banner="$UNAUTHORIZED ACCESS TO THIS DEVICE IS PROHIBITED\nYou must have explicit, authorized permission to access or configure this device. Unauthorized attempts and actions\nto access or use this system may result in civil and/or criminal penalties. All activities performed on this device are logged and monitored.$"
exectimeout="5 30"

with open(outFile,"w") as f:
    #basic conf
    f.write(
f"""
! secure exec mode
enable algorithm-type scrypt {enpass}
line con 0
password {linepass}
transport input ssh
login local
exec-timeout {exectimeout}
!
line vty 0 15
password {linepass}
transport input ssh
login local
exec-timeout {exectimeout}
! encrypt passwords
service password-encryption
! additional password security
security passwords min-length 8
login block-for 120 attempts 3 within 60
! banners
banner motd {banner}
hostname {hostname}
"""
    )

