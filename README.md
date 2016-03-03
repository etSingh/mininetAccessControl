# mininetAccessControl

## Setup
http://www.brianlinkletter.com/set-up-mininet/

## Init 
###-> in virtual machine 
$ sudo dhclient eth1
$ ifconfig eth1

###-> in Terminal
// in terminal
$ ssh -Y mininet@192.168.56.101

*user: mininet | pw: mininet

## Add custom topologie
$ nano ~/mininet/custom/authTopo.py

*paste the content of authTopo.py from the github repo

## test custom topologie
$ sudo mn --custom ~/mininet/custom/authTopo.py --topo authtopo --te