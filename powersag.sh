#!/bin/sh
pypy /root/sendpsag.py &
echo Raspberry Pi: Sag occured on `date` >> /var/log/powerfail.log
