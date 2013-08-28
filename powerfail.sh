#!/bin/sh
#shutdown imac
pypy /root/sendpf.py &
echo Raspberry Pi: Power failure occured on `date` >> /var/log/powerfail.log

#shutdown NAS
sshpass -p 'password' ssh -o StrictHostKeyChecking=no root@192.168.XXX.YYY 'shutdown -h now' ###shutdown -h now

#wake iMac
wakeonlan 00:11:22:aa:bb:cc
while true; sleep 1; do ping -q -c 1 192.168.2.YYY > /dev/null && break; done
#shutdown iMac
sshpass -p 'password' ssh -o StrictHostKeyChecking=no root@192.168.XXX.ZZZ 'shutdown -h now' ###shutdown -h now
#shutdown Pi
shutdown -h now

